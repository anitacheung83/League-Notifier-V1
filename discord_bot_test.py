from discord.ext import commands
from dotenv import load_dotenv
import os
import pytest

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)


@client.tree.command(name="active")
async def test_active():
    """
    Test active command
    """
    summoner_name = "Kid Orpheus"
    active_game = responses.active(summoner_name)
    assert expected_active_game == active_game
