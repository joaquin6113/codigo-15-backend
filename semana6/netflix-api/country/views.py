from django.http import JsonResponse
from .models import Country
import requests
import json


def create_countries(request):
    data = requests.get("https://cuik-projects.github.io/country-list/countries.json")

    json.res = data.json()

    for country in json.res:
        new_country = Country(name=country["name"], dial_code=country["dial_code"], code=country["code"], emoji=country["emoji"])
        new_country.save()

    return JsonResponse({
        "message": "create country"
    })


def delete_countries(request):
    Country.objects.all().delete()
    return JsonResponse({
        "message": "deleted countries"
    })