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
TOKEN = 'TOKEN'
guild = discord.Object(id="713404775357743216")
error_responses_file = open("error_responses.txt", "r")
error_responses = (error_responses_file.read()).split("\n")
error_responses_file.close()

def get_current_time():
    current_time = datetime.now().strftime("%H:%M")
    return current_time

class aclient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    
    async def on_ready(self):
        print(f"Logged in as {self.user}.")
        
    async def setup_hook(self):
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

intents = discord.Intents.default()        
client = aclient(intents=intents)


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
        rank = self.rank
        clock_in = datetime.strptime(str((self.clock_in)), "%H:%M")
        clock_out = datetime.strptime(str((self.clock_out)), "%H:%M")
        total_time = clock_out - clock_in
        date_now = datetime.now().strftime("%Y-%m-%d")
        url = f""" https://docs.google.com/forms/d/e/1FAIpQLSdmCZb3q4hK39JAF1VUTxbKZOLqoXH5WBi8OL5xKAQqIkwOBg/formResponse?usp=pp_url&entry.1981853841={self.other}&entry.851308795=nic&entry.1182622261={self.civ_callsign}&entry.403682742={str(rank).replace(' ', '+')}&entry.1123833559={str(discord_user).replace('#', '%23')}&entry.484096161={date_now}&entry.1016489151=normal&entry.1750041982={str(self.clock_in).zfill(5)}&entry.1697757237={str(self.clock_out).zfill(5)}&entry.1158350909={str(total_time).zfill(8)}&entry.1805919228=Yes" """
        await interaction.response.send_message(url)
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"{random.choice(error_responses)} **Error:** {error}")
        print(error)

class LSPDForm(ui.Modal, title="LSPD Clock-in/out Form"):
    name = ui.TextInput(label = 'Name', style=discord.TextStyle.short, max_length= 50, placeholder= "Input Name", default='Jimmy M.')
    rank = ui.TextInput(label = 'Rank', style=discord.TextStyle.short, max_length= 30, placeholder= "Input Rank", default='Police Officer II')
    clock_in = ui.TextInput(label='Clock In', style=discord.TextStyle.short, max_length=6, placeholder='Input Clock In')
    clock_out = ui.TextInput(label='Clock Out', style=discord.TextStyle.short, max_length=6, placeholder='Input Clock Out')
    patrol_type = ui.TextInput(label = 'Patrol Type', style=discord.TextStyle.short, max_length= 30, placeholder= "Input Patrol Type", default='Normal Patrol')
    async def on_submit(self, interaction: discord.Interaction):
        discord_user = interaction.user
        callsign = "410"
        email ='gamingthingemail@gmail.com'
        clock_in = datetime.strptime(str((self.clock_in)), "%H:%M")
        clock_out = datetime.strptime(str((self.clock_out)), "%H:%M")
        total_time = clock_out - clock_in
        date_now = datetime.now().strftime("%Y-%m-%d")
        #formsubresponse = requests.get(f"https://docs.google.com/forms/d/e/1FAIpQLSdmCZb3q4hK39JAF1VUTxbKZOLqoXH5WBi8OL5xKAQqIkwOBg/formResponse?usp=pp_url&emailAddress=gamingthingemail@gmail.com")
        #print(formsubresponse)
        url = f"https://docs.google.com/forms/d/e/1FAIpQLSfcc65OmXOdpoe-LMTHxhkqGnxKH3IAEw9dffmZjB-9MBHenQ/formResponse?usp=pp_url&emailAddress={email}&entry.1503124298={str(self.name).replace(' ', '+')}&entry.1563281728={callsign}&entry.909843694={str(discord_user).replace('#', '%23')}&entry.650105918={str(self.rank).replace(' ', '+')}&entry.22974012={str(self.clock_in).zfill(5)}&entry.289301560={str(self.clock_out).zfill(5)}&entry.1474572841={str(total_time).zfill(8)}&entry.1799406772={date_now}&entry.386319268={str(self.patrol_type).replace(' ', '+')}"
        await interaction.response.send_message(url)
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"{random.choice(error_responses)} **Error:** {error}")
        print(error)

class SAFDForm(ui.Modal, title="SAFD Clock-in/out Form"):
    name = ui.TextInput(label = 'Name', style=discord.TextStyle.short, max_length= 50, placeholder= "Input Name", default='Jimmy M.')
    callsign = ui.TextInput(label = 'Callsign', style=discord.TextStyle.short, max_length= 30, placeholder= "Input Callsign", default='FD-14')
    clock_in = ui.TextInput(label='Clock In', style=discord.TextStyle.short, max_length=6, placeholder='Input Clock In')
    clock_out = ui.TextInput(label='Clock Out', style=discord.TextStyle.short, max_length=6, placeholder='Input Clock Out')
    notes = ui.TextInput(label = 'Notes', style=discord.TextStyle.short, max_length= 100, placeholder= "Input Notes", required=False)
    async def on_submit(self, interaction: discord.Interaction):
        clock_in = datetime.strptime(str((self.clock_in)), "%H:%M")
        clock_out = datetime.strptime(str((self.clock_out)), "%H:%M")
        total_time = clock_out - clock_in
        date_now = datetime.now().strftime("%Y-%m-%d")
        url = f"https://docs.google.com/forms/d/e/1FAIpQLSd-G-oCDsHjdZX9l1DYoXl9GN5I7LJ2jTCuRg2KFG-lCxJ_PA/formResponse?usp=pp_url&entry.924437591={str(self.name).replace(' ', '+')}&entry.1740414105={self.callsign}&entry.333732655={self.notes}&entry.522182144={str(self.clock_in).zfill(5)}&entry.522100359={str(self.clock_out).zfill(5)}&entry.2145413509={str(total_time).zfill(8)}&entry.1362587187={date_now}"
        await interaction.response.send_message(url)
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(f"{random.choice(error_responses)} **Error:** {error}")
        print(error)


@client.tree.command(name = "unixtime", description = "Unix Time Converter", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(TimeModal())

@client.tree.command(name = "kianform", description = "Kian Clock-in/out Form", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(KianForm())

@client.tree.command(name = "lspdform", description = "LSPD Clock-in/out Form", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(LSPDForm())

@client.tree.command(name = "safdform", description = "SAFD Clock-in/out Form", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(SAFDForm())
    
@client.tree.command(name='sync', description='Banana only', guild=guild)
async def self(interaction: discord.Interaction):
    if interaction.user.id == 624733100064112683:
        self.tree.copy_global_to()
        await interaction.response.send_message(f'Synced: {await tree.sync()}')
        print('Command tree synced by Banana')

    else:
        await interaction.response.send_message('You must be the one and only Banana to use this command!')
        
client.run(TOKEN)
