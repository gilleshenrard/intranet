from django.test import TestCase, Client
from django.core.urlresolvers import reverse, NoReverseMatch
from rest_framework import status
from api.models import User
from django.contrib.auth import get_user
import json
from api.serializers import UserSerializer


class getHomeTest(TestCase):
    """Test module for GET requests on Home page"""

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def test_get_home(self):
        # get home page with all profiles
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'web/home.html')

    def test_get_invalid_home(self):
        # get home page with parameters
        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse('home', args=['test']))


class postHomeTest(TestCase):
    """Test module for POST requests on Home page"""

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.clientCSRF = Client(enforce_csrf_checks=True)
        self.john = User.objects.create_user('john', password='test')
        self.johnJson = dict(username='john', password='test')
        self.johnJsonInvalid = dict(username='john', password='test2')

    def test_post_enforceCSRF_home(self):
        # try to authenticate without CSRF token
        response = self.clientCSRF.post(reverse("home"), data=self.johnJson)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTemplateNotUsed(response, 'web/home.html')
        self.assertEqual(get_user(self.client).is_authenticated(), False)

    def test_post_valid_home(self):
        # try to authenticate properly
        response = self.client.post(reverse("home"), data=self.johnJson)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'web/home.html')
        self.assertEqual(get_user(self.client).is_authenticated(), True)

    def test_post_invalid_home(self):
        # try to authenticate with invalid password
        response = self.client.post(reverse("home"), data=self.johnJsonInvalid)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'web/home.html')
        self.assertEqual(get_user(self.client).is_authenticated(), False)


class getProfileTest(TestCase):
    """Test module for GET requests on Profile page"""

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.john = User.objects.create(
            username='john', password='test', first_name='John', last_name='Doe', country='UK', email='test@test.com',
            phone='+44123456789', field='Diplomacy', occupation='Spy', birthdate='1963-05-01', description='Tall guy')

    def test_valid_get_profile(self):
        response = self.client.get(reverse('profile', kwargs={'usrname': self.john.username}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'web/profile.html')

    def test_invalid_firstname_notexist_get_profile(self):
        response = self.client.get(reverse('profile', kwargs={'usrname': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTemplateNotUsed("web/profile.html")


class postBadgeTest(TestCase):
    """Test module for POST requests on Badge page"""

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.john = User.objects.create(
            username='john', password='test', first_name='John', last_name='Doe', country='UK', email='test@test.com',
            phone='+44123456789', field='Diplomacy', occupation='Spy', birthdate='1963-05-01', description='Tall guy')

        self.serialiser = UserSerializer(instance=self.john)

        self.valid_payload = {
            'username': 'john',
            'password': 'test',
            'first_name': 'John-John',
            'last_name': 'Doe2',
            'country': 'UK2',
            'email': 'test2@test.com',
            'phone': '+441234567892',
            'field': 'Diplomacy2',
            'occupation': 'Spy2',
            'birthdate': '1963-05-02',
            'description': 'Tall guy2'
        }

    def test_valid_post_profile(self):
        response = self.client.post(reverse('profile', kwargs={'usrname': self.serialiser.data['username']}),
                                    data=json.dumps(self.valid_payload),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'web/profile.html')

    def test_invalid_url_post_profile(self):
        # get badge page with wrong parameters
        with self.assertRaises(NoReverseMatch):
            self.client.post(reverse('profile', kwargs={'usrname': '@@@'}))

    def test_invalid_firstname_notexist_post_profile(self):
        response = self.client.post(reverse('profile', kwargs={'usrname': 'test'}), data=self.serialiser.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTemplateNotUsed("web/profile.html")
