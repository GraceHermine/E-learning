# IIT/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),  # Route pour la page "about"
    path('contact/', views.contact, name='contact'),  # Nouvelle route pour la page "contact"
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    # Ajoutez d'autres routes ici si nécessaire
]
