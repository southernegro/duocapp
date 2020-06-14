from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .forms import CreateUserForm, materialApoyoForm


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
    for i in cursos:
        material = materialApoyo.objects.filter(curso=i)
    criticos = AlumnosCriticos.objects.filter(alumno = student.id)
    data={
        'cursos': cursos, 'criticos':criticos, 'material':material
        }
    return render(request, 'duocmobile/listado_asignaturas.html', data)

@login_required
def listado_cursos(request):
    docente = request.user.perfil.docente
    cursos = Curso.objects.filter(docente = docente.id)
    data={
        'cursos': cursos
    }
    return render(request, 'duocmobile/listado_cursos.html', data)

#@login_required
#def alumnos_criticos(request):
#    docente = request.user.perfil.docente
#    cursos = Curso.objects.filter(docente = docente.id)
#    alumnos = AlumnosCriticos.objects.filter(docente = docente.id)
#    data={
#        'alumnos': alumnos, 'cursos':cursos
#    }
#    if request.method == 'POST':
#        uploaded_file = request.FILES['document']
#        fs = FileSystemStorage()
#        name = fs.save(uploaded_file.name, uploaded_file)
#        url = fs.url(name)
#        data['url'] = fs.url(name)
#    return render(request, 'duocmobile/alumnos_criticos.html', data)

@login_required
def alumnos_criticos(request):
    docente = request.user.perfil.docente
    cursos = Curso.objects.filter(docente = docente.id)
    alumnos = AlumnosCriticos.objects.filter(docente = docente.id)
    data={
        'alumnos': alumnos, 'cursos':cursos, 'form': materialApoyoForm()
    }
    if request.method=='POST':
        formulario = materialApoyoForm(request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario = formulario.save(commit=False)
            formulario.docente = docente
            formulario.save()
            data['mensaje']='Producto agregado con éxito'
        data['form'] = formulario
    return render(request, 'duocmobile/alumnos_criticos.html', data)


def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Cuenta creada con éxito para ' + user)
			return redirect('login')

	context = {'form':form}
	return render(request, 'duocmobile/index.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('')
		else:
			messages.info('Usuario o Contraseña incorrectos')
	context= {}
	return render(request, 'registration/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def misNotas(request):
    alumno = request.user.perfil
    notas = Notas.objects.filter(alumno = alumno.id)
    data={
        'notas':notas
    }
    return render(request, 'duocmobile/listado-notas.html', data)
