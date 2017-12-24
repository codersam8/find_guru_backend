from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Tutor
from .utils import get_req_body


def welcome(request):
    return render(request,
                  'list_tutor/hello.html')


@csrf_exempt
def add_tutor(request):
    req_body = get_req_body(request)

    a_tutor = Tutor()
    a_tutor.mail_id = req_body['mailId']
    a_tutor.first_name = req_body['firstName']
    a_tutor.last_name = req_body['lastName']
    a_tutor.qualification = req_body['qualification']
    a_tutor.institute = req_body['institute']
    a_tutor.mobile = req_body['mobile']
    a_tutor.location = req_body['location']
    a_tutor.save()

    return HttpResponse(json.dumps('request success knuth'))


def search_tutors(request):
    return HttpResponse(json.dumps(['search_tutors working fine', 'reshma', 'sampath']))
