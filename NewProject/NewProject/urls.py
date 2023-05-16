"""NewProject URL Configuration

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
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='hii'),
    path('hi/<str:name>/',views.hai),
    path('hi/<str:name>/<int:age>/',views.hai),
    path('hlo/',views.helo,name='hello'),
    path('hi/<str:name>/<int:age>/<int:sal>/',views.hai),
    path('stu/<str:fname>/<str:lname>/<int:age>/',views.details),
    path('sample/',views.alerts),
    path('det/<str:fname>/<str:lname>/<int:age>/<int:adhar>/<int:pno>/',views.det),
    path('reg/',views.reg),
    path('sg/',views.index,name='home'),
    path('about/',views.about,name='ab'),
    path('contact/',views.contact,name='co'),
    path('',views.operations,name="op"),
    path('stview/<int:sv>/',views.sview,name="sv1"),
    path('sup/<int:u>/',views.supdate,name="sup"),
    path('sdel/<int:d>/',views.sdelete,name="sdelete1"),
]
