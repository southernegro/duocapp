from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .forms import CustomUserForm, materialApoyoForm, ProfileForm, DocenteForm, StudentForm, SolicitudForm


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


def registerStudent(request):
    data = {
        'form': CustomUserForm(),
        'profile': ProfileForm(),
        'student': StudentForm()
    }
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        student = StudentForm(request.POST)
        if form.is_valid() and profile.is_valid() and student.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            student = student.save()
            student.user = profile
            student.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect(to='index')
        data['form']=form
        data['profile']=profile
        data['student']=student
    return render(request, 'registration/register_student.html', data)

def registerDocente(request):
    data = {
       'form': CustomUserForm(),
        'profile': ProfileForm(),
        'docente': DocenteForm()
    }
    if request.method=='POST':
        form = CustomUserForm(request.POST)
        profile = ProfileForm(request.POST)
        docente = DocenteForm(request.POST)
        if form.is_valid() and profile.is_valid() and docente.is_valid():
            new_user = form.save()
            profile = profile.save(commit=False)
            profile.user = new_user
            profile.save()
            docente = docente.save(commit=False)
            docente.profile = profile
            docente.save()
            #autenticar el usuario y redirigirlo
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            #autentificamos credenciales del usuario
            user = authenticate(username=username, password=password)
            return redirect(to='listado_usuarios')
        data['form']=form
        data['profile']=profile
        data['docente']=docente
    return render(request, 'registration/register_docente.html', data)

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

def listUser(request):
    users = Perfil.objects.all()
    data={
        'users': users
    }
    return render(request, 'duocmobile/listado_usuarios.html', data)

def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    perfil = Perfil.objects.get(user_id=pk)
    user.delete()
    perfil.delete()
    return redirect(to='listado_usuarios')

@login_required
def asistencia(request):
    student = request.user.perfil.student
    cursos = Curso.objects.filter(student = student.id)
    data={
        'cursos': cursos
        }
    return render(request, 'duocmobile/asistencia.html', data)

@login_required
def solicitud(request):
    usuario = request.user.perfil
    data={
        'usuario':usuario, 'form': SolicitudForm()
    }
    if request.method=='POST':
        formulario = SolicitudForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        data['form'] = formulario
    return render(request, 'duocmobile/solicitud.html', data)

def certificado(request):
    return render(request, 'duocmobile/certificado.html', {})

def horario(request):
    return render(request, 'duocmobile/horario.html', {})

@login_required
def horario(request):
    return render(request, 'duocmobile/horario.html', {})

@login_required
def calendario(request):
    return render(request, 'duocmobile/calendario.html', {})

@login_required
def biblioteca(request):
    return render(request, 'duocmobile/biblioteca.html', {})

@login_required
def asistencia_doc(request):
    docente = request.user.perfil.docente
    alumnos = Student.objects.all()
    cursos = Curso.objects.filter(docente = docente.id)
    data={
        'alumnos': alumnos, 'cursos':cursos
        }
    return render(request, 'duocmobile/asistencia_doc.html', data)

def edit_user(request, pk):
    usuario = User.objects.get(pk=pk)
    perfil = Perfil.objects.get(user_id=pk)
    data = {
        'form': CustomUserForm(instance=usuario),
        'profile': ProfileForm(instance=perfil)
    }
    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST, instance=usuario)
        profile = ProfileForm(data=request.POST, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            profile.save()
            data['mensaje']='Usuario modificado correctamente'
            return redirect(to='listado_usuarios')
        data['form']=CustomUserForm(instance=User.objects.get(pk=pk))
        data['profile']=ProfileForm(instance=perfil)
    return render(request,'registration/edit_user.html', data)