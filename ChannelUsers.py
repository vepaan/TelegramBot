import configparser
import json
import asyncio
import webbrowser
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, PeerChannel

# Reading configs
config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Creating the client and connect
client = TelegramClient(username, api_id, api_hash)


async def main(phone):
    await client.start()
    print("Client Created")
    if await client.is_user_authorized() == False: #send code to phone to know user is real
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    user_input_channel = input("Enter entity (Telegram URL or entity id):")

    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    async def handle_new_messages(event):
        message = event.message
        print(f"New message received: '{message.message}'")

        # Check if the message contains a number
        if any(char.isdigit() for char in message.message):
            print("Message contains a number. Opening YouTube...")
            webbrowser.open("youtube.com") #put your desired website here

    client.add_event_handler(handle_new_messages, event=events.NewMessage(incoming=True, chats=[my_channel]))

    print("Listening for new messages...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main(phone))
