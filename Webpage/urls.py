"""Webpage URL Configuration

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
from django.urls import path
from Details.views import extract_data, all_Details
from Details.views import extract
from Details.views import savedata
#from Details.views import my_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # /path('',extract_data/<str:url>/<str:xpath>/,name="extract_data"),
    path('',extract,name="extract"),
   # path('savedata/',savedata,name="savedata")
    path('Details/',all_Details,name="list"),

]
