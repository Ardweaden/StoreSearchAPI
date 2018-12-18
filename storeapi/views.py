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
	if "no_database" in request.query_params:
		if request.query_params["no_database"] == "True":
			no_database = True
		else:
			no_database = False
	else:
		no_database = False

	print("no_database IS INDEED",no_database)
	print(phrase)

	if len(phrase) < 4:
		return Response("Too short")
	else:
		related = search(phrase,no_database=no_database)
		return Response(json.dumps(related))