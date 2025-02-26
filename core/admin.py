from django.contrib import admin
from .models import Project, Drawing


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields= ( 'created', 'updated')

class DrawingAdmin(admin.ModelAdmin):
    readonly_fields= ( 'created', 'updated')
    #list_display= ('PN', 'Description','Revision', 'Status','ruta','Emisor__username','Aprobador__username', 'proyecto__name','date')
    #ordering= ('author', 'publish')
    #search_fields=('title','content', 'author__username')
    list_filter= ('Emisor__username','proyecto__name')


   # def post_categories(self,obj):

       # return ",".join([c.name for c in obj.categories.all().order_by("name")])
    #post_categories.short_description="categorias"

admin.site.register(Project, ProjectAdmin)
admin.site.register(Drawing, DrawingAdmin)