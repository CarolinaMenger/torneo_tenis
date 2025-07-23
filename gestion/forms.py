from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Jugador, Torneo, Partido
from datetime import date
from django.contrib.auth.models import User


class JugadorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.DateInput(format="%d/%m/%Y", attrs={'placeholder': 'DD/MM/AAAA'})
    )

    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'pais', 'ranking']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre', 'sede', 'pais', 'fecha_inicio', 'fecha_fin']

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise forms.ValidationError(
                "Ups... la fecha de finalización no puede ser anterior a la de inicio. ¿Nos fijamos?"
            )

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = [
            'modalidad',
            'jugador1',
            'jugador2',
            'jugador3',
            'jugador4',
            'torneo',
            'fecha',
            'resultado',
            'ganador'
        ]

    def clean(self):
        cleaned_data = super().clean()
        modalidad = cleaned_data.get('modalidad')
        j1 = cleaned_data.get('jugador1')
        j2 = cleaned_data.get('jugador2')
        j3 = cleaned_data.get('jugador3')
        j4 = cleaned_data.get('jugador4')
        resultado = cleaned_data.get('resultado')

        if modalidad == 'DOBLES':
            if not j3 or not j4:
                raise forms.ValidationError("Para dobles tenés que elegir cuatro jugadores 👫👫")
            if len({j1, j2, j3, j4}) < 4:
                raise forms.ValidationError("¡Ojo! No podés repetir jugadores en dobles.")
        else:
            if j3 or j4:
                raise forms.ValidationError("Para single solo deben cargarse dos jugadores.")
            if j1 == j2:
                raise forms.ValidationError("Los jugadores deben ser distintos.")

        if resultado and not all("-" in set.strip() for set in resultado.split(",")):
            raise forms.ValidationError("Ingresá el resultado como sets con guión, ej. 6-4, 3-6, 7-5 🎯")

class BusquedaJugadorForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=True)
    last_name = forms.CharField(label='Apellido', max_length=30, required=True)
    email = forms.EmailField(label='Correo electrónico', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

from .models import Perfil

class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
        labels = {'foto': 'Foto de perfil'}