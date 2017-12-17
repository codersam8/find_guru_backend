import json


def get_req_body(request):
    req_body = request.read()
    req_body = req_body.decode('utf-8')
    req_body = json.loads(req_body)
    return req_body
