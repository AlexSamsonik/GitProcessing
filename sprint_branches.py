import logging
from subprocess import Popen, PIPE

from assistants import run_command


def create_local_release_branches(sprint_numbers, cwd=None):
    for sprint in sprint_numbers:
        branch_name = f'release/sprint_{sprint}'

        # Check if the branch already exists
        command = f'git rev-parse --verify {branch_name}'
        process = Popen(command.split(), cwd=cwd, stdout=PIPE, stderr=PIPE)
        _, _ = process.communicate()
        if process.returncode == 0:
            logging.info(f'Branch "{branch_name}" already exists. Switching to branch ...')
            run_command(f'git switch {branch_name}', cwd=cwd)
            logging.info(f'Pulling changes for branch "{branch_name}" ...')
            run_command(f'git pull origin {branch_name}', cwd=cwd)
        else:
            logging.info(f'Creating branch "{branch_name}" ...')
            run_command(f'git checkout -b {branch_name} origin/{branch_name}', cwd=cwd)
