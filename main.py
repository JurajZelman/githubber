"""Copyright (c) 2022 Juraj Zelman"""

import json
import os

import click
from github import Github

__version__ = "1.0.0"


@click.command()
@click.argument(
    "repo_name",
    type=click.STRING,
    nargs=1,
)
@click.option(
    "-v",
    "--version",
    type=click.STRING,
    default="3.8.8",
    show_default=True,
    help="Version of Python to be installed by pipenv.",
)
@click.option(
    "-l",
    "--license",
    type=click.BOOL,
    default=True,
    show_default=True,
    help="Boolean choice whether to include the MIT license file.",
)
@click.version_option(version=__version__, message="%(version)s")
def githubber(repo_name, version, license):
    """Comment"""

    token = load_github_token()
    # print(token)

    # First create a Github instance:
    # g = Github(token)
    # user = g.get_user()

    # Then play with your Github objects:
    # for repo in user.get_repos():
    #     print(repo.name)

    # repo = user.create_repo(repo_name)


def load_github_token() -> str:
    """Loads and returns the github access token."""
    file = os.path.join(
        click.get_app_dir("githubber", roaming=True), "config", "account.json"
    )
    try:
        with open(file, "r") as jsonfile:
            token = json.load(jsonfile)["github_token"]
    except FileNotFoundError:
        raise click.FileError(
            file,
            hint="File account.json not found!",
        )

    return token


if __name__ == "__main__":
    githubber()
