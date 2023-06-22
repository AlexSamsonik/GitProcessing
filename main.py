from argparse import ArgumentParser

from clone import clone_repository

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--sprint_numbers', metavar='SPRINTS', type=str, required=True)
    args = parser.parse_args()

    sprints = args.sprint_numbers.split('.')

    print(f'Sprints to be processed: {sprints}')
    clone_repository()
