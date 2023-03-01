from django.shortcuts import render
from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):

    # This part of the code is only necessary to handle the data we are adding to our get request form the py_client
    body = request.body # Byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # Takes in a string of JSON data and convert it -> to python dictionary
    except:
        pass

    print(data)
    # data["headers"] = request.headers
    print(request.headers)
    data["content_type"] = request.content_type

    return JsonResponse(data)