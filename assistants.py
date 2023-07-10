import logging
from subprocess import Popen, PIPE


def run_command(command, cwd=None):
    process = Popen(command.split(), cwd=cwd, stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    if output:
        logging.info(output.strip().decode('utf-8'))
    if error:
        logging.info(output.strip().decode('utf-8'))
    return process, output, error
