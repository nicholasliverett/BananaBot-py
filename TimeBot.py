import discord
from discord.ext import commands
from datetime import date
import datetime
import time
import calendar
today = date.today()
year = date.today()
TOKEN = 'Nzc1ODM2NTgyNjYxMDYyNzM3.X6sIHw.D4j7RwH6oz-G3ENLYwlQjfLBJ5Q'
bot = commands.Bot(command_prefix="?")
base_date = date(year.year, 1, 1)
timedif = today - base_date

def convert_to_unix_time(date: datetime.datetime, days: int, hours: int, minutes: int, seconds: int) -> str:
# Get the end date
    end_date = date + datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

# Get a tuple of the date attributes
    date_tuple = (end_date.year, end_date.month, end_date.day, end_date.hour, end_date.minute, end_date.second)

# Convert to unix time
    return f'<t:{int(time.mktime(datetime.datetime(*date_tuple).timetuple()))}:R>'

@bot.event
async def on_ready():
    print(bot.user.name + ' Logged on' + "\n")

@bot.command(name='repeat')
async def repeat(ctx, arg):
	await ctx.channel.send(arg)

@bot.command(name='time')
async def unixtime(ctx):
    now = datetime.datetime.now()
    utime = time.mktime(now.timetuple())
    embed = discord.Embed(colour=discord.Colour.dark_blue())
    embed.add_field(name=f'Current Time: <t:{int(utime)}>', value=f'Message Sender: {ctx.message.author}')
    print('working')
    await ctx.channel.send(embed=embed)

@bot.listen('on_message')
async def on_message(message):
    hourr = 0
    dateadd = 1
    if message.author == bot.user:
        return
    elif (':') in message.content:
        text = message.content
        hour = text[text.find(":") - 2:].split(':')[0]
        minutes = text[text.find(":") + 1:].split()[0]
        if ' am' in message.content:
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
        elif ' pm' in message.content:
            hourr = 12
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
            hours = int(hour) + hourr + 6
            if hours >= 24:
                hours = hours - 24
                dateadd = 2
                minutes = minutes.replace('?', '')
                embed = discord.Embed(colour=discord.Colour.dark_blue())
                embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                value=f'Original Message: {message.content}')
                await message.channel.send(embed=embed)
            else:
                minutes = minutes.replace('?', '')
                embed = discord.Embed(colour=discord.Colour.dark_blue())
                embed.add_field(name=f'{year.year}:{timedif.days + dateadd}:{int(hours)}:{minutes}:00 A.C (UTC +0)',
                                value=f'Original Message: {message.content}')
                await message.channel.send(embed=embed)

    else:
        return

bot.run(TOKEN)
