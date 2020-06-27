from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Perfil)
admin.site.register(Carrera)
admin.site.register(Asignatura)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Student)
admin.site.register(Notas)
admin.site.register(AlumnosCriticos)
admin.site.register(materialApoyo)
admin.site.register(Admin)
admin.site.register(Solicitud)

class CursosAlumno(admin.ModelAdmin):
    fields = ['cursos', 'student']
    list_display = ('get_cursos', 'student')

    def get_cursos(self):
        return "\n".join([c.cursos for c in cursos.product.all()])