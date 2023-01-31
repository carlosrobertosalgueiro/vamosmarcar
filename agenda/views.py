from django.http import HttpResponse
from django.shortcuts import render
from agenda.models import eventos
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Olá, mundo!")

def exibir_evento(request):
    evento =  eventos[1]  
    return render(request=request, context={"evento": evento},template_name="agenda/exibir_agenda.HTML")

    