import requests
import json
import pytest
#import sys
#sys.path.insert(0,"..")
import rest_client_initialization_and_actions


@pytest.mark.skip(reason="skip while developing other tests")
def test_getPetsWhichAreSold():
    client_of_the_application = initialise_a_client_of_the_application()
    response = client_of_the_application.getPetsWhichAre("sold")
    assert response.status_code==200
    #print(response.json())

    # Store JSON data in API_Data
    API_Data = response.json()



def test_addPetToTheStore():
    client_of_the_application = initialise_a_client_of_the_application()
    response = client_of_the_application.addPetToTheStore(
                                             "name_of_pet", 
                                             "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
    print(response.json())
    
    assert response.status_code==200
    #print(response.json())

    # Store JSON data in API_Data
    API_Data = response.json()






def initialise_a_client_of_the_application():
    rest_client = rest_client_initialization_and_actions.RestClientInitializationAndActions()
    return rest_client

    
