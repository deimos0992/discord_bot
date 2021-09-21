import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

#Create client
client = discord.Client()
my_secret = os.environ['TOKEN']

sad_words = ['vaccino', 'erba', 'fumo']
starter_encouragments = ['si mi sono vaccinato', 'fra vieni qua']

def get_text():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ispire'):
        quote = get_text()
        await message.channel.send(quote)

    msg = message.content
    quale_vaccino = ['quale', 'che tipo']
    if "vaccino" in msg:
      await message.channel.send("si mi sono vaccinato")

    if any(word in msg for word in quale_vaccino):
      await message.channel.send("quello che si fanno tutti")

keep_alive()
client.run(my_secret)

#ciao pesceeeeee
