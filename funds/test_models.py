from django.test import TestCase
from .models import Fund

class TestModels(TestCase):

    def test_name_is_required(self):
        fund = Fund.objects.create(name='')
        self.assertFalse(fund.name)
