import configparser
from telethon import TelegramClient
from telethon.events import NewMessage
import asyncio
import webbrowser

async def handle_new_messages(event: NewMessage.Event): #an asynchronous function that handles incoming messages
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

    api_id = config['Telegram']['api_id']
    api_hash = config['Telegram']['api_hash']
    phone = config['Telegram']['phone']
    username = config['Telegram']['username']
    
    client = TelegramClient(username, api_id, api_hash)
    await client.start()
    print("Client Created")

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except Exception as e:
            print(f"Error signing in: {e}")
            return

# this part takes input for the telegram group that you want to check.
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
