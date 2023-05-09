from typing import List


class Team():
    """
    Team DTO (Data Transfer Object) for a team

    == Instance Attributes ==
    id: Team id
    participants: List of participants in the team
    win: Win result of the team
    """
    id: int
    participants: List[str]
    win: bool

    def __init__(self, id: int, participants: List[str], win=None):
        """
        Initialize a Team object

        Args:
            id: Team id
            participants: List of participants in the team
            win: Win result of the team

        Return:
            None
        """
        self.id = id
        self.participants = participants
        self.win = win

    def __eq__(self, other: object) -> bool:
        """
        Return True if self and other are equal, and False otherwise

        Args:
            other: object to compare self to

        Return:
            True if self and other are equal, and False otherwise
        """
        if not isinstance(other, Team):
            return False
        return self.id == other.id and self.participants == other.participants and self.win == other.win

    def __str__(self) -> str:
        """
        Return a string representation of a Team object

        Args:
            None

        Return:
            A string representation of a Team object
        """
        return f"Team id: {self.id}\nparticipants: {self.participants}\nWin: {self.win}"
