import discord
import asyncio

import settings

Settings = settings.Settings()

client = discord.Client()

@client.event
async def on_ready():
    print("로그인 성공!!")
    print(client.user.name + "(%s)" %client.user.id)

    #change chatbot's game status
    game = discord.Game(name="명령 대기")
    await client.change_presence(status=discord.Status.idle, activity=game)

client.run(Settings.token)
