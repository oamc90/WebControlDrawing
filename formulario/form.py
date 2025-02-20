from django import forms
from core.models import Project, Drawing
from django.contrib.auth.models import User


# solo formulario sin enlace al modelo
# class FormularioForm(forms.Form):
#   Descripcion = forms.CharField(label="Descripcion")
 #   Ruta = forms.CharField(label="Ruta")
  #  Proyecto = forms.ModelChoiceField(queryset=Project.objects.all(), empty_label="Selecciona el proyecto")
   # Emisor = forms.ModelChoiceField(queryset=User.objects.all(), label="Emisor")
    #Aprovador = forms.ModelChoiceField(queryset=User.objects.all(), label="Aprobador")



class FormularioForm(forms.ModelForm):
    class Meta:
        model = Drawing
        fields = ['Description', 'ruta', 'proyecto', 'Emisor', 'Aprobador'] # campos visibles en el formulario

    Description = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Nombre del archivo"}), min_length=3, max_length=100)
    ruta = forms.CharField(label="Ruta", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Ruta en disco"}), min_length=3, max_length=100)
    proyecto = forms.ModelMultipleChoiceField(queryset=Project.objects.all(), label="Proyecto",required=True) # Para ManyToMany
    Emisor = forms.ModelChoiceField(queryset=User.objects.all(), label="Emisor", required=True)
    Aprobador = forms.ModelChoiceField(queryset=User.objects.all(), label="Aprobador", required=True)


class ProjectFilterForm(forms.Form):
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        empty_label="------",  # Opción para mostrar todos los proyectos
        required=False  # No es obligatorio seleccionar un proyecto
    )