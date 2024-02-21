import os
import discord
from settings import *
from discord.ext import commands
from discord.ext.commands import CommandNotFound

class Main(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=COMMAND_PREFIX,
            intents= discord.Intents.all(),
            application_id = APPLICATION_ID
        )

# ----- Load cogs
    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and filename != "__init__.py":
                await self.load_extension(f'cogs.{filename[:-3]}')
        await bot.tree.sync()

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="/info"))
        print(f"{self.user} has connected to Discord!")

    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            print("WaffBot.main_py.L3: Command not found")
            await ctx.reply("Comando no encontrado, intenta Usar \"/\"")

bot = Main()
bot.run(DISCORD_TOKEN)
