import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
secret = os.environ['TOKEN']
# 
# Eventos del bot
#
@bot.event
# Evento nada más iniciarse ...
async def on_ready():
  # Estatus y actividad del bot
  activity = discord.Streaming(name="Viendote desde la webcam | $help ", url="https://www.twitch.tv")
  await bot.change_presence(status= discord.Status.online, activity=activity)
  # Imprimir un mensaje cuando se inicie
  print('Tamos activos papi')
keep_alive()
bot.run(secret)
