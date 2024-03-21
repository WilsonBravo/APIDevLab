import json
import random

from django.shortcuts import render
from django.http import HttpResponse

# Class--------------------------------------------------------------------------------------
class card:
    def __init__(self,suit,value,img):
        self.suit= suit,
        self.value= value,
        self.img= img

        self.json={
            "suit": self.suit[0],
            "value": self.value[0],
            "img": self.img
        }

class deck:
    url='https://api-dev-lab.vercel.app'
    cardSuit=['clubs','diamonds','hearts','spades']
    cardValue=["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
    dataDeck=[]
    jsonDataDeck=[]
    count=0

    def __init__(self):  
        for suit in self.cardSuit:
            for value in self.cardValue:
                cardImg=f'{self.url}/media/PNG-cards/{value}_of_{suit}.png'
                self.dataDeck.append(card(suit,value,cardImg))

        cardImg=f'{self.url}/media/PNG-cards/red_joker.png'
        self.dataDeck.append(card("red","joker",cardImg))
        cardImg=f'{self.url}/media/PNG-cards/black_joker.png'
        self.dataDeck.append(card("black","joker",cardImg))
        self.count+=1
    
    def shuffle(self):
        random.shuffle(self.dataDeck)

    def to_json(self):

        self.jsonDataDeck=[]

        for card in self.dataDeck:
            self.jsonDataDeck.append(card.json)

# Variables ---------------------------------------------------------------------------
dataDeck = deck()
dataDeck.to_json()

# Views -------------------------------------------------------------------------------
def cardsDeck(request, dataDeck=dataDeck):    
    data={
        "size":len(dataDeck.jsonDataDeck),
        "order": [
            'clubs','diamonds','hearts','spades',"joker"
            ],
        "deck":dataDeck.jsonDataDeck
    }

    # Convertir el diccionario a una cadena JSON
    datos_json = json.dumps(data)

    # Crear una respuesta HTTP con el tipo de contenido establecido en 'application/json'
    response = HttpResponse(datos_json, content_type='application/json')

    # Devolver la respuesta HTTP
    return response

def shuffle(request, dataDeck=dataDeck):
    dataDeck.shuffle()
    dataDeck.to_json()
    data={
        "size":len(dataDeck.jsonDataDeck),
        "order": [
            'clubs','diamonds','hearts','spades',"joker"
            ],
        "deck":dataDeck.jsonDataDeck
    }

    # Convertir el diccionario a una cadena JSON
    datos_json = json.dumps(data)

    # Crear una respuesta HTTP con el tipo de contenido establecido en 'application/json'
    response = HttpResponse(datos_json, content_type='application/json')

    # Devolver la respuesta HTTP
    return response