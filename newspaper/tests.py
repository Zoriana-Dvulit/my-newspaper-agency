from django.contrib.auth import get_user_model

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
