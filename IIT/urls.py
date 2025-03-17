<<<<<<< HEAD
from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
# import administration.views


urlpatterns = [
    # ramene la page de l'acceuil
    path('', views.index, name="index"),
    path("about/", views.about, name="about"),
    path("error/", views.error, name="404"),
    path("cours/", views.cours, name="cours"),
    path("contact/", views.contacts, name="contact"),
    path('forum/', views.forum_view, name='forum'),
    path('chat/', views.chat_view, name='chat'),
    # ramene la page d'acceuil de l'eleve
    path('Homepage/', views.Studentpage, name='StudentHome'),
    # ramene la page d'acceuil de l'enseignant
    path('administration/', include('administration.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
# =======
# from django.urls import path,include 
# from django.contrib.auth import views as auth_views
# from . import views
# urlpatterns = [
#    path("", views.index, name="index"),
#    path("about/", views.about, name="about"),
#    path("error/", views.error, name="404"),
#    path("cours/", views.cours, name="cours"),
#    path("contact/", views.contacts, name="contact"),
#    path('forum/', views.forum_view, name='forum'),
#    path('chat/', views.chat_view, name='chat'),
   path('api-auth/', include('rest_framework.urls')),
 
# >>>>>>> d908e0825373ee22157592428c5789a66a55e449
]



