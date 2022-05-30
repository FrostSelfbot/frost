import discord
import asyncio
from discord.ext import commands

class Animations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command() 
    async def memz(self,ctx):
        await ctx.message.edit(content="`Downloading MEMZ.exe .`")
        await asyncio.sleep(1)
        await ctx.message.edit(content="`Downloading MEMZ.exe ..`")
        await asyncio.sleep(1)
        await ctx.message.edit(content="`Downloading MEMZ.exe ...`")
        await asyncio.sleep(1)
        await ctx.message.edit(content="`Done!`")
        await asyncio.sleep(1)
        await ctx.message.edit(content="`Running MEMZ.exe..`")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":boom:")
    @commands.command()
    async def fuckyou(self,ctx):
        message = ctx.message
        while True:
            try:
                await message.edit(content="F")
                await asyncio.sleep(0.5)
                await message.edit(content="FU")
                await asyncio.sleep(0.5)
                await message.edit(content="FUC")
                await asyncio.sleep(0.5)
                await message.edit(content="FUCK")
                await asyncio.sleep(0.5)
                await message.edit(content="FUCK Y")
                await asyncio.sleep(0.5)
                await message.edit(content="FUCK YO")
                await asyncio.sleep(0.5)
                await message.edit(content="FUCK YOU")
                return
            except Exception as err:
                print(err)
    @commands.command()
    async def bomb(self,ctx):
        await ctx.message.edit(content=":bomb: ----------- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: ---------- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: --------- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: -------- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: ------- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: ------ :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: ----- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: ---- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: ---- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: --- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: -- :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: - :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":bomb: :fire:")
        await asyncio.sleep(1)
        await ctx.message.edit(content=":boom:")
    @commands.command()
    async def suckmy(self,ctx):
        await ctx.message.edit(content="`YOU CAN S`")
        await asyncio.sleep(0.5)
        await ctx.message.edit(content="`YOU CAN SU`")
        await asyncio.sleep(0.5)
        await ctx.message.edit(content="`YOU CAN SUC`")
        await asyncio.sleep(0.5)
        await ctx.message.edit(content="`YOU CAN SUCK`")
        await asyncio.sleep(0.5)
        await ctx.message.edit(content="`YOU CAN SUCK M`")
        await asyncio.sleep(0.5)
        await ctx.message.edit(content="`YOU CAN SUCK MY`")
        await asyncio.sleep(0.5)
        await ctx.message.edit(content="`Dick.`")
def setup(bot):
    bot.add_cog(Animations(bot))