from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   path("", views.index, name="index"),
   path("about/", views.about, name="about"),
   path("error/", views.error, name="404"),
   path("cours/", views.cours, name="cours"),
   path("contanct/", views.contacts, name="contact"),
   path('forum/', views.forum_view, name='forum'),
   path('chat/', views.chat_view, name='chat'),
]
