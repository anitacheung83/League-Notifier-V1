
class Summoner():
    """
    Summoner DTO (Data Transfer Object)

    === Instance Attributes ===
    name: Summoner's name
    id: Summoner's id
    puuid: Summoner's puuid
    """
    name: str
    id: str
    puuid: str

    def __init__(self, name: str, id: str, puuid: str) -> None:
        """
        Initialize a Summoner object

        Args:
            name: Summoner's name
            id: Summoner's id
            puuid: Summoner's puuid

        Return:
            None
        """
        self.name = name
        self.id = id
        self.puuid = puuid

    def __eq__(self, other: object) -> bool:
        """
        Return True if self and other are equal, and False otherwise

        Args:
            other: object to compare self to

        Return:
            True if self and other are equal, and False otherwise
        """
        if not isinstance(other, Summoner):
            return False
        return self.name == other.name and self.id == other.id and self.puuid == other.puuid

    def __str__(self) -> str:
        """
        Return a string representation of a Summoner object

        Args:
            None

        Return:
            A string representation of a Summoner object
        """
        return f"Summoner Name: {self.name} \nSummoner id: {self.id} \nSummoner puuid: {self.puuid}"
