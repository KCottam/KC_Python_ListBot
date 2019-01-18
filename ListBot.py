import discord
import os
import os.path
import sys
import asyncio
import re
import shutil

def remove_folder(path):
    # check if folder exists
    if os.path.exists(path):
         # remove if exists
         shutil.rmtree(path)

client = discord.Client()
dir_path = os.path.dirname(os.path.realpath(__file__))+'/Content/'
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    if not os.path.exists(dir_path):
        print('Content folder does not exist. Creating...')
        os.mkdir(dir_path)
    print('dir_path: '+dir_path)
    print('Linux Program TREE is required.')

async def addAList(message):
    matchedContent = re.compile('!add list (?:\"(.*)\")').match(message.content)
    if matchedContent is not None:
        if  os.path.exists(dir_path+matchedContent[1]) is not False:
            print('Command Failed: List already exists.')
            await client.send_message(message.channel, 'List already exists: '+matchedContent[1])
            return
        os.makedirs(dir_path+matchedContent[1])
        print('Made List: '+matchedContent[1])
        await client.send_message(message.channel, 'Made List: '+matchedContent[1])
    else:
        print('Command Failed: Bad Syntax')
        await client.send_message(message.channel, 'Try again.')
        await client.send_message(message.channel, 'The command syntax is "!add list "<list name>"')

async def addToList(message, matchedContent):
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

async def addASublist(message, matchedContent):
    print('Matched regex 1 list 2...')
    if os.path.exists(dir_path+matchedContent[1]):
        print('List "'+matchedContent[1]+'" exists... ')
        if os.path.exists(dir_path+matchedContent[1]+'/'+matchedContent[2]):
            print('Sublist "'+matchedContent[2]+'" already exists!')
            await client.send_message(message.channel, 'Sublist "'+matchedContent[2]+'" already exists!')
            return
        os.mkdir(dir_path+matchedContent[1]+'/'+matchedContent[2])
        print('Added sublist "'+matchedContent[2]+'" to list "'+matchedContent[1]+'"')
        await client.send_message(message.channel, 'Added sublist "'+matchedContent[2]+'" to list "'+matchedContent[1]+'"')

async def addToSublist(message, matchedContent):
    print('Matched regex 1, 2, 3...')
    if os.path.exists(dir_path+matchedContent[1]+'/'+matchedContent[2]):
        print('Sublist "'+matchedContent[2]+'" exists in list "'+matchedContent[1]+'"...')
        f = open(dir_path+matchedContent[1]+'/'+matchedContent[2]+'/'+matchedContent[3],'w+')
        f.close()
        print('Added "'+matchedContent[3]+'" to sublist "'+matchedContent[2]+'" in list "'+matchedContent[1]+'"')
        await client.send_message(message.channel, 'Added "'+matchedContent[3]+'" to sublist "'+matchedContent[2]+'" in list "'+matchedContent[1]+'"')
    else:
        if os.path.exists(dir_path+matchedContent[1]):
            print('Sublist "'+matchedContent[2]+'" does not exist in list "'+matchedContent[1]+'"...')
            await client.send_message(message.channel, 'Sublist "'+matchedContent[2]+'" does not exist in list "'+matchedContent[1]+'"')
        else:
            print('List "'+matchedContent[1]+'" does not exist.')
            await client.send_message(message.channel, 'List "'+matchedContent[1]+'" does not exist.')

async def removeAList(message):
    print('Trying to remove a list...')
    matchedContent = re.compile('!remove list (?:\"(.*)\")').match(message.content)
    if matchedContent is not None:
        if  os.path.exists(dir_path+matchedContent[1]) is not False:
            remove_folder(dir_path+matchedContent[1])
            print('Removed List: '+matchedContent[1])
            await client.send_message(message.channel, 'Removed List: '+matchedContent[1])
            return
        print('Command Failed: List does not exist.')
        await client.send_message(message.channel, 'List does not exist: '+matchedContent[1])
    else:
        print('Command Failed: Bad Syntax')
        await client.send_message(message.channel, 'Try again.')
        await client.send_message(message.channel, 'The command syntax is "!remove list "<list name>"')

async def removeFromList(message, matchedContent):
    print('Matched regex 1, 2...')
    if os.path.exists(dir_path+matchedContent[1]+'/'+matchedContent[2]):
        print('Item "'+matchedContent[2]+'" exists... ')
        os.remove(dir_path+matchedContent[1]+'/'+matchedContent[2])
        print('Removed "'+matchedContent[2]+'" from list "'+matchedContent[1]+'"')
        await client.send_message(message.channel, 'Removed "'+matchedContent[2]+' from list "'+matchedContent[1]+'"')
    else:
        print('Item "'+matchedContent[2]+'" does not exist.')
        await client.send_message(message.channel, 'Item "'+matchedContent[3]+'" does not exist.')

