from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from item.models import item
import time
import json
from django.core import serializers

def index(request):
    return HttpResponse("Hello, you're at the item page")

def detail(request, item_id):
    obj = item.objects.get(id = item_id)
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)
    return JsonResponse(struct[0]['fields'])

def calculate_score(votes, item_hour_age, gravity=1.8):
    return (votes - 1) / pow((item_hour_age+2), gravity)

def topstories(request):
    l = []
    raw = item.objects.all()[:10]
    now = int(time.time())
    for i in raw:
        data = serializers.serialize('json', [i,])
        struct = json.loads(data)
        l.append(struct[0]['pk'])
    struct = json.loads(str(l[:100]))
    return JsonResponse(struct, safe=False)
