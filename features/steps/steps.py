import os

from behave import *
from sudoblark_python_core import GitHubClient
import random

TEST_REPO = "sudoblark/sudoblark.python.core"
TEST_PR = 3  # Hard-coded as the integration testing PR for above repo


@given('the repository of "{repo}"')
def step_impl(context, repo: str):
    owner, repo = repo.split('/')
    context.repo_owner = owner.strip()
    context.repo_name = repo.strip()


@given('the organisation of "{org}"')
def step_impl(context, org: str):
    context.org = org.strip()


@given('that we are testing for comment interactions')
def step_impl(context):
    client = GitHubClient(os.getenv("GITHUB_TOKEN"))
    owner, repo = TEST_REPO.split('/')
    repository = client.get_repository(owner, repo)
    context.pull_request = repository.get_pull_request(TEST_PR)


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


@when('we have the content of "{body}"')
def step_impl(context, body):
    context.body = body


@then("the response should not be None or empty")
def step_impl(context):
    assert context.response is not None
    if isinstance(context.response, list): assert len(context.response) != 0


@then('we should be able to "{operation}" a comment')
def step_impl(context, operation):
    match operation:
        case "post":
            new_comment = context.pull_request.post_comment(context.body)
            assert new_comment is not None
        case "update":
            random_comment = random.choice(context.pull_request.get_comments())
            assert random_comment.update(context.body)
        case "overwrite":
            random_comment = random.choice(context.pull_request.get_comments())
            assert random_comment.overwrite(context.body)
        case "delete":
            random_comment = random.choice(context.pull_request.get_comments())
            assert random_comment.delete()
        case _:
            pass

@then('we should be able to delete a comment')
def step_impl(context):
    random_comment = random.choice(context.pull_request.get_comments())
    assert random_comment.delete()