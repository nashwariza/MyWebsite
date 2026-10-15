from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('doctors/', views.doctors, name='doctors'),
    path('add_doc', views.add_doctor, name='add_doctor'),
    path('edit_doc', views.edit_doctor, name='edit_doctor'),
    
]