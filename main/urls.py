from django.urls import path
from . import views

urlpatterns = [
    path('', views.notas, name='notas'),
    path('nova_nota/', views.nova_nota, name='nova_nota'),
    path('editar_nota/<int:id>/', views.editar_nota, name='editar_nota'),
    path('deletar_nota/<int:id>/', views.deletar_nota, name='deletar_nota'),
]