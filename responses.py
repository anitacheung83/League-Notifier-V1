from typing import List, Dict
import riot_requests
from weekly_report import WeeklyReport
import matplotlib.figure as fig


def active(summoner_name: str) -> str:
    """
    Return a string of active game information given summoner_name.

    Args:
        summoner_name (str): summoner name

    Returns:
        active_game (str): a string of active game information
    """
    summoner = riot_requests.get_summoners_by_name(summoner_name)

    active_game = riot_requests.get_active_games_by_summoner_id(summoner.id)

    return str(active_game)


def past(summoner_name: str) -> str:
    """
    Return a string of past game information given summoner_name.

    Args:
        summoner_name (str): summoner name

    Returns:
        past_games_str (str): a string of past game information
    """
    summoner = riot_requests.get_summoners_by_name(summoner_name)

    past_games_id = riot_requests.get_matches_by_puuid(summoner.puuid)

    past_games_str = ""

    for game_id in past_games_id:
        game = riot_requests.get_matches_by_match_id(game_id)
        past_games_str += str(game)

    return past_games_str


def weekly_report(summoner_name: str) -> WeeklyReport:
    """
    Return a string of graph given summoner_name.

    Args:
        summoner_name (str): summoner name

    Returns:
        weekly_report (WeeklyReport): a WeeklyReport object
    """
    summoner = riot_requests.get_summoners_by_name(summoner_name)

    past_games_id, start_date = riot_requests.get_last_week_matches_by_puuid(
        summoner.puuid)

    past_games = []

    for game_id in past_games_id:
        game = riot_requests.get_matches_by_match_id(game_id)
        past_games.append(game)

    weekly_report = WeeklyReport(summoner, past_games, start_date)

    return weekly_report
