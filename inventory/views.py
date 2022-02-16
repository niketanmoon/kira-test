from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from inventory import models as inventory_models
from inventory import serializers as inventory_serializer
from django.views.decorators.csrf import csrf_exempt
import requests
import json

from django.core import serializers


# Create your views here.
class InventoryList(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
        results = list()
        name = request.query_params.get("name")
        if name:
            inventory_list = inventory_models.Inventory.objects.filter(
                name=name
            )
        else:
            inventory_list = inventory_models.Inventory.objects.all()
        for obj in inventory_list:
            if obj not in results:
                results.append(obj.get_inventory_dict())
        return Response({
            "results": results,
            "message": "Success"
        }, status=200)


@csrf_exempt
def inventory_list_through_api(request):
    context = {}
    # getting objects from api
    response = requests.get("http://localhost:8000/api/inventory")
    open_dict = {}
    if response.status_code == 200:
        for k,v in response.json().items():
            open_dict.update({
                k:v
            })
        
        context = {
            "items": open_dict["results"]
        }

    return render(request, 'inventory.html', context)

@csrf_exempt
def inventory_detail(request, item_id):
    obj = inventory_models.Inventory.objects.filter(
        id=item_id
    )
    if not obj:
        context = {
            "items": []
        }
        return render(request, 'inventory_detail.html', context)
    context = {
        "items": obj
    }
    return render(request, 'inventory.html', context)

