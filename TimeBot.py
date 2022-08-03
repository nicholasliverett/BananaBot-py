import discord
from discord import ui, app_commands
from discord.ext import commands
from datetime import datetime
import time 
import calendar
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