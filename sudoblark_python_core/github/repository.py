from dataclasses import dataclass
from requests import Session

@dataclass
class Repository:
    """This class represents aa Repository within GitHub.

    It may be used to perform actions within the context of the Repository.

    Attributes:
        identifier (int): Unique identifier of the Repository
        client (requests.Session): Session used to make requests to the RESTful API, intended
                          to be passed in when instance is created via Client/Organisation
        base_url (str): Base URL we should use for querying the RESTAPI within the context of the Repository
        full_name (str): Full name of the Repository, in the form of owner/repository
        private (bool): True if the Repository is private, else False
    """
    identifier: int
    client: Session
    base_url: str
    full_name: str
    private: bool

    def __str__(self) -> str:
        """
        Returns:
            Information string representation
        """
        return self.full_name

    def __hash__(self) -> int:
        """
        Returns:
            Unique int representation of instance.
        """
        return hash(self.identifier)

    def __eq__(self, other: object) -> bool:
        """
        Args:
            other: Object to compare against

        Returns:
            True if instances are equal, False otherwise.
        """
        if not isinstance(other, type(self)):
            return False
        return self.identifier == other.identifier
