from django.shortcuts import render, redirect
from .form import FormularioForm
from django.urls import reverse


# Create your views here.
def formulario(request):
    if request.method == 'POST':
        formulario = FormularioForm(request.POST)
        if formulario.is_valid():
            drawing = formulario.save()  # Guarda el formulario en el modelo Drawing
            return redirect(reverse('formulario')+"?ok") # Redirige a una página de éxito
            # o return HttpResponseRedirect('/success/')
    else:
        formulario = FormularioForm()
    return render(request,"formulario/formulario.html", {'formulario': formulario})