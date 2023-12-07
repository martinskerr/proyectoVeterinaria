from django.shortcuts import render
from djangoVetMartin.models import Pacientes
from .forms import PacienteForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    data={
    }
    return render(request, 'index.html', data) 

def listaPacientes(request):
    Paciente = Pacientes.objects.all()
    data = {
        "pacientes": Paciente
    }
    return render(request, 'mascotas.html', data)

            

def crearPaciente(request):
    form = PacienteForm()

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse("lista_mascota"))

    data = {'form': form,
            'titulo': 'Agregar Paciente'
            }
    return render(request, 'form.html',data)


def editarPaciente(request, id):
    paciente = Pacientes.objects.get(id=id)
    form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("lista_mascota"))
        else:
            print(form.errors)  # Muestra los errores del formulario en la consola

    data = {'form': form,
            'titulo': 'Actualizar Paciente'
            }
    return render(request, 'form.html', data)

def eliminarPaciente(request, id):

    paciente = Pacientes.objects.get(id = id)
    paciente.delete()
    return HttpResponseRedirect(reverse("lista_mascota"))