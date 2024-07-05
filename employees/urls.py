from django.urls import path  # Importa la función path de Django para definir rutas URL
from . import views  # Importa las vistas definidas en el módulo actual (presumiblemente 'views.py')

urlpatterns = [
    path('employee_count/', views.employee_count, name='employee_count'),  # Define la ruta 'employee_count/' y asigna la vista 'employee_count' a esa ruta
]
