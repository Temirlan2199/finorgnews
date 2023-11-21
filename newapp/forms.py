from django import forms
from .models import FinancialOrganizationModel

class FinancialOrganizationForm(forms.ModelForm):
    class Meta:
        model = FinancialOrganizationModel
        fields = '__all__'
        labels = {
            'chairman_SD': 'Председатель Совета директоров',
            'chairman_board': 'Председатель Правления',
            'board_members': 'Совет директоров',
            'chief_accountant': 'Главный бухгалтер',
            'orgbin': 'БИН',
            'address': 'Адрес (город, улица, дом, квартира)',
            'telephone': 'Телефон',
            'fax': 'Факс',
            'email': 'Email',
            'website': 'Web-сайт',
            'bank_license': 'Банк второго уровня',
            'custodian': 'Кастодиан',
            'major_participants': 'Крупные участники',
            'broker_dealers': 'Брокеры-дилеры',
            'bank_holdings': 'Банковские холдинги',
            'bank_name': 'Наименование организации',  
        }