async def removeFromSublist(message, matchedContent):
    print('Matched regex 1, 2, 3...')
    if os.path.exists(dir_path+matchedContent[1]+'/'+matchedContent[2]+'/'+matchedContent[3]):
        print('Item "'+matchedContent[3]+'" exists in sublist "'+matchedContent[2]+'" in list "'+matchedContent[1]+'"...')
        os.remove(dir_path+matchedContent[1]+'/'+matchedContent[2]+'/'+matchedContent[3])
        print('Removed "'+matchedContent[3]+'" from sublist "'+matchedContent[2]+'" in list "'+matchedContent[1]+'"')
        await client.send_message(message.channel, 'Removed "'+matchedContent[3]+'" from sublist "'+matchedContent[2]+'" in list "'+matchedContent[1]+'"')
    else:
        print('Item "'+matchedContent[3]+'" does not exist.')
        await client.send_message(message.channel, 'Item "'+matchedContent[3]+'" does not exist.')

async def removeASublist(message, matchedContent):
    print('Matched regex 1 list 2...')
    if os.path.exists(dir_path+matchedContent[1]+'/'+matchedContent[2]):
        print('Sublist "'+matchedContent[2]+'" exists... ')
        remove_folder(dir_path+matchedContent[1]+'/'+matchedContent[2])
        print('Removed List: '+matchedContent[2])
        await client.send_message(message.channel, 'Removed List: '+matchedContent[2])
        return
    print('Command Failed: List does not exist.')
    await client.send_message(message.channel, 'Sublist does not exist: '+matchedContent[2])

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.content.startswith('!add list'):
        print(message.content+'\n')
        print('Trying to make a list...')
        await addAList(message)
        print('\n')
    elif message.content.startswith('!add'):
        print(message.content+'\n')
        print('Trying to add to a list...')
        matchedContent = re.compile('!add \"(.*)\" \"(.*)\" \"(.*)\"').match(message.content)
        if matchedContent is not None:
            await addToSublist(message, matchedContent)
            print('\n')
            return
        matchedContent = re.compile('!add \"(.*)\" \"(.*)\"').match(message.content)
        if matchedContent is not None:
            await addToList(message, matchedContent)
            print('\n')
            return
        matchedContent = re.compile('!add \"(.*)\" list \"(.*)\"').match(message.content)
        if matchedContent is not None:
            await addASublist(message, matchedContent)
            print('\n')
            return
        print('Command failed: Bad Syntax\n')
        await client.send_message(message.channel, 'Command failed: Bad Syntax')
    elif message.content.startswith('!remove list'):
        print(message.content+'\n')
        print('Trying to remove a list...')
        await removeAList(message)
        print('\n')
    elif message.content.startswith('!remove'):
        print(message.content+'\n')
        print('Trying to remove from a list...')
        matchedContent = re.compile('!remove \"(.*)\" \"(.*)\" \"(.*)\"').match(message.content)
        if matchedContent is not None:
            await removeFromSublist(message, matchedContent)
            print('\n')
            return
        matchedContent = re.compile('!remove \"(.*)\" \"(.*)\"').match(message.content)
        if matchedContent is not None:
            await removeFromList(message, matchedContent)
            print('\n')
            return
        matchedContent = re.compile('!remove \"(.*)\" list \"(.*)\"').match(message.content)
        if matchedContent is not None:
            await removeASublist(message, matchedContent)
            print('\n')
            return
        print('Command failed: Bad Syntax\n')
        await client.send_message(message.channel, 'Command failed: Bad Syntax')
    elif message.content.startswith('!list'):
        print(message.content+'\n')
        print('Displaying Lists...')
        os.system("tree -n -F -a Content | sed 's/├\|─\|│\|└/ /g' > lists")
        await client.send_message(message.channel, 'Here is all of the lists.')
        f = open("lists","r")
        line = f.readline()
        while line:
            await client.send_message(message.channel, '_ _ '+line)
            print(line)
            line = f.readline()
            if line == '\n':
                line = None
        f.close()
        os.remove(os.path.dirname(os.path.realpath(__file__))+'/lists')
        await client.send_message(message.channel, 'End of Content.')        
        print('End Command\n')

        
f=open("/home/pi/KC_Python_ListBot/token.txt","r")
token = f.readline();
f.close()
client.run(token)
