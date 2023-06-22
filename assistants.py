from subprocess import Popen, PIPE


def run_command(command, cwd=None):
    process = Popen(command.split(), cwd=cwd, stdout=PIPE)
    output, error = process.communicate()
    if output:
        print(output.strip().decode('utf-8'))
