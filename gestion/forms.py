from django import forms
from .models import Jugador, Torneo, Partido

class JugadorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.DateInput(format="%d/%m/%Y", attrs={'placeholder': 'DD/MM/AAAA'})
    )

    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'ranking']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = '__all__'

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'

class BusquedaJugadorForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)

    class TorneoForm(forms.ModelForm):
        class Meta:
            model = Torneo
            fields = '__all__'

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'