import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!country'):
        country_name = message.content[9:].strip()

        country_info = get_country_info(country_name)

        if country_info:
            response = f"Country Information for {country_name}\n"
            response += f"Name: {country_info.get('name', 'N/A')}\n"
            response += f"Population: {country_info.get('population', 'N/A')}\n"
            response += f"Region: {country_info.get('region', 'N/A')}\n"
            response += f"Capital: {country_info.get('capital', 'N/A')}\n"

            await message.channel.send(response)
        else:
            await message.channel.send(f"Sorry, I couldn't find information for {country_name}.")

bot.run('MTE0NzQxODEyNzk3MDMzNjgyOA.GPhZkn.65tT-RnToPsxdJJ2ceAawwl-iVxzAnYN2mYFUw')
