# gestion/models.py

from django.db import models
from datetime import date

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    ranking = models.IntegerField()

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

    def __str__(self):
        return f"{self.nombre} ({self.sede})"

class Partido(models.Model):
    jugador1 = models.ForeignKey(Jugador, related_name='partidos_jugador1', on_delete=models.CASCADE)
    jugador2 = models.ForeignKey(Jugador, related_name='partidos_jugador2', on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.jugador1} vs {self.jugador2} – {self.torneo}"