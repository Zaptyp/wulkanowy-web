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
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Wulkanowy.views import default_view, error_view, grades_view, timetable_view, exams_view, homework_view, attendance_view, messeges_view, notes_view

urlpatterns = [
    path('', default_view, name='home'),
    path('error/', error_view, name='error'),
    path('oceny/', grades_view, name='grades'),
    path('plan/', timetable_view, name='timetable'),
    path('sprawdziany/', exams_view, name='exams'),
    path('zadania/', homework_view, name='homework'),
    path('frekwencja/', attendance_view, name='attendance'),
    path('wiadomosci/', messeges_view, name='messeges'),
    path('uwagi/', notes_view, name='notes'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
