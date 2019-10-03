"""archikon_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from archikon_backend import views

router = routers.DefaultRouter()
router.register(r'slideshows', views.SlideShowViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'awards', views.AwardViewSet)
router.register(r'about', views.AboutViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'contact', views.ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
