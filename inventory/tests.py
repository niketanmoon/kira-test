from django.test import TestCase
from inventory import models as inventory_models

# Create your tests here.
class BasicTest(TestCase):
    def setUp(self):
        supplier = inventory_models.Supplier.objects.create(
            name="Swiggy"
        )
        inventory_models.Inventory.objects.create(
            name="First",
            description="Hello",
            note="Notes",
            stock=2,
            availability=True,
            supplier=supplier
        )
        inventory_models.Inventory.objects.create(
            name="Second",
            description="Hello",
            note="Notes",
            stock=2,
            availability=True,
            supplier=supplier
        )

    def test_inventory_list(self):
        response = self.client.get('/api/inventory', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_inventory_list_through_api(self):
        response = self.client.get('/inventory/', follow=True)
        self.assertEqual(response.status_code, 200)
        
    def test_inventory_detail(self):
        response = self.client.get('/inventory/2', follow=True)
        self.assertEqual(response.status_code, 200)