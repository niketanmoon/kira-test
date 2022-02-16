from django.contrib import admin

# Register your models here.
from .models import Inventory, Supplier

class InventoryAdmin(admin.ModelAdmin):
    list_display = ["name", "availability", "stock", "supplier"]


class SupplierAdmin(admin.ModelAdmin):
    pass


admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Supplier, SupplierAdmin)