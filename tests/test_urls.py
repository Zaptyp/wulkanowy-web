from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import default_view, content_view
from app.views import login, grades, timetable, exams, homeworks, attendance, notes

class TestUrls(SimpleTestCase):
    #views
    def test_home_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, default_view)

    def test_content_is_resolved(self):
        url = reverse('content')
        self.assertEquals(resolve(url).func, content_view)

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