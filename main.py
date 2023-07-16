from argparse import ArgumentParser
from os import environ

from branch import create_local_backport_release_branches, create_local_branch, \
    collecting_commit_hashes_from_local_branch, cherry_pick_and_push
from clone import clone_repository

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--sprint_numbers', metavar='SPRINTS', type=str, required=True)
    parser.add_argument('-t', '--ticket', metavar='TICKET_NUMBER', type=str, required=True)
    parser.add_argument('-a', '--author', metavar='AUTHOR_EMAIL', type=str, required=True)
    parser.add_argument('-b', '--branch', metavar='WORKING_BRANCH', type=str, required=True)
    args = parser.parse_args()

    sprints = args.sprint_numbers.split('.')

    repo_dir = environ.get('REPO_DIR')
    repo_url = environ.get('REPO_URL')

    print(f'Sprints to be processed: {sprints}')
    clone_repository(repo_dir, repo_url)
    create_local_backport_release_branches(sprints, args.ticket, repo_dir)
    create_local_branch(args.branch, args.branch, repo_dir)
    commit_hashes = collecting_commit_hashes_from_local_branch(args.branch, args.author, repo_dir)
    print(commit_hashes)
    cherry_pick_and_push(sprints, commit_hashes, args.ticket, repo_dir)
