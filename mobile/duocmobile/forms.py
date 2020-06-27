from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        exclude = ('email',)

class materialApoyoForm(ModelForm):
	class Meta:
		model = materialApoyo
		fields = ['titulo', 'archivo', 'curso', 'docente']
		exclude = ('docente',)

class ProfileForm(ModelForm):
	class Meta:
		model = Perfil
		fields = ['nombre', 'apellido', 'telefono', 'email']

class DocenteForm(ModelForm):
    class Meta:
        model = Docente
        fields = []

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['cursos']

class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitud
        fields = ['matricula', 'categoria', 'servicio', 'comentario']