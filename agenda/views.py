from django.http import HttpResponse
from django.shortcuts import render
from agenda.models import eventos

# Create your views here.

def index(request):
    return HttpResponse("Olá, mundo!")

def exibir_evento(request):
    evento =  eventos[0]  
    return HttpResponse(f"""
    <html><h1>Evento: {evento.nome}</html>
    <p>Categoria: {evento.categoria}</p>
    """)