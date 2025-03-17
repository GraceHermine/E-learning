from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('enseignanthomepage/', views.HomeEnseignant, name='enseignanthomepage'),
    path("Emplois du Temps/",views.emploi_du_temps_view, name='emploidutemps'),
    path("Home/",views.emploi_du_temps_view, name='Home'),
    
#     path('login/', auth_views.LoginView.as_view(template_name='administration/templates/logout.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
]