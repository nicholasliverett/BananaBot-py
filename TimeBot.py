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
Time = time
TOKEN = 'Nzc1ODM2NTgyNjYxMDYyNzM3.X6sIHw.D4j7RwH6oz-G3ENLYwlQjfLBJ5Q'
guild = discord.Object(id="713404775357743216")
error_responses_file = open("error_responses.txt", "r")
error_responses = (error_responses_file.read()).split("\n")
error_responses_file.close()

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
            response = requests.get("https://sg.bananaserver.tk/api/push/OabUoSSB5s?status=up&msg=OK&ping=")
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
    async def on_submit(self, interaction: discord.Interaction,):
        utime = datetime.strptime(str((self.modaltime)), "%H:%M")
        inputtime = datetime(datetime.now().year, int(str(self.modalmonth)), int(str(self.modalday)), utime.hour, utime.minute)
        preunixtime = Time.mktime(inputtime.timetuple())
        unixtime = f"<t:{int(preunixtime)}"
        embed = discord.Embed(title= self.title, description = f"{unixtime}>\n{unixtime} >", timestamp = datetime.now(), color = discord.Colour.yellow())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"{random.choice(error_responses)} **Error:** {error}")

@tree.command(name = "utime", description = "testing unix time thingy", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(TimeModal())

client.run(TOKEN)
