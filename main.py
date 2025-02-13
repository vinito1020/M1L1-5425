import discord
from discord.ext import commands
import os
import random
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")  # Cambia "general" por el nombre del canal
    if channel:
        await channel.send(f"🎉 Bienvenido {member.mention} al servidor!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola, soy {bot.user}!")

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)
@bot.command()
async def mem(ctx):
    with open('image/1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def men(ctx):
    meme = random.choice(os.listdir("image"))
    with open(f'image/{meme}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)



@bot.command()
async def eco(ctx):
    # Elegir una imagen aleatoria de la carpeta 'eco_images'
    eco_image = random.choice(os.listdir("eco_images"))
    
    # Asegúrate de que las imágenes estén en la carpeta eco_images
    with open(f'eco_images/{eco_image}', 'rb') as f:
        eco_picture = discord.File(f)
    
    # Enviar la imagen como mensaje
    await ctx.send(file=eco_picture)

# Comando para dar consejos de reciclaje
@bot.command()
async def reciclar(ctx):
    consejos = [
        "Usa botellas reutilizables en vez de botellas de plástico de un solo uso.",
        "Recicla las latas de aluminio, ¡son 100% reciclables!",
        "Evita el uso de plásticos de un solo uso como bolsas o pajillas.",
        "Si tienes residuos orgánicos, crea un compost en casa.",
        "Apaga las luces cuando no las necesites para reducir tu huella de carbono."
    ]
    
    # Seleccionar un consejo aleatorio
    consejo = random.choice(consejos)
    
    # Enviar el consejo al canal
    await ctx.send(consejo)

