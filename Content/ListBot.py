import discord
import os
import os.path
import sys
import asyncio
import re

client = discord.Client()
dir_path = os.path.dirname(os.path.realpath(__file__))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#args = message.content.slice(prefix.length).trim().split(/ +/g);
#command = args.shift().shift().toLowerCase();

#re.compile('!add \"(.*)\" list \"(.*)\"|!add list (?:\"(\w+)\")')

@client.event
async def on_message(message):
    if message.content.startswith('!add list'):
        matchedContent = re.compile('!add list (?:\"(\w+)\")').match(message.content)
        os.makedirs(dir_path+matchedContent[1])
        await client.send_message(message.channel, 'Calculating messages...')

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('NDkxNjk0MzA0MTI2MDQyMTEy.DrogKg.PEATf9YqFIMVNEj1c6PE8dqtTKY')
