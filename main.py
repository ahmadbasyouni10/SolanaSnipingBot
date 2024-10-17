from telethon import TelegramClient, events

import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
GROUPID = os.getenv('GROUPID')
PHONE = os.getenv('PHONE')

# Check if variables are loaded correctly
if not all([API_ID, API_HASH, PHONE, GROUPID]):
    print("Error: One or more environment variables are not set.")
    exit(1)

phone_number = os.getenv('PHONE')

client = TelegramClient('crypto_tracker', API_ID, API_HASH)

async def fetch_users1():
    try:
        group = await client.get_entity(GROUPID)
        print(f"Fetched group: {group.title}")
    except Exception as e:
        print(f"Error fetching group: {e}")

async def fetch_users():
    try:
        users = await client.get_participants(GROUPID)
        print(f"Total participants: {len(users)}")
        for user in users:
            print(f"Username = {user.id}")
    

    except Exception as e:
        print(f"Error fetching users: {e}")
    

async def main():
    # Initialize client using telethon
    await client.start(phone = PHONE)
    print("Client Created")
    await fetch_users1()
    await fetch_users()

    # Listen for new Messages
    @client.on(events.NewMessage(chats=GROUPID)) # GROUPID
    async def handler(event):
        if event.message.from_id == "SolSnatcher_bot":
            message = event.message.message
            print("Received message from @SolSnatcher_bot")
            print(message)
            # HERE WILL PARSE CORRECT MESSAGE ONLY
            # SET LOGIC HERE FOR CONTRACT, BUY AMOUNT, ETC
        sender = await event.get_sender()
        print(f"Message by: {sender.id}")


    print("Listening for messages")
    await client.run_until_disconnected()

asyncio.run(main())










