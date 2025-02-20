from django import forms
from core.models import Project, Drawing
from django.contrib.auth.models import User


class EditarForm(forms.ModelForm):
    class Meta:
        model = Drawing
        fields = ['PN','Description', 'Revision','Status','ruta', 'proyecto','Emisor','Aprobador'] # campos visibles en el formulario
        widgets = {
            'PN': forms.TextInput(attrs={'readonly': True}), 
            'Revision': forms.TextInput(attrs={'readonly': True}),
            'Description': forms.TextInput(attrs={'readonly': True}), # Hace que PN sea de solo lectura
            
        }
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Emisor'].disabled = True
            self.fields['Aprobador'].disabled = True  # Desactiva la edición del campo
            self.fields['proyecto'].disabled = True # Desactiva la edición del campo
    
            
