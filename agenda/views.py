from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from agenda.models import Evento

# Create your views here.


def listar_eventos(request):
    #filtra e mostras os eventos maior que a data atual
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    return render(request=request,
                  context={"eventos": eventos},
                  template_name="agenda/listar_evento.HTML")


def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    #evento = Evento.objects.get(id=id)
    return render(request=request,
                  context={"evento": evento},
                  template_name="agenda/exibir_agenda.HTML")
