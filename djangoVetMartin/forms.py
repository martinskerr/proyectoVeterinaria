from django import forms
from djangoVetMartin.models import Pacientes, Tratamiento
from django.core import validators


#Actualizar el dato
class PacienteForm(forms.Form):

    nombre = forms.CharField(max_length=50,)
    microchip = forms.CharField(max_length=50)
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    motivo = forms.CharField(max_length=50)
    diagnostico = forms.CharField(max_length=50)
    observaciones = forms.CharField(max_length=50)
    valor = forms.IntegerField()
    
    tratamiento = forms.ModelChoiceField(queryset=Tratamiento.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    fecha_atencion.widget.attrs['class'] = 'form-control'
    motivo.widget.attrs['class'] = 'form-control'
    diagnostico.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'
    valor.widget.attrs['class'] = 'form-control'

    
#Crear el dato y almacenarlo en la DB
class PacienteForm(forms.ModelForm):

    nombre = forms.CharField(max_length=50,)
    microchip = forms.CharField(max_length=50)
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    motivo = forms.CharField(max_length=50)
    diagnostico = forms.CharField(max_length=50)
    observaciones = forms.CharField(max_length=50)
    valor = forms.IntegerField()

    tratamiento  = forms.ModelChoiceField(queryset=Tratamiento.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    microchip.widget.attrs['class'] = 'form-control'
    fecha_atencion.widget.attrs['class'] = 'form-control'
    motivo.widget.attrs['class'] = 'form-control'
    diagnostico.widget.attrs['class'] = 'form-control'
    observaciones.widget.attrs['class'] = 'form-control'
    valor.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Pacientes
        fields = '__all__'