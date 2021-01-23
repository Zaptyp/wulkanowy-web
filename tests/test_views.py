from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('home')
        self.detail_url = reverse('content')

    def test_views(self):
        #DEFAULT_VIEW
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/index.html')

        #CONTENT_VIEW
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 302)