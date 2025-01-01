from django.test import TestCase
from model_bakery import baker
from crud.models import Person



class PersonTestBakery(TestCase):

    def test_person_model_creation_bakery(self):

        person = baker.make(Person)
        
        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person.__str__(), person.name)
        self.assertIsNotNone(person.name)

