import requests
from requests import Request, Session
import json
import pytest

import logging
logging.basicConfig(level=logging.DEBUG)

import http.client
http.client.HTTPConnection.debuglevel = 1


ENDPOINT = 'https://petstore.swagger.io/v2'



class RestClientInitializationAndActions:
    

    def __init__(self):
        pass


    
    def getPetsWhichAre(self, status):
        response = requests.get(ENDPOINT + "/pet/findByStatus?status=" + status)
        return response
    

    def addPetToTheStore(self, name, photoUrls):
         
        body = {}
        body['name'] = name
        body['photoUrls'] = [photoUrls]
        #json_body = json.dumps(body)

        json_headers = {"Content-Type": "application/json"}
        #r = Request('POST', ENDPOINT + "/pet", headers=json_headers, json=json_body)
        #print(r.prepare().url)
        #print(r.prepare().body)
        #print("one")
        #print(r.prepare().headers)

        response = requests.post(ENDPOINT + "/pet", headers=json_headers, json=body )
#
        #print(response.request.headers)
        #print("response.request.body")
        #print(response.request.body)
        #print("one")
        #print(response.request.body)
        return response

