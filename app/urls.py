from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs',views.index),
    path('blogs/nuevo', views.nuevo),
    path('blogs/crear', views.crear),
    path('blogs/<int:number>', views.mostrar),
    path('blogs/<int:number>/editar', views.editar),
    path('blogs/<int:number>/borrar', views.borrar),
    path('blogs/json', views.json1)
]