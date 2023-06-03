from datetime import datetime, timedelta
from match import PastMatch, ActiveMatch
import json
import os
import requests
from team import Team
from dotenv import load_dotenv
from exceptions import SummonerNotFound
from summoner import Summoner
import time
from typing import List, Dict, Tuple

# Load .env keys
load_dotenv()
api_key = os.getenv('API_KEY')

# Riot game API URL
na1_api_url = "https://na1.api.riotgames.com"
americas_api_url = "https://americas.api.riotgames.com"


###################################################################
# Helper Functions

def get_teams_info(participants: List, active: bool) -> List[Team]:
    """
    Return a list of teams in the match including participants and win result

    Args:
        participants (List): a list of participants in the match

    Returns:
        teams (List[Team]): a list of teams in the match
    """

    if active:
        team0 = Team(100, [])
        team1 = Team(200, [])
    else:
        team0 = Team(100, [], participants[0]["win"])
        team1 = Team(200, [], participants[9]["win"])

    for participant in participants:
        # Add participant to List
        if team0.id == participant["teamId"]:
            team0.participants.append(participant["summonerName"])
        else:
            team1.participants.append(participant["summonerName"])

    teams = [team0, team1]

    return teams

###################################################################


def get_summoners_by_name(summoner_name: str) -> Summoner:
    """
    Return summoner DTO (Data Transfer Object) given summoner_name.

    Args:
        summoner_name (str): summoner name

    Returns:
        summoner (Summoner): A summoner object representing the summoner with the given name.

    Raises:
        SummonerNotFound: if no summoner with the given name was found.
    """

    path_param = f"/lol/summoner/v4/summoners/by-name/{summoner_name}"
    query = na1_api_url + path_param + '?api_key=' + api_key
    res = requests.get(query)

    if res.status_code == 404:
        raise SummonerNotFound(summoner_name)

    summoner_info = res.json()

    summonerDTO = Summoner(
        summoner_info['name'], summoner_info['id'], summoner_info['puuid'])

    return summonerDTO


def get_matches_by_puuid(summoner_puuid: str) -> List[str]:
    """
    Return 5 latest matches given summoner's puuid.
    Call Match-V5 API: Get a list of match ids by puuid

    Args:
        puuid (str): summoner puuid

    Returns:
        matchtes_info (List): A list of the latest 5 matches by summoner

    Raises:
        MatchNotFound: if no matches with the summoner puuid was found.

    """

    path_param = f"/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?start=0&count=5"
    query = americas_api_url + path_param + '&api_key=' + api_key

    res = requests.get(query)
    matches_info = res.json()

    return matches_info


def get_last_week_matches_by_puuid(summoner_puuid: str) -> Tuple[List[str], int]:
    """
    Return matches from last week given summoner's puuid.
    Call Match-V5 API: Get a list of match ids by puuid

    Args:
        puuid (str): summoner puuid

    Returns:
        matches_info (List): A list of matches from last week by summoner

    Raises:
        MatchNotFound: if no matches with the summoner puuid was found.
    """
    current_time = time.time()
    seconds_in_week = 7 * 24 * 60 * 60
    last_week = current_time - seconds_in_week

    path_param = f"/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?startTime={int(last_week)}&endTime={int(current_time)}&count=100"
    query = americas_api_url + path_param + '&api_key=' + api_key

    res = requests.get(query)
    matches_info = res.json()

    return (matches_info, last_week)


def get_matches_by_match_id(match_id: str):
    """
    Return match DTO (Data Transfer Object) given match id.
    Call Match-V5 API: Get a match by match id

    Args:
        match_id (str): match id

    Returns:
        past_match (Match): A match object representing the match with the given match_id

    Raises:
        MatchNotFound: if no matches with the match id was found.
    """

    print("match_id: ", match_id)

    path_param = f"/lol/match/v5/matches/{match_id}"
    query = americas_api_url + path_param + "?api_key=" + api_key

    res = requests.get(query)
    match_info = res.json()

    # filename = os.path.join("test", "mock_get_matches_by_match_id.json")
    # with open(filename, 'w') as f:
    #     json.dump(match_info, f)

    game_start = datetime.fromtimestamp(
        match_info['info']['gameStartTimestamp']//1000)

    game_end = datetime.fromtimestamp(
        match_info['info']['gameEndTimestamp']//1000)

    game_duration = match_info['info']['gameDuration']
    minutes, seconds = divmod(game_duration, 60)
    game_duration = timedelta(minutes=minutes, seconds=seconds)

    # print(match_info['info']['participants'])

    # filename = os.path.join("test", "mock_get_teams_info.json")
    # with open(filename, 'w') as f:
    #     json.dump(match_info['info']['participants'], f)

    if match_info['info']['participants'] == []:
        teams = []
    else:
        teams = get_teams_info(match_info['info']['participants'], False)

    match = PastMatch(game_start, game_end, game_duration, teams)

    return match


def get_active_games_by_summoner_id(summoner_id: str):
    """
    Return current game information given summoner_id
    Call Sepectator-V4 API: Get current game information for the given summoner ID

    Args:
        summoner_id: summoner id

    Returns:
        active_match (Match): A match object representing the active game currently play by summoner_id

    Raises:
        MatchNotFound: if no currently active match is played by summoner_id
    """

    path_param = f"/lol/spectator/v4/active-games/by-summoner/{summoner_id}"
    query = na1_api_url + path_param + "?api_key=" + api_key

    res = requests.get(query)

    if (res.status_code != 200):
        return f"{summoner_id} isn't playing League of Legends right now."

    match_info = res.json()

    game_start = datetime.fromtimestamp(
        match_info['info']['gameStartTimestamp']//1000)

    game_duration = match_info['gameLength']
    minutes, seconds = divmod(game_duration, 60)
    game_duration = timedelta(minutes=minutes, seconds=seconds)

    teams = get_teams_info(match_info['participants'], True)

    match = ActiveMatch(game_start, game_duration, teams)

    return match
