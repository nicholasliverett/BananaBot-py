import discord
from discord.ext import commands
from datetime import date
import os
today = date.today()
year = date.today()
TOKEN = 'os.environ['DISCORD_TOKEN']'
bot = commands.Bot(command_prefix=":")
base_date = date(2020, 1, 1)
timedif = today - base_date


@bot.event
async def on_ready():
    print(bot.user.name + ' Logged on' + "\n")


@bot.event
async def on_message(message):
    hourr = 0
    dateadd = 1
    if message.author == bot.user:
        return
    elif (':') in message.content:
        text = message.content
        hour = text[text.find(":") - 2:].split(':')[0]
        minutes = text[text.find(":") + 1:].split()[0]
        if int(hour) <= 12:
            ampm = text[text.find(":") + 3:].split()[0]
            ampm = ampm.replace('?', '')
            if ampm == 'am':
                hourr = 0
                hours = int(hour) + hourr + 6
                if hours >= 24:
                    hours = hours - 24
                    dateadd = 2
                    embed = discord.Embed(colour=discord.Colour.dark_blue())
                    embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                    value=f'Original Message: {message.content}')
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(colour=discord.Colour.dark_blue())
                    embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                    value=f'Original Message: {message.content}')
                    await message.channel.send(embed=embed)
            elif ampm == 'pm':
                hourr = 12
                print(x)
                print(message.content)
                hours = int(hour) + hourr + 6
                if hours >= 24:
                    hours = hours - 24
                    dateadd = 2
                    embed = discord.Embed(colour=discord.Colour.dark_blue())
                    embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                    value=f'Original Message: {message.content}')
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(colour=discord.Colour.dark_blue())
                    embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                    value=f'Original Message: {message.content}')
                    await message.channel.send(embed=embed)
        else:
            print(x)
            print(message.content)
            hours = int(hour) + hourr + 6
            if hours >= 24:
                hours = hours - 24
                dateadd = 2
                embed = discord.Embed(colour=discord.Colour.dark_blue())
                embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                value=f'Original Message: {message.content}')
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(colour=discord.Colour.dark_blue())
                embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                value=f'Original Message: {message.content}')
                await message.channel.send(embed=embed)

    else:
        return

bot.run(TOKEN)
