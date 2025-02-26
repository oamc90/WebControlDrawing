from django.shortcuts import render, redirect, get_object_or_404
from .form import EditarForm
from core.models import Drawing
from django.urls import reverse
from django.http import Http404
from django.core.mail import send_mail  # Importa la función para enviar correos
from django.conf import settings  # Importa la configuración de Django


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

            # Envío de correo electrónico
            asunto = f'Plano editado: {drawing.PN} - Revisión {drawing.Revision}'
            mensaje = f'El plano {drawing.PN} con revisión {drawing.Revision} ha sido editado.\n\n '
            #mensaje += f'Editado por: {drawing.Emisor}'
            mensaje += f'Estado del documento: {drawing.Status}'

            correo_desde = settings.EMAIL_HOST_USER  # Usa el correo configurado en settings.py
            correo_destino = [drawing.Aprobador.email, drawing.Emisor.email]  # Reemplaza con el destinatario

            send_mail(asunto, mensaje, correo_desde, correo_destino)

            return redirect(reverse('editar') + "?ok")  # Redirige en caso de éxito

    return render(request, 'editar/editar.html', {'form': form, 'drawing': drawing})
