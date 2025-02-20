from django import forms
from core.models import Drawing
from django.contrib.auth.models import User


class RevisionForm(forms.ModelForm):
    class Meta:
        model = Drawing
        fields = ['PN','Description', 'Revision','Status','ruta', 'proyecto','Emisor','Aprobador'] # campos visibles en el formulario
        widgets = {
            'PN': forms.TextInput(attrs={'readonly': True}), 
            'Description': forms.TextInput(attrs={'readonly': True}),
            'Revision': forms.TextInput(attrs={'readonly': True}),
             # Hace que PN sea de solo lectura
        }