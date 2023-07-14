"""This module provides functions for managing sprint release branches."""

from subprocess import run


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
        result = run(f"git branch --list {backport_branch_name}".split(), cwd=repo_dir, capture_output=True,
                     text=True)
        if result.stdout:
            print(f'Branch "{backport_branch_name}" already exists.')
            run(f'git switch {backport_branch_name}'.split(), cwd=repo_dir)
            print(f'Pulling changes for branch "{release_branch_name}" ...')
            run(f'git pull origin {release_branch_name}'.split(), cwd=repo_dir)
        else:
            print(f'Branch "{backport_branch_name}" is not exists.')
            print(f'Creating branch "{backport_branch_name}" ...')
            run(f'git checkout -b {backport_branch_name} origin/{release_branch_name}'.split(), cwd=repo_dir)
