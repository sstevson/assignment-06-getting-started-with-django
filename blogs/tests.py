from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    fixtures = ['blogs_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)
