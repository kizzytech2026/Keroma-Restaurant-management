import unittest

from app.models.menu import MenuItem, Menu
from app.services.menu_service import MenuService


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu_service = MenuService()

    def test_create_menu_item(self):
        item = MenuItem(
            item_id="1",
            name="Chicken",
            price=500
        )

        self.assertEqual(item.name, "Chicken")
        self.assertEqual(item.price, 500)
        self.assertTrue(item.available)

    def test_add_menu_item(self):
        item = self.menu_service.add_item(
            name="Burger",
            price=350
        )

        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Burger")
        self.assertEqual(item.price, 350)

    def test_add_item_with_invalid_price(self):
        with self.assertRaises(ValueError):
            self.menu_service.add_item(
                name="Burger",
                price=-100
            )

    def test_update_menu_item(self):
        item = self.menu_service.add_item(
            name="Burger",
            price=350
        )

        updated = self.menu_service.update_item(
            item.item_id,
            name="Cheese Burger",
            price=400
        )

        self.assertEqual(updated.name, "Cheese Burger")
        self.assertEqual(updated.price, 400)

    def test_remove_menu_item(self):
        item = self.menu_service.add_item(
            name="Burger",
            price=350
        )

        result = self.menu_service.remove_item(item.item_id)

        self.assertTrue(result)

    def test_menu_item_availability(self):
        item = MenuItem(
            item_id="1",
            name="Pizza",
            price=800
        )

        item.set_availability(False)

        self.assertFalse(item.available)

    def test_unavailable_item_cannot_be_ordered(self):
        item = MenuItem(
            item_id="1",
            name="Pizza",
            price=800,
            available=False
        )

        self.assertFalse(item.available)


if __name__ == "__main__":
    unittest.main()