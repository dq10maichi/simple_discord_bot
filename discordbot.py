import discord
import configparser

inifile = configparser.ConfigParser()
inifile.read('./config.ini','UTF-8')

token = inifile.get('discord','token')
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("こん"):
        if client.user != message.author:
            m = "こんにちは" + message.author.name + "さん！"
            await message.channel.send(m)
client.run(token)
