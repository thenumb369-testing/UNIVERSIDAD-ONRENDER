from django.shortcuts import render, redirect
from .models import Curso

# 1. Vista principal: Carga la tabla con los cursos
def home(request):
    cursosListados = Curso.objects.all()
    # Usamos "gestioncursos.html" en minúsculas para que coincida con tu archivo
    return render(request, "gestioncursos.html", {"cursos": cursosListados})

# 2. Registrar curso: Guarda los datos del formulario
def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

# 3. Eliminar curso: Borra un registro usando su código
def eliminarCurso(request, codigo): 
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

# 4. Abrir formulario de edición: Carga los datos en edicionCurso.html
def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

# 5. Procesar la actualización: Guarda los cambios editados
def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')