import discord
from discord.ext import commands
from discord import File


class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def playing(self,ctx,*,gameName):
        await ctx.message.delete()
        game = discord.Game(
            name=gameName
        )
        await self.bot.change_presence(activity=game)
    @commands.command()
    async def stopactivity(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(activity=None, status=discord.Status.dnd)
    @commands.command()
    async def watching(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name=message
            ))
    @commands.command()
    async def listening(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name=message, 
            ))
    @commands.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name = message,
            url = "https://www.twitch.tv/", 
        )
        await self.bot.change_presence(activity=stream)  
def setup(bot):
    bot.add_cog(Activity(bot))