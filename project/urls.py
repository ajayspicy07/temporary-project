

''' PROJECT URLS '''

from django.urls import path
from . import views



urlpatterns = [
  
    path('projects/', views.projects , name="Projects"),
    path('Projects/<slug:pk>/', views.projectdetail, name="Project_Details"),
    path('banners/<slug:pk>/', views.banner,name="Banner"),
    
    path('<slug:pk>/createproject/', views.createproject, name="Create_Project"),
    
    path('<slug:ppk>/<slug:pk>/updateproject/', views.updateproject, name="Update_Post"),
    
    path('<slug:ppk>/<slug:pk>/deleteproject/', views.deleteproject, name="Delete_Project"),
    
]


