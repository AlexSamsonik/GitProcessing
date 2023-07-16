"""This module provides functions for managing sprint release branches."""

from subprocess import run


def create_local_branch(local_branch: str, remote_branch: str, repo_dir: str):
    """
    Creates a local branch based on a remote branch in a specified repository directory.

    :param local_branch: The name of the local branch to create.
    :param remote_branch: The name of the remote branch to base the local branch on.
    :param repo_dir: The path to the repository directory.
    :return: None
    """
    print(f'Local branch "{local_branch}" is not exists.')
    print(f'Creating local branch "{local_branch}" ...')
    run(f'git checkout -b {local_branch} origin/{remote_branch}'.split(), cwd=repo_dir)


def pull_from_remote_branch(local_branch: str, remote_branch: str, repo_dir: str):
    """
    Pulls changes from a remote branch to an existing local branch in a specified repository directory.

    :param local_branch: The name of the existing local branch.
    :param remote_branch: The name of the remote branch to pull changes from.
    :param repo_dir: The path to the repository directory.
    :return: None
    """
    print(f'Local branch "{local_branch}" already exists.')
    run(f'git switch {local_branch}'.split(), cwd=repo_dir)
    print(f'Pulling changes for branch "{remote_branch}" ...')
    run(f'git pull origin {remote_branch}'.split(), cwd=repo_dir)


def create_local_backport_release_branches(sprint_numbers: list, ticket_number: str, repo_dir: str = None):
    """
    Creates local backport release branches for the given sprint numbers and ticket number.

    :param sprint_numbers: A list of sprint numbers for which the backport release branches need to be created.
    :param ticket_number: The ticket number for which the backport release branches are being created.
    :param repo_dir: The current repository directory where the branches need to be created. Defaults to None.
    :return: None
    """
    for sprint in sprint_numbers:
        release_branch_name = f'release/sprint_{sprint}'
        backport_branch_name = f'{ticket_number}_backport_for_sprint_{sprint}'

        print(f"Check if the branch {backport_branch_name} exists.")
        branch_list_cmd = f"git branch --list {backport_branch_name}"
        result = run(branch_list_cmd.split(), cwd=repo_dir, capture_output=True, text=True)
        if result.stdout:
            pull_from_remote_branch(backport_branch_name, release_branch_name, repo_dir)
        else:
            create_local_branch(backport_branch_name, release_branch_name, repo_dir)
