import enum
from dataclasses import dataclass
from requests import Session


class PullRequestState(enum.Enum):
    """Valid pull request states.

    Attributes:
        open (str): Open pull request
        closed (str): Closed pull request
        all (str): Any pull request
    """
    open = "open"
    closed = "closed"
    all = "all"

@dataclass
class PullRequest:
    """This class represents a PullRequest on a specific repository.

    It may be used to perform actions within the context of the PullRequest.

    Attributes:
        identifier (int): Unique identifier of the Repository
        client (requests.Session): Session used to make requests to the RESTAPI, intended
                          to be passed in when instance is created via Repository
        base_url (str): Base URL we should use for querying the RESTAPI within the context of the PullRequest
        title (str): Title given to the PullRequest
        repo (str): Name of the Repository which the instance is associated with
        state (PullRequestState): State of the pull request
    """
    identifier: int
    client: Session
    base_url: str
    title: str
    repo: str
    state: PullRequestState

    def __str__(self) -> str:
        """
        Returns:
            Information string representation
        """
        return f"Repo: {self.repo} , Pull request ID: {self.identifier} , Title: {self.title} , State: {self.state}"

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
