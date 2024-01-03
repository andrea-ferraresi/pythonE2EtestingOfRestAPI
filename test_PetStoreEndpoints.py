import requests
import json
import pytest


ENDPOINT = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'


def test_get_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code==200
    print(response)

    print("me")

    print(response.json())


    # Store JSON data in API_Data
    API_Data = response.json()

    listOfPets = API_Data.values(["id"])

    print(listOfPets)
    
