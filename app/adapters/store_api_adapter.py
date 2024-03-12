import json
import logging
from typing import List
from datetime import datetime  # Import datetime module
import requests
from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_api_gateway import StoreGateway

class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        try:
            print("Api problrem --- ", processed_agent_data_batch)
            # Make a POST request to the Store API endpoint with the processed data
            my_dict = {}
            # for data in processed_agent_data_batch:
            #     my_dict[data.]

            # data_json = json.dumps([data.dict() for data in processed_agent_data_batch], default=default)
            # print(" JSON", data_json)
            # response = requests.post(f"{self.api_base_url}/processed_agent_data", json=data_json)

            
            data = [json.loads(item.json()) for item in processed_agent_data_batch]
            print("-----------------------",data)
            response = requests.post(f"{self.api_base_url}/processed_agent_data/", json=data)
            if response.status_code == 200:
            
                return True
            else:
                return False
        except Exception as e:
            print(f"Error saving data to Store API: {e}")
            return False

def default(o):
    return o.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'