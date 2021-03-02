import discord
import asyncio

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
        await message.channel.send("검색하고 싶은 음악 제목을 입력해주세요!")

client.run(Settings.token)
