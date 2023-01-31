from django.db import models

# Create your models here.

class Evento:
        def __init__(self, nome, categoria, local=None, link=None):
             self.nome = nome
             self.categoria = categoria
             self.local = local
             self.link = link

aula_python = Evento("Aula de python", "backend", "Salgueiro") 
aula_java = Evento("Aula de java", "backend","petrolina", link="salgueiro.com")   

eventos = [
    aula_python, aula_java
]