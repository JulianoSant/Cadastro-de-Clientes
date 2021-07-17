
from django.db import models

# tabela

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    cod = models.IntegerField()
