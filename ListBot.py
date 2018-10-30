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
    dir_path = os.path.dirname(os.path.realpath(__file__))+'/Content'
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    if not os.path.exists(dir_path):
        print('Content folder does not exist. Creating...')
        os.mkdir(dir_path)
    dir_path+='/'

#args = message.content.slice(prefix.length).trim().split(/ +/g);
#command = args.shift().shift().toLowerCase();

#re.compile('!add \"(.*)\" list \"(.*)\"|!add list (?:\"(\w+)\")')

@client.event
async def on_message(message):
    if message.content.startswith('!add list'):
        print('Trying to make a list...')
        matchedContent = re.compile('!add list (?:\"(\w+)\")').match(message.content)
        if matchedContent is not None:
            if os.path.exists(dir_path+matchedContent[1]):
                print('Command Failed: List already exists.')
                await client.send_message(message.channel, 'List already exists: '+matchedContent[1])
            else:
                os.makedirs(dir_path+matchedContent[1])
                print('Made List: '+matchedContent[1])
                await client.send_message(message.channel, 'Made List: '+matchedContent[1])
        else:
            print('Command Failed: Bad Syntax')
            await client.send_message(message.channel, 'Try again.')
            await client.send_message(message.channel, 'The command syntax is "!add list "<list name>"')


    elif message.content.startswith('!add'):
        print('Trying to add to a list...')
        matchedContent = re.compile('!add \"(.*)\" \"(.*)\"').match(message.content)
        if matchedContent is not None:
            print('Matched regex 1, 2...')
            if os.path.exists(dir_path+matchedContent[1]):
                print('List "'+matchedContent[1]+'" exists... ')
                f = open(dir_path+matchedContent[1]+'/'+matchedContent[2],'w+')
                f.close()
                print('Added "'+matchedContent[2]+'" to list "'+matchedContent[1]+'"')
                await client.send_message(message.channel, 'Added "'+matchedContent[2]+' to list "'+matchedContent[1]+'"')
            else:
                print('List "'+matchedContent[1]+'" does not exist.')
                await client.send_message(message.channel, 'List "'+matchedContent[1]+'" does not exist.')
        else:
            print('Command failed: Bad Syntax')
            await client.send_message(message.channel, 'Try again.')
            await client.send_message(message.channel, 'The command syntax is "!add "<list>" "<item>"')
    print('\n')
    


client.run('NDkxNjk0MzA0MTI2MDQyMTEy.DrogKg.PEATf9YqFIMVNEj1c6PE8dqtTKY')
