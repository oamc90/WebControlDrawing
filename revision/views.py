from django.shortcuts import render, redirect, get_object_or_404
from .form import RevisionForm
from core.models import Drawing
from django.urls import reverse
from django.http import Http404


def revision(request):
    drawing = None
    form = None
    if request.method == 'GET':
        PN = request.GET.get('PN')
        Revision = request.GET.get('Revision')
        if PN and Revision:
            try:
                drawing = get_object_or_404(Drawing, PN=PN, Revision=Revision)
                drawing.Revision = chr(ord(drawing.Revision)+1)
            except Http404:
                return redirect(reverse('revision') + "?error")

    form = RevisionForm(instance=drawing)  # Instancia el formulario con el Drawing (si existe)

    if request.method == 'POST':
        form = RevisionForm(request.POST)
        if form.is_valid():
            pn = request.POST.get('PN')
            revision = request.POST.get('Revision')
            if pn and revision and Drawing.objects.filter(PN=pn, Revision=revision).exists():
                return redirect(reverse('revision') + "?Nok")
            else:
                form.save()
                return redirect(reverse('revision') + "?ok")  # Redirige después de guardar

    return render(request, 'revision/revision.html', {'form': form, 'drawing': drawing})
