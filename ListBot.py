import discord
import os
import os.path
import sys
import asyncio

client = discord.Client()
dir_path = os.path.dirname(os.path.realpath(__file__))+'/Content/'

def CheckFolder(path):
    if os.path.exists(path):
        return True
    else:
        return False

def RemoveFolder(path):
    if CheckFolder(path):
        shutil.rmtree(path)

def AddFolder(path):
    if not CheckFolder(path):
        os.mkdir(path)

def AddItem(path):
    if not CheckFolder(path):
        return
    f=open(path,'w+')
    f.close()

def RemoveItem(path):
    RemoveFolder(path)
    return

@client.event
async def on_ready():
    print('Linux Program TREE is required.')
    print('Logged in as' + client.user.name + ' ' + client.user.id+'')
    print('------')
    if not CheckFolder(dir_path):
        print('Content folder does not exist. Creating...')
        os.mkdir(dir_path)
    print('dir_path: '+dir_path)

@client.event
async def on_message(message):
    content = message.content.lower().split()
    print(content)
    if content[0] == '!add':
        if 'list' in content:
            curPath = dir_path
            i = 1
            while content[i] != 'list':
                if not CheckFolder(curPath):
                    await client.send_message(message.channel, 'ERROR: There is no list called '+ content[i] +'!')
                    return
                curPath += '/'+content[i]
                i += 1
            AddFolder(curPath+'/'+content[len(content)-1])
            await client.send_message(message.channel, 'INFO: Created a list called '+content[i]+'!')
            return
        else:
            curPath = dir_path
            i = 1
            while i != len(content) - 2:
                if not CheckFolder(curPath):
                    await client.send_message(message.channel, 'ERROR: There is no list called '+ content[i] +'!')
                    return
                curPath += content[i]
                i += 1
            AddItem(curPath+'/'+content[len(content)-1])
            return
        return
    elif content[0] == '!remove':
        if 'list' in content:
            curPath = dir_path
            i = 1
            while content[i] != 'list':
                if not CheckFolder(curPath):
                    await client.send_message(message.channel, 'ERROR: There is no list called '+ content[i] +'!')
                    return
                curPath += '/'+content[i]
                i += 1
            RemoveFolder(curPath+'/'+content[len(content)-1])
            await client.send_message(message.channel, 'INFO: Removed a list called '+content[len(content_=1)]+'!')
            return
        else:
            curPath = dir_path
            i = 1
            while i != len(content) - 2:
                if not CheckFolder(curPath):
                    await client.send_message(message.channel, 'ERROR: There is no list called '+ content[i] +'!')
                    return
                curPath += content[i]
                i += 1
            RemoveItem(curPath+'/'+content[len(content)-1])
            return
        return
    elif message.content.startswith('!list'):
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
        
<<<<<<< HEAD
f=open("/home/pi/KC_Python_ListBot/token.txt","r")
token = f.readline();
=======
f=open("token.txt","r")
token = f.readline()
>>>>>>> 07da2c909d88cf925ee3d9c0d89b30b856e4fefc
f.close()
client.run(token)
