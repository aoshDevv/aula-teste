from django.db import models

# Create your models here.
class nota_fiscal(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    endereço = models.CharField(max_length=50)
    transportadora = models.CharField(max_length=50)
    num_serie= models.CharField(max_length=50)