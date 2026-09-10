import unittest

from app.models.user import User, Admin, Waiter, KitchenStaff
from app.services.auth_service import AuthService


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()

    def test_user_registration(self):
        user = self.auth_service.register(
            username="john",
            password="password123",
            role="waiter"
        )

        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john")
        self.assertEqual(user.role, "waiter")

    def test_duplicate_username_is_rejected(self):
        self.auth_service.register(
            username="john",
            password="password123",
            role="waiter"
        )

        with self.assertRaises(ValueError):
            self.auth_service.register(
                username="john",
                password="differentpassword",
                role="waiter"
            )

    def test_login_with_correct_credentials(self):
        self.auth_service.register(
            username="john",
            password="password123",
            role="waiter"
        )

        user = self.auth_service.login(
            username="john",
            password="password123"
        )

        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john")

    def test_login_with_wrong_password(self):
        self.auth_service.register(
            username="john",
            password="password123",
            role="waiter"
        )

        with self.assertRaises(ValueError):
            self.auth_service.login(
                username="john",
                password="wrongpassword"
            )

    def test_admin_role(self):
        user = Admin("admin", "admin123")

        self.assertEqual(user.role, "admin")

    def test_waiter_role(self):
        user = Waiter("waiter", "waiter123")

        self.assertEqual(user.role, "waiter")

    def test_kitchen_staff_role(self):
        user = KitchenStaff("chef", "chef123")

        self.assertEqual(user.role, "kitchen")

    def test_password_is_not_stored_as_plain_text(self):
        user = User("john", "password123")

        self.assertNotEqual(
            user.password,
            "password123"
        )


if __name__ == "__main__":
    unittest.main()
