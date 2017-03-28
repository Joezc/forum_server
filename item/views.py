from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from item.models import item

import json
from django.core import serializers

def index(request):
    return HttpResponse("Hello, you're at the item page")

def detail(request, item_id):
    obj = item.objects.get(id = item_id)
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)
    return JsonResponse(struct[0]['fields'])
