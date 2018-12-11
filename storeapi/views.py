from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapi._helper_functions import search
from django.views.decorators.http import require_http_methods
import json

# Create your views here.

@require_http_methods(['GET'])
def index(request):
	return render(request,'storeapi/index.html')

@api_view(['GET'])
def relevant_apis(request,phrase):
	print(phrase)
	if len(phrase) < 4:
		return Response("Too short")
	else:
		related = search(phrase)
		return Response(json.dumps(related))