"""This module provides utility functions for running commands using subprocess."""

import logging
from subprocess import Popen, PIPE


def run_command(command: str, cwd: str = None) -> tuple:
    """
    Run a command using subprocess.

    :param command: The command to run.
    :param cwd: The working directory in which to run the command. (default: None)
    :return: A tuple containing the process object, the command output, and the error output.
    """
    process = Popen(command.split(), cwd=cwd, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if output:
        logging.info(output.strip().decode('utf-8'))
    if error:
        logging.info(output.strip().decode('utf-8'))
    return process, output, error
