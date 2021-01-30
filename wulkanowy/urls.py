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

from frontend.views import default_view, content_view, account_manager_view
from app.views import login, grades, timetable, exams, homeworks, attendance, notes, registered_devices, register_device_, received_messages, sent_messages, deleted_messages, school_data, dashboard, recipients, send, message_content, student_data

urlpatterns = [
    #views
    path('', default_view, name='home'),
    path('content/', content_view, name='content'),
    path('account-manager/', account_manager_view, name='account_manager'),
    #api
    path('api/login', login, name='login'),
    path('api/grades', grades, name='grades'),
    path('api/timetable', timetable, name='timetable'),
    path('api/exams', exams, name='exams'),
    path('api/homeworks', homeworks, name='homeworks'),
    path('api/attendance', attendance, name='attendance'),
    path('api/notes', notes, name='notes'),
    path('api/school_data', school_data, name='school_data'),
    path('api/dashboard', dashboard, name='dashboard'),
    path('api/student_data', student_data, name='student_data'),
    #MOBILE ACCESS
    path('api/mobile/registered', registered_devices, name='registered_devices'),
    path('api/mobile/register', register_device_, name='register_device'),
    #MESSAGES
    path('api/messages/received', received_messages, name='received_messages'),
    path('api/messages/sent', sent_messages, name='sent_messages'),
    path('api/messages/deleted', deleted_messages, name='deleted_messages'),
    path('api/messages/recipients', recipients, name='recipients'),
    path('api/messages/send', send, name='send_message'),
    path('api/messages/content', message_content, name='message_content'),
]

urlpatterns += staticfiles_urlpatterns()