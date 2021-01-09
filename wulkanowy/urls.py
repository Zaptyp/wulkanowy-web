"""mypage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from app.views import default_view, content_view
from app.views import login, grades, timetable, exams

urlpatterns = [
    #views
    path('', default_view, name='home'),
    path('content/', content_view, name='content'),
    #api
    path('api/login', login, name='login'),
    path('api/grades', grades, name='grades'),
    path('api/timetable', timetable, name='timetable'),
    path('api/exams', exams, name='exams')
]

urlpatterns += staticfiles_urlpatterns()