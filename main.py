from argparse import ArgumentParser
from os import environ

from clone import clone_repository

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--sprint_numbers', metavar='SPRINTS', type=str, required=True)
    args = parser.parse_args()

    sprints = args.sprint_numbers.split('.')

    print(f'Sprints to be processed: {sprints}')
    repo_dir = environ.get('REPO_DIR')
    repo_url = environ.get('REPO_URL')
    clone_repository(repo_dir, repo_url)
