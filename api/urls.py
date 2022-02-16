from django.urls import include, path
from inventory import views as inventory_views

urlpatterns = [
    path("inventory/", inventory_views.InventoryList.as_view(), name="inventories"),
]