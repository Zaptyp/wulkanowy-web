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
        print("Testing login view...")
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/index.html')
        if response.status_code == 200:
            print("Passed!")

        #CONTENT_VIEW
        print("Testing content view...")
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 302)
        if response.status_code == 302:
            print("Passed!")

        #ACCOUNT_MANAGER
        print("Testing account manager view...")
        response = self.client.get(reverse('account_manager'))
        
        self.assertEquals(response.status_code, 302)
        if response.status_code == 302:
            print("Passed!")

        #API
        data = {
            "loginName": "jan@fakelog.cf",
            "Password": "jan123",
            "Symbol": "powiatwulkanowy",
            "diaryUrl": "http://cufs.fakelog.cf/"
        }
        
        print("Testing login...")

        response = self.client.post(reverse('login'), content_type='application/xml', data=json.dumps(data))
        cookies_data = response.json()
        
        self.assertEquals(response.status_code, 200)

        students = cookies_data['data']['students']['data']
        #JAN
        print("Testing registering as Jan Kowalski...")
        jan_data = students[0]
        cookies_data['data']['students']['data'] = [jan_data]
        get_data_test(self.client, cookies_data, self.assertEquals)
        if response.status_code == 200:
            print("Passed!")
        #JOANNA
        print("Testing registering as Joanna Czerwińska...")
        joanna_data = students[3]
        cookies_data['data']['students']['data'] = [joanna_data]
        get_data_test(self.client, cookies_data, self.assertEquals)
        log_out_test(self.client, self.assertEquals)
        if response.status_code == 200:
            print("Passed!")


def get_data_test(client, cookies_data, assertEquals):
    #GRADES
    print("Testing grades...")
    response = client.post(reverse('grades'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #TIMETABLE
    print("Testing timetable...")
    response = client.post(reverse('timetable'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #EXAMS
    print("Testing exams...")
    response = client.post(reverse('exams'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #HOMEWORKS
    print("Testing homeworks...")
    response = client.post(reverse('homeworks'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #ATTENDANCE
    print("Testing attendance...")
    response = client.post(reverse('attendance'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #NOTES
    print("Testing notes...")
    response = client.post(reverse('notes'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #SCHOOL DATA
    print("Testing school data...")
    response = client.post(reverse('school_data'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #DASHBOARD
    print("Testing dashboard...")
    response = client.post(reverse('dashboard'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")
    
    #MOBILE ACCESS
    #REGISTERED DEVICES
    print("Testing registered devices...")
    response = client.post(reverse('registered_devices'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #REGISTER DEVICE
    print("Testing registering device...")
    response = client.post(reverse('register_device'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #MESSAGES
    #RECEIVED MESSAGES
    print("Testing received messages...")
    messages_ids = []
    response = client.post(reverse('received_messages'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    messages_ids.append([response.json()['data']])
    if response.status_code == 200:
       print("Passed!")

    #SENT MESSAGES
    print("Testing sent messages...")
    response = client.post(reverse('sent_messages'), content_type='appication/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    for id in response.json()['data']:
        messages_ids.append(id)
    if response.status_code == 200:
       print("Passed!")

    #DELETED MESSAGES
    print("Testing deleted messages...")
    response = client.post(reverse('deleted_messages'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    messages_ids.append([response.json()['data']])
    if response.status_code == 200:
       print("Passed!")

    #GET RECIPIENTS
    print("Testing getting recipients...")
    response = client.post(reverse('recipients'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    recipients = response.json()['addressee']['data']
    if response.status_code == 200:
       print("Passed!")

    #STUDENT DATA
    print("Testing student data...")
    response = client.post(reverse('student_data'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #STATS
    #PARTIAL
    print("Testing partial grades stats...")
    response = client.post(reverse('partial'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #YEAR
    print("Testing year grades stats...")
    response = client.post(reverse('year'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")

    #SEND MESSAGE
    print("Testing sending message...")
    for recipient in recipients:
        send_data = {
            'cookies_data': json.dumps(cookies_data),
            'data': recipient,
            'subject': 'Test subject',
            'content': 'Test content'
        }
        response = client.post(reverse('send_message'), content_type='application/xml', data=json.dumps(send_data))
        assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")
        
    #GETTING MESSAGE CONTENT
    print("Testing getting content of message...")
    for id in messages_ids:
        send_data = {
            'cookies_data': json.dumps(cookies_data),
            'message_id': id
        }
        response = client.post(reverse('message_content'), content_type='application/xml', data=json.dumps(send_data))
        assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("Passed!")
    
def log_out_test(client, assertEquals):
    #LOG OUT
    print("Testing logging out...")
    response = client.get(reverse('log_out'), content_type='application/xml')
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92m Passed!")
