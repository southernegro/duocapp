from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return render(request, 'duocmobile/index.html', {})

def perfil(request):

    user = request.user
    perfil = Perfil.objects.get(user_id = user.id)
    data={      
        'perfil': perfil
    }
    return render(request, 'duocmobile/perfil.html', data)

@login_required
def listado_asignaturas(request):
    student = request.user.perfil.student
    cursos = Curso.objects.filter(student = student.id)
    criticos = AlumnosCriticos.objects.filter(alumno = student.id)
    data={
        'cursos': cursos, 'criticos':criticos
        }
    return render(request, 'duocmobile/listado_asignaturas.html', data)

@login_required
def listado_cursos(request):
    asignatura = request.user.perfil.docente
    cursos = Curso.objects.filter(asignatura = asignatura.id)
    data={
        'cursos': cursos
    }
    return render(request, 'duocmobile/listado_cursos.html', data)

@login_required
def alumnos_criticos(request):
    docente = request.user.perfil.docente
    alumnos = AlumnosCriticos.objects.filter(docente = docente.id)
    data={
        'alumnos': alumnos
    }
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        data['url'] = fs.url(name)
    return render(request, 'duocmobile/alumnos_criticos.html', data)


