from django.urls import path
from IIT import views
urlpatterns = [
   path('', views.index, name='index'),
]
