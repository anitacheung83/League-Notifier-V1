from datetime import datetime, timedelta
from team import Team
from typing import List


class Match():
    """
    Match DTO (Data Transfer Object) for a match

    === Instance Attributes ===
    start_time: Match start time
    duration: Match duration
    teams: Teams that participated in the match
    """

    start_time: datetime
    duration: timedelta
    teams: List[Team]

    def __init__(self, start_time: datetime, duration: timedelta, teams: List[Team]) -> None:
        self.start_time = start_time
        self.duration = duration
        self.teams = teams


class PastMatch(Match):
    """
    Past Match DTO (Data Transfer Object) for a match happened in the past.

    === Instance Attributes ===
    start_time: Match start time
    end_time: Match end time
    duration: Match duration
    teams: Teams that participated in the match
    """

    start_time: datetime
    end_time: datetime
    duration: timedelta
    teams: List[Team]

    def __init__(self, start_time: datetime, end_time: datetime, duration: timedelta, teams: List[Team]) -> None:
        self.end_time = end_time
        super().__init__(start_time, duration, teams)

    def __str__(self) -> str:
        game_start_str = self.start_time.strftime("%m/%d/%Y, %H:%M:%S")
        game_end_str = self.end_time.strftime("%m/%d/%Y, %H:%M:%S")
        duration_str = str(self.duration)
        team_str = '\n'.join(str(team) for team in self.teams)
        return f"Match started at: {game_start_str}\nMatch ended at: {game_end_str}\nDuration: {duration_str}\nTeams:\n{team_str}\n"


class ActiveMatch(Match):
    """
    Active Match DTO (Data Transfer Object) for an active match

    === Instance Attributes ===
    start_time: Match start time
    duration: Match duration
    teams: Teams that participated in the match
    """

    start_time: datetime
    duration: timedelta
    teams: List[Team]

    def __init__(self, start_time: datetime, duration: timedelta, teams: List[Team]) -> None:
        super().__init__(start_time, duration, teams)

    def __str__(self) -> str:
        game_start_str = self.start_time.strftime("%m/%d/%Y, %H:%M:%S")
        duration_str = str(self.duration)
        team_str = '\n'.join(str(team) for team in self.teams)
        return f"Match started at: {game_start_str}\nDuration: {duration_str}\nTeams:\n{team_str}\n"
