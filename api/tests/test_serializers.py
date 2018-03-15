from django.test import TestCase
from ..models import User
from ..serializers import UserSerializer
import logging

logger = logging.getLogger(__name__)


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

        self.janePartialJson = dict(first_name='Jim',
                                    last_name='Damn',
                                    email='jim@test.com',
                                    country='ES',
                                    phone='+34123456789',
                                    field='IT',
                                    occupation='Developer',
                                    birthdate='1973-11-04',
                                    description='Fun guy')

    def test_valid_serializer_user(self):
        serializer = UserSerializer(data=self.jimJson)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=self.jimJson['username'])
            self.assertEqual(user.occupation, serializer.data['occupation'])
        else:
            for field, errors in serializer.errors.items():
                for error in errors:
                    logger.error(field + " -> " + error)
            raise ValueError('Serializer.save() test failed')

    def test_invalid_serializer_incomplete_user(self):
        serializer = UserSerializer(data=self.janePartialJson)
        self.assertEqual(serializer.is_valid(), False)

    def test_valid_serializer_update_user(self):
        serializer = UserSerializer(instance=self.john, data=self.janePartialJson, partial=True)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=self.john.username)
            self.assertEqual(user.occupation, self.janePartialJson['occupation'])
            self.assertEqual(user.first_name, self.janePartialJson['first_name'])
        else:
            for field, errors in serializer.errors.items():
                for error in errors:
                    logger.error(field + " -> " + error)
            raise ValueError('Serializer.save() test failed')
