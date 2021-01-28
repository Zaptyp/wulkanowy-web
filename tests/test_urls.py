from django.test import SimpleTestCase
from django.urls import reverse, resolve
from frontend.views import default_view, content_view, account_manager_view
from app.views import login, grades, timetable, exams, homeworks, attendance, notes, school_data, dashboard, registered_devices, register_device_, received_messages, sent_messages, deleted_messages, recipients, send, message_content

class TestUrls(SimpleTestCase):
    #views
    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, default_view)

    def test_content_is_resolved(self):
        url = reverse('content')
        self.assertEquals(resolve(url).func, content_view)

    def test_account_manager_is_resolved(self):
        url = reverse('account_manager')
        self.assertEquals(resolve(url).func, account_manager_view)

    #API
    def test_login_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_grades_is_resolved(self):
        url = reverse('grades')
        self.assertEquals(resolve(url).func, grades)

    def test_timetable_is_resolved(self):
        url = reverse('timetable')
        self.assertEquals(resolve(url).func, timetable)

    def test_exams_is_resolved(self):
        url = reverse('exams')
        self.assertEquals(resolve(url).func, exams)

    def test_homeworks_is_resolved(self):
        url = reverse('homeworks')
        self.assertEquals(resolve(url).func, homeworks)

    def test_attendance_is_resolved(self):
        url = reverse('attendance')
        self.assertEquals(resolve(url).func, attendance)

    def test_notes_is_resolved(self):
        url = reverse('notes')
        self.assertEquals(resolve(url).func, notes)

    def test_school_data_is_resolved(self):
        url = reverse('school_data')
        self.assertEquals(resolve(url).func, school_data)

    def test_dashboard_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    #MOBILE ACCESS
    def test_registered_devices_is_resolved(self):
        url = reverse('registered_devices')
        self.assertEquals(resolve(url).func, registered_devices)

    def test_register_device_is_resolved(self):
        url = reverse('register_device')
        self.assertEquals(resolve(url).func, register_device_)

    #MESSAGES
    def test_received_messages_is_resolved(self):
        url = reverse('received_messages')
        self.assertEquals(resolve(url).func, received_messages)

    def test_sent_messages_is_resolved(self):
        url = reverse('sent_messages')
        self.assertEquals(resolve(url).func, sent_messages)

    def test_deleted_messages_is_resolved(self):
        url = reverse('deleted_messages')
        self.assertEquals(resolve(url).func, deleted_messages)

    def test_get_recipients_is_resolved(self):
        url = reverse('recipients')
        self.assertEquals(resolve(url).func, recipients)

    def test_send_message_is_resolved(self):
        url = reverse('send_message')
        self.assertEquals(resolve(url).func, send)

    def test_get_message_content_is_resolved(self):
        url = reverse('message_content')
        self.assertEquals(resolve(url).func, message_content)