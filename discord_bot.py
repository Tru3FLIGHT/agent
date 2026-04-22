import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

from functions.get_files_info import get_files_info
from functions.path_validation import validate_path

load_dotenv()

cwd = None
scope_limiter = "/home/zalea/Documents/"

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()
    print("Synced slash commands.")

@bot.tree.command(name="create_channel", description="Creates a new text channel.")
@discord.app_commands.describe(channel_name="The name of the channel to create.")
async def create_text_channel_command(interaction: discord.Interaction, channel_name: str):
    """
    Creates a new text channel in the guild where the command was sent.
    """
    if interaction.guild:
        try:
            new_channel = await interaction.guild.create_text_channel(channel_name)
            await interaction.response.send_message(f'Created new channel: {new_channel.mention}', ephemeral=False)
        except discord.Forbidden:
            await interaction.response.send_message("I don't have permission to create channels.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)
    else:
        await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)

@bot.tree.command(name="delete_channel", description="Deletes a text channel.")
@discord.app_commands.describe(channel_name_to_delete="The name of the channel to delete.")
async def delete_text_channel_command(interaction: discord.Interaction, channel_name_to_delete: str):
    """
    Deletes a text channel by name in the guild where the command was sent.
    """
    if interaction.guild:
        channel_to_delete = discord.utils.get(interaction.guild.channels, name=channel_name_to_delete)
        if channel_to_delete:
            try:
                await channel_to_delete.delete()
                await interaction.response.send_message(f'Deleted channel: `{channel_name_to_delete}`', ephemeral=False)
            except discord.Forbidden:
                await interaction.response.send_message("I don't have permission to delete channels.", ephemeral=True)
            except Exception as e:
                await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)
        else:
            await interaction.response.send_message(f"Channel `{channel_name_to_delete}` not found.", ephemeral=True)
    else:
        await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)


@bot.tree.command(name="cwd", description="changes the cwd on host machine")
@discord.app_commands.describe(path="The path to the working dir on host machine")
async def cwd_f(interation: discord.Interaction, path:str):
    try:
        validate_path(scope_limiter, path) 
    except Exception as e:
        await interation.response.send_message(f"{e}", ephemeral=True)
    cwd = path
    print(f"path = {cwd}")
    await interation.response.send_message(f"Current woring directory changed to `{path}`", ephemeral=True)


            

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if DISCORD_TOKEN:
    bot.run(DISCORD_TOKEN)
else:
    print("DISCORD_TOKEN not found in .env file.")
