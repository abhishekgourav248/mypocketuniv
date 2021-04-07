from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('AdminHome/', views.index, name="AdminHome"),
    path('StaffHome/', views.StaffHome, name="StaffHome"),
    path('StudentHome/', views.StudentHome, name="StudentfHome"),
]
