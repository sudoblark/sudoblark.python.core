# GitHubClient

> **_NOTE:_**  GitHub extensive document on how
> to generation tokens [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
> 
> Once generated, you may base64 encode it however you wish. However, it should be noted
> that such tokens need to be treated with the upmost secrecy. If you are using
> this library via GitHub Actions it is thus recommended to either:
> 
>   - Auto-generate a limited access token as per the [docs](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)
>   - Use [JWT](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app) to generate a limited access token
>   - [Fine-grain](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization) your organisational access to a secret access token

::: sudoblark_python_core.github.client.Client