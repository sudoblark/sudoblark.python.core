import os

from behave import *
from sudoblark_python_core import GitHubClient


@given('the repository of "{repo}"')
def step_impl(context, repo: str):
    owner, repo = repo.split('/')
    context.repo_owner = owner.strip()
    context.repo_name = repo.strip()


@given('the organisation of "{org}"')
def step_impl(context, org: str):
    context.org = org.strip()


@when("we use the core library to query the repository")
def step_impl(context):
    client = GitHubClient(os.getenv("GITHUB_TOKEN"))
    context.response = client.get_repository(context.repo_owner, context.repo_name)

@when("we use the core library to query for all pull requests")
def step_impl(context):
    client = GitHubClient(os.getenv("GITHUB_TOKEN"))
    context.response = client.get_repository(context.repo_owner, context.repo_name).get_pull_requests(state="all")

@when("we use the core library to query the organisation")
def step_impl(context):
    client = GitHubClient(os.getenv("GITHUB_TOKEN"))
    context.response = client.get_organisation(context.org)


@then("the response should not be None or empty")
def step_impl(context):
    assert context.response is not None
    if isinstance(context.response, list): assert len(context.response) != 0
