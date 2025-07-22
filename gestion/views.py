from django.views.generic import ListView, CreateView
from django.shortcuts import render
from .models import Jugador, Torneo, Partido
from .forms import JugadorForm, TorneoForm, PartidoForm, BusquedaJugadorForm

def inicio(request):
    return render(request, 'gestion/inicio.html')

class JugadorCreate(CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'gestion/jugador_form.html'
    success_url = '/jugadores/'

class JugadorList(ListView):
    model = Jugador
    template_name = 'gestion/jugador_list.html'
    context_object_name = 'jugadores'

def buscar_jugadores(request):
    form = BusquedaJugadorForm(request.GET)
    resultados = []
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Jugador.objects.filter(nombre__icontains=nombre)
    return render(request, 'gestion/buscar_jugador.html', {'form': form, 'resultados': resultados})

class TorneoCreate(CreateView):
    model = Torneo
    form_class = TorneoForm
    template_name = 'gestion/torneo_form.html'
    success_url = '/torneos/'

class TorneoList(ListView):
    model = Torneo
    template_name = 'gestion/torneo_list.html'
    context_object_name = 'torneos'

class PartidoCreate(CreateView):
    model = Partido
    form_class = PartidoForm
    template_name = 'gestion/partido_form.html'
    success_url = '/partidos/'

class PartidoList(ListView):
    model = Partido
    template_name = 'gestion/partido_list.html'
    context_object_name = 'partidos'

def about_view(request):
    return render(request, 'gestion/about.html')