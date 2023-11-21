import requests
from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from .forms import FinancialOrganizationForm
from celery import shared_task
import time

@shared_task
def update_news_for_organization(bank_name):
    api_key = 'b8eb8f3300ff4d51ba5a22c558d8b658'
    query = bank_name
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'

    response = requests.get(url)
    news_data = response.json().get('articles', [])

    for article in news_data:
        title = article.get('title', '')
        description = article.get('description', '')
        url = article.get('url', '')
        FinancialOrganizationNewsModel.objects.create(
            bank_name=bank_name,
            title=title,
            description=description,
            url=url
        ) 

@shared_task
def update_news_for_all_organizations():
    financial_organizations = FinancialOrganizationModel.objects.all()

    for organization in financial_organizations:
        update_news_for_organization.delay(organization.bank_name)

def get_news(request):
    financial_organizations = FinancialOrganizationModel.objects.all()

    for organization in financial_organizations:
        update_news_for_organization.delay(organization.bank_name)

    return render(request, 'update_in_progress.html')



def add_organization(request):
    if request.method == 'POST':
        form = FinancialOrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list') 
    else:
        form = FinancialOrganizationForm()

    return render(request, 'add_organization.html', {'form': form})

def organization_list(request):
    organizations = FinancialOrganizationModel.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def organization_info(request, bank_name):
    organizations = FinancialOrganizationModel.objects.filter(bank_name=bank_name)

    if not organizations.exists():
        raise Http404("Organization does not exist")


    organization = organizations.first()
    news = FinancialOrganizationNewsModel.objects.filter(bank_name=bank_name)
    return render(request, 'organization_info.html', {'organization': organization, 'news': news})

def organization_news(request, bank_name):
    news = FinancialOrganizationNewsModel.objects.filter(bank_name=bank_name)
    return render(request, 'organization_news.html', {'news': news, 'bank_name': bank_name})