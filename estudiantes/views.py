from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm

def index(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {'estudiantes': estudiantes})

def add_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/estudiante_form.html', {'form': form})

def edit_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/estudiante_form.html', {'form': form})

def delete_estudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('index')