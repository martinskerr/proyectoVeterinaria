from django.contrib import admin

from djangoVetMartin.models import Pacientes

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','microchip','fecha_atencion', 'motivo', 'diagnostico','tratamiento', 'observaciones', 'valor']


admin.site.register(Pacientes, PacienteAdmin)