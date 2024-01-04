import requests
import json
import pytest
#import sys
#sys.path.insert(0,"..")
import rest_client_initialization_and_actions


def test_getPetsWhichAreSold():
    response = rest_client_initialization_and_actions.RestClientInitializationAndActions.getPetsWhichAre("sold")
    assert response.status_code==200
    print(response)

    print("me")

    print(response.json())


    # Store JSON data in API_Data
    API_Data = response.json()

    listOfPets = API_Data.values(["id"])

    print(listOfPets)
    
