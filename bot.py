import os
import discord
from dotenv import load_dotenv

from weather import get_weather
from logic import interpret_weather, generate_advice

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Ping test
    if message.content.lower() == "!ping":
        await message.channel.send("Pong 🏓")

    # Weather command
    if message.content.lower() == "!weather":
        temp, wind, code = get_weather()

        condition = interpret_weather(code)
        advice = generate_advice(temp, code)

        reply = f"""
🌤️ Weather Report
Temp: {temp}°C
Wind: {wind} km/h
Condition: {condition}

👉 {advice}
"""
        await message.channel.send(reply)

    if message.content.lower() == '!hi':
        await message.channel.send("Hey there!")


client.run(TOKEN)