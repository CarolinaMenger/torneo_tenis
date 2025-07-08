# gestion/models.py

from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    ranking = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} (Ranking {self.ranking})"

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