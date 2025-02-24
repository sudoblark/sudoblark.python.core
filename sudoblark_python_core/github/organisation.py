from dataclasses import dataclass
from requests import Session

@dataclass
class Organisation:
    """This class represents an Organisation within GitHub.

    It may be used to perform actions within the context of the organisation.

    Attributes:
        identifier (int): Unique identifier of the organisation within GitHub
        company (str): The company associated with the organisation
        repos_url (str): RESTAPI endpoint for retrieval of repos in the organisation
        client (requests.Session): Session used to make requests to the RESTful API, intended
                          to be passed in when instance is created via GitHubClient.get_organisation
        base_url (str): Base URL we should use for querying this RESTAPI within the context of the organisation

    """
    identifier: int
    company: str
    repos_url: str
    client: Session
    base_url: str

    def __str__(self) -> str:
        """
        Returns:
            Information string representation
        """
        return self.company

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



