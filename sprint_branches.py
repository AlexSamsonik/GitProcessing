"""This module provides functions for managing release branches."""

import logging

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
            logging.info(f'Branch "{branch_name}" already exists. Switching to branch ...')
            run_command(f'git switch {branch_name}', cwd=cwd)
            logging.info(f'Pulling changes for branch "{branch_name}" ...')
            run_command(f'git pull origin {branch_name}', cwd=cwd)
        else:
            logging.info(f'Creating branch "{branch_name}" ...')
            run_command(f'git checkout -b {branch_name} origin/{branch_name}', cwd=cwd)
