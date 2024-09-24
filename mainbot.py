import json
import webbrowser

with open('channel_messages.json', 'r') as file: # Loading json data from telegram 
    data = json.load(file)

for message in data:
    message_text = message.get('message', '')
    
    #im checking if the message contains a number. In my target telegram group, it was only allowed to post "Update" or a number if the appointments were open"
    if any(char.isdigit() for char in message_text):
        webbrowser.open("https://www.youtube.com/") #using youtube as a dummy website but enter your desired website
        break  # Stop the loop if the desired website is opened.
