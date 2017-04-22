from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from users.models import user

import json
from django.core import serializers

def index(request):
    return HttpResponse("Hello, you're at the user page")

def detail(request, user_id):
    obj = user.objects.get(id = user_id)
    data = serializers.serialize('json', [obj, ])
    struct = json.loads(data)
    return JsonResponse(struct[0]['fields'])
