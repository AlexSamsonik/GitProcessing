"""This module provides functions for managing sprint release branches."""


from assistants import run_command


def create_local_release_branches(sprint_numbers: list, cwd: str = None):
    """
    Creates local release branches for the specified sprints.

    :param sprint_numbers: A list of sprint numbers to create release branches for.
    :param cwd: The current working directory to run the git commands in.
    :return: None
    """
    for sprint in sprint_numbers:
        branch_name = f'release/sprint_{sprint}'

        # Check if the branch already exists
        process, _, _ = run_command(f'git rev-parse --verify {branch_name}', cwd=cwd)
        if process.returncode == 0:
            print(f'Branch "{branch_name}" already exists. Switching to branch ...')
            run_command(f'git switch {branch_name}', cwd=cwd)
            print(f'Pulling changes for branch "{branch_name}" ...')
            run_command(f'git pull origin {branch_name}', cwd=cwd)
        else:
            print(f'Creating branch "{branch_name}" ...')
            run_command(f'git checkout -b {branch_name} origin/{branch_name}', cwd=cwd)


def create_local_backport_release_branches(sprint_numbers: list, ticket_number: str, cwd: str = None):
    """
    Creates local backport release branches for the given sprint numbers and ticket number.

    :param sprint_numbers: A list of sprint numbers for which the backport release branches need to be created.
    :param ticket_number: The ticket number for which the backport release branches are being created.
    :param cwd: The current working directory where the branches need to be created. Defaults to None.
    :return: None
    """
    for sprint in sprint_numbers:
        release_branch_name = f'release/sprint_{sprint}'
        backport_branch_name = f'{ticket_number}_backport_for_sprint_{sprint}'

        # Check if the branch already exists
        process, _, _ = run_command(f'git rev-parse --verify {backport_branch_name}', cwd=cwd)
        if process.returncode == 0:
            print(f'Branch "{backport_branch_name}" already exists. Switching to branch ...')
            run_command(f'git switch {backport_branch_name}', cwd=cwd)
            print(f'Pulling changes for branch "{release_branch_name}" ...')
            run_command(f'git pull origin {release_branch_name}', cwd=cwd)
        else:
            print(f'Creating branch "{backport_branch_name}" ...')
            run_command(f'git checkout -b {backport_branch_name} origin/{release_branch_name}', cwd=cwd)

