from django.urls import path
from storeapi import views

urlpatterns = [
    path('relevant_apis/<phrase>', views.relevant_apis),
]