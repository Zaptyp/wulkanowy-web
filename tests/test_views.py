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
        print("\033[94mTesting login view...")
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'frontend/index.html')
        if response.status_code == 200:
            print("\033[92mPassed!")
        else:
            print("\033[91mFailed!")

        #CONTENT_VIEW
        print("\033[94mTesting content view...")
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 302)
        if response.status_code == 302:
            print("\033[92mPassed!")
        else:
            print("\033[91mFailed!")

        #ACCOUNT_MANAGER
        print("\033[94mTesting account manager view...")
        response = self.client.get(reverse('account_manager'))
        
        self.assertEquals(response.status_code, 302)
        if response.status_code == 302:
            print("\033[92mPassed!")
        else:
            print("\033[91mFailed!")

        #API
        data = {
            "loginName": "jan@fakelog.cf",
            "Password": "jan123",
            "Symbol": "powiatwulkanowy",
            "diaryUrl": "http://cufs.fakelog.cf/"
        }
        
        print("\033[94mTesting login...")

        response = self.client.post(reverse('login'), content_type='application/xml', data=json.dumps(data))
        cookies_data = response.json()
        
        self.assertEquals(response.status_code, 200)
        if response.status_code == 200:
            print("\033[92mPassed!")
        else:
            print("\033[91mFailed!")

        students = cookies_data['data']['students']['data']
        #JAN
        print("\033[94mTesting registering as Jan Kowalski...")
        jan_data = students[0]
        cookies_data['data']['students']['data'] = [jan_data]
        get_data_test(self.client, cookies_data, self.assertEquals)
        if response.status_code == 200:
            print("\033[92mPassed!")
        else:
            print("\033[91mFailed!")
        print("\033[95m============================================================")
        #JOANNA
        print("\033[94mTesting registering as Joanna Czerwińska...")
        joanna_data = students[3]
        cookies_data['data']['students']['data'] = [joanna_data]
        get_data_test(self.client, cookies_data, self.assertEquals)
        log_out_test(self.client, self.assertEquals)
        if response.status_code == 200:
            print("\033[92mPassed!")
        else:
            print("\033[91mFailed!")


def get_data_test(client, cookies_data, assertEquals):
    #GRADES
    print("\033[94mTesting grades...")
    response = client.post(reverse('grades'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #TIMETABLE
    print("\033[94mTesting timetable...")
    response = client.post(reverse('timetable'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #EXAMS
    print("\033[94mTesting exams...")
    response = client.post(reverse('exams'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #HOMEWORKS
    print("\033[94mTesting homeworks...")
    response = client.post(reverse('homeworks'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #ATTENDANCE
    print("\033[94mTesting attendance...")
    response = client.post(reverse('attendance'), content_type='application/xml', data=json.dumps({'cookies': json.dumps(cookies_data), 'week': 0}))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #NOTES
    print("\033[94mTesting notes...")
    response = client.post(reverse('notes'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #SCHOOL DATA
    print("\033[94mTesting school data...")
    response = client.post(reverse('school_data'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #DASHBOARD
    print("\033[94mTesting dashboard...")
    response = client.post(reverse('dashboard'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")
    
    #MOBILE ACCESS
    #REGISTERED DEVICES
    print("\033[94mTesting registered devices...")
    response = client.post(reverse('registered_devices'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #REGISTER DEVICE
    print("\033[94mTesting registering device...")
    response = client.post(reverse('register_device'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #MESSAGES
    #RECEIVED MESSAGES
    print("\033[94mTesting received messages...")
    messages_ids = []
    response = client.post(reverse('received_messages'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    messages_ids.append([response.json()['data']])
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #SENT MESSAGES
    print("\033[94mTesting sent messages...")
    response = client.post(reverse('sent_messages'), content_type='appication/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    for id in response.json()['data']:
        messages_ids.append(id)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #DELETED MESSAGES
    print("\033[94mTesting deleted messages...")
    response = client.post(reverse('deleted_messages'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    messages_ids.append([response.json()['data']])
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #GET RECIPIENTS
    print("\033[94mTesting getting recipients...")
    response = client.post(reverse('recipients'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    recipients = response.json()['addressee']['data']
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #STUDENT DATA
    print("\033[94mTesting student data...")
    response = client.post(reverse('student_data'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #STATS
    #PARTIAL
    print("\033[94mTesting partial grades stats...")
    response = client.post(reverse('partial'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")

    #YEAR
    print("\033[94mTesting year grades stats...")
    response = client.post(reverse('year'), content_type='application/xml', data=json.dumps(cookies_data))
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
        print("\033[91mFailed!")

    #SEND MESSAGE
    print("\033[94mTesting sending message...")
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
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")
        
    #GETTING MESSAGE CONTENT
    print("\033[94mTesting getting content of message...")
    for id in messages_ids:
        send_data = {
            'cookies_data': json.dumps(cookies_data),
            'message_id': id
        }
        response = client.post(reverse('message_content'), content_type='application/xml', data=json.dumps(send_data))
        assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")
    
def log_out_test(client, assertEquals):
    #LOG OUT
    print("\033[94mTesting logging out...")
    response = client.get(reverse('log_out'), content_type='application/xml')
    assertEquals(response.status_code, 200)
    if response.status_code == 200:
       print("\033[92mPassed!")
    else:
       print("\033[91mFailed!")
