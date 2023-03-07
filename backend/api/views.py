"""This portion of code is used to solidify fundamental understanding
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
    """

from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict # Can be used to  

def api_home(request, *args, **kwargs):
    # 1. Getting a model instance
    model_data = Product.objects.all().order_by('?').first()

    # 2. Converting the model instance to Python dict
    data = {}
    if model_data:
        # Approach 1: Populating the dictionary yourself
        # This approach of converting model instance to dict is tedious since you have to do it one by one but it is very useful in some cases
        # data['id'] = model_data.id # By default an id is added to every model so we can access it
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price

        # Approach 2: Using the model_to_dict method
        data = model_to_dict(model_data) 


        # What is happening?
        # 1. Model instance
        # 2. Turn to python dict
        # 3. Return JSON to my client

    # Returning JSON to client
    return JsonResponse(data)