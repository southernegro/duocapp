from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIPO_USUARIO = (
('Alumno', 'Alumno'),
('Docente', 'Docente'),
('Admin', 'Admin'),
)

MATRICULA = (
(' ', ' '),
('INGENIERIA INFORMATICA', 'INGENIERIA INFORMATICA'),
)
CATEGORIA = (
(' ', ' '),    
('ACADEMICO', 'ACADEMICO'),
('FINANCIERO', 'FINANCIERO'),
)
SERVICIO = (
(' ', ' '),
('ACTUALIZACION DATOS', 'ACTUALIZACION DATOS'),
('CONVALIDACION ASIGNATURA', 'CONVALIDACION ASIGNATURA'),
('NOTA PENDIENTE', 'NOTA PENDIENTE'),
('RENUNCIA', 'RENUNCIA'),
)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    tipo = models.CharField(default='Alumno', max_length=50, choices=TIPO_USUARIO)

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True, related_name='asignatura_carrera')
    codigo = models.CharField(max_length=10, null=True)
    nombre = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nombre

class Docente(models.Model):
    user = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.__str__()
    @property
    def is_docente(self):
        docente = False
        tipo = self.user.tipo
        if (tipo == 'Docente'):
            docente = True
        else:
            docente = False
        return docente

class Curso(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='curso_docente')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.SET_NULL, null=True, blank=True, related_name='curso_asignatura')
    seccion = models.CharField(max_length=10, null=True)
    def __str__(self):
        cod_asig = self.asignatura.codigo
        seccion = self.seccion
        codigo_curso = cod_asig + '-' + seccion
        return codigo_curso
    @property
    def docente_curso(request):
        return self.docente.user.nombre


class Student(models.Model):
    user = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    cursos = models.ManyToManyField(Curso)
    def __str__(self):
        return self.user.__str__()

    @property
    def is_alumno(self):
        alumno = False
        tipo = self.user.tipo
        if (tipo == 'Alumno'):
            alumno = True
        else:
            alumno = False
        return alumno

class Notas(models.Model):
    alumno = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='notas_alumno')
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True, related_name='notas_curso')
    nota1 = models.FloatField()
    nota2 = models.FloatField()
    nota3 = models.FloatField()
    notaP = models.FloatField()
    notaET = models.FloatField()
    notaFinal = models.FloatField()
    
    def __str__(self):
        alumno = self.alumno.user.nombre
        asignatura = self.curso.asignatura.codigo
        curso_cod = self.curso.seccion
        name_object = 'Notas ' + alumno +' '+ asignatura+'-'+curso_cod
        return name_object

    @property
    def prom(self):
        prom = (self.nota1 + self.nota2 + self.nota3)/3
        return prom

class AlumnosCriticos(models.Model):
    alumno = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='alumno_critico')
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True, related_name='alumno_curso')
    notas = models.ForeignKey(Notas, on_delete=models.SET_NULL, null=True, blank=True, related_name='notas_alumno')
    docente =models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='docente_alumno_critico')

class materialApoyo(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    archivo = models.FileField(upload_to ='media/') 
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True, related_name='material_curso')
    docente =models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='docente_material')

class Admin(models.Model):
    user = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.__str__()
    @property
    def is_admin(self):
        admin = False
        tipo = self.user.tipo
        if (tipo == 'Admin'):
            admin = True
        else:
            admin = False
        return admin

class Solicitud(models.Model):
    matricula = models.CharField(default='', max_length=500, choices=MATRICULA)
    categoria = models.CharField(default='', max_length=500, choices=CATEGORIA)
    servicio = models.CharField(default='', max_length=500, choices=SERVICIO)
    comentario = models.TextField(max_length=500, null=True)