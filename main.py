import logging
from argparse import ArgumentParser
from os import environ

from clone import clone_repository
from sprint_branches import create_local_release_branches

logging.basicConfig(format="%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
                    datefmt="%Y-%m-%d %H:%M:%S", level=10)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--sprint_numbers', metavar='SPRINTS', type=str, required=True)
    args = parser.parse_args()

    sprints = args.sprint_numbers.split('.')

    logging.info(f'Sprints to be processed: {sprints}')
    repo_dir = environ.get('REPO_DIR')
    repo_url = environ.get('REPO_URL')
    clone_repository(repo_dir, repo_url)
    create_local_release_branches(sprints, repo_dir)
