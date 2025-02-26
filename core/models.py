from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Proyecto"
        #verbose_name_pural="Proyectos"
        ordering=["-created"]

    def __str__(self):
        return self.name
    
class Drawing(models.Model):
    PN= models.CharField(max_length=100)
    Description= models.CharField(max_length=100)
    Revision=models.CharField(max_length=10, default="A")

    estados = (
        ('Not Started', 'Not Started'),
        ('Ready for review', 'Ready for review'),
        ('Sent for corrections', 'Sent for corrections'),
        ('Proposal OK', 'Proposal OK'),
        ('PLM uploaded', 'PLM uploaded'),
    )
    Status= models.CharField(max_length=100, choices=estados, default='Not started')

    ruta= models.CharField(max_length=100)
    proyecto= models.ManyToManyField(Project, verbose_name="Proyectos")
    Emisor= models.ForeignKey(User,verbose_name="Emisor", on_delete=models.CASCADE, related_name="Emisor")
    Aprobador=models.ForeignKey(User,verbose_name="Aprobador", on_delete=models.CASCADE, related_name="Aprovador")
    date=models.DateTimeField(verbose_name="Fecha de emision", default=now())
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Drawing"
        #verbose_name_pural="Proyectos"
        ordering=["-created"]

    def save(self, *args, **kwargs):
        if not self.PN:  # Solo actualizar si PN está vacío
            self.PN = self.Description[:8] if self.Description else ""
        super().save(*args, **kwargs)

    def __str__(self):
        return self.PN
    