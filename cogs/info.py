import discord
import yaml
from settings import *
from discord.ext import commands
from discord import app_commands

class InfoCommand(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="info", description="Conoce información de nuestro servidor")
    async def sv_ip(self, interaction:discord.Interaction):
        with open('settings_files/server_info.yml', 'r', encoding='utf8') as file:
            modalidades = ""
            comandos = ""
            data = yaml.safe_load(file)
            for i in range(len(data['info_cmd']['games'])):
                modalidades += data['info_cmd']['games'][i] + "\n"
            for comando in data['info_cmd']['comands']:
                comandos += comando
            info_embed=discord.Embed(title=data['info_cmd']['name'], color=EMBEDS_COLOR)
            info_embed.add_field(name="IP\t", value=data['info_cmd']['ip'], inline=True)
            info_embed.add_field(name="Version", value=data['info_cmd']['version'], inline=True)
            info_embed.add_field(name="Puerto (Bedrock)", value=data['info_cmd']['port'], inline=False)
            info_embed.add_field(name="Modalidades", value=modalidades, inline=True)
            info_embed.add_field(name="Tienda", value=data['info_cmd']['store'], inline=True)
            info_embed.add_field(name="Comandos de bot", value=comandos, inline=False)
        print(f"-----\n{interaction.user.display_name} Executed command: /info\n-----")
        await interaction.response.send_message(embed=info_embed, ephemeral=True)

async def setup(bot):
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    await bot.add_cog(InfoCommand(bot), guilds=guilds)
