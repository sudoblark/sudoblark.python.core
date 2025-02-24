# GitHubClient
Once a `GITHUB_TOKEN` is present in your environment variables, the below
examples should work just fine.

For more information on why this is required, and how to generate such a 
token, see [GitHubClient](../known-interfaces/github/client.md) documentation.



## Get all repositories in an organisation
```python
from sudoblark_python_core import GitHubClient
client = GitHubClient()
for repository in client.get_organisation("sudoblark").get_repositories():
    print(repository)
```

## Get a personal repository:

```python
from sudoblark_python_core import GitHubClient
client = GitHubClient()
print(client.get_repository("benjaminlukeclark", "Get-Duplicate-Files"))
```

## Get a repository in an organisation

* Either traverse via the Organisation instance:

```python
from sudoblark_python_core import GitHubClient
client = GitHubClient()
organisation = client.get_organisation("sudoblark")
print(organisation.get_repository("sudoblark.terraform.github"))
```

* Or simply query the base client with the Organisation as the owner:

```python
from sudoblark_python_core import GitHubClient
client = GitHubClient()
print(client.get_repository("sudoblark", "sudoblark.terraform.github"))
```

## Get all pull requests for a given repository

```python
from sudoblark_python_core import GitHubClient
client = GitHubClient()
repository = client.get_repository("sudoblark", "sudoblark.terraform.github")
for request in repository.get_pull_requests("all"):
    print(request)
```

## Comment on a pull request
Given the intended operation within CI/CD environments, there are some
examples below for how to use these classes to comment on pull requests
in the simplest manner possible.

This all follow two assumptions:

- `GITHUB_TOKEN` is an environment variable available to the agent running the job
- `./file.md` is present, and contains the markdown we wish to utilise for the comment

> **_NOTE:_**  As an Organisation is listed as the owner of a repository, these
> example will work both for repositories which are:
> 
>   * Present on a personal GitHub account
>   * Stored within an Organisation

### GitHub Actions
GitHub actions pre-populates certain environment variables, an extensive
list of which is available via their own [docs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables).

Assuming a build has been triggered by a commit to a pull request, we have all the contextual information
required in order to post a comment to the trigger pull request.

```python
import os
from sudoblark_python_core import GitHubClient

REPO_OWNER: str = os.getenv("GITHUB_REPOSITORY_OWNER")
REPO_NAME: str = os.getenv("GITHUB_REPOSITORY").split("/")[-1]
PULL_REQUEST_ID: int = int(os.getenv("GITHUB_REF_NAME").split("/")[0])

client = GitHubClient()
repository = client.get_repository(REPO_OWNER, REPO_NAME)
pull_request = repository.get_pull_request(PULL_REQUEST_ID)

with open("./file.md", "r") as file:
    content = file.read()

pull_request.post_comment(content)
```

### Azure DevOps Pipelines
Azure DevOps pipelines pre-populates certain environment variables, an extensive
list of which is available via their own [docs](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml).

Assuming a build has been triggered by a commit to a pull request, we have all the contextual information
required in order to post a comment to the trigger pull request.

```python
from sudoblark_python_core import GitHubClient

REPO_OWNER: str = "$(Build.Repository.Name)".split("/")[0]
REPO_NAME: str = "$(Build.Repository.Name)".split("/")[-1]
PULL_REQUEST_ID: int = int("$(System.PullRequest.PullRequestNumber)")

client = GitHubClient()
repository = client.get_repository(REPO_OWNER, REPO_NAME)
pull_request = repository.get_pull_request(PULL_REQUEST_ID)

with open("./file.md", "r") as file:
    content = file.read()

pull_request.post_comment(content)
```

### CircleCI
CircleCI pre-populates certain environment variables, an extensive
list of which is available via their own [docs](https://circleci.com/docs/variables/#built-in-environment-variables).

Assuming a build has been triggered by a commit to a pull request, we have all the contextual information
required in order to post a comment to the trigger pull request.

```python
import os
from sudoblark_python_core import GitHubClient

REPO_OWNER: str = os.getenv("CIRCLE_PR_REPONAME").split("/")[0]
REPO_NAME: str = os.getenv("CIRCLE_PR_REPONAME").split("/")[-1]
PULL_REQUEST_ID: int = int(os.getenv("CIRCLE_PR_NUMBER").split("/")[0])

client = GitHubClient()
repository = client.get_repository(REPO_OWNER, REPO_NAME)
pull_request = repository.get_pull_request(PULL_REQUEST_ID)

with open("./file.md", "r") as file:
    content = file.read()

pull_request.post_comment(content)
```
