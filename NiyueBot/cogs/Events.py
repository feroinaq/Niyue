import disnake
from disnake.ext import commands
from random import randint, choice
import random

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
   


def setup(bot):
    bot.add_cog(Events(bot))
    print(f"Extension {__name__} is ready")