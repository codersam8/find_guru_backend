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
    else:
        print('IN POST')
    req = request.read().decode('utf-8')
    print(request.read().decode('utf-8'))
    print(repr(req))
    obj_req = json.loads(req)
    print('obj_req')
    print(obj_req)
    print(obj_req['id'])

    return HttpResponse(json.dumps('request success knuth'))
