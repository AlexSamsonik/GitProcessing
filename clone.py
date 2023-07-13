"""This module provides a function for cloning a Git repository."""

from os.path import isdir, join

from assistants import run_command


def clone_repository(repo_dir: str = None, repo_url: str = None):
    """
    Clones a git repository from the specified URL into the specified directory.

    :param repo_dir: The directory to clone the repository into.
    :param repo_url: The URL of the repository to clone.
    :return: None
    """
    # Check if the environment variables REPO_DIR and REPO_URL has been setting
    if not repo_dir or not repo_url:
        print('Please set environment variables REPO_DIR and REPO_URL')
        return

    # Check if the repository has been cloned and the .git directory exists
    if isdir(repo_dir) and isdir(join(repo_dir, '.git')):
        print(f'Repository has been cloned and the ".git" directory exists in directory "{repo_dir}"')
    else:
        print(f'Repository has not been cloned or the ".git" directory is missing in directory "{repo_dir}"')
        # Clone the repository
        print(f'Start cloning ...')
        run_command(f'git clone {repo_url}')
