from django.db import models

# Create your models here.
class produto(models.Model):
    descricao = models.CharField(max_length=100)
    peso = models.CharField(max_length=100)
    barcode = models.CharField(max_length=28)
    tamanho = models.CharField(max_length=5)
    qtd = models.CharField(max_length=100)          