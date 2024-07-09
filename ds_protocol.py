# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883

import json
from collections import namedtuple
from Profile import Profile, Post

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ['response','type','message'])


def extract_json(json_msg:str) -> DataTuple:
    '''
    Call the json.loads function on a json string and convert it to a DataTuple object
    TODO: replace the pseudo placeholder keys with actual DSP protocol keys
    '''
    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        typee = json_obj['response']["type"]
        message = json_obj['response']['message']

    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(response, typee, message)


def join_act(username, password):
    print("User joined.")
    print()
    client_msg = {"join": {"username": username,"password": password,"token":""}}
    return client_msg


def post_act(new_post, token=None):
    client_msg = {"token": token, "post": new_post}#CHECK FORMAT
    json_post = json.dumps(client_msg)
    return json_post


def bio_act(new_post, token=None):
    client_msg = {"token": token, "bio": {"entry": new_post,"timestamp": ""}}
    json_bio = json.dumps(client_msg)
    return json_bio
