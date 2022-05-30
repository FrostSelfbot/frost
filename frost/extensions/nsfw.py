import discord
import json
import requests
import aiohttp
import io

from discord.ext import commands

class NSFW(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def hentai(self, ctx):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.gif'))
                except:
                    return
    @commands.command()
    async def boobs(self, ctx):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/boobs")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                except:
                    return
def setup(bot):
    bot.add_cog(NSFW(bot))