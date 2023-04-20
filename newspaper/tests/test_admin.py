from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


# class AdminSiteTests(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             username="admin",
#             password="admin12345",
#         )
#         self.client.force_login(self.admin_user)
#         self.redactor = get_user_model().objects.create_user(
#             username="redactor",
#             password="redactor123",
#         )

    # def test_driver_license_number_listed(self):
    #     """Tests that driver's license_number is in
    #     list_display on driver admin page"""
    #     url = reverse("admin:taxi_driver_changelist")
    #     res = self.client.get(url)
    #
    #     self.assertContains(res, self.driver.license_number)
    #
    # def test_driver_detailed_license_number_listed(self):
    #     """Tests that driver's license_number is
    #     in driver detail admin page"""
    #     url = reverse("admin:taxi_driver_change", args=[self.driver.id])
    #     res = self.client.get(url)
    #
    #     self.assertContains(res, self.driver.license_number)

class RedactorModelTests(TestCase):
    def test_create_redactor_without_years_of_experience(self):
        User = get_user_model()
        redactor = User.objects.create_user(
            username="redactor",
            password="password",
        )
        self.assertIsNone(redactor.years_of_experience)
