from unittest import TestCase

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.utils import json

from newspaper.models import Topic, Redactor, Newspaper

User = get_user_model()


class TestUserMixin:
    def create_test_user(self, **kwargs):
        defaults = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password",
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)


class NewspaperAPITest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")
        self.redactor = Redactor.objects.create(username="testuser", password="testpassword", first_name="Test",
                                                last_name="User")
        self.newspaper = Newspaper.objects.create(title="Test Newspaper", content="Test content",
                                                  published_date="2023-04-19", topic=self.topic)
        self.newspaper.publishers.add(self.redactor)

    def test_get_newspaper_list(self):
        response = self.client.get("/api/newspapers/")
        self.assertEqual(response.status_code, 200)
        newspapers = json.loads(response.content)
        self.assertEqual(len(newspapers), 1)
        self.assertEqual(newspapers[0]["title"], "Test Newspaper")

    def test_get_newspaper_detail(self):
        response = self.client.get("/api/newspapers/{}/".format(self.newspaper.id))
        self.assertEqual(response.status_code, 200)
        newspaper = json.loads(response.content)
        self.assertEqual(newspaper["title"], "Test Newspaper")
        self.assertEqual(newspaper["content"], "Test content")
        self.assertEqual(newspaper["published_date"], "2023-04-19")
        self.assertEqual(newspaper["topic"]["name"], "Test Topic")
        self.assertEqual(len(newspaper["publishers"]), 1)
        self.assertEqual(newspaper["publishers"][0]["username"], "testuser")
        self.assertEqual(newspaper["publishers"][0]["first_name"], "Test")
        self.assertEqual(newspaper["publishers"][0]["last_name"], "User")

    def test_create_newspaper(self):
        data = {
            "title": "New Newspaper",
            "content": "New content",
            "published_date": "2023-04-20",
            "topic": self.topic.id,
            "publishers": [self.redactor.id],
        }
        response = self.client.post("/api/newspapers/", data=data)
        self.assertEqual(response.status_code, 201)
        newspaper = json.loads(response.content)
        self.assertEqual(newspaper["title"], "New Newspaper")
        self.assertEqual(newspaper["content"], "New content")
        self.assertEqual(newspaper["published_date"], "2023-04-20")
        self.assertEqual(newspaper["publishers"][0]["username"], "testuser")
        self.assertEqual(newspaper["publishers"][0]["first_name"], "Test")
        self.assertEqual(newspaper["publishers"][0]["last_name"], "User")

    def test_update_newspaper(self):
        data = {
            "title": "Updated Newspaper",
            "content": "This is an updated newspaper content",
            "published_date": "2023-04-19",
            "topic": self.topic.id,
            "publishers": [self.redactor.id]
        }
        response = self.client.put(reverse("newspaper:newspaper-detail", args=[self.newspaper.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["content"], data["content"])
        self.assertEqual(response.data["published_date"], data["published_date"])
        self.assertEqual(response.data["topic"], self.topic.id)
        self.assertEqual(response.data["publishers"][0]["id"], self.redactor.id)

class RedactorTestCase(TestCase, TestUserMixin):
    def setUp(self):
        # self.client = APIClient()
        self.redactor = Redactor.objects.create(
            username="testuser", email="testuser@example.com", password="password"
        )

    def test_redactor_list(self):
        url = reverse("redactor-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_redactor_detail(self):
        url = reverse("redactor-detail", kwargs={"pk": self.redactor.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_redactor_create(self):
        url = reverse("redactor-list")
        data = {
            "username": "testuser2",
            "email": "testuser2@example.com",
            "password": "password",
            "years_of_experience": 2
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_redactor_update(self):
        url = reverse('redactor-detail', kwargs={'pk': self.redactor.pk})
        data = {'years_of_experience': 3}
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_redactor_delete(self):
        url = reverse('redactor-detail', kwargs={'pk': self.redactor.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TopicAPITest(TestCase):
    def setUp(self):
        # self.client = APIClient()
        self.topic1 = Topic.objects.create(name="Politics")
        self.topic2 = Topic.objects.create(name="Technology")

    def test_get_topic_list(self):
        response = self.client.get(reverse("topic-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_topic(self):
        data = {"name": "Sports"}
        response = self.client.post(reverse("topic-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Topic.objects.count(), 3)

    def test_get_topic_detail(self):
        response = self.client.get(reverse("topic-detail", args=[self.topic1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.topic1.name)

    def test_update_topic(self):
        data = {"name": "Economy"}
        response = self.client.put(reverse("topic-detail", args=[self.topic1.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Topic.objects.get(id=self.topic1.id).name, "Economy")

    def test_delete_topic(self):
        response = self.client.delete(reverse("topic-detail", args=[self.topic1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Topic.objects.count(), 1)
