import discord
from discord.ext import commands, tasks
from discord.embeds import *
import requests


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.command('random')
async def cat(ctx):
    embed = discord.Embed()
    open('tmp.png', 'wb').write(requests.get('https://cataas.com/cat').content)
    file = discord.File("tmp.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


@bot.event
async def on_message(message):
    if str(message.content).startswith('cat'):
        channel = bot.get_channel('1025230130806784013')
        embed = discord.Embed()
        open('tmp.png', 'wb').write(requests.get(
            'https://cataas.com/cat/says/'+message.content[4:]).content)
        file = discord.File("tmp.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        channel = await bot.fetch_channel('1025230130806784013')
        await channel.send(file=file, embed=embed)


@tasks.loop(minutes=5)
async def send_message():
    channel = bot.get_channel('1025230130806784013')
    embed = discord.Embed()
    open('tmp.png', 'wb').write(requests.get('https://cataas.com/cat').content)
    file = discord.File("tmp.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    channel = await bot.fetch_channel('1025230130806784013')
    await channel.send(file=file, embed=embed)


@bot.event
async def on_ready():
    send_message.start()


bot.run("MTAyNzIxNjEyNDQ1MjAxNjE4OA.Gyciuh.8RA09mygfrYwTYc4mDa7oLzKllrpWq6u-3lp7w")
