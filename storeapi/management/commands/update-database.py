from django.core.management.base import BaseCommand, CommandError
from storeapi.models import API
from storeapi._helper_functions import get_api_list
from rest_framework.parsers import JSONParser
from storeapi.serializers import relevantAPISerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        apis = get_api_list()

        for api in apis:
        	api = JSONParser.parse(api)
        	id = api["id"]

        	try:
        		api_instance = API.get(id=id)
        		serializer = relevantAPISerializer(api_instance,data=api)
        		serializer.save()
        	except Exception as e:
        		print(e)
        		api_instance = API(id=id)
        		api_instance.save()


        	
