"""inventmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views as inventory_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', inventory_views.inventory_list_through_api, name="normal_inventory_list"),
    path('inventory/<int:item_id>', inventory_views.inventory_detail, name="inventory_detail"),
    path("api/", include(("api.urls", "api"), namespace="api")),
]
