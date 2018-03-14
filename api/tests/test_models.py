from django.test import TestCase
from ..models import User
from ..serializers import UserSerializer


class UserTest(TestCase):
    """ Test module for User model """

    def setUp(self):
        self.john = User.objects.create_user('john', 'test@test.com', 'test', first_name='John', last_name='Doe')
        self.john.country = 'UK'
        self.john.phone = '+44123456789'
        self.john.field = 'Diplomacy'
        self.john.occupation = 'Spy'
        self.john.birthdate = '1963-05-01'
        self.john.description = 'Tall guy'
        self.john.save()

        self.jane = User.objects.create_user('jane', 'test2@test.com', 'test', first_name='Jane', last_name='Dean')
        self.jane.country = 'US'
        self.jane.phone = '+1123456789'
        self.jane.field = 'Administration'
        self.jane.occupation = 'Accountance'
        self.jane.birthdate = '1982-05-01'
        self.jane.description = 'Smart girl'
        self.jane.save()

    def test_valid_get_user(self):
        user = User.objects.get(username=self.john['username'])
        self.assertEqual(str(user), self.john['username'])

        user = User.objects.get(username=self.jane['username'])
        self.assertEqual(str(user), self.jane['username'])

    def test_invalid_username_doesnotexist_person(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='test')

    def test_valid_delete_user(self):
        user = User.objects.get(username=self.john['username'])
        user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=self.john['username'])


class SerializerTest(TestCase):
    """ Test module for User serialiser """

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

        self.johnJson = dict(username='john',
                             password='test',
                             first_name='John',
                             last_name='Doe',
                             email='john@test.com',
                             country='UK',
                             phone='+44123456789',
                             field='Diplomacy',
                             occupation='Spy',
                             birthdate='1963-05-01',
                             description='Tall guy')

        self.jimJson = dict(username='jim',
                            password='test',
                            first_name='Jim',
                            last_name='Damn',
                            email='jim@test.com',
                            country='ES',
                            phone='+34123456789',
                            field='IT',
                            occupation='Developer',
                            birthdate='1973-11-04',
                            description='Fun guy')

    def test_valid_serializer_person(self):
        serializer = UserSerializer(self.jimJson)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=self.jimJson['username'])
            self.assertEqual(data, serializer.data)
