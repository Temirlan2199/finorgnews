from django.db import models

# Create your models here.
class FinancialOrganizationModel(models.Model):
    chairman_SD = models.CharField(max_length=255, null=True, blank=True)
    chairman_board = models.CharField(max_length=255, null=True, blank=True)
    board_members = models.CharField(max_length=255, null=True, blank=True)
    chief_accountant = models.CharField(max_length=255, null=True, blank=True)
    orgbin = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    telephone = models.CharField( max_length=255,null=True, blank=True)
    fax = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    website = models.URLField(max_length=255,null=True, blank=True)
    bank_license = models.CharField(max_length=255,null=True, blank=True)
    custodian = models.CharField(max_length=255,null=True, blank=True)
    major_participants = models.CharField(max_length=255,null=True, blank=True)
    broker_dealers = models.CharField(max_length=255,null=True, blank=True)
    bank_holdings = models.CharField(max_length=255,null=True, blank=True)
    bank_name = models.CharField(max_length=255)  

    def __str__(self):
        return self.bank_name
    

    
class FinancialOrganizationNewsModel(models.Model):
    bank_name=models.CharField(max_length=255)
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title