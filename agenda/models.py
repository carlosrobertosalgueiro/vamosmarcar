from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=265, unique=True)

# aimprime observações do objeto
    def __str__(self):
        return f"{self.nome} <{self.id}>"


class Evento(models.Model):
    nome = models.CharField(max_length=256)
    Categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(null=True)

    def __str__(self):
        return f"{self.nome} - {self.Categoria} - {self.local} - {self.link}"
