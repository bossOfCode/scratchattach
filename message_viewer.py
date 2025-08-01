"""Module importing scratchattach to use for the projrct"""
import os
import sys
import time
import warnings
import scratchattach as scratch3
from scratchattach import Encoding

warnings.filterwarnings('ignore', category=scratch3.LoginDataWarning)

passwrd = os.environ.get('PASS')

session = scratch3.login("Boss_1sALT", passwrd)
cloud = session.connect_cloud("1054907254") #replace with your project id
client = cloud.requests()

@client.request
def message_ping(argument1):
    "Main client request"
    print(f"Message Count requested for {argument1}")
    os.system(f"echo Message Count requested for {argument1}")
    user = scratch3.get_user(argument1)
    return user.message_count()

@client.request
def new_scratcher_detect(argument1):
    "Secondary client request"
    print(f"Checking if {argument1} is a new scratcher")
    os.system(f"echo Checking if {argument1} is a new scratcher")
    user = session.connect_user(argument1)
    answer = Encoding.encode(user.is_new_scratcher())
    return answer

@client.event
def on_ready():
    "Runs when client is ready."
    print("Request handler is running")
    os.system("echo Request handler is running")

@client.event
def on_error(request, e):
    "Runs when client runs into error"
    print("Request: ", request.request.name, request.requester, request.arguments, request.timestamp, request.request_id)
    print("Error that occured: ", e)

@client.event
def on_request(request):
    "Runs when client receives request"
    print("Received request", request.request.name, request.requester, request.arguments, request.timestamp, request.request_id)
    
client.start(thread=True) #make sure this is ALWAYS at the bottom of your Python file
