from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pymongo import MongoClient

from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()

db_url = os.getenv("AtlasdbURL")
client = MongoClient(db_url)   # URL
db = client.sample_mflix # Database
data = db.sample_data # Collection

find_date = datetime(2023, 12, 13, 12)

# data = list(data.find({}, {"_id": 0}))
data = list(data.find({"Date": {"$lt": find_date}}, {"_id": 0}))

@api_view(['GET'])
def get_data(request):
    return Response(data,status=status.HTTP_200_OK)