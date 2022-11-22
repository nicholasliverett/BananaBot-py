import asyncio
from cProfile import label
import discord
from discord import Embed, ui, app_commands
from discord.ext import commands, tasks
from datetime import date, datetime
import time 
from discord import ui
import random
from threading import Timer
import requests
TOKEN = 'Nzc1ODM2NTgyNjYxMDYyNzM3.GN8Wkh.L2KE7y0_yRlJxlxzxXAxk_iWUGVuO20k3ECP-o'
guild = discord.Object(id="713404775357743216")
error_responses_file = open("error_responses.txt", "r")
error_responses = (error_responses_file.read()).split("\n")
error_responses_file.close()

def get_current_time():
    current_time = datetime.now().strftime("%H:%M")
    return current_time

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def setup_hook(self) -> None:
        self.bg_task = self.loop.create_task(self.pushmonitor())
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id="713404775357743216"))
            self.synced = True
        print(f"We have logged in as {self.user}.")

    async def pushmonitor(self):
        await self.wait_until_ready()
        while not self.is_closed():
            response = requests.get("https://uptime.bananaproject.tk/api/push/rGEAHK9Jfp?status=up&msg=OK&ping=")
            await asyncio.sleep(30)

client = aclient()
tree = app_commands.CommandTree(client)

class TimeModal(ui.Modal, title="Unix Time Converter"):
    todayday = datetime.now().day
    todaymonth = datetime.now().month
    todaytime = datetime.now().strftime("%H:%M")
    modalmonth = ui.TextInput(label="Month", style=discord.TextStyle.short, max_length=6, placeholder="Input Month", default=todaymonth)
    modalday = ui.TextInput(label="Day", style=discord.TextStyle.short, max_length= 6, placeholder= "Input Day", default=todayday)
    modaltime = ui.TextInput(label = 'Time', style=discord.TextStyle.short, max_length= 6, placeholder= "Input Time", default=todaytime)
    async def on_submit(self, interaction: discord.Interaction):
        utime = datetime.strptime(str((self.modaltime)), "%H:%M")
        inputtime = datetime(datetime.now().year, int(str(self.modalmonth)), int(str(self.modalday)), utime.hour, utime.minute)
        preunixtime = time.mktime(inputtime.timetuple())
        unixtime = f"<t:{int(preunixtime)}"
        embed = discord.Embed(title= self.title, description = f"{unixtime}>\n{unixtime}\n *Add a '>' to the end*", timestamp = datetime.now(), color = discord.Colour.yellow())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"{random.choice(error_responses)} **Error:** {error}")

class KianForm(ui.Modal, title="Kian Clock-in/out Form"):
    civ_callsign = ui.TextInput(label="CC Callsign", style=discord.TextStyle.short, max_length= 7, placeholder= "Input CC Callsign", default='CIV-100')
    rank = ui.TextInput(label = 'Rank', style=discord.TextStyle.short, max_length= 15, placeholder= "Input Rank", default='Supervisor')
    clock_in = ui.TextInput(label='Clock In', style=discord.TextStyle.short, max_length=6, placeholder='Input Clock In')
    clock_out = ui.TextInput(label='Clock Out', style=discord.TextStyle.short, max_length=6, placeholder='Input Clock Out')
    other = ui.TextInput(label = 'Other (Put Recovery or Tranport)', style=discord.TextStyle.short, max_length=9, placeholder='Input Recovery or Transport', default='Recovery')
    async def on_submit(self, interaction: discord.Interaction):
        discord_user = interaction.user
        rate_experience = '6'
        business = 'Kian Services'
        clock_in = datetime.strptime(str((self.clock_in)), "%H:%M")
        clock_out = datetime.strptime(str((self.clock_out)), "%H:%M")
        total_time = clock_out - clock_in
        await interaction.response.send_message(f'User: {discord_user}\nCiv Callsign: {self.civ_callsign}\nBusiness: {business}\nRank: {self.rank}\nClock In: {self.clock_in}\nClock Out: {self.clock_out}\nTotal Time: {total_time}\nRating: {rate_experience}\nOther: {self.other}')
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"{random.choice(error_responses)} **Error:** {error}")


@tree.command(name = "unixtime", description = "Unix Time Converter", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(TimeModal())

@tree.command(name = "kianform", description = "Kian Clock-in/out Form", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(KianForm())

client.run(TOKEN)