import requests
import json
import pytest


ENDPOINT = 'https://petstore.swagger.io/v2'



class RestClientInitializationAndActions:
    

    def __init__(self):
        pass


    
    def getPetsWhichAre(status):
        response = requests.get(ENDPOINT + "/pet/findByStatus?status=" + status)
        return response

