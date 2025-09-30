"""
URL configuration for exp_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mymap import views as image_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', image_views.map),
    path('map/mangal/', image_views.mangal, name="mangal"), 
    path('map/hotbreads/', image_views.hotbreads, name="hotbreads"),
    path('map/marriage/', image_views.marriage, name="marriage"),
    path('map/tskrishna/', image_views.tskrishna, name="tskrishna"),
    path('map/aadhar/', image_views.aadhar, name="aadhar"),
]
