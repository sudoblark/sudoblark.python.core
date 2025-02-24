import os
from sudoblark_python_core import GitHubClient

REPO_OWNER: str = os.getenv("GITHUB_REPOSITORY_OWNER")
REPO_NAME: str = os.getenv("GITHUB_REPOSITORY").split("/")[-1]
PULL_REQUEST_ID: int = int(os.getenv("GITHUB_REF_NAME").split("/")[0])

client = GitHubClient()
repository = client.get_repository(REPO_OWNER, REPO_NAME)
pull_request = repository.get_pull_request(PULL_REQUEST_ID)

with open("./content.txt", "r") as file:
    content = file.read()

pull_request.post_comment(content)