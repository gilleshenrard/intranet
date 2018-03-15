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
