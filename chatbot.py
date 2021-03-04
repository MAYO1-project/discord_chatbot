import discord
import asyncio
import youtube_dl
import re

import token_settings

Settings = token_settings.Settings()

client = discord.Client()

@client.event
async def on_ready():
    print("로그인 성공!!")
    print(client.user.name + "(%s)" %client.user.id)

    #change chatbot's game status
    game = discord.Game(name="명령 대기")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!music"):
        msg = message.content.split(" ")
        #await message.channel.send("재생하고 싶은 음악의 youtube url을 입력해주세요!")
        url = msg[1]

        ydl_opts = {
            'format':'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',

            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        #channel = message.author.voice.channel
        #await channel.connect()
      
        
client.run(Settings.token)
