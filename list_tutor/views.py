from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json


def welcome(request):
    return render(request,
                  'list_tutor/hello.html')


@csrf_exempt
def add_tutor(request):
    if request.method == 'GET':
        return HttpResponse('Get works')
    print(request.POST)

    return HttpResponse(json.dumps(request.POST))