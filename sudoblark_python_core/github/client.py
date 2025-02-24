"""
This module is responsible for configuration of the base GitHub Client class,
which is exported at the root of the project as GitHubClient.
"""
from sudoblark_python_core.abstracts.restapi import IClient
from sudoblark_python_core.github.organisation import Organisation
from typing import Union
from typing import List


class Client(IClient):
    """This is our primary interface for interacting with the GitHub RESTAPI.

    It requires a bearer token for authentication, base64 encoded
    as `user:token`. This may either:

    * Be exported to the `GITHUB_TOKEN` environment variable
    * Passed explicitly to the constructor

    Attributes:
        client (requests.Session): object created by `IClient` to handle interaction with the RESTAPI


    Example:
        With an explicit token provided:

        ```python
        from sudoblark_python_core import GitHubClient
        client = GitHubClient("<TOKEN>")
        ```

        When `GITHUB_TOKEN` is a known environment variable:
        ```python
        from sudoblark_python_core import GitHubClient
        client = GitHubClient()
        ```
    """

    def _get_auth_type(self) -> str:
        return "bearer"

    def _get_base_url(self) -> str:
        return "https://api.github.com"

    def _get_auth_endpoint(self) -> str:
        return "/user"

    def _get_api_name(self) -> str:
        return "GitHub RESTAPI"

    def _get_auth_secret_environment_variable(self) -> str:
        return "GITHUB TOKEN"

    def __post__init__(self):
        """
        Overwritten IClient method to execute at the end of IClient init, mutates
        headers etc to be those recommended for GitHub.
        """
        self.headers["Accept"] = "application/vnd.github.v3+json"
        self.headers["X-GitHub-Api-Version"] = "2022-11-28"
        self.client.headers.update(self.headers)

    def get_organisations(self) -> List[Organisation]:
        """
        Examples:
            ```python
            get_organisations()
            ```

        Returns:
            List of Organisations which `Client` has access to.
        """
        organisations: List[Organisation] = []
        github_restapi_request = self.client.get(
            url=f"{self._get_base_url()}/organizations"
        )
        if github_restapi_request.status_code == 200:
            for organisation in github_restapi_request.json():
                organisations.append(
                    Organisation(
                        identifier=organisation["id"],
                        company=organisation["url"].split("/")[-1],
                        repos_url=organisation["repos_url"],
                        client=self.client,
                        base_url=organisation["url"]
                    )
                )
        return organisations

    def get_organisation(self, name: str) -> Union[None, Organisation]:
        """
        Args:
            name: The name of the organisation

        Examples:
            ```python
            get_organisation("Sudoblark")
            ```

        Returns:
            `Organisation` instance if found, else None
        """
        organisation: Union[None, Organisation] = None

        github_restapi_request = self.client.get(
            url=f"{self._get_base_url()}/orgs/{name}"
        )
        if github_restapi_request.status_code == 200:
            response_data = github_restapi_request.json()
            organisation = Organisation(
                identifier=response_data["id"],
                company=response_data["name"],
                repos_url=response_data["repos_url"],
                client=self.client,
                base_url=response_data["url"]
            )
        return organisation
