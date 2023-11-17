from django.db import models

# Create your models here.



class Tratamiento(models.Model):
   nombreTratamiento = models.CharField(max_length=50)

   def __str__(self):
       return self.nombreTratamiento
   

class Pacientes(models.Model):
    nombre = models.CharField(max_length=50)
    microchip = models.CharField(max_length=50)
    fecha_atencion = models.DateField()
    motivo = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=50)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=50)
    valor = models.IntegerField()