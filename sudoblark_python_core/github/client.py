class Client:
    """
    This is our primary interface for interacting with the GitHub RESTAPI.

    It requires a bearer token for authentication, base64 encoded
    as `user:token`. This may either:
    - Be exported to the `GITHUB_TOKEN` environment variable
    - Passed explicitly to the constructor

    Example:
    Retrieve a GitHub

    """
    def hello(self):
        print("world")