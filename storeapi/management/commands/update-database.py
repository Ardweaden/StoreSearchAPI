from django.core.management.base import BaseCommand, CommandError
from storeapi.models import API
from storeapi._helper_functions import get_api_list,get_details
from storeapi._helper_functions import get_lemmatised_list
from rest_framework.parsers import JSONParser
import sys
import json


class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument("only_new",type=bool, nargs='?', default=False)

    def handle(self, *args, **options):
        only_new = options['only_new']
        apis = get_api_list()

        for api in apis:
            id = api["id"]

            if API.objects.filter(id=id).exists() and not only_new:
                # Update the objects
                details = get_details(id)

                tags = " ".join(details["tags"])

                if api["description"] is None:
                    desc = ""
                else:
                    desc = str(api["description"]).strip()

                sys.stdout.write("Updating " + id + "...\n")

                keywords = get_lemmatised_list(str(api["name"]).strip() + " " + desc + " " + tags)
                keywords = json.dumps(keywords)

                API.objects.filter(id=id).update(name=api["name"],description=api["description"],context=api["context"],version=api["version"],provider=api["provider"],status=api["status"],tags=details["tags"],apiDefinition=details["apiDefinition"],endpointURLs=details["endpointURLs"],businessInformation=details["businessInformation"],keywords=keywords)
            else:
                # Create a new instance of the model
                details = get_details(id)
                sys.stdout.write("Creating new instance with id: " + id + "...\n")

                tags = " ".join(details["tags"])

                if api["description"] is None:
                    desc = ""
                else:
                    desc = str(api["description"]).strip()

                keywords = get_lemmatised_list(str(api["name"]).strip() + " " + desc + " " + tags)
                keywords = json.dumps(keywords)

                API.objects.create(id=id,name=api["name"],description=api["description"],context=api["context"],version=api["version"],provider=api["provider"],status=api["status"],tags=details["tags"],apiDefinition=details["apiDefinition"],endpointURLs=details["endpointURLs"],businessInformation=details["businessInformation"],keywords=keywords)



    
