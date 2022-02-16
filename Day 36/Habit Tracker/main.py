
from urllib import response
import requests
import datetime as dt
import os
from dotenv import load_dotenv


load_dotenv()

USERNAME = os.environ['username']
TOKEN = os.environ["token"]
GRAPHID = os.environ["graphid"]
pixela_endpoint = "https://pixe.la/v1/users"

user_parameter = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
today = dt.datetime.now()

# response = requests.post(url = pixela_endpoint,json = user_parameter)
# print(response.text)
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_quantity_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
graph_quantity_endpoint_edit = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20220213"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/20220213"


graph_parameters = {
    "id":GRAPHID,
    "name":"Hours Learnt",
    "unit":"Hours",
    "type": "float",
    "color": "momiji" 
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# Creating a graph #
# response = requests.post(url=graphs_endpoint,json=graph_parameters,headers=headers)
# print(response.text)


quantity_parameter = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("How many hours you learned coding today ?"),
}
edit_quantity_parameter ={
    "quantity":"1"
}

# Posting a data using ///POST///
response = requests.post(graph_quantity_endpoint,json=quantity_parameter,headers=headers)
print(response.text)


# Editing a Data using ///PUT///
# response = requests.put(graph_quantity_endpoint_edit,json=edit_quantity_parameter,headers=headers)
# print(response.text)


# Deleting a data using ///DELETE///
# response = requests.delete(delete_endpoint,headers=headers)
# print(response.text)