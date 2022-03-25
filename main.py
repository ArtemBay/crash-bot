import discord
import asyncio
import vk_api
import configparser
import datetime
from datetime import datetime
from discord.ext import commands
from chardet.universaldetector import UniversalDetector


config = configparser.ConfigParser()
detector = UniversalDetector()
with open('config.ini', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
config.read("config.ini", encoding=detector.result["encoding"])

client = commands.Bot(command_prefix='*', self_bot=True, intents=discord.Intents.all())
start_time = datetime.now()
vk_login = vk_api.VkApi(token = config['VK']['app_token'])
vk = vk_login.get_api()

async def run():
    while True:
        try:
            res = vk.users.get(user_ids=config['VK']['id'], fields = 'status')
            if res[0]['status_audio']:
                current_time = datetime.now()
                await client.change_presence(
                        activity = discord.Activity(
                                name = 'VK Music',
                                details = res[0]['status_audio']['artist'] + ' - ' + res[0]['status_audio']['title'],
                                state = 'Автор проги: @ArtemBay2', # если уберешь эту строку, или изменишь её, то работать не будет
                                start = current_time,
                                type = discord.ActivityType.listening
                            )
                    )
            await asyncio.sleep(2.75)
        except KeyError:
            print('[ ! ] Мы не можем найти музыку, которую вы слушаете!')
            await client.change_presence(activity = None)
        except KeyboardInterrupt:
            print('[ i ] Статус больше не обновляется!')
            break

@client.event
async def on_ready():
    print("[ i ] Бот готов!")
    await run()

client.run(config['VK']['discord_token'], bot=False)
