import discord
import os
import os.path
import sys
import asyncio
import shutil

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

@client.event
async def on_ready():
    print('Linux Program TREE is required.')
    print('Logged in as ' + client.user.name + ' ' + str(client.user.id)+'')
    print('------')
    if not CheckFolder(dir_path):
        print('Content folder does not exist. Creating...')
        os.mkdir(dir_path)
    print('dir_path: '+dir_path)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower().split()
    print(content)
    if content[0] == '!add':
        if 'item' in content:
            curPath = dir_path
            messageCurPath = ""
            i = 1
            while content[i] != 'item':
                if not CheckFolder(curPath):
                    await message.channel.send('ERROR: There is no item called '+ content[i+1] +'!')
                    return
                curPath += '/'+content[i]
                messageCurPath += content[i]+'/'
                i += 1
            AddFolder(curPath+'/'+content[i+1])
            await message.channel.send('INFO: Created a item called '+messageCurPath+content[i+1]+'!')
            return
        else:
            await message.channel.send('ERROR: Bad syntax! You must use \"item\" in your command.')
            return
        return
    elif content[0] == '!remove':
        if 'item' in content:
            curPath = dir_path
            messageCurPath = ""
            i = 1
            while content[i] != 'item':
                if not CheckFolder(curPath):
                    await message.channel.send('ERROR: There is no item called '+ content[i+1] +'!')
                    return
                curPath += '/'+content[i]
                messageCurPath += content[i]+'/'
                i += 1
            RemoveFolder(curPath+'/'+content[i+1])
            await message.channel.send('INFO: Removed a item called '+messageCurPath+content[i+1]+'!')
            return
        else:
            await message.channel.send('ERROR: Bad syntax! You must use \"item\" in your command.')
            return
        return
    elif content[0] == '!item':
        os.system("tree -n -F -a Content | sed 's/├\|─\|│\|└/ /g' > items")
        await message.channel.send('Here is all of the items.')
        f = open("items","r")
        line = f.readline()
        while line:
            await message.channel.send('_ _ '+line)
            print(line)
            line = f.readline()
            if line == '\n':
                line = None
        f.close()
        os.remove(os.path.dirname(os.path.realpath(__file__))+'/items')
        await message.channel.send('End of Content.')        
        print('End Command\n')
        
f=open("token.txt","r")
token = f.readline()
f.close()
client.run(token)
