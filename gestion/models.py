# gestion/models.py

from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    ranking = models.IntegerField()
    pais = models.CharField(max_length=100, default="Argentina")
    
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    sede = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(default=date(2025, 12, 31))
    pais = models.CharField(max_length=100, default="Argentina")


    def __str__(self):
        return f"{self.nombre} ({self.sede})"

class Partido(models.Model):
    MODALIDADES = [
        ('SINGLE', 'Single'),
        ('DOBLES', 'Dobles'),
    ]

    jugador1 = models.ForeignKey(Jugador, related_name='partidos_jugador1', on_delete=models.CASCADE)
    jugador2 = models.ForeignKey(Jugador, related_name='partidos_jugador2', on_delete=models.CASCADE)
    jugador3 = models.ForeignKey(Jugador, related_name='partidos_jugador3', on_delete=models.CASCADE, null=True, blank=True)
    jugador4 = models.ForeignKey(Jugador, related_name='partidos_jugador4', on_delete=models.CASCADE, null=True, blank=True)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=10, choices=MODALIDADES, default='SINGLE')
    resultado = models.CharField(max_length=100)  # ejemplo: "6-3, 4-6, 7-5"
    ganador = models.ForeignKey(Jugador, related_name='partidos_ganados', on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()

    def __str__(self):
        texto_base = f"{self.jugador1} y {self.jugador3}" if self.modalidad == 'DOBLES' else f"{self.jugador1}"
        texto_vs = f"{self.jugador2} y {self.jugador4}" if self.modalidad == 'DOBLES' else f"{self.jugador2}"
        return f"{texto_base} vs {texto_vs} – {self.torneo}"
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
