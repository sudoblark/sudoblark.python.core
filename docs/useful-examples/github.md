# GitHubClient useful examples
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

## Get all comments on a given pull request
```python
from sudoblark_python_core import GitHubClient
client = GitHubClient()
pull_request = client.get_repository("vexx32", "PSKoans").get_pull_request(241)
for comment in pull_request.get_comments():
    print(comment)
```

## Interaction with pull requests within a CI/CD environment
Given the intended operation within CI/CD environments, there are some
examples below for how to use these classes to interact with pull requests
in the simplest manner possible.

This all follow two assumptions:

- `GITHUB_TOKEN` is an environment variable available to the agent running the job
- `./file.md` is present, and contains the markdown we wish to utilise for the comment

> **_NOTE:_**  As an Organisation is listed as the owner of a repository, these
> example will work both for repositories which are:
> 
>   * Present on a personal GitHub account
>   * Stored within an Organisation

All of these examples essentially rely upon the fact that most CI/CD systems out
there prepopulate information in the build with contextual information. Said contextual
information can be used to discover the pull request associated with the build
with relative ease. The docs regarding what values are prepopulated, and how,
have been linked below for reference.

| Platform               | Docs                                                                                                                         | Syntax                                                                                                                                     |
|------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| GitHub Actions         | [docs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables) | Grab via environment variables                                                                                                             |
| Azure DevOps pipelines | [docs](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml)                 | Reference via `"$(VAR_NAME)"` directly in script, or <br/>add to the `env` block of you task to <br/>reference via an environment variable |
| CircleCI               | [docs](https://circleci.com/docs/variables/#built-in-environment-variables)                                                  | Reference via environment variables                                                                                                        |


### Adding a new comment

<details close>
<summary>GitHub Actions</summary>
<br>

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

</details>
<br>

<details close>
<summary>Azure DevOps pipelines</summary>
<br>

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

</details>
<br>

<details close>
<summary>CircleCI</summary>
<br>

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

</details>
<br>