import asyncio
import discord
import responses
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from exceptions import MessageNotSend

load_dotenv()


def run_discord_bot() -> None:
    """
    Runs the discord bot

    Args:
        None

    Returns:
        None
    """
    TOKEN = os.getenv("TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready() -> None:
        """
        Runs when the bot is ready

        Args:
            None

        Returns:
            None
        """
        print(f"{client.user} is now running!")
        try:
            synced = await client.tree.sync()
        except Exception as e:
            print(e)

    @client.tree.command(name="active")
    @app_commands.describe(summoner_name="Summoner Name")
    async def active(interaction: discord.Interaction, summoner_name: str) -> None:
        """
        Sends a message to the user with the active game of the summoner

        Args:
            interaction (discord.Interaction): The Discord interaction object representing the original message
            summoner_name (str): The summoner name

        Returns:
            None
        """
        active_game = responses.active(summoner_name)
        await interaction.response.send_message(active_game)

    @client.tree.command(name="past")
    @app_commands.describe(summoner_name="Summoner Name")
    async def past(interaction: discord.Interaction, summoner_name: str) -> None:
        """
        Sends a message to the user with the past 10 games of the summoner

        Args:
            interaction (discord.Interaction): The Discord interaction object representing the original message
            summoner_name (str): The summoner name

        Returns:
            None
        """
        await interaction.response.defer()
        past_games = responses.past(summoner_name)
        await asyncio.sleep(10)
        await interaction.followup.send(past_games)

    @client.tree.command(name="graph")
    @app_commands.describe(summoner_name="Summoner Name")
    async def graph(interaction: discord.Interaction, summoner_name: str) -> None:
        """
        Sends a graph to the user with games played in last week of the summoner

        Args:
            interaction (discord.Interaction): The Discord interaction object representing the original message
            summoner_name (str): The summoner name

        Returns:
            None
        """

        await interaction.response.defer()
        weekly_report = responses.weekly_report(summoner_name)
        graph = weekly_report.graph
        # Save graph as image
        graph.savefig("graph.png")
        # Send graph to user
        try:
            # await interaction.followup.send(f"Total Number of Games Played by {weekly_report.summoner.name} last Week: {weekly_report.number_of_matches}")
            # for i, match in enumerate(weekly_report.matches):
            #     await interaction.followup.send(f"Match {i + 1}\n" + str(match))
            await interaction.followup.send(file=discord.File("graph.png"))

        except Exception as e:
            raise MessageNotSend(
                "Message could not be send. Please try again later.")
        # Delete graph
        os.remove("graph.png")

    @client.tree.command(name="weekly_report")
    @app_commands.describe(summoner_name="Summoner Name")
    async def weekly_report(interaction: discord.Interaction, summoner_name: str) -> None:
        """
        Sends a graph to the user with games played in last week of the summoner

        Args:
            interaction (discord.Interaction): The Discord interaction object representing the original message
            summoner_name (str): The summoner name

        Returns:
            None
        """

        await interaction.response.defer()
        weekly_report = responses.weekly_report(summoner_name)
        graph = weekly_report.graph
        # Save graph as image
        graph.savefig("graph.png")
        # Send graph to user
        try:
            await interaction.followup.send(f"Total Number of Games Played by {weekly_report.summoner.name} last Week: {weekly_report.number_of_matches}")
            for i, match in enumerate(weekly_report.matches):
                await interaction.followup.send(f"Match {i + 1}\n" + str(match))
            await interaction.followup.send(file=discord.File("graph.png"))

        except Exception as e:
            raise MessageNotSend(
                "Message could not be send. Please try again later.")
        # Delete graph
        os.remove("graph.png")

    client.run((str(TOKEN)))
