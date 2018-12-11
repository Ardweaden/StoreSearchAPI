from rest_framework import serializers
from storeapi.models import API


class relevantAPISerializer(serializers.Serializer):
    id = serializers.CharField(required=True, allow_blank=False, default='')
    name = serializers.CharField(required=True, allow_blank=False, default='')
    description = serializers.TextField(required=False, allow_blank=True,default='')
    context = serializers.CharField(required=False, allow_blank=True, default='')
    version = serializers.CharField(required=False, allow_blank=True, default='')
    provider = serializers.CharField(required=False, allow_blank=True, default='')
    status = serializers.CharField(required=False, allow_blank=True, default='')

    def create(self, validated_data):
        """
        Create and return a new `API` instance, given the data.
        """
        return API.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `API` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.context = validated_data.get('context', instance.context)
        instance.version = validated_data.get('version', instance.version)
        instance.provider = validated_data.get('provider', instance.provider)
        instance.status = validated_data.get('status', instance.status)
        instance.tags = models.TextField('tags', instance.tags)
		instance.apiDefinition = models.TextField('apiDefinition', instance.apiDefinition)
		instance.endpointURLs = models.TextField('endpointURLs', instance.endpointURLs)
		instance.businessInformation = models.TextField('businessInformation', instance.businessInformation)
		instance.keywords = models.TextField('keywords', instance.keywords)
        instance.save()
        return instance