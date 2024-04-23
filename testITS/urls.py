"""
URL configuration for testITS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import generate_video_view
from .views import logs_view
from .views import generate_video_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-video/<str:text>/', generate_video_view, name='generate_video_url'),
    path('generate-video/', generate_video_page, name='generate_video_page'),
    path('logs/', logs_view, name='query_logs')
]
