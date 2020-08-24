from dotenv import load_dotenv
import os
import random
from datetime import datetime
import discord

load_dotenv()

TOKEN = os.getenv("TOKEN")

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
    
    elif str.lower(message.content) == '$help':
        e = discord.Embed()
        e.add_field(name = "response", value = """here are the commands that you can type they are :
                    1) Whenever you wish someone happy birthday it will also respond happy birthday
                    2) Type $help to execute this command which will display the commands that you can execute
                    3) Type $time to show the current time and date
                    4) Type $toss to peform the a coin toss
                    5) Type $date to show current date
                    6) Type $tell me a joke to get a random joke from the internet""" , inline = False)
        await message.channel.send(embed=e)

    elif str.lower(message.content) == '$toss':
        response = "Coin tossed"
        await message.channel.send(response)
        TossNum = random.randint(0, 1)
        if TossNum == 0:
            await message.channel.send("Heads")
        else :
            await message.channel.send("Tails")
    
    elif str.lower(message.content) == '$time':
        time = "The current time is " + str(datetime.now().time())
        await message.channel.send(time)
    
    elif str.lower(message.content) == '$date':
        date = "Today's date is " + str(datetime.now().date())
        await message.channel.send(date)
    
    elif message.content.startswith('bye'):
        await message.channel.send('Bye see you soon')
   
    elif str.lower(message.content) == 'yeet':
        await message.channel.send('Yeet!')
    
    elif str.lower(message.content) == '$tell me a joke':
        e = discord.Embed()
        RandomDate = random.randint(0, 4)
        if RandomDate == 0:
            e.set_image(url = "https://play.google.com/store/apps/details?id=com.jazzyworlds.englishjokesimages&hl=en_US")
        elif RandomDate == 1:
            e.set_image(url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fshort-funny.com%2F&psig=AOvVaw1R65P2bgMExS3GBU0iXkhS&ust=1598355352106000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMDhvMbfs-sCFQAAAAAdAAAAABAD")
        elif RandomDate == 2:
            e.set_image(url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fin.pinterest.com%2Fpin%2F840976930405154357%2F&psig=AOvVaw1-itUr0j6l0SEljJx5fsv1&ust=1598355479794000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCODZj4Pgs-sCFQAAAAAdAAAAABAD")
        elif RandomDate == 3:
            e.set_image(url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fin.pinterest.com%2Fpin%2F187814246932936755%2F&psig=AOvVaw35U1qrMdQRnh1ku2I0jtrW&ust=1598355588908000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLiqkrfgs-sCFQAAAAAdAAAAABAD")
        elif RandomDate == 4:
            e.set_image(url="https://www.jokescoff.com/wp-content/uploads/2017/12/Very-Funny-Jokes-for-Kids-in-English.jpg")
        await message.channel.send(embed = e)

    elif message.content.startswith('$') and message.content != '$date' and message.content != '$time' and message.content != '$toss':
       await message.channel.send("That command does not exist")

client.run(TOKEN)
