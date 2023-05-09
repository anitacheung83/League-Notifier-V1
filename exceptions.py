
class SummonerNotFound(Exception):
    """
    Raised when a summoner is not found.
    """

    def __init__(self, summoner_name):
        """
        Initialize a SummonerNotFound object
        """
        self.summoner_name = summoner_name
        self.message = f"Summoner '{summoner_name}' not found"
        super().__init__(self.message)


class MatchNotFound(Exception):
    """
    Raised when a match is not found.
    """

    def __init__(self, match):
        """
        Initialize a MatchNotFound object
        """
        self.match = match
        self.message = f"Match '{match}' not found"
        super().__init__(self.message)


class MessageNotSend(Exception):
    """
    Raises if there is an error sending the message
    """

    def __init__(self) -> None:
        """
        Initialize a MessageNotSend object
        """
        self.message = "Message not send"
        super().__init__(self.message)
