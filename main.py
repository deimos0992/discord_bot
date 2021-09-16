import discord
import os
import requests
import json

#Create client
client = discord.Client()
my_secret = os.environ['TOKEN']


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


client.run(my_secret)

#ciao sono lucia e sono una sirena
