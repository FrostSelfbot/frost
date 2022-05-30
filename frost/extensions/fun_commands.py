from pickletools import read_unicodestring1
import discord
import random
import asyncio
import aiohttp
import io
import pyfiglet
import uwuify
import requests
from functions import functions
from zalgo_text import zalgo
from discord.ext import commands
from faker import Faker
import json
fake = Faker()

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def lenny(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send(' ͡° ͜ʖ ͡°')
    @commands.command()
    async def eightball(self,ctx,*,question:str=None):
        await ctx.message.delete()
        if not question:
            functions.warnf("No question provided for the 8ball.")
        else:
            answers = ["Yeah", "Nope", "Def not", "Doubt it", "I agree", "Surely", "Def", "Yuh", "Highly doubt it", "No. Just no.", "Think about your question and ask again.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "Oh hell nah", "It's possible.", "Reply hazy, try again.", "Signs point to yes.", "It is certain.", "Cannot predict now.", "Uhh", "My sources say no.", "Very doubtful."]
            await ctx.channel.send('``'+random.choice(answers)+'``')
    @commands.command()
    async def suntzu(self,ctx):
        quotes = ["If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.", "The supreme art of war is to subdue the enemy without fighting.", "Appear weak when you are strong, and strong when you are weak.", "Let your plans be dark and impenetrable as night, and when you move, fall like a thunderbolt.", "Supreme excellence consists of breaking the enemy's resistance without fighting.", "All warfare is based on deception. Hence, when we are able to attack, we must seem unable; when using our forces, we must appear inactive; when we are near, we must make the enemy believe we are far away; when far away, we must make him believe we are near.", "In the midst of chaos, there is also opportunity", "Victorious warriors win first and then go to war, while defeated warriors go to war first and then seek to win", "If your enemy is secure at all points, be prepared for him. If he is in superior strength, evade him. If your opponent is temperamental, seek to irritate him. Pretend to be weak, that he may grow arrogant. If he is taking his ease, give him no rest. If his forces are united, separate them. If sovereign and subject are in accord, put division between them. Attack him where he is unprepared, appear where you are not expected.", "The greatest victory is that which requires no battle.", "To know your Enemy, you must become your Enemy.", "Engage people with what they expect; it is what they are able to discern and confirms their projections. It settles them into predictable patterns of response, occupying their minds while you wait for the extraordinary moment — that which they cannot anticipate.", "There is no instance of a nation benefitting from prolonged warfare.", "Treat your men as you would your own beloved sons. And they will follow you into the deepest valley."]
        randomQuote = random.choice(quotes)
        await ctx.message.delete()
        await ctx.channel.send(randomQuote)
    @commands.command()
    async def floodchat(self,ctx):
        await ctx.message.delete()
        for each in range(0, 11):
            d = "⠀\n⠀"*100
            await ctx.send(f"{d}")
    @commands.command()
    async def ben(self,ctx):
        await ctx.message.delete()
        gifs = ["https://images-ext-2.discordapp.net/external/JTcKNV_Fk5AAKe4xt8IebZZCRqIEwhU2gZsbOgIrKNk/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/yrttOircNjcAAAPo/talking-ben-says.mp4", "https://images-ext-1.discordapp.net/external/hi8ilNzrxnjeIYbLGqx36RnwihV40RM8WpxNkxI1bxE/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/AKkrwSZSpZ0AAAPo/talking-ben.mp4", "https://images-ext-1.discordapp.net/external/hi8ilNzrxnjeIYbLGqx36RnwihV40RM8WpxNkxI1bxE/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/AKkrwSZSpZ0AAAPo/talking-ben.mp4", "https://images-ext-2.discordapp.net/external/vfoTbW-F0_vtptuQNSPyElPcS6m1YkDoi-oQHrja3c0/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/hdPVLfpe81cAAAPo/talking-ben-drinking.mp4", "https://images-ext-1.discordapp.net/external/f7VGo0FS6y8d6DiYvgK2mAHaNdnC69HH7R6YevwUzlw/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/EBbGfZGzWbIAAAPo/ben-talking-ben.mp4"]
        await ctx.channel.send(random.choice(gifs))

    @commands.command()
    async def hack(self,ctx,*,user:str=None):
        if not user: return functions.warnf("No user provided for the hack command.")
        emails = ["bruh6987@gmail.com", "whytho@yahoo.com", "ilovebbc@gmail.com", "yujgfhrg@gmail.com"]
        passwords = ["6XXXZ898n", "password", "lego", "Batman", "spiderman697", "1245647623"]
        await ctx.message.edit(content=f"Tracking {user}'s location..")
        await asyncio.sleep(3)
        await ctx.message.edit(content="Getting their personal info..")
        await asyncio.sleep(3)
        await ctx.message.edit(content="Hacking into their accounts..")
        await asyncio.sleep(3)
        await ctx.message.edit(content=f"Done! Email: {random.choice(emails)} Password: {random.choice(passwords)}")
        await asyncio.sleep(5)
        await ctx.message.delete()
    @commands.command()
    async def slap(self,ctx,user:discord.User=None):
        await ctx.message.delete()
        if not user: return functions.warnf("No user provided for the slap command.")
        req = requests.get("https://nekos.life/api/v2/img/slap")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["url"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                    await ctx.channel.send(user.mention + " L", delete_after=10)
                except:
                    pass
    @commands.command()
    async def hug(self,ctx,user:discord.User=None):
        await ctx.message.delete()
        if not user: return functions.warnf("No user provided for the hug command.")
        req = requests.get("https://nekos.life/api/v2/img/hug")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["url"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                    await ctx.channel.send(user.mention + " This could be us <3", delete_after=10)
                except:
                    pass
    @commands.command()
    async def kiss(self,ctx,user:discord.User=None):
        await ctx.message.delete()
        if not user: return functions.warnf("No user provided for the kiss command.")
        req = requests.get("https://nekos.life/api/v2/img/kiss")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["url"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                    await ctx.channel.send(user.mention + " This could be us <3", delete_after=10)
                except:
                    pass
    @commands.command()
    async def panda(self,ctx):
        await ctx.message.delete()
        req = requests.get("https://some-random-api.ml/img/panda")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["link"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                except:
                    functions.errorf("There was an error while trying to parse the panda image.")
    @commands.command()
    async def dog(self,ctx):
        await ctx.message.delete()
        req = requests.get("https://some-random-api.ml/img/dog")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["link"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                except:
                    functions.errorf("There was an error while trying to parse the dog image.")
    @commands.command()
    async def cat(self,ctx):
        await ctx.message.delete()
        req = requests.get("https://some-random-api.ml/img/cat")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["link"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                except:
                    functions.errorf("There was an error while trying to parse the cat image.")
    @commands.command()
    async def fox(self,ctx):
        await ctx.message.delete()
        req = requests.get("https://some-random-api.ml/img/fox")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["link"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                except:
                    functions.errorf("There was an error while trying to parse the fox image.")
    @commands.command()
    async def birb(self,ctx):
        await ctx.message.delete()
        req = requests.get("https://some-random-api.ml/img/birb")
        res = req.json()
        async with aiohttp.ClientSession() as ses:
            async with ses.get(res["link"]) as resp:
                if resp.status != 200: return await print("Failed to send image.")
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.channel.send(file=discord.File(data, 'img.png'), delete_after=10)
                except:
                    functions.errorf("There was an error while trying to parse the bird image.")
    @commands.command()
    async def to100(self,ctx): # TODO: Move to a different category
        for number in range(100):
            await ctx.message.edit(content=f"{number}")
            await asyncio.sleep(1)
    @commands.command(aliases=["cf"])
    async def coinflip(self,ctx):
        await ctx.message.delete()
        yes = ["`heads`", "`tails`"]
        await ctx.channel.send(random.choice(yes), delete_after=5)
    @commands.command()
    async def ghostping(self,ctx,user:discord.User):
        await ctx.message.delete()
        await ctx.channel.send(f"{user.mention}", delete_after=0.5)
    @commands.command()
    async def ascii(self,ctx,*,text:str=None):
        await ctx.message.delete()
        if text is None:
            return
        else:
            figletFont = pyfiglet.Figlet(font="Slant")
            toASCII = figletFont.renderText(text)
            await ctx.channel.send(f"```{toASCII}```")
    @commands.command()
    async def uwu(self,ctx,*,text:str=None):
        await ctx.message.delete()
        if text is None:
            return functions.warnf("No text given for the uwu command.")
        else:
            await ctx.channel.send(uwuify.uwu(text))
    @commands.command()
    async def frostembed(self,ctx):
        await ctx.message.delete()
        msg = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        msg += "https://frost-bot.cf"
        await ctx.channel.send(msg)
    @commands.command()
    async def chucknorris(self,ctx):
        await ctx.message.delete()
        with requests.session() as session:
            site = requests.get("https://api.chucknorris.io/jokes/random")
            tojson = site.json()
            await ctx.channel.send(f"{tojson['value']}")
    @commands.command()
    async def lmgtfy(self,ctx,search):
        await ctx.message.delete()
        if not search:
            return
        else:
            await ctx.channel.send("https://lmgtfy.com/?q={}".format(search.replace(" ", "+")))
    @commands.command()
    async def dox(self,ctx,user:discord.User):
        await ctx.message.delete()
        with open("./misc/other/names.json") as j:
            names = json.load(j)
            first_name = random.choice(names["first"])
            second_name = random.choice(names["last"])
            await ctx.channel.send(f"{user.mention} get doxxed L! ```ini\n[frost bot]\nFirst name: {first_name}\nSecond name: {second_name}\nAddress: {fake.address()}\n[frost bot]```")
    @commands.command()
    async def randombypassedslur(self,ctx):
        await ctx.message.delete()
        slurs = ["n­igga", "n­igger", "r­etard", "g­ay", "tr­anny", "f­aggot"]  
        await ctx.channel.send(random.choice(slurs))
    @commands.command()
    async def emojiflood(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send(":thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: :thinking: ")
    @commands.command()
    async def bypass(self,ctx,*,slur):
        await ctx.message.delete()
        if slur == "n word":
            await ctx.channel.send("n­igga")
        elif slur == "gay slur":
            await ctx.channel.send("f­aggot")
        elif slur == "trans slur":
            await ctx.channel.send("tr­anny")
        elif slur == "r word":
            await ctx.channel.send("r­etard")
    @commands.command()
    async def zalgo(self,ctx,*,text:str=None):
        await ctx.message.delete()
        for commands in self.bot.commands:
            print(f"{commands}")
        if text == None:
            return
        else:
            await ctx.channel.send(zalgo.zalgo().zalgofy(text))
    @commands.command()
    async def gayrate(self,ctx,user:discord.User):
        await ctx.message.delete()
        await ctx.channel.send(f"{user.mention} is {random.randint(1, 100)}% gay!", delete_after=10)
    @commands.command()
    async def retardrate(self,ctx,user:discord.User):
        await ctx.message.delete()
        await ctx.channel.send(f"{user.mention} is {random.randint(1, 100)}% retarded!", delete_after=10)
    @commands.command()
    async def cmdlistprint(self,ctx):
        await ctx.message.delete()
        for command in self.bot.commands:
            print(command)
def setup(bot):
    bot.add_cog(Fun(bot))