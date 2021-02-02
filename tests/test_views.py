from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.csrf_token = Client(enforce_csrf_checks=True)
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

        #ACCOUNT_MANAGER
        response = self.client.get(reverse('account_manager'))
        
        self.assertEquals(response.status_code, 302)

        #API
        data = {
            "loginName": "jan@fakelog.cf",
            "Password": "jan123",
            "Symbol": "powiatwulkanowy",
            "diaryUrl": "http://cufs.fakelog.cf/"
        }

        response = self.client.post(reverse('login'), content_type='application/xml', data=json.dumps(data))
        cookies_data = response.json()
        
        self.assertEquals(response.status_code, 200)

        students = cookies_data['data']['students']['data']
        #JAN
        jan_data = students[0]
        cookies_data['data']['students']['data'] = [jan_data]
        get_data_test(self.client, cookies_data, self.assertEquals)
        #JOANNA
        joanna_data = students[3]
        cookies_data['data']['students']['data'] = [joanna_data]
        get_data_test(self.client, cookies_data, self.assertEquals)
        log_out_test(self.client, self.assertEquals)


def get_data_test(client, cookies_data, assertEquals):
    #GRADES
    response = client.post(reverse('grades'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)

    #TIMETABLE
    response = client.post(reverse('timetable'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)

    #EXAMS
    response = client.post(reverse('exams'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)

    #HOMEWORKS
    response = client.post(reverse('homeworks'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)

    #ATTENDANCE
    response = client.post(reverse('attendance'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)

    #NOTES
    response = client.post(reverse('notes'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)

    #SCHOOL DATA
    response = client.post(reverse('school_data'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)

    #DASHBOARD
    response = client.post(reverse('dashboard'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    
    #MOBILE ACCESS
    #REGISTERED DEVICES
    response = client.post(reverse('registered_devices'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)

    #REGISTER DEVICE
    response = client.post(reverse('register_device'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)

    #MESSAGES
    #RECEIVED MESSAGES
    messages_ids = []
    response = client.post(reverse('received_messages'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    messages_ids.append([response.json()['data']])

    #SENT MESSAGES
    response = client.post(reverse('sent_messages'), content_type='appication/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    for id in response.json()['data']:
        messages_ids.append(id)

    #DELETED MESSAGES
    response = client.post(reverse('deleted_messages'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    messages_ids.append([response.json()['data']])

    #GET RECIPIENTS
    response = client.post(reverse('recipients'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    recipients = response.json()['addressee']['data']

    #STUDENT DATA
    response = client.post(reverse('student_data'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)

    #SEND MESSAGE
    for recipient in recipients:
        send_data = {
            'cookies_data': json.dumps(cookies_data),
            'data': recipient,
            'subject': 'Test subject',
            'content': 'Test content'
        }
        response = client.post(reverse('send_message'), content_type='application/xml', data=json.dumps(send_data))
        assertEquals(response.status_code, 200)
        
    #GETTING MESSAGE CONTENT
    for id in messages_ids:
        send_data = {
            'cookies_data': json.dumps(cookies_data),
            'message_id': id
        }
        response = client.post(reverse('message_content'), content_type='application/xml', data=json.dumps(send_data))
        assertEquals(response.status_code, 200)
    
def log_out_test(client, assertEquals):
    #LOG OUT
    response = client.get(reverse('log_out'), content_type='application/xml')
    assertEquals(response.status_code, 200)