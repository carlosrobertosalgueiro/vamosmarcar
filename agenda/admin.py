from django.contrib import admin
from agenda.models import Evento, Categoria

#Registra as classe para imprimir na tela admin.
admin.site.register(Evento)
admin.site.register(Categoria)