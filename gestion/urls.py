from django.urls import path
from .views import (
    inicio,
    JugadorCreate, JugadorList, buscar_jugadores,
    TorneoCreate, TorneoList,
    PartidoCreate, PartidoList,
    about_view,
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
]