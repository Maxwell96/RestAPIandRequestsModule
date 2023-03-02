"""This portion of code is used to solidify fundamental understanding"""
from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):

    # This part of the code is only necessary to handle the data we are adding to our get request form the py_client
    body = request.body # Byte string of JSON data
    print(request.GET) # To print URL query params
    print(request.POST)  
    data = {}
    try:
        data = json.loads(body) # Takes in a string of JSON data and convert it -> to python dictionary
    except:
        pass

    print(data)
    # data['headers'] = request.headers
    # data['headers'] = json.dupms(request.headers)
    # json.dumps(dict(request.headers))
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)