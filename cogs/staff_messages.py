import discord
import yaml
from settings import *
from discord.ext import commands
from discord import app_commands


class MessagesCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @app_commands.checks.has_any_role(OWNER_ID, ADMIN_ID)
    # @app_commands.command(name="send-list", description="Envia un mensage embed (Configuralo en settings_files/msg.yml)")
    # @app_commands.rename(channel_id="canal")
    # @app_commands.describe(channel_id="Canal al que quieres embiar el embed")
    # async def send_list(self, interaction: discord.Interaction, channel_id: discord.TextChannel):
    #     field_value = ''
    #     embed = discord.Embed(
    #         title="**Staff Celestial Network**", color=EMBEDS_COLOR)
    #     with open('settings_files/staff_msg.yml', 'r', encoding='utf8') as file:
    #         data = yaml.safe_load(file)
    #         for field in data['message']['fields']:
    #             field_title = data['message']['fields'][field]['title']
    #             inline = data['message']['fields'][field]['inline']
    #             for line in data['message']['fields'][field]['value']:
    #                 field_value += f'{line}\n'
    #             embed.add_field(name=field_title, value=field_value, inline=inline)
    #             field_value = ''

    #     # await interaction.response.send_message(embed=embed, )
    #     await interaction.response.send_message(content="Mensage enviado correctamente")
    #     await channel_id.send(content="@everyone", embed=embed)


    """ Edit list
    @app_commands.command(name="edit-list", description="Conoce información de nuestro servidor")
    @app_commands.rename(channel_id="canal")
    @app_commands.describe(message="Mensaje que quieres editar")
    async def edit_list(self, interaction: discord.Interaction, channel_id: discord.TextChannel, message):
        text = ''
        with open('settings_files/msg.yml', 'r', encoding='utf8') as file:
            data = yaml.safe_load(file)
            for line in data['staff']:
                text += f'{line}\n'

        embed = discord.Embed(
            title="**Staff Celestial Network**", color=EMBEDS_COLOR)
        embed.add_field(name='', value=text, inline=False)
        # await interaction.response.send_message(embed=embed, )
        await interaction.response.send_message(content="Mensage enviado correctamente")
        await channel_id.send(content="@everyone", embed=embed)
"""
    
    @app_commands.checks.has_any_role(OWNER_ID, ADMIN_ID)
    @app_commands.command(name="anuncio", description="Envia un anuncio largo a un canal especifico")
    async def large_message(self, interaction: discord.Interaction, channel_id: discord.TextChannel, message_id:str):
        print(f"Comando Usado por {interaction.user.display_name}")
        message = await interaction.channel.fetch_message(int(message_id))
        await interaction.response.send_message("Anuncio enviado", ephemeral=True)
        await channel_id.send(content=message.content)

    @app_commands.checks.has_any_role(OWNER_ID, ADMIN_ID)
    @app_commands.command(name="anuncio2", description="Envia un anuncio corto a un canal especifico")
    async def fast_message(self, interaction: discord.Interaction, channel_id: discord.TextChannel, message:str):
        print(f"Comando Usado por {interaction.user.display_name}")
        await interaction.response.send_message("Anuncio enviado", ephemeral=True)
        await channel_id.send(content=f"{message}")


async def setup(bot):
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    await bot.add_cog(MessagesCommands(bot), guilds=guilds)
