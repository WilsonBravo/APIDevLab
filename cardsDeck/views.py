import json

from django.shortcuts import render
from django.http import HttpResponse

def cardsDeck(request):
    # url principal
    url='localhost:8000'

    # Crear un diccionario con los datos que deseas devolver
    datos = [
        {
            'suit': 'clubs',
            'value': '10',
            'img': f'{url}/static/PNG-cards/10_of_clubs.png',
        },
        {
            'suit': 'diamonds',
            'value': '10',
            'img': f'{url}/static/PNG-cards/10_of_diamonds.png',
        },
        {
            'suit': 'hearts',
            'value': '10',
            'img': f'{url}/static/PNG-cards/10_of_hearts.png',
        },
        {
            'suit': 'spades',
            'value': '10',
            'img': f'{url}/static/PNG-cards/10_of_spades.png',
        }
    ]

    # Convertir el diccionario a una cadena JSON
    datos_json = json.dumps(datos)

    # Crear una respuesta HTTP con el tipo de contenido establecido en 'application/json'
    response = HttpResponse(datos_json, content_type='application/json')

    # Devolver la respuesta HTTP
    return response