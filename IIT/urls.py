from django.urls import path,include 
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
# import administration.views
urlpatterns = [
   path("", views.index, name="index"),
   path("about/", views.about, name="about"),
   
   path("cours/", views.cours, name="cours"),

   
   path('forum/', views.forum_view, name='forum'),
   path('chat/', views.chat_view, name='chat'),
   path('detail_forum/<int:id>/', views.forum_detail, name='details_forum'),

 
   path('forum/', views.forum_view, name='forum'),
   path('chat/', views.chat_view, name='chat'),
   path('api-auth/', include('rest_framework.urls')),
   path('Homepage/', views.Studentpage, name='StudentHome'),
    # ramene la page d'acceuil de l'enseignant
   path('administration/', include('administration.urls')),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),


]


