from argparse import ArgumentParser
from os import environ

from branch import create_local_backport_release_branches
from clone import clone_repository

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--sprint_numbers', metavar='SPRINTS', type=str, required=True)
    parser.add_argument('-t', '--ticket', metavar='TICKET', type=str, required=True)
    args = parser.parse_args()

    sprints = args.sprint_numbers.split('.')

    repo_dir = environ.get('REPO_DIR')
    repo_url = environ.get('REPO_URL')

    print(f'Sprints to be processed: {sprints}')
    clone_repository(repo_dir, repo_url)
    create_local_backport_release_branches(sprints, args.ticket, repo_dir)
