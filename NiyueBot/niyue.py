import disnake
from disnake.ext import commands
from answering import get_answer  
from disnake.ui import Select, View, Button
from typing import Optional
import os
from collections import defaultdict
import asyncio
import threading
import aioconsole

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[*********************])
original_activity = disnake.Activity(type=disnake.ActivityType.watching, name="за вами")


async def terminal_input():
    await bot.wait_until_ready()
    channel = bot.get_channel(*********)
    dev_mode = False
    while True:
        msg = await aioconsole.ainput("|message| ")
        if not msg.strip():
            continue
        if msg.lower() == "_dev" and not dev_mode:
            await bot.change_presence(activity=disnake.CustomActivity(name="В разработке"))
            await channel.send("[DEV MODE ON]")
            dev_mode = True
        elif msg.lower() == "_undev" and dev_mode:
            await bot.change_presence(activity=original_activity)
            await channel.send("[DEV MODE OFF]")
            dev_mode = False
        else:
            await channel.send(msg)    

    
        
@bot.event
async def on_message(message: disnake.Message):
    if message.mentions and message.mentions[0] == bot.user:
        msg = get_answer(message.content)
        await message.reply(msg, mention_author=False)


@bot.event
async def on_ready():
    channel = bot.get_channel(***************)
    await channel.send(str("Бот активен"))    
    asyncio.create_task(terminal_input())


bot.load_extension("cogs.SlashCommands")
bot.load_extension("cogs.Events")
#bot.load_extension("cogs.voting")
#bot.load_extension("cogs.devmode")

       

print("active right")
bot.run("********************") 



        
 