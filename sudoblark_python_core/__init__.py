"""
Sudoblark Core Python library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


This is a core library, written in Python, to provide a good, known, fully unit tested
working class library to assist Sudoblark in code writing activities.

Public interfaces are exported for interaction with various RESTAPIs.

For effective usage of the library, it is recommended to configure logging in order to recieve
additional information regarding library operations:

    >>> import logging
    >>> logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(name)s - %(asctime)s - %(message)s')

Known interface documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~
Authentication is via a base64 encoded user:pass token, present either:
- Via the GITHUB_TOKEN environment variable
- Explicitly as an argument to the client
- Via an explicitly provided base64 user

    >>> from sudoblark_python_core import GitHubClient
    >>> help(GitHubClient)

For example, to comment on a specific pull request for a specific repository:
    >>> from sudoblark_python_core import GitHubClient
    >>> client = GitHubClient("<GITHUB_TOKEN>")
    >>> client.get_repository("<name>").get_pull_request("<id>").post_comment(
    >>>)
    >>> help(GitHubClient)

"""

from .github.client import (  # noqa: F401 # Imported but not used for readability reasons
    Client as GitHubClient,
)