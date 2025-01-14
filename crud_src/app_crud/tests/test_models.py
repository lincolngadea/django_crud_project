from django.test import TestCase
from app_crud.models import User

class StrTest(TestCase):
    def setUp(self):
        self.user = User(nome='Lincoln', telefone='1234567890', email='teste@teste.com')

    def test_str(self):
        self.assertEqual(str(self.user), "Nome: Lincoln, Telefone:1234567890, Email:teste@teste.com")

