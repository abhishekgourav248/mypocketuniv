from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage, name='login'),
    path('logout/', views.dologout, name='logout'),
    path('dologin', views.dologin),
    path('app/', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
