from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    inicio,
    JugadorCreate, JugadorList, buscar_jugadores,
    TorneoCreate, TorneoList,
    PartidoCreate, PartidoList,
    about_view, registrar_usuario, bienvenida_view, perfil_view,
    editar_perfil_view, subir_foto_view,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about_view, name='about'),
 
    path('jugadores/nuevo/', JugadorCreate.as_view(), name='jugador_nuevo'),
    path('jugadores/', JugadorList.as_view(), name='jugador_lista'),
    path('jugadores/buscar/', buscar_jugadores, name='buscar_jugador'),
    path('torneos/nuevo/', TorneoCreate.as_view(), name='torneo_nuevo'),
    path('torneos/', TorneoList.as_view(), name='torneo_lista'),
    path('partidos/nuevo/', PartidoCreate.as_view(), name='partido_nuevo'),
    path('partidos/', PartidoList.as_view(), name='partido_lista'),
    path('registro/', registrar_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='gestion/login.html', redirect_authenticated_user=True, next_page='bienvenida'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('bienvenida/', bienvenida_view, name='bienvenida'),
    path('perfil/', perfil_view, name='perfil'),
    path('perfil/editar/', editar_perfil_view, name='editar_perfil'),
    path('perfil/cambiar-password/', auth_views.PasswordChangeView.as_view(template_name='gestion/cambiar_password.html',
    success_url='/perfil/',), name='cambiar_password'),
    path('perfil/foto/', subir_foto_view, name='subir_foto'),
]