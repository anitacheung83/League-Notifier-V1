from datetime import datetime, timedelta
from match import Match
from summoner import Summoner
from typing import List, Dict
import time
import matplotlib.pyplot as plt
import matplotlib.figure as fig


class WeeklyReport():
    """
    Weekly report for last week match played by summoner

    == Instance Attribute ==
    summoner: Summoner DTO (Data Transfer Object)
    matches:  A list of matches played by summoner last week
    number_of_matches: the total number of matches played by summoner last week
    graph: A graph of the number of matches played by summoner last week
    """
    matches: List[Match]
    number_of_matches: int
    start_date: datetime
    matches_by_date: Dict
    graph: fig.Figure

    def __init__(self, summoner: Summoner, matches: List[Match], start_date: time.time) -> None:
        """
        Initialize a WeeklyReport object

        Args:
            summoner: Summoner DTO (Data Transfer Object)
            matches: A list of matches played by summoner last week
        Return:
            None
        """
        self.summoner = summoner
        # reverse the list so that the most recent match is at the end
        self.matches = matches[::-1]
        self.start_date = datetime.fromtimestamp(start_date)
        self.number_of_matches = self.__get_total_matches_played()
        self.matches_by_date = self.__get_matches_by_date()
        self.games_played_graph = self.__get_games_played_graph()
        self.total_time_played_graph = self.__get_total_time_played_graph()

    def __get_total_matches_played(self) -> int:
        """
        Return the total number of matches played by summoner last week

        Args:
            None

        Return:
            The total number of matches played by summoner last week
        """
        return len(self.matches)

    def __get_matches_by_date(self) -> Dict:
        """
        Return a dictionary of matches played by summoner last week

        Args:
            None

        Return:
            A dictionary of matches played by summoner last week
        """

        matches_by_date = {}
        start_date = self.start_date

        for i in range(8):
            key = start_date.strftime("%m-%d\n%a")
            print(f"key: {key}")
            matches_by_date[key] = []
            start_date += timedelta(days=1)

        for match in self.matches:
            match_date = match.start_time.strftime("%m-%d\n%a")

            # if match_date not in matches_by_date:
            #     matches_by_date[match_date] = []
            if match_date in matches_by_date:
                matches_by_date[match_date].append(match)

        return matches_by_date

    def __get_games_played_graph(self) -> fig.Figure:
        """
        Return a graph of the number of matches played by summoner last week

        Args:
            None

        Return:
            A graph of the number of matches played by summoner last week
        """
        fig = plt.figure()

        x = list(self.matches_by_date.keys())
        y = [len(matches) for matches in self.matches_by_date.values()]

        barplot = plt.bar(x, y)
        plt.bar_label(barplot, labels=y, label_type='edge')
        # plt.bar_label(barplot, labels=y, label_type='center')

        plt.title(f"Number of Games Played by {self.summoner.name} Last Week")

        # plt.xlabel("Date")

        plt.ylabel("Number of Game Played")

        return fig

    def __get_total_time_played_graph(self) -> fig.Figure:
        """
        Return a graph of the total time played by summoner last week

        Args:
            None

        Return: 
            A graph of the total time played by summoner last week
        """
        fig = plt.figure()

        x = list(self.matches_by_date.keys())
        # y is the duration of match played on that day in minutes, cannot use sum() because it is a timedelta object
        y = [sum([match.duration.total_seconds() for match in matches]
                 ) / 60 for matches in self.matches_by_date.values()]

        y_labels = [f"{int(time / 60)}h {int(time % 60)}m" for time in y]

        barplot = plt.bar(x, y)
        plt.bar_label(barplot, labels=y_labels, label_type='edge')
        # plt.bar_label(barplot, labels=y, label_type='center')

        plt.title(f"Total Time Played by {self.summoner.name} Last Week")

        plt.ylabel("Total Time Played (minutes)")

        return fig

    def __str__(self) -> str:
        """
        Return a string representation of WeeklyReport object

        Args:
            None

        Return:
            A string representation of WeeklyReport object
        """
        match_str = '\n'.join(str(match) for match in self.matches)
        return f"Number of Games Played by {self.summoner.name} last Week: {self.number_of_matches}\n{match_str}"
