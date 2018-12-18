from django.db import models

# Create your models here.

class API(models.Model):
    """
    Defining a model for an API offered on Ekosmart Store
    """
    id = models.CharField(primary_key=True,max_length=100, blank=False, default='')
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField(default='',blank=True,null=True)
    context = models.CharField(max_length=100, default='')
    version = models.CharField(max_length=100, default='')
    provider = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')
    tags = models.TextField(default='')
    apiDefinition = models.TextField(default="")
    endpointURLs = models.TextField(default="")
    businessInformation = models.TextField(default="")

    """
    Preprocessed lemmatised keywords from API's name, description and tags
    """

    keywords = models.TextField(default='')

    def __str__(self):
        return self.name