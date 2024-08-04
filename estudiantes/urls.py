from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiante/add/', views.add_estudiante, name='add_estudiante'),
    path('estudiante/edit/<int:id>/', views.edit_estudiante, name='edit_estudiante'),
    path('estudiante/delete/<int:id>/', views.delete_estudiante, name='delete_estudiante'),
]