import requests
import json
import pytest
#import sys
#sys.path.insert(0,"..")
import rest_client_initialization_and_actions


def test_getPetsWhichAreSold():
    rest_client = instantiate_a_client()
    response = rest_client.getPetsWhichAre("sold")
    assert response.status_code==200
    #print(response.json())
    
    # Store JSON data in API_Data
    API_Data = response.json()





def instantiate_a_client():
    rest_client = rest_client_initialization_and_actions.RestClientInitializationAndActions()
    return rest_client

    
