
import discord
from discord.ext import commands
from Logger import log
import Config as cfg
import csv
from FileLoader import *
import random
from string import punctuation
from datetime import datetime

client = discord.Client()
words = {}
blacklist = set()
ingorePrefixes = set()
last = ("", "")

def start():
    global ingorePrefixes

    wordlist = cfg.get("replacer", required = True)
    with offsetOpen(wordlist) as file:
        reader = csv.reader(file, skipinitialspace = True)
        for line in reader:
            words[line[0]] = line[1:]
    
    wordlist = cfg.get("blacklist", required = True)
    with offsetOpen(wordlist) as file:
        for line in file:
            blacklist.add(line[:-1])

    ingorePrefixes = set([i for i in cfg.get("botPrefixes")])

    client.run(cfg.get("BotToken", required = True))


@client.event
async def on_ready():
    theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log(f"Bot started on {theTime}")
    log(f"Wordlist:\n\t{words}")
    log(f"Blacklist:\n\t{blacklist}")
    log(f"IgnoringPrefixes:\n\t{ingorePrefixes}")
    log(f"TriggeredBy:\n\t{cfg.get('botTrigger')}")
    log(f"Bot Ready and in {len(client.guilds)} servers")

    for s in client.guilds:
        log("\t" + s.name)

    log("")


@client.event
async def on_message(message):
    global last
    
    if message.content.startswith(cfg.get("botTrigger", required = True)):
        log(message.content, f"Original: {last[0]}", f"Replaced: {last[1]}", "")
        await message.channel.send("Error Reported")
        return

    for p in ingorePrefixes:
        if message.content.startswith(p):
            return

    author = message.author

    if author.name + "#" + str(author.discriminator) in blacklist:
        return

    text = str(message.content).split(" ")
    newtext = ""
    for t in text:
        nt = t.strip(punctuation)
        nt = nt.lower()
        if nt in words:
            t = t.lower() # sad hack for the time being
            t = t.replace(nt, random.choice(words[nt]))
        newtext += t + " "

    newtext = newtext[:-1]
    
    if newtext == message.content:
        return

    last = (newtext, message.content)

    out = "I think <@"
    out += str(author.id)
    out += "> meant to say:\n```"
    out += newtext + "```"
    
    await message.delete()
    await message.channel.send(out)


