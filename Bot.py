import discord
import random
import os
import requests
from discord.ext import commands

# Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Comando heh
@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

# Comando choose
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

# Función para obtener imagen de pato
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

# Comando duck
@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Comando mem (envía memes aleatorios)
@bot.command()
async def mem(ctx):
    images = os.listdir('imagenes')
    img_name = random.choice(images)

    with open(f'imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

# Ejecutar bot
bot.run("Token")
