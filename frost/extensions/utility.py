import asyncio
from aiohttp import payload_type
import discord
from discord.ext import commands
from discord import File
import random
import os
from printy import printy
import requests
import json
import subprocess
import base64
from functions import functions
import hashlib
import webbrowser
import brainfuckery
import sys
from printy import printy
from printy import inputy
from datetime import datetime
import time

import discum

from extensions import copypastas

from faker import Faker
import requests

fake = Faker()

with open("config.json") as f:
    c = json.load(f)

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send(file=discord.File("misc/cmds/cmds.ini"), delete_after=60)
        
    @commands.command()
    async def spam(self,ctx,delay:int,interval:int,*,message):
        await ctx.message.delete()
        for i in range(interval):
            await ctx.channel.send(message)
            await asyncio.sleep(delay)
    @commands.command()
    async def copypastahelp(self,ctx): # Might remove
        await ctx.message.delete()
        await ctx.channel.send(file=discord.File("misc/cmds/copypasta_cmds.txt"), delete_after=60)
    @commands.command()
    async def generateidentity(self, ctx):
        await ctx.message.delete()
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address()
        phone = fake.phone_number()
        emails = ["gmail.com", "yahoo.com", "yahoo.co.uk"]
        emailchoice = random.choice(emails)
        birthdate = fake.date_of_birth()
        email = f"{first_name}.{last_name}@{emailchoice}"

        await ctx.channel.send(f"**Generated new identity!**\nName: {first_name} {last_name}\nAddress: {address}\nPhone number: {phone}\nEmail: {email}\nBirthdate: {birthdate}", delete_after=30)
    @commands.command() # TODO: Add support for more programs
    async def open(self,ctx,*,app:str=None):
        await ctx.message.delete()
        if not app:
            return
        else:
            if app.lower() == "firefox":
                try:
                    subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe', '-new-tab'])
                except Exception as err:
                    print(f'{err}')
            elif app.lower() == "roblox studio":
                try:
                    subprocess.Popen([os.getenv("LOCALAPPDATA") + r'\Roblox\Versions\RobloxStudioLauncherBeta.exe'])
                except Exception as err:
                    print(f'{err}')
            elif app.lower() == "visual studio code":
                try:
                    subprocess.Popen([os.getenv("LOCALAPPDATA") + r'\Programs\Microsoft VS Code\Code.exe'])
                except Exception as err:
                    print(f'{err}')
            elif app.lower() == "brave":
                try:
                    subprocess.Popen([r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'])
                except Exception as err:
                    print(f'{err}')
            else:
                try:
                    subprocess.Popen([app])
                except Exception as err:
                    print(f'{err}')
    @commands.command()
    async def openhelp(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send(f"**Supported programs:**\n```\nFirefox\nRoblox studio\nVisual studio code\nBrave\n```\nIf your app isn't supported, just do `open FILEPATH`", delete_after=15)
    @commands.command()
    async def ping(self,ctx,*,host=None):
        await ctx.message.delete()
        if not host: 
            return
        else:
            try:
                ping = subprocess.getoutput(f"ping -w 4 {host}")
                await ctx.channel.send(ping, delete_after=20)
            except Exception as err:
                print(f'{err}')
    @commands.command()
    async def googlemaps(self,ctx,*,address):
        await ctx.message.delete()
        words = [x.strip() for x in address.split('+')]
        joined = ''.join(words)
        webbrowser.open(f'https://google.com/maps/place/{joined}')
    @commands.command()
    async def setnickname(self,ctx,*,nickname:str=None):
        await ctx.message.delete()
        if not nickname:
            return functions.warnf("No nickname given for the setnickname command.")
        else:
            await ctx.author.edit(nick=nickname)
    @commands.command()
    async def invisnick(self,ctx):
        await ctx.message.delete()
        await ctx.author.edit(nick="‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵")
    @commands.command()
    async def afk(self,ctx,type:str=None):
        await ctx.message.delete()
        is_afk = False
        if not type:
            return
        else:
            if type.lower() == "on":
                is_afk = True
                await ctx.channel.send("```You are now AFK!```", delete_after=2)
            if type.lower() == "off":
                is_afk = False
                await ctx.channel.send("```You are no longer AFK!```", delete_after=2)
    @commands.command()
    async def stealpfp(self,ctx,user:discord.User=None):
        await ctx.message.delete()
        if user is None: return functions.warnf("No user given for the stealpfp command.")
        else:
            await ctx.channel.send(user.avatar_url)
            await user.avatar_url_as(format="png").save(fp=f"./misc/images/pfps/{user.name}.png")
    @commands.command()
    async def serverpfp(self,ctx):
        await ctx.message.delete()
        await ctx.channel.send(ctx.guild.icon_url)
        await ctx.guild.icon_url_as(format="png").save(fp=f"./misc/images/servers/{ctx.guild.name}.png")
    @commands.command()
    async def hypesquad(self,ctx,house:str=None):
        await ctx.message.delete()
        if not house: return functions.warnf("No house given for the hypesquad command.")
        else:
            if house.lower() == "bravery":
                requests.post('https://discordapp.com/api/v6/hypesquad/online', headers={'Authorization': c["token"], 'Content-Type': 'application/json'}, json={'house_id': 1})
                printy(f"\n[c]  [+] Set your HypeSquad to Bravery!")
            elif house.lower() == "brilliance":
                requests.post('https://discordapp.com/api/v6/hypesquad/online', headers={'Authorization': c["token"], 'Content-Type': 'application/json'}, json={'house_id': 2})
                printy(f"\n[c]  [+] Set your HypeSquad to Brilliance!")
            elif house.lower() == "balance":
                requests.post('https://discordapp.com/api/v6/hypesquad/online', headers={'Authorization': c["token"], 'Content-Type': 'application/json'}, json={'house_id': 3})
                printy(f"\n[c]  [+] Set your HypeSquad to Balance!")
    @commands.command()
    async def serverinfo(self,ctx):
        await ctx.message.delete()
        date_format = "%a, %d %b %Y %I:%M %p"
        try:
            await ctx.channel.send(f"```Server name: {ctx.guild.name}\nCreated at: {ctx.guild.created_at.strftime(date_format)}\nOwner ID: {ctx.guild.owner_id}\nServer ID: {ctx.guild.id}\nMember count: {ctx.guild.member_count}```")
        except:
            return functions.errorf("Couldn't get the server information.")
    @commands.command()
    async def whois(self,ctx,*,user:discord.User=None):
        await ctx.message.delete()
        if not user: return functions.warnf("No user given for the whois command.")
        else:
            date_format = "%a, %d %b %Y %I:%M %p"
            await ctx.channel.send("Account created at: " + user.created_at.strftime(date_format))
    @commands.command()
    async def clear(self,ctx,amount:int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                return functions.errorf("Couldn't clear messages.")
    @commands.command()
    async def base64(self, ctx, *, args):
        await ctx.message.delete()
        msg = base64.b64encode('{}'.format(args).encode('ascii'))
        enc = str(msg)
        enc = enc[2:len(enc)-1]
        await ctx.send(enc)
    @commands.command()
    async def md5(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.md5(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
    @commands.command()
    async def sha512(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_512(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
    @commands.command()
    async def sha224(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_224(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
    @commands.command()
    async def sha384(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_384(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)
    @commands.command()
    async def price(self,ctx,*,currency:str=None):
        await ctx.message.delete()
        if not currency:
            return functions.warnf("No currency given for the hacker command.")
        elif currency.lower() == "btc" or currency.lower() == "bitcoin":
            with requests.session() as session:
                resp = session.get('https://blockchain.info/ticker')
                USD = resp.json()['USD']['last']
                EUR = resp.json()['EUR']['last']
                GBP = resp.json()['GBP']['last']
                await ctx.channel.send(f"```BTC Current Price:\nIn USD: ${USD}\nIn EUR: €{EUR}\nIn GBP: £{GBP}```", delete_after=40)
        elif currency.lower() == "eth" or currency.lower() == "ethereum":
            with requests.session() as session:
                resp = session.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP')
                USD = resp.json()['USD']
                EUR = resp.json()['EUR']
                GBP = resp.json()['GBP']
                await ctx.channel.send(f"```Ethereum Current Price:\nIn USD: ${USD}\nIn EUR: €{EUR}\nIn GBP: £{GBP}```", delete_after=40)
    @commands.command()
    async def reboot(self,ctx):
        await ctx.message.delete()
        os.execv(sys.executable, ['python'] + sys.argv)
    @commands.command()
    async def cloneserver(self,ctx,guildid:int=None):
        await ctx.message.delete()
        guildx = self.bot.get_guild(guildid)
        await ctx.guild.edit(name=str(guildx.name))
        guild = ctx.guild
        roles = []
        role: discord.Role
        for role in guildx.roles:
            try:
                if role.name != "@everyone":
                    roles.append(role)
            except:
                pass
        roles = roles[::-1]
        for role in roles:
            try:
                await guild.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
            except:
                pass
        for channels in guild.channels:
            await channels.delete()
        channels = guildx.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
            except:
                pass
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        category = None
        for channel_text in guildx.text_channels:
            try:
                for category in guild.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        category = None
                        break
                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guildx.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
            except:
                pass
        category = None
        for channel_voice in guildx.voice_channels:
            try:
                for category in guild.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                        )
                except:
                    new_channel = await guild.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
            except:
                pass
    @commands.command()
    async def tobrainfuck(self,ctx,*,text):
        await ctx.message.delete()
        await ctx.channel.send("```" + brainfuckery.Brainfuckery().convert(text) + "```")
    @commands.command()
    async def executebrainfuck(self,ctx,*,text):
        await ctx.message.delete()
        await ctx.channel.send("```" + brainfuckery.Brainfuckery().interpret(text) + "```")
    @commands.command()
    async def lua(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```lua\n{code}```")
    @commands.command()
    async def js(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```js\n{code}```")
    @commands.command()
    async def java(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```java\n{code}```")
    @commands.command()
    async def cpp(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```cpp\n{code}```")
    @commands.command()
    async def cs(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```cs\n{code}```")
    @commands.command()
    async def ini(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```ini\n{code}```")
    @commands.command()
    async def py(self,ctx,*,code):
        await ctx.message.delete()
        await ctx.channel.send(f"```py\n{code}```")
    @commands.command()
    async def hacker(self,ctx,*,text:str=None):
        await ctx.message.delete()
        if text is None: return functions.warnf("No text given for the hacker command.")
        else:
            for letter in text:
                text = text.replace("a", str(4))
                text = text.replace("e", str(3))
                text = text.replace('i', str(1))
                text = text.replace('o', str(0))
                text = text.replace('t', str(7))
                text = text.replace('s', '$')
                text = text.replace('you', 'j00')
            await ctx.channel.send(f"{text}")
    @commands.command()
    async def saveprofile(self,ctx,*,text:str=None):
        await ctx.message.delete()
        user_name = ctx.message.author.name
        discriminator = ctx.message.author.discriminator
        avatar = ctx.message.author.avatar_url
        f = open("./misc/other/profile.txt", "w")
        f.write(f"{user_name}#{discriminator}\n{avatar}")
    @commands.command()
    async def fakename(self,ctx):
        await ctx.message.delete()
        with open("./misc/other/names.json") as j:
            names = json.load(j)
            first_name = random.choice(names["first"])
            second_name = random.choice(names["last"])
            await ctx.channel.send(f"```{first_name} {second_name}```")
    @commands.command()
    async def leaveserver(self,ctx,*,name): # Haven't tested but it should work, as I made it in my old selfbot.
        await ctx.message.delete()
        if not name:
            return
        else:
            guild = discord.utils.get(self.bot.guilds, name=l)
            await guild.leave()
    @commands.command()
    async def coronastats(self,ctx):
        await ctx.message.delete()
        with requests.session() as session:
            site = requests.get("https://corona-stats.online/?format=json")
            tojson = site.json()
            await ctx.channel.send(f"```ini\n[frost bot]\ntoday's cases: {tojson['worldStats']['todayCases']}\nworldwide cases: {tojson['worldStats']['cases']}\n[frost bot]```")
def setup(bot):
    bot.add_cog(Utility(bot))