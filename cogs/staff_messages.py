import discord
import yaml
from settings import *
from discord.ext import commands
from discord import app_commands


class MessagesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.checks.has_any_role(OWNER_ID, ADMIN_ID)
    @app_commands.command(name="anuncio", description="Envia un anuncio largo a un canal especifico")
    async def large_message(self, interaction: discord.Interaction, channel_id: discord.TextChannel, message_id:str):
        print(f"Comando Usado por {interaction.user.display_name}")
        message = await interaction.channel.fetch_message(int(message_id))
        print(f"-----\n{interaction.user.display_name} Executed command: /anuncio\n-----")
        await interaction.response.send_message("Anuncio enviado", ephemeral=True)
        await channel_id.send(content=message.content)

    @app_commands.checks.has_any_role(OWNER_ID, ADMIN_ID)
    @app_commands.command(name="anuncio2", description="Envia un anuncio corto a un canal especifico")
    async def fast_message(self, interaction: discord.Interaction, channel_id: discord.TextChannel, message:str):
        print(f"-----\n{interaction.user.display_name} Executed command: /anuncio2\n-----")
        await interaction.response.send_message("Anuncio enviado", ephemeral=True)
        await channel_id.send(content=f"{message}")


async def setup(bot):
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    await bot.add_cog(MessagesCommands(bot), guilds=guilds)
