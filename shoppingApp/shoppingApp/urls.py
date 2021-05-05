"""shoppingApp URL Configuration

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
    2. Add a URL to urlpatterns:  path('products/', include('products.urls'))
"""
from products.views import search_auto
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('userAuthentication/', include('django.contrib.auth.urls')),
    path('userAuthentication/', include('userAuthentication.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('search_auto/', views.search_auto, name='search_auto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
