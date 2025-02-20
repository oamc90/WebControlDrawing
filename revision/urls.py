from django.urls import path
from . import views

urlpatterns = [
    path('',views.revision, name="revision"),
]