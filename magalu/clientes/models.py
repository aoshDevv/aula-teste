from msilib.schema import Class
from django.db import models

# Create your models here.
class clientes(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    tel = models.CharField(max_length=13)
    mail = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
