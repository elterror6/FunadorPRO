#
# Imports
#
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="$", description='A great bot with a great power', help_command=help, intents=intents)
#
# Comando 'help' ...
#
@bot.command(name="help")
async def help(ctx):
  # Creación de un embed en una variable
  answer = discord.Embed(title=":white_check_mark: **__Comandos FunadorPRO__** :white_check_mark:", description="Estos son los __comandos del bot:__", colour=0xff0000)
  # Creación del contenido del embed                               
  answer.add_field(name=":one: **__$help__**", value="Devuelve una **lista con todos los comandos**.", inline=False)
  answer.add_field(name=":two: **__$ping__**", value="Devuelve la **latencia del bot**.", inline=False)
  answer.add_field(name=":three: **__$con__**",value="Convierte un número decimal a un número **binario**, **octal** o **hexadecimal**. ejemplo `$con 8 [bin,oct,hex]`", inline=False)
  answer.add_field(name=":four: **__$hola__**", value="El bot te responde hola muy educadamente.", inline=False)
  answer.add_field(name=":five: **__$funar__**", value="Te permite **funar** a quien tu quieras con total libertad.", inline=False) 
  answer.add_field(name=":six: **__$suggest__**", value="Sirve para enviar **sugerencias al admin**.", inline=False)
  answer.set_thumbnail(url="https://i.pinimg.com/originals/5f/d8/77/5fd87787aeab40264f807b1ccff5e7cf.png")
  answer.set_image(url="https://c.tenor.com/l6jY1QOLBEQAAAAC/among-us-pet.gif")
  await ctx.author.send(embed=answer)
#
# Comando 'ping' ...
#
@bot.command(name="ping")
async def ping(ctx):
  # Calculo del ping del bot
  ping = round(bot.latency*1000)
  await ctx.send('🏓Pong! '+ str(ping) +'ms')
#
# Comando 'converse' ...
#
@bot.command(name="con")
async def con(ctx,n: int, s: str):
  # struct: $con <int> <[bin,oct,hex]>
  # Si es s = 'bin' ...
  if (s == "bin")==True:
    bin = format(n, "b")
    answer = discord.Embed(title=':beginner: Convertir el número decimal '+str(n)+' a binario :beginner:', colour=0xff0000)
    answer.add_field(name='**__Número binario:__**', value=bin, inline=True)
    await ctx.send(embed=answer)
  # Si s = 'oct' ...
  elif (s == "oct")==True:
    oct = format(n, "o")
    answer = discord.Embed(title=':beginner: Convertir el número decimal '+str(n)+' a octal :beginner:', colour=0xff0000)
    answer.add_field(name='**__Número octal__**', value=oct, inline=True)
    await ctx.send(embed=answer)
  # Si s = 'hex' ...
  elif (s == "hex")==True:
    hex = format(n, "X")
    answer = discord.Embed(title=':beginner: Convertir el número decimal '+str(n)+' a hexadecimal :beginner:', colour=0xff0000)
    answer.add_field(name='**__Número hexadecimal__**', value=hex, inline=True)
    await ctx.send(embed=answer)
  # Si no es ninguna de las opciones anteriores ...
  else:
    await ctx.send('Error: el comando tiene la estructura `$con n{int} s{str, [bin, oct, hex]`')
#
# Comando 'hola' ...
#
@bot.command(name="hola")
async def hola(ctx):
  user_name = str(ctx.author.mention)
  await ctx.send('Hola '+user_name+', ¿Qué tal estamos ||guapetón/a||?')
#
# Comando 'funar' ...
#
@bot.command(name="funar")
async def funar(ctx, s: discord.User):
  # Creación del embed en una variable
  user_name = str(ctx.author.mention)
  description = user_name+" ha funado a "+str(s)
  # Creación del contenido del embed
  answer = discord.Embed(description=description, colour=0xff0000) 
  answer.set_image(url='https://empantallados.com/main-files/uploads/2020/10/Among-Us-Portada.gif')
  await ctx.send(embed=answer)
#
# Comando 'suggest' ...
#
@bot.command(pass_context=True,name="suggest")
async def suggest(ctx, *, message): 
  g = ctx.message.guild
  r = g.get_role(928055563600941076)
  list_gifs = ["https://c.tenor.com/__B1-Og_lmgAAAAC/love.gif", "https://c.tenor.com/NUwvtAsBre0AAAAC/ok-okie.gif", "https://c.tenor.com/mSH19mop5egAAAAC/intense-cat-ok.gif", "https://c.tenor.com/NEzCaMxJ2TkAAAAM/damn-ok-the-rock.gif", "https://c.tenor.com/HX3l1H9LucUAAAAC/skate-slide.gif", "https://c.tenor.com/83thdVyblF8AAAAM/thumbs-up-borat.gif", "https://c.tenor.com/iV__D-FgJQQAAAAC/good-fine.gif", "https://c.tenor.com/XTsLyyT2KRgAAAAC/thumbs-up-simon-cowell.gif", "https://c.tenor.com/b_kisO1zQU0AAAAC/minions-thumbs-up.gif","https://c.tenor.com/ctHRUl7eAoQAAAAC/thumbs-thumbs-up.gif"]
  embed_m = discord.Embed(title="SUGERENCIA ENVIADA CON EXITO", description="Su solicitud ha sido enviado a los admin con exito. Gracias "+ ctx.author.name+" por hacer del servidor un lugar mejor.")
  embed_m.set_image(url=random.choice(list_gifs))
  embed_dm =  discord.Embed(title="SUGERENCIA "+ctx.author.name, description=message, colour=0xff0000)
  for admin_members in r.members:
    await admin_members.send(embed=embed_dm)
  #print(str(len(rm))+" "+r.name)
  # await r.send(embed=embed_dm)
  await ctx.send(embed=embed_m)
