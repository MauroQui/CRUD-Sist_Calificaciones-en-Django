from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nombre