import unittest

from app.models.menu import MenuItem
from app.models.order import Order, OrderItem


class TestOrders(unittest.TestCase):

    def setUp(self):
        self.burger = MenuItem(
            item_id="1",
            name="Burger",
            price=350
        )

        self.pizza = MenuItem(
            item_id="2",
            name="Pizza",
            price=800
        )

        self.order = Order(
            order_id="ORD001",
            table_number=5
        )

    def test_create_order(self):
        self.assertEqual(
            self.order.order_id,
            "ORD001"
        )

        self.assertEqual(
            self.order.table_number,
            5
        )

        self.assertEqual(
            self.order.status,
            "PENDING"
        )

    def test_add_item_to_order(self):
        self.order.add_item(
            self.burger,
            quantity=2
        )

        self.assertEqual(
            len(self.order.items),
            1
        )

    def test_order_item_quantity(self):
        item = OrderItem(
            menu_item=self.burger,
            quantity=3
        )

        self.assertEqual(
            item.quantity,
            3
        )

    def test_order_total(self):
        self.order.add_item(
            self.burger,
            quantity=2
        )

        self.order.add_item(
            self.pizza,
            quantity=1
        )

        expected_total = (350 * 2) + 800

        self.assertEqual(
            self.order.calculate_total(),
            expected_total
        )

    def test_remove_item_from_order(self):
        self.order.add_item(
            self.burger,
            quantity=2
        )

        self.order.remove_item("1")

        self.assertEqual(
            len(self.order.items),
            0
        )

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.order.add_item(
                self.burger,
                quantity=0
            )

    def test_order_status_changes(self):
        self.order.start_preparing()

        self.assertEqual(
            self.order.status,
            "PREPARING"
        )

        self.order.mark_ready()

        self.assertEqual(
            self.order.status,
            "READY"
        )

        self.order.complete()

        self.assertEqual(
            self.order.status,
            "COMPLETED"
        )


if __name__ == "__main__":
    unittest.main()