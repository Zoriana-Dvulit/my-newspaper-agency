import os

import django
from django.contrib.auth import get_user_model
from django.test import TransactionTestCase, Client
from django.urls import reverse

from newspaper.models import Topic

User = get_user_model()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper_agency.settings')
django.setup()


class TestUserMixin:
    def create_test_user(self, **kwargs):
        defaults = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)


class TopicTests(TestUserMixin, TransactionTestCase):
    def setUp(self):
        self.client = Client()
        self.topic = Topic.objects.create(name="test topic")
        self.user = self.create_test_user()

    def test_topic_list_view(self):
        response = self.client.get(reverse("newspaper:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["object_list"]), 1)

    def test_topic_create_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("newspaper:topic-create"), data={"name": "new topic"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(name="new topic").exists())

    def test_topic_update_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("newspaper:topic-update", kwargs={"pk": self.topic.pk}),
                                    data={"name": "updated topic"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(name="updated topic").exists())

    def test_topic_delete_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("newspaper:topic-delete", kwargs={"pk": self.topic.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Topic.objects.filter(name="test topic").exists())
