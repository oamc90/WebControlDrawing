from django.shortcuts import render, redirect, get_object_or_404
from .form import EditarForm
from core.models import Drawing
from django.urls import reverse
from django.http import Http404


def editar(request):
    drawing = None
    form = None
    if request.method == 'GET':
        PN = request.GET.get('PN')
        Revision = request.GET.get('Revision')
        if PN and Revision:
            try:
                drawing = get_object_or_404(Drawing, PN=PN, Revision=Revision)
            except Http404:
                return redirect(reverse('revision') + "?error")

    form = EditarForm(instance=drawing)  # Instancia el formulario con el Drawing (si existe)

    if request.method == 'POST':
        PN = request.POST.get('PN')  # Asegurar que obtenemos los mismos datos del GET
        Revision = request.POST.get('Revision')

        if PN and Revision:
            drawing = Drawing.objects.filter(PN=PN, Revision=Revision).first()
        
        if drawing:  # Verifica que se haya encontrado el objeto antes de editar
            form = EditarForm(request.POST, instance=drawing)

        if form.is_valid():
            form.save()
            return redirect(reverse('editar') + "?ok")  # Redirige en caso de éxito

    return render(request, 'editar/editar.html', {'form': form, 'drawing': drawing})
