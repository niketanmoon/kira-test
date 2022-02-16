import uuid
from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(
        max_length=200
    )
    description = models.CharField(
        max_length=255
    )
    note = models.TextField()
    stock = models.PositiveIntegerField(
        default=0
    )
    availability = models.BooleanField(
        default=False
    )
    supplier = models.ForeignKey(
        'inventory.Supplier',
        on_delete=models.CASCADE,
        related_name="supplier",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.name

    def get_inventory_dict(self):
        return {
            "inventory_name": self.name,
            "suppliear_name": self.supplier.get_supplier_dict() if self.supplier else "",
            "availability": self.availability
        }


class Supplier(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_supplier_dict(self):
        return {
            "name": self.name
        }
