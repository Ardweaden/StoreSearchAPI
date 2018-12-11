from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapi._helper_functions import search
import json

# Create your views here.

@api_view(['GET'])
def relevant_apis(request,phrase):
	print(phrase)
	if len(phrase) < 4:
		return Response("Too short")
	else:
		related = search(phrase)
		return Response(json.dumps(related))