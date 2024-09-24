import json
import webbrowser

# Load the JSON data
with open('channel_messages.json', 'r') as file:
    data = json.load(file)

# Iterate over each message
for message in data:
    # Get the message text
    message_text = message.get('message', '')
    
    # Check if the message contains a number
    if any(char.isdigit() for char in message_text):
        # Open YouTube if a number is found
        webbrowser.open("https://www.youtube.com/")
        break  # Stop iterating if YouTube is opened
