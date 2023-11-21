from django.urls import path
from .views import *


urlpatterns = [
    path('news/', get_news, name='get_news'),
    path('add_organization/', add_organization, name='add_organization'),
    path('organization_list/', organization_list, name='organization_list'),
    path('organization_info/<str:bank_name>/', organization_info, name='organization_info'),
    path('organization_news/<str:bank_name>/', organization_news, name='organization_news'),
  
]

