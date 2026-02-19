# Copyright (c) 2025 devgagan : https://github.com/devgaganin
# Licensed under the GNU General Public License v3.0.
# See LICENSE file in the repository root for full license text.

print(">>> SC: importing shared_client")

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import sys

print(">>> SC: config and libraries imported")

print(">>> SC: before Telethon client")
client = TelegramClient("telethonbot", API_ID, API_HASH)
print(">>> SC: after Telethon client")

print(">>> SC: before Pyrogram bot client")
app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
print(">>> SC: after Pyrogram bot client")

print(">>> SC: before Pyrogram userbot client")
userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)
print(">>> SC: after Pyrogram userbot client")

async def start_client():
    print(">>> SC: entering start_client()")
    if not client.is_connected():
        print(">>> SC: starting Telethon bot client")
        await client.start(bot_token=BOT_TOKEN)
        print("SpyLib started...")

    if STRING:
        try:
            print(">>> SC: starting Pyrogram userbot client")
            await userbot.start()
            print("Userbot started...")
        except Exception as e:
            print(f"Hey honey!! check your premium string session, it may be invalid or expired: {e}")
            sys.exit(1)
    else:
        print(">>> SC: no STRING provided, skipping userbot start")

    print(">>> SC: starting Pyrogram bot app")
    await app.start()
    print("Pyro App Started...")
    return client, app, userbot
