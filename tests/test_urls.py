from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import default_view, grades_view, timetable_view, exams_view, homework_view, attendance_view, messages_view, notes_view, change_messages_content
from app.views import login

class TestUrls(SimpleTestCase):
    #views
    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, default_view)

    def test_grades_is_resolved(self):
        url = reverse('grades')
        self.assertEquals(resolve(url).func, grades_view)

    def test_timetable_is_resolved(self):
        url = reverse('timetable')
        self.assertEquals(resolve(url).func, timetable_view)

    def test_exams_is_resolved(self):
        url = reverse('exams')
        self.assertEquals(resolve(url).func, exams_view)
    
    def test_homework_is_resolved(self):
        url = reverse('homework')
        self.assertEquals(resolve(url).func, homework_view)

    def test_attendance_is_resolved(self):
        url = reverse('attendance')
        self.assertEquals(resolve(url).func, attendance_view)

    def test_messages_is_resolved(self):
        url = reverse('messages')
        self.assertEquals(resolve(url).func, messages_view)

    def test_notes_is_resolved(self):
        url = reverse('notes')
        self.assertEquals(resolve(url).func, notes_view)

    def test_cmc_is_resolved(self):
        url = reverse('cmc')
        self.assertEquals(resolve(url).func, change_messages_content)

    #API
    def test_login_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)