from discord.ext import commands
import json
from printy import printy
from datetime import datetime

with open("./config.json") as f:
    configuration = json.load(f)

gp_detect = configuration.get("ghost_ping_detection")
class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        #for commands in self.bot.commands:
            #print(f"{commands}")
        if gp_detect == "True":   
            if self.bot.user.mentioned_in(message):
                time = datetime.now().strftime("%H:%M")
                printy(f"{time} | You were ghost pinged in {message.channel.guild}, #{message.channel}")
def setup(bot):
    bot.add_cog(Events(bot))