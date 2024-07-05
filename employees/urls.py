from django.urls import path
from . import views

urlpatterns = [
    path('employee_count/', views.employee_count, name='employee_count'),
]
