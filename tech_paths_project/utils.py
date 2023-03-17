import requests
from datetime import datetime
from .models import ABLine
from django.http import HttpResponse


def import_abline_from_api(request):
    # URL API
    url = "https://mocki.io/v1/cbf7bb1d-c5b1-4dfa-83d2-5800f78ffb8d"

    # pobranie danych z API
    response = requests.get(url)

    # przetworzenie danych w formacie JSON
    resp = response.json()

    # zapisanie danych w bazie danych
    for data in resp['values']:
        abline = ABLine(
            type=data['type'],
            heading=data['heading'],
            aPoint_lat=data['aPoint']['lat'],
            aPoint_lon=data['aPoint']['lon'],
            bPoint_lat=data['bPoint']['lat'],
            bPoint_lon=data['bPoint']['lon'],
            id=data['id'],
            name=data['name'],
            lastModifiedTime=datetime.strptime(data['lastModifiedTime'], '%Y-%m-%dT%H:%M:%S.%fZ'),
            archived=data['archived'],
        )
        abline.save()
    return HttpResponse("Successfully imported.")
