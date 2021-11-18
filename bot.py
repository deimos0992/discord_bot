import discord
import os
import requests
import json
import base64
import io
from keep_alive import keep_alive
from sqlalchemy import *
import psycopg2
import PIL.Image as Image

connection = psycopg2.connect(user="petlmngsmdejbj",
                              password="1d342b9b10822e18b5970cc19fe1e27cd7c6a04a20d036a72f78ee59f32a4e35",
                              host="ec2-52-213-119-221.eu-west-1.compute.amazonaws.com",
                              port="5432",
                              database="d540qif68vehha")

print("Using Python variable in PostgreSQL select Query")
cursor = connection.cursor()
postgreSQL_select_Query = "select image from images where user_id=%s;"

cursor.execute(postgreSQL_select_Query, (1,))
mobile_records = cursor.fetchone()
print(mobile_records)

if connection:
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed \n")

# Create client
client = discord.Client()
my_secret = os.environ['TOKEN']

sad_words = ['vaccino', 'erba', 'fumo']
starter_encouragments = ['si mi sono vaccinato', 'fra vieni qua']


def get_text():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(mobile_records)
        await message.channel.send('Hello!')

    if message.content.startswith('$image'):
        b = base64.b64decode(mobile_records[0])
        img = Image.open(io.BytesIO(b))
        img.show()
        file = discord.File(io.BytesIO(base64.decodebytes(mobile_records[0])))
        await message.channel.send(file)

    if message.content.startswith('$ispire'):
        quote = get_text()
        await message.channel.send(quote)

    msg = message.content
    quale_vaccino = ['quale', 'che tipo']
    if "vaccino" in msg:
        await message.channel.send("si mi sono vaccinato")

    if any(word in msg for word in quale_vaccino):
        await message.channel.send("quello che si fanno tutti")

    await message.channel.send(f"a fess e mamm {(message.author.mention)}")

    await message.channel.send(f'called user {message.author.name}')
    voice_state = message.author.voice
    channel = client.get_channel(887812762854629380)
    members = channel.members
    if voice_state is not None:
        channelState = voice_state.channel
        await message.channel.send(channelState.mention)
        await message.channel.send(len(channelState.members))
        await message.channel.send(message.author.id)
        for member in members:
            await message.channel.send(f'Name: {member.name} ID: {member.id}')

        for u in channelState.members:
            await message.channel.send(u.name)
    else:
        await message.channel.send(f'user {message.author.name} is not currently in a voice channel')


keep_alive()
client.run(my_secret)

# ciao pesceeeeee
