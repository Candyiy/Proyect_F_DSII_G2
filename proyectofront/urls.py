"""
URL configuration for proyectofront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from appvista import views
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
=======
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> 5f3ae44d9e6ece5b9db81cfaac1b3de8adf6f898
    path('', views.home, name='home'),
    path('job/', views.job, name='job'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('empleos/', include('job.urls')),
<<<<<<< HEAD
    path('profile/', views.profile, name='profile'),
    path('listaPostulantes/', views.listapostulantes, name='lista_postulantes'),

]
=======
    path('listaPostulantes/', views.listapostulantes, name='lista_postulantes'),
    path('', include('usuarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 5f3ae44d9e6ece5b9db81cfaac1b3de8adf6f898
