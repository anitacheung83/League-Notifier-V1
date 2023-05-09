import json
import pytest
import requests
from datetime import datetime, timedelta
from exceptions import SummonerNotFound
from riot_requests import get_summoners_by_name, get_matches_by_puuid, get_matches_by_match_id, get_active_games_by_summoner_id, get_last_week_matches_by_puuid, get_teams_info
from summoner import Summoner
from team import Team
from match import PastMatch
from unittest.mock import patch

expected_summoner = Summoner("Kid Orpheus", "ii9IPVp8k7MZ33wazChECinTlHDRzgkMMF5VCY-sFRjcnOg",
                             "pfB-gQaB5s62NVK_YTWT7w6Y1NKIjpdzB38-8rFS2cssK-P6i5lFqqT2iVZHZ_rKmGceVc72TTU9Gw")

expected_start_time = datetime(2023, 4, 3, 23, 7, 19)

expected_end_time = datetime(2023, 4, 3, 23, 24, 42)

expected_duration = timedelta(minutes=17, seconds=22)

expected_team0 = Team(100, ['Aeras', 'Kid Orpheus',
                      'Supreme555', 'Xx BrianG 21 xX', 'Grimm Deth'], False)

expected_team1 = Team(200, ['Raymmp', 'uselessbody',
                      'demented liger', 'wow animetiddies', 'realgirlboob'], True)

expected_teams = [expected_team0, expected_team1]

expected_matches = ["NA1_4620466509", "NA1_4620443769",
                    "NA1_4620414214", "NA1_4603467615", "NA1_4601936458"]

expected_past_match = PastMatch(expected_start_time,
                                expected_end_time, expected_duration, expected_teams)


# Test get_teams_info() with a valid match id.

with open("test/mock_get_teams_info.json") as f:
    mock_get_teams_info = json.load(f)


def test_get_teams_info():
    teams = get_teams_info(mock_get_teams_info, active=False)
    assert expected_teams == teams


# Test get_summoners_by_name() with a valid summoner name.

@pytest.fixture
def mock_get_summoners_by_name_sucess():
    with open("test/mock_get_summoners_by_name_success.json") as f:
        return json.load(f)


def test_get_summoners_by_name_success(mock_get_summoners_by_name_sucess):
    """
    Test get_summoners_by_name() with a valid summoner name.
    """

    summoner_name = "Kid Orpheus"
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_get_summoners_by_name_sucess
        summoner = get_summoners_by_name(summoner_name)

    assert expected_summoner == summoner


# Test get_summoners_by_name() with a invalid summoner name.

@pytest.fixture
def mock_get_summoners_by_name_not_found():
    with open("test/mock_get_summoners_by_name_not_found.json") as f:
        return json.load(f)


def test_get_summoners_by_name_not_found(mock_get_summoners_by_name_not_found):
    """
    Test get_summoners_by_name() with a invalid summoner name.
    """
    summoner_name = "not a summoner name"
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = mock_get_summoners_by_name_not_found
        with pytest.raises(SummonerNotFound) as e:
            get_summoners_by_name(summoner_name)
        assert str(e.value) == f"Summoner '{summoner_name}' not found"


# Test get_matches_by_puuid() with a valid puuid.

@pytest.fixture
def mock_get_matches_by_puuid():
    with open("test/mock_get_matches_by_puuid.json") as f:
        return json.load(f)


def test_get_matches_by_puuid(mock_get_matches_by_puuid):
    """
    Test get_matches_by_puuid() with a valid puuid.
    """

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_get_matches_by_puuid
        matches = get_matches_by_match_id(expected_summoner.puuid)

    assert expected_matches == matches


# Test get_last_week_matches_by_puuid() with a valid puuid.

@pytest.fixture
def mock_get_last_week_matches_by_puuid():
    with open("test/mock_get_matches_by_puuid") as f:
        return json.load(f)


def test_get_last_week_matches_by_puuid():
    """
    Test get_last_week_matches_by_puuid() with a valid puuid.
    """
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_get_last_week_matches_by_puuid
        matches = get_last_week_matches_by_puuid(expected_summoner.puuid)

    assert expected_matches == matches


# Test get_matches_by_match_id() with a valid match id.

@pytest.fixture
def mock_get_matches_by_match_id():
    with open("test/mock_get_matches_by_match_id.json") as f:
        return json.load(f)


def test_get_matches_by_match_id(mock_get_matches_by_match_id):
    """
    Test get_matches_by_match_id
    """
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_get_matches_by_match_id
        match = get_matches_by_match_id("NA1_4620414214")

    assert expected_past_match == match

# Test get_active_games_by_summoner_id() with a valid summoner id.


# Need to ask for a mock for this one.
@pytest.fixture
def mock_get_active_games_by_summoner_id():
    pass


def test_get_active_games_by_summoner_id():
    pass
