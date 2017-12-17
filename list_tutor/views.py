from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json

from .utils import get_req_body


def welcome(request):
    return render(request,
                  'list_tutor/hello.html')


@csrf_exempt
def add_tutor(request):
    req_body = get_req_body(request)
    print(req_body)

    return HttpResponse(json.dumps('request success knuth'))
