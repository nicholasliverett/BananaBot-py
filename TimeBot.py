from cProfile import label
import discord
from discord import Embed, ui, app_commands
from discord.ext import commands
from datetime import datetime
import time 
import calendar
from discord import ui
Time = time
TOKEN = 'Nzc1ODM2NTgyNjYxMDYyNzM3.X6sIHw.D4j7RwH6oz-G3ENLYwlQjfLBJ5Q'
guild = discord.Object(id="713404775357743216")

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id="713404775357743216"))
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

class TimeModal(ui.Modal, title="Unix Time Converter"):
    todayday = datetime.now().day
    todaymonth = datetime.now().month
    monthlist = [discord.SelectOption(label="1"), discord.SelectOption(label="2"), discord.SelectOption(label="3"), discord.SelectOption(label="4"), discord.SelectOption(label="5"), discord.SelectOption(label="6"), discord.SelectOption(label="7"), discord.SelectOption(label="8"), discord.SelectOption(label="9"), discord.SelectOption(label="10"), discord.SelectOption(label="11"), discord.SelectOption(label="12")]
    modalmonth = ui.Select(placeholder=todaymonth, options=monthlist)
    modalday = ui.TextInput(label="Day", style=discord.TextStyle.short, max_length= 6, placeholder= todayday, required=False)
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title= self.title, description = f"**Month**\n{self.modalmonth._selected_values}\n\n**Day**\n{self.modalday}", timestamp = datetime.now(), color = discord.Colour.yellow())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)

@tree.command(name="modaltest", guild=guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_modal(TimeModal())

@tree.command(name = "utime", description = "testing unix time thingy", guild=guild)
async def self(interaction: discord.Interaction, time:str):
    rtime = datetime.strptime(time, '%m/%d/%y %H:%M')
    now = datetime.now()
    utime = Time.mktime(now.timetuple())
    rutime = Time.mktime(rtime.timetuple())
    runixtime = f"<t:{int(rutime)}>"
    unixtime = f"<t:{int(utime)}>"
    await interaction.response.send_message(f"Requested Time:{runixtime} Time Now:{unixtime}")

client.run(TOKEN)