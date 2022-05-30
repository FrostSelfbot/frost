import json
import os
import discord
import requests
import webbrowser
import sys
import requests
import time

sys.path.append(".")

from extensions import copypastas

from printy import printy
from printy import inputy
from datetime import datetime

from colorama import Fore

from discord.ext import commands

if sys.platform == "linux":
    print("\33]0;Frost\a", end="", flush=True)
elif sys.platform == "win32":
    os.system("title Frost")

try:
    with requests.session() as session:
        response = session.get(
            "https://frost-bot.cf/changelogs.json"
        ) 
        toJson = response.json()
        if toJson["version"] != 1.03:
            print("[*] Downloading new update..")
            webbrowser.open("https://frost-bot.cf/files/frost.zip")
            print("[*] Done!")
except Exception as err:
    print(f"{err}")

with open("config.json") as f:
    configuration = json.load(f)

time = datetime.now().strftime("%H:%M")


token = configuration.get("token")
prefix = configuration.get("prefix")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

printy(f"[c]{time} | Frost has been loaded.")

# I won't be updating the terminal as much due to lack of motivation, if anything doesn't work in it then don't DM me about it


@bot.command()
async def terminalmode(self, ctx):
    await ctx.message.delete()
    while True:
        try:
            command = str(inputy(f"[c]{time} | "))
            if command.lower() == "help":
                printy(f"[c]{time} | Current commands are: help, ping")
                continue
            elif command.lower() == "ping":
                await ctx.channel.send("Pong!")
            else:
                printy(f"[c]{time} | Not a valid option.")
                continue
        except ValueError:
            printy(f"[c]{time} | Not a valid command")
            continue


for filename in os.listdir("./extensions"):
    if filename.endswith(".py"):
        bot.load_extension(f"extensions.{filename[:-3]}")

bot.run(token)
