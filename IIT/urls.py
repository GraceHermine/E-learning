from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
   path("", views.index, name="index"),
   path("about/", views.about, name="about"),
   
   path("cours/", views.cours, name="cours"),
   
   path('forum/', views.forum_view, name='forum'),
   path('chat/', views.chat_view, name='chat'),
   path('detail_forum/<int:id>/', views.forum_detail, name='details_forum'),
   
]
