"""Python_PSQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Configuración de la vista del esquema Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Python y PSQL",
      default_version='v1',
      description="Documentación para una consulta a una BD PSQL por medio de Python",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

# Lista de URLs configuradas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')), # URLs de la aplicación 'employees'
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # URL para la interfaz de Swagger
]
