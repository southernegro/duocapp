from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.index, name="index"),
	path('login/', views.loginPage, name="login"),
	path('register_student/', views.registerStudent, name="register_student"),
	path('register_docente/', views.registerDocente, name="register_docente"),
	path('listado_usuarios/', views.listUser, name="listado_usuarios"),
	path('accounts/logout/', views.logoutUser, name="logout"),
	path('accounts/profile/', views.perfil, name="perfil"),
	path('listadoasignaturas/', views.listado_asignaturas, name="listado_asignaturas"),
	path('listadocursos/', views.listado_cursos, name="listado_cursos"),
	path('alumnoscriticos/', views.alumnos_criticos, name="alumnos_criticos"),
	path('listanonotas/', views.misNotas, name="listado_notas"),
	path('admin/users/delete/<pk>/',views.deleteUser, name='delete_user'),
	path('asistencia/', views.asistencia, name="asistencia"),
	path('solicitud/', views.solicitud, name="solicitud"),
	path('certificado/', views.certificado, name="certificado"),
	path('horario/', views.horario, name="horario"),
	path('calendario/', views.calendario, name="calendario"),
	path('biblioteca/', views.biblioteca, name="biblioteca"),
	path('asistencia_doc/', views.asistencia_doc, name="asistencia_doc"),
	path('edit_user/<pk>/', views.edit_user, name="edit_user"),
	path('config/', views.config, name="config"),
	path('tne/', views.tne, name="tne"),
	path('registro_secciones/', views.registro_secciones, name="registro_secciones"),
	path('contenido/', views.contenido, name="contenido"),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)