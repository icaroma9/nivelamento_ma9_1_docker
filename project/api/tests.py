from rest_framework.test import APIRequestFactory, APILiveServerTestCase

from app.models import Usuario

# Create your tests here.


class ObtainTokenTestCase(APILiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = cls.live_server_url + "/api/token/"
        cls.user_data = {
            "username": "test",
            "password": "test",
            "email": "test@test.com",
        }

    def setUp(self):
        Usuario.objects.create_user(**self.user_data)

    def test_get_token_fail_invalid_data(self):
        """Endpoint must return 400 on invalid data"""
        request = self.client.post(
            self.url, {"email": "", "password": ""}, format="json",
        )
        self.assertEqual(request.status_code, 400)

        request = self.client.post(self.url, {"email": ""}, format="json",)
        self.assertEqual(request.status_code, 400)

        request = self.client.post(
            self.url, {"email": "", "pas2sword": ""}, format="json",
        )
        self.assertEqual(request.status_code, 400)

    def test_get_token_fail_auth(self):
        """Endpoint must return 401 on failed authentication attempt"""
        request = self.client.post(
            self.url,
            {"email": "test2@test.com", "password": "test"},
            format="json",
        )
        self.assertEqual(request.status_code, 401)

    def test_get_token_success(self):
        request = self.client.post(
            self.url,
            {
                "email": self.user_data["email"],
                "password": self.user_data["password"],
            },
            format="json",
        )
        result_json = request.json()
        self.assertIn("refresh", result_json)
        self.assertIn("access", result_json)
