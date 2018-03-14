from rest_framework import status
from django.test import TestCase, Client
from django.core.urlresolvers import reverse, NoReverseMatch
from ..models import User
from ..serializers import UserSerializer
import json

# initialize the APIClient app
client = Client()


class MethodsTest(TestCase):
    """Test module for request methods on API"""

    def setUp(self):
        self.john = User.objects.create_user('john', 'test@test.com', 'test', first_name='John', last_name='Doe')

    def test_invalid_methods(self):
        # send delete on get_post_people
        response = client.delete(reverse('get_post_profiles'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # send put on get_post_people
        response = client.put(reverse('get_post_profiles'))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # send post on get_delete_update_person
        response = client.post(reverse('get_delete_update_profile', kwargs={'usrname': self.john.username}))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class GetAllProfilesTest(TestCase):
    """ Test module for GET all profiles API """

    def setUp(self):
        self.john = User.objects.create_user('john', 'john@test.com', 'test', first_name='John', last_name='Doe')
        self.john.country = 'UK'
        self.john.phone = '+44123456789'
        self.john.field = 'Diplomacy'
        self.john.occupation = 'Spy'
        self.john.birthdate = '1963-05-01'
        self.john.description = 'Tall guy'
        self.john.save()

        self.jane = User.objects.create_user('jane', 'jane@test.com', 'test', first_name='Jane', last_name='Dean')
        self.jane.country = 'US'
        self.jane.phone = '+1123456789'
        self.jane.field = 'Administration'
        self.jane.occupation = 'Accountance'
        self.jane.birthdate = '1982-05-01'
        self.jane.description = 'Smart girl'
        self.jane.save()

        self.jack = User.objects.create_user('jack', 'jack@test.com', 'test', first_name='Jack', last_name='Damn')
        self.jack.country = 'ES'
        self.jack.phone = '+34123456789'
        self.jack.field = 'IT'
        self.jack.occupation = 'Developer'
        self.jack.birthdate = '1963-05-03'
        self.jack.description = 'Funny guy'
        self.jack.save()

        self.jim = User.objects.create_user('jim', 'jim@test.com', 'test', first_name='Jim', last_name='Done')
        self.jim.country = 'FR'
        self.jim.phone = '+3323456789'
        self.jim.field = 'Maintenance'
        self.jim.occupation = 'Janitor'
        self.jim.birthdate = '1982-05-04'
        self.jim.description = 'Sweet guy'
        self.jim.save()

    def test_get_all_profiles(self):
        # get API response
        response = client.get(reverse('get_post_profiles'))
        # get data from db
        people = User.objects.all()
        serializer = UserSerializer(people, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProfileTest(TestCase):
    """ Test module for GET single profile API """

    def setUp(self):
        self.john = User.objects.create_user('john', 'john@test.com', 'test', first_name='John', last_name='Doe')
        self.john.country = 'UK'
        self.john.phone = '+44123456789'
        self.john.field = 'Diplomacy'
        self.john.occupation = 'Spy'
        self.john.birthdate = '1963-05-01'
        self.john.description = 'Tall guy'
        self.john.save()

        self.jane = User.objects.create_user('jane', 'jane@test.com', 'test', first_name='Jane', last_name='Dean')
        self.jane.country = 'US'
        self.jane.phone = '+1123456789'
        self.jane.field = 'Administration'
        self.jane.occupation = 'Accountance'
        self.jane.birthdate = '1982-05-01'
        self.jane.description = 'Smart girl'
        self.jane.save()

        self.jack = User.objects.create_user('jack', 'jack@test.com', 'test', first_name='Jack', last_name='Damn')
        self.jack.country = 'ES'
        self.jack.phone = '+34123456789'
        self.jack.field = 'IT'
        self.jack.occupation = 'Developer'
        self.jack.birthdate = '1963-05-03'
        self.jack.description = 'Funny guy'
        self.jack.save()

        self.jim = User.objects.create_user('jim', 'jim@test.com', 'test', first_name='Jim', last_name='Done')
        self.jim.country = 'FR'
        self.jim.phone = '+3323456789'
        self.jim.field = 'Maintenance'
        self.jim.occupation = 'Janitor'
        self.jim.birthdate = '1982-05-04'
        self.jim.description = 'Sweet guy'
        self.jim.save()

    def test_get_valid_single_profile(self):
        response = client.get(
            reverse('get_delete_update_profile', kwargs={'usrname': self.john.username}))
        user = User.objects.get(username=self.john.username)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_profile(self):
        response = client.get(
            reverse('get_delete_update_profile', kwargs={'usrname': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_invalid_single_profile_url_type(self):
        with self.assertRaises(NoReverseMatch):
            client.get(reverse('get_delete_update_person', kwargs={'usrname': 30}))

    def test_get_invalid_single_profile_url_length(self):
        with self.assertRaises(NoReverseMatch):
            client.get(reverse('get_delete_update_profile', kwargs={'usrname': "abcdefghijklmnopqrstuvwxyzabcdefg"}))


class CreateNewProfileTest(TestCase):
    """ Test module for inserting a new profile """

    def setUp(self):
        self.valid_payload = dict(username='john', password='test', first_name='John', last_name='Doe',
                                  email='test@test.com', country='UK', phone='+44123456789',
                                  field='Diplomacy', occupation='Spy', birthdate='1963-05-01',
                                  description='Tall guy')

        self.invalid_username_payload = dict(username='*****', password='test', first_name='John', last_name='Doe',
                                             email='test@test.com', country='UK', phone='+44123456789',
                                             field='Diplomacy', occupation='Spy', birthdate='1963-05-01',
                                             description='Tall guy')

        self.invalid_email_payload = dict(username='john', password='test', first_name='John', last_name='Doe',
                                          email='test', country='UK', phone='+44123456789',
                                          field='Diplomacy', occupation='Spy', birthdate='1963-05-01',
                                          description='Tall guy')

    def test_create_valid_profile(self):
        response = client.post(
            reverse('get_post_profiles'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_person_username(self):
        response = client.post(
            reverse('get_post_profiles'),
            data=json.dumps(self.invalid_username_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_profiles_email(self):
        response = client.post(
            reverse('get_post_profiles'),
            data=json.dumps(self.invalid_email_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProfileTest(TestCase):
    """ Test module for updating an existing profile record """

    def setUp(self):
        self.john = User.objects.create(
            username='john', first_name='John', last_name='Doe', country='UK', email='test@test.com',
            phone='+44123456789', field='Diplomacy', occupation='Spy', birthdate='1963-05-01', description='Tall guy')

        self.valid_payload = dict(first_name='John-John', last_name='Doe2', country='UK2', email='test2@test.com',
                                  phone='+441234567892', field='Diplomacy2', occupation='Spy2',
                                  birthdate='1963-05-02', description='Tall guy2', username='john')

        self.valid_partial_payload = dict(country='UK2', email='jim@test.com',
                                  phone='+341234567892', field='IT', occupation='Developer',
                                  birthdate='1983-10-02', description='Fun guy')

        self.invalid_username_payload = dict(first_name='*****', last_name='Doe', country='UK', email='test@test.com',
                                              phone='+44123456789', field='Diplomacy', occupation='Spy',
                                              birthdate='1963-05-01', description='Tall guy', username="john")

    def test_valid_update_person(self):
        response = client.put(
            reverse('get_delete_update_profile', kwargs={'usrname': self.john.username}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_valid_update_partial_person(self):
        response = client.put(
            reverse('get_delete_update_profile', kwargs={'usrname': 'john'}),
            data=json.dumps(self.valid_partial_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_person(self):
        response = client.put(
            reverse('get_delete_update_profile', kwargs={'usrname': self.john.username}),
            data=json.dumps(self.invalid_username_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
