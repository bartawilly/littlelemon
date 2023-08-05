from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        menu = Menu.objects.create(Title="Desserts")
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100, MenuID=menu)
        self.assertEqual(str(item), "IceCream : 80")