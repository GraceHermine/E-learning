# api/urls.py
...
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EtudiantViewSet, ForumViewSet, ReclamationViewSet, CoursViewSet, SalleViewSet, EvaluationViewSet, NoteViewSet

router = DefaultRouter()
router.register(r'etudiants', EtudiantViewSet)
router.register(r'forums', ForumViewSet)
router.register(r'reclamations', ReclamationViewSet)
router.register(r'cours', CoursViewSet)
router.register(r'salles', SalleViewSet)
router.register(r'evaluations', EvaluationViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
