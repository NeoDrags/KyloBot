# import date
import os
import random
import time
import discord

TOKEN = "NzQwODU1NjczNjk2NDE5ODYw.XyvFnQ.dGoekmCe6y5pfKU53NBnX8CYQaE"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('happy birthday'):
        response = "happy birthday!"
        await message.channel.send(response)
    elif message.content == '$help':
        response = """here are the commands that you can type they are : 
                    1) Whenever you wish someone happy birthday it will also respond happy birthday  
                    2) Type $help to execute this command which will display the commands that you can execute
                    3) Type $time to show the current time
                    4) Type $toss to peform the a coin toss
                    5) Type $date to show current date"""
        await message.channel.send(response)
    elif message.content == '$toss':
        response = "Coin tossed"
        await message.channel.send(response)
        TossNum = random.randint(0, 1)
        if TossNum == 0:
            await message.channel.send("Heads")
        else :
            await message.channel.send("Tails")
    elif message.content == '$time':
        time = time.localtime(time.time())
        await message.channel.send("The cureent time is : ", time)
    elif message.content == '$date':
        date = date.today()
        await message.channel.send('Today is : ', date)
    elif message.content.startswith('bye'):
        await message.channel.send('Bye see you soon')
    elif message.content.startswith('$') and message.content != '$date' and message.content != '$time' and message.content != '$toss' :
        await message.channel.send("That command does not exist")
client.run(TOKEN)
