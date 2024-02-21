import discord
import yaml
from settings import *
from discord.ext import commands
from discord import app_commands

#### -------------------- Selection Menu -------------------- ####
class RanksMenu(discord.ui.Select):
    def __init__(self):
        with open('settings_files/ranks.yml', 'r', encoding='utf8') as file:
            options = []
            data = yaml.safe_load(file)
            for rank in data['ranks']:
                options.append(discord.SelectOption(label=data['ranks'][rank]['name'],description="", emoji=data['ranks'][rank]['emoji']))
        super().__init__(placeholder='Selecciona una opción', min_values=1, max_values=1, options=options)

    async def callback(self, interaction:discord.Interaction):
        with open('settings_files/ranks.yml', 'r', encoding='utf8') as file:
            data = yaml.safe_load(file)
            for rank in data['ranks']:
                if data['ranks'][rank]['name'] == self.values[0]:
                    title = f"{data['ranks'][rank]['emoji']} {data['ranks'][rank]['name']}"
                    ranks_embed=discord.Embed(title=title)
                    for section in data['ranks'][rank]['rewards']:
                        rewards=""
                        for reward in range(len(data['ranks'][rank]['rewards'][section])):
                            rewards+= f"{data['ranks'][rank]['rewards'][section][reward]}\n"
                        ranks_embed.add_field(name=section.capitalize(), value=rewards)
        await interaction.response.edit_message(embed=ranks_embed)


#### -------------------- Main Class Rank Commands -------------------- ####
class RankCommand(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name="rangos", description="¡Conoce los rangos disponibles en el servidor y sus beneficios!")
    async def rangos(self, interaction:discord.Interaction):
        view = discord.ui.View()
        view.add_item(RanksMenu())
        
        with open('settings_files/ranks.yml', 'r', encoding='utf8') as file:
            ranks_embed=discord.Embed(title="Rangos del servidor", color=EMBEDS_COLOR)
            data = yaml.safe_load(file)
            for rank in data['ranks']:
                value = f"{data['ranks'][rank]['emoji']} {data['ranks'][rank]['name']}"
                ranks_embed.add_field(name="", value=value, inline=True)
        print(f"-----\n{interaction.user.display_name} Executed command: /rangos\n-----")
        await interaction.response.send_message(embed=ranks_embed, ephemeral=True, view=view)


async def setup(bot):
    guilds = []
    for guild in bot.guilds:
        guilds.append(guild.id)
    await bot.add_cog(RankCommand(bot), guilds=guilds)
