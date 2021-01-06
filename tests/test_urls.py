from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import default_view, content_view
from app.views import login

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