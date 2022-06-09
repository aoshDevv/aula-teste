from django.db import models

# Create your models here.
class fornecedor(models.Model):
    razao_social = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=13)
    tel = models.CharField(max_length=13)
    mail = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)