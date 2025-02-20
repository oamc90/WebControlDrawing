from django.shortcuts import render
from .models import Drawing, Project
from formulario.form import ProjectFilterForm

# Create your views here.
def home(request):
    drawings=Drawing.objects.all()

    project_id = request.GET.get('project')  # Obtén el ID del proyecto del query string

    if project_id:
        try:
            project_id = int(project_id)  # Convierte a entero
            drawings = drawings.filter(proyecto__id=project_id)  # Filtra por proyecto
        except ValueError:
            pass  # Ignora si project_id no es un entero válido

    form = ProjectFilterForm(request.GET or None)  # Inicializa el formulario con datos GET

    return render(request,"core/home.html", {'drawings':drawings, 'form':form})

