import httpimport
with httpimport.github_repo('dalbeh', 'telegram-telethon', branch = 'main'):
    import telegramTelethon
import asyncio


telegramClient = telegramTelethon.telegramBot('raw-data-extracted')
loop = asyncio.get_event_loop()
client = loop.run_until_complete(telegramClient.connect())

group = 'https://t.me/WalkWithStepTelegram'


# Get Users Admins
loop.run_until_complete(telegramClient.getParticipants(client, group, 100, 'ADMIN'))