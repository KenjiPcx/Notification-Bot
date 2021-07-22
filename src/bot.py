import discord 
import os
from pymongo import MongoClient
from utils import  string_to_month, month_to_string, body_formatter
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
db_client = MongoClient(os.getenv("DB_CONNECTION"))
events = db_client["eventsDatabase"]["events"]

# events = list(events.find())

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith("$hello"):
        await message.channel.send("Hello!")

    if msg.startswith("$eventsIn"):
        try:
            month = msg.split(" ")[1]
            month = string_to_month(month)
            data = list(events.find({"Month" : month}))
            data = map(lambda d: f"{d['Event Name']},  ({d['Day']}/{d['Month']}) \n", data)
            res_title = f"{month_to_string(month).title()} Events \n"
            res_body = body_formatter(data)
            response = f"{res_title}{res_body}"
            await message.channel.send(response)
        except Exception:
            response = f"Error executing command. \nPlease enter in this format: \n$eventsIn <Month in Letters>"
            await message.channel.send(response)

client.run(os.getenv("TOKEN"))
