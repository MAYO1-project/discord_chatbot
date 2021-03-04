import discord
import asyncio
import youtube_dl
import re

import token_settings

Settings = token_settings.Settings()

client = discord.Client()

@client.event
async def on_ready():
    print("Login Success!!")
    print(client.user.name + "(%s)" %client.user.id)

    #change chatbot's game status
    game = discord.Game(name="Waiting")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!music"):
        msg = message.content.split(" ")
        #await message.channel.send("재생하고 싶은 음악의 youtube url을 입력해주세요!")
        url = msg[1]

        # download music from youtube url
        ydl_opts = {
            'format':'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',

            }],
            'outtmpl': 'song.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # bot join in user's voice channel
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect()
        
        vc.play(discord.FFmpegPCMAudio('song.mp3'))

        # change bot status to Music Playing
        game = discord.Game(name="Music Playing♪")
        await client.change_presence(status=discord.Status.online, activity=game)
        await message.channel.send("Now playing~♪")

''' # Finish music playing
    if message.content == "!Fin":
        voice_channel = message.author.voice.channel
        #vc = await voice_channel.connect()
        await vc.disconnect()
        await message.channel.send("Leave this voice channel!")
        
        game = discord.Game(name="Waiting")
        await client.change_presence(status=discord.Status.online, activity=game)
'''    
client.run(Settings.token)
