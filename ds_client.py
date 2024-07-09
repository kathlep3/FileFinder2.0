# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python
#client
# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883
#post bio join
import socket
from ds_protocol import extract_json, join_act, post_act, bio_act
import json
from Profile import Profile, Post

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
    '''
    The send function joins a ds server and sends a message, bio, or both
    :param server: The ip address for the ICS 32 DS server.
    :param port: The port where the ICS 32 DS server is accepting connections.
    :param username: The user name to be assigned to the message.
    :param password: The password associated with the username.
    :param message: The message to be sent to the server.
    :param bio: Optional, a bio for the user.
    '''
    print()
    print("About to connect...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))
        print(f"Client connected to {server} on {port}.")

        send = client.makefile("w")
        recv = client.makefile("r")

        send_server = join_act(username, password)
        
        trans_mess = json.dumps(send_server)
        
        send.write(trans_mess)
        send.flush()

        srv_tuple = str(recv.readline())
        extracted_resp = extract_json(srv_tuple)

        e_response = extracted_resp[0]
        e_type = extracted_resp[1]
        e_message = extracted_resp[2]
        print(e_message)
        print()

        if len(e_response) > 2:
            token = e_response['token']

        if e_type == 'ok':
            if message is not '':
                send_post = str(post_act(message, token))
                send.write(send_post)
                send.flush()
                print("You have successfully posted!")
                print()
            if bio:
                send_bio = str(bio_act(bio, token))
                send.write(send_bio)
                send.flush()
                print("Your bio has been updated!")
                print()
            return True
        
        elif e_type == 'error':
            return False

# IPaddress = "168.235.86.101"
# Port = 3021