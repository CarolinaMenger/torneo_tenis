from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Jugador, Torneo, Partido, Perfil
from .forms import JugadorForm, TorneoForm, PartidoForm, BusquedaJugadorForm, RegistroForm, FotoPerfilForm

# 🏠 Vista de inicio
def inicio(request):
    return render(request, 'gestion/inicio.html')

# 🧍 Crear jugador
class JugadorCreate(LoginRequiredMixin, CreateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'gestion/jugador_form.html'
    success_url = '/jugadores/'

# ✏️ Modificar jugador
class JugadorUpdate(LoginRequiredMixin, UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'gestion/jugador_form.html'
    success_url = '/jugadores/'

# 👥 Ver jugadores
class JugadorList(ListView):
    model = Jugador
    template_name = 'gestion/jugador_list.html'
    context_object_name = 'jugadores'

# 🔍 Buscar jugadores
def buscar_jugadores(request):
    form = BusquedaJugadorForm(request.GET)
    resultados = []
    consulta = ""  

    if form.is_valid():
        consulta = form.cleaned_data['nombre_completo'].strip()
        partes = consulta.split()

        if len(partes) == 2:
            nombre, apellido = partes
            resultados = Jugador.objects.filter(
                Q(nombre__icontains=nombre),
                Q(apellido__icontains=apellido)
            )
        elif len(partes) == 1:
            resultados = Jugador.objects.filter(
                Q(nombre__icontains=partes[0]) | Q(apellido__icontains=partes[0])
            )

    return render(request, 'gestion/buscar_jugador.html', {
        'form': form,
        'resultados': resultados,
        'consulta': consulta
    })


# 🎾 Crear torneo
class TorneoCreate(LoginRequiredMixin, CreateView):
    model = Torneo
    form_class = TorneoForm
    template_name = 'gestion/torneo_form.html'
    success_url = '/torneos/'

# 📋 Ver torneos
class TorneoList(ListView):
    model = Torneo
    template_name = 'gestion/torneo_list.html'
    context_object_name = 'torneos'

# 🆚 Crear partido
class PartidoCreate(LoginRequiredMixin, CreateView):
    model = Partido
    form_class = PartidoForm
    template_name = 'gestion/partido_form.html'
    success_url = '/partidos/'

# 📋 Ver partidos
class PartidoList(ListView):
    model = Partido
    template_name = 'gestion/partido_list.html'
    context_object_name = 'partidos'

# ℹ️ Acerca de mí
def about_view(request):
    return render(request, 'gestion/about.html')

# 📋 Registro de usuario con datos completos
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.first_name = form.cleaned_data['first_name']
            usuario.last_name = form.cleaned_data['last_name']
            usuario.email = form.cleaned_data['email']
            usuario.save()

            Perfil.objects.create(usuario=usuario)
            
            login(request, usuario)
            return redirect('bienvenida')
    else:
        form = RegistroForm()
    return render(request, 'gestion/registro.html', {'form': form})

# 👋 Vista de bienvenida
@login_required
def bienvenida_view(request):
    return render(request, 'gestion/bienvenida.html')

# 👤 Vista de Mi Perfil
@login_required
def perfil_view(request):
    usuario = request.user
    return render(request, 'gestion/perfil.html', {'usuario': usuario})

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# 👤 Editar Mi Perfil
@login_required
def editar_perfil_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, '✅ Perfil actualizado con éxito 🎉')
        return redirect('perfil')
    return render(request, 'gestion/editar_perfil.html', {'usuario': request.user})

# 🔒 Cambiar Contraseña
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages

class CambioPasswordView(PasswordChangeView):
    template_name = 'gestion/cambiar_password.html'
    success_url = '/perfil/'

    def form_valid(self, form):
        messages.success(self.request, '✅ Contraseña actualizada con éxito 🔒')
        return super().form_valid(form)
    
# 📸 Cambiar Foto de Perfil    
@login_required
def subir_foto_view(request):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Foto de perfil actualizada 📸')
            return redirect('perfil')
    else:
        form = FotoPerfilForm(instance=perfil)
    return render(request, 'gestion/subir_foto.html', {'form': form})

