from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from agenda.models import Evento

# Create your views here.


def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request=request, context={"eventos": eventos}, template_name="agenda/listar_evento.HTML")



def exibir_evento(request):
    evento = {"nome": "Aula de java",
              "categoria": "backend",
              "local": "petrolina",
              "link": "salgueiro.com"}
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_agenda.HTML")
