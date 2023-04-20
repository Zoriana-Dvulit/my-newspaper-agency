import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newspaper_agency.settings")

from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Newspaper, Topic


class ModelsTests(TestCase):
    def test_topic_str(self):
        name_ = Topic.objects.create(
            name="test",
        )
        self.assertEqual(str(name_), {name_.name})

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="Test first",
            last_name="Test last"
        )

        self.assertEqual(
            str(redactor), f"{redactor.username}"
                           f" ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        name_ = Topic.objects.create(
            name="test",
        )
        newspaper = Newspaper.objects.create(
            title="Testing",
            topic=name_
        )

        self.assertEqual(str(newspaper), newspaper.title)
