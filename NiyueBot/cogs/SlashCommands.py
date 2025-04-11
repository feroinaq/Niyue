import disnake
from disnake.ext import commands
from random import randint, choice
import random
import time
from disnake.ui import Select, View
import asyncio
from collections import defaultdict

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        
    '''Команда проверки состояния бота'''
    @commands.slash_command(description="Проверить состояние бота")
    async def niyue(self, inter):
        await inter.send(f"{inter.author.mention} я тут!")


    '''Команда калькулятора'''
    @commands.slash_command(description="Простой калькулятор")
    async def calc(self, inter, число1: int, действие: str, число2: int):
        if действие == "+":
            result = число1 + число2
        elif действие == "-":
            result = число1 - число2
        elif действие == "/":
            result = число1 // число2
        elif действие == "*":
            result = число1 * число2
        else:
            result = "Такого действия не существует"
        await inter.send(str(result))


    '''Команда с выводом случайного числа'''    
    @commands.slash_command(description="Случайное число от 1 до 100")
    async def rand(self, inter):
        await inter.send(randint(0,100))


    '''Команда с инфой о боте'''  
    @commands.slash_command(description="Информация о боте")
    async def about(self, inter):
        embed = disnake.Embed(
            title="niyue",
            description="Самый сваговый бот сервера ублюдков \n Версия: V2.0.0 \n Свага: Имеется \n Картель: Скоро будет",
            color=0x8a2be2,     
        )
        embed.set_author(
            name="by feroinaq",
            url="https://steamcommunity.com/profiles/76561199128488309/",
            icon_url="https://i.pinimg.com/736x/69/f2/0b/69f20b55cf81c071d65c3e2f87f1e808.jpg",
                    
        )       
        await inter.send(embed=embed)


    '''Команда с описанием пользователя'''    
    @commands.slash_command(description="Бот опишет любого участника сервера")
    async def descrp(self, inter, описание: str):
        with open(r'Z:\DiscordBot\FilesTxt\Glaza.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        glaza = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Volosi.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        volosi = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Atmosferu.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        atmosferu = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Dvizenie.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        dvizenie = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Glavnogo.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        glavnogo = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Lishnego.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        lishnego = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Lyudei.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        lyudei = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Mesto.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        mesto = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Nastoyaschim.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        nastoya = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Nastroit.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        nastroit = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Obshenie.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        obshenie = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Slegka.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        slegka = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Ulibka.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        ulibka = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Umel.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        umel = random.choice(lines)
        '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' '''''''''''''''''''''''' 
        with open(r'Z:\DiscordBot\FilesTxt\Vzglyad.txt', 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        vzglyad = random.choice(lines)



        await inter.send(f"Глаза {описание} были {glaza}, а взгляд — {vzglyad}. В каждом его движении чувствовалась {dvizenie}, словно он всегда знал, куда идет, и зачем. Его волосы были {volosi}, слегка {slegka}, часто спадали на лоб, добавляя образу некую загадочность. На лице — не яркая, но {ulibka} улыбка, которая могла рассеять любые сомнения и настроить на {nastroit}. Он умел {umel}, и каждый разговор с ним был не просто обменом словами, а настоящим {nastoya}, в котором всегда находилось место для {mesto}. Он предпочитал {atmosferu} атмосферу и избегал лишнего {lishnego}, но в его присутствии ощущалась энергия, которая заставляла людей {lyudei}. В общении он был {obshenie}, не допуская ни малейшей спешки, что выделяло его среди окружающих как главного {glavnogo}")


    '''Команда рассчета комиссии стима'''
    @commands.slash_command(description="Рассчитает сколько нужна заплатить, что бы получить нужную вам сумму(мтс)")
    async def steam(self, inter, сколько_хотите_получить: float):
        if сколько_хотите_получить >= 300:    
            result = сколько_хотите_получить + (сколько_хотите_получить * 0.07) + 50
            await inter.send(f"Вам надо заплатить {result} рублей")
        elif сколько_хотите_получить < 300:
            await inter.send("Введите сумму!")
        else:
            await inter.send("Такого действия не существует") 
     
        
def setup(bot):
    bot.add_cog(SlashCommands(bot))
    print(f"Extension {__name__} is ready")
        