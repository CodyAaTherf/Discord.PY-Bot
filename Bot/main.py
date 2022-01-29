import discord
from discord.ext import commands

INTENTS = discord.Intents.all()
bot = commands.Bot(
    command_prefix = ">",
    intents = INTENTS
)

@bot.event
async def on_ready():
    print("Bot is online!")

bot.run("TOKEN")