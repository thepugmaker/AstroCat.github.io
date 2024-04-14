from discord.ext import commands
from discord import Interaction
from datetime import timedelta
from discord import Webhook
from discord_webhook import DiscordWebhook
from discord import Color
import discord
import datetime
import aiohttp

bot = commands.Bot(command_prefix= ";", intents=discord.Intents.all())

token = ""

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} with the id of {bot.user.id}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for /senddm"))
    print("Syncing")
    await bot.tree.sync()
    print("Synced")  

@bot.tree.command(name="help", description="Helps you")
async def help(interaction: Interaction):
    await interaction.response.send_message("""
    Commands are: 
        >   /help
        >   /senddm @username message (Have to have manage messages permission)
    """)

@bot.tree.command(name="senddm", description="Sends a dm from the bot to the member you want it to")
@commands.has_permissions(manage_messages=True)
async def senddm(interaction: Interaction, member: discord.Member, *, message: str):
    await member.send(f"{message}")
    await interaction.response.send_message(f"Successfully sent DM to {member}, Message was {message}")

bot.run(token)

