import httpimport
with httpimport.github_repo('dalbeh', 'telegram-telethon', 'telegramTelethon', branch='main'):
    import telegramTelethon
import asyncio


telegramClient = telegramTelethon.telegramBot('raw-data-extracted')
loop = asyncio.get_event_loop()
client = loop.run_until_complete(telegramClient.connect())

group = 'https://t.me/WalkWithStepTelegram'


# Get Messages Historic
loop.run_until_complete(telegramClient.getMessagesFromDays(client, group, 100, '25/12/21','08/05/22'))