from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self): # django recommended setUp
        self.i_1 = Menu.objects.create(title='Lasagna', price=16, inventory=100)
        self.i_2 = Menu.objects.create(title='Spaghetti', price=12, inventory=100)
        self.i_3 = Menu.objects.create(title='Pasta', price=12, inventory=100)

    def test_get_all(self):
        response = self.client.get('/restaurant/menu/')

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.json(), serializer.data)