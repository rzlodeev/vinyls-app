import unittest

import django

from app_api.views import UserList
from rest_framework.permissions import IsAdminUser, AllowAny
from django.conf import settings

settings.configure()


class TestUserList(unittest.TestCase):
    def setUp(self):
        self.instance = UserList()

    def test_list_action(self):
        self.instance.action = 'list'
        expected_permissions = [IsAdminUser]
        permissions = self.instance.get_permissions()
        self.assertEqual(permissions, expected_permissions)


if __name__ == '__main__':
    unittest.main()
