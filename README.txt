Kathleen Pham
kathlep3@uci.edu

Assignment3


The a3.py file interacts with the user by displaying a print menu which will prompt them to enter a command. When the user enters an input beginning with the command O or C, they are joined to the server through the ds_client.py send function which will collect username and password to create or load an existing profile. Then, the user is asked if they want to edit or print any contents of their profile. If so, they can add a bio or a post. Server, port, username, password, bio, and post are collected as parameters of the send function. They will also be converted with json.dumps to their respective functions, either bio_act or post_act, depending on which the user would like to interact with. The file ds_protocol.py is meant to convert all the servers messages to the client and convert them into usable information through extract_json.py. Towards the middle of the send function there are also methods to extract tokens and messages from the tuples and dictionaries. 