"""This module provides functions for managing sprint release branches."""

from subprocess import run, PIPE


def create_local_branch(local_branch: str, remote_branch: str, repo_dir: str):
    """
    Creates a local branch based on a remote branch in a specified repository directory.

    :param local_branch: The name of the local branch to create.
    :param remote_branch: The name of the remote branch to base the local branch on.
    :param repo_dir: The path to the repository directory.
    :return: None
    """
    if local_branch_exist(local_branch, repo_dir):
        print(f" A branch '{local_branch}' already exists.")
    else:
        print(f"Local branch '{local_branch}' is not exists.")
        print(f"Creating local branch '{local_branch}' ...")
        run(f"git checkout -b {local_branch} origin/{remote_branch}".split(), cwd=repo_dir)


def local_branch_exist(local_branch: str, repo_dir: str):
    """
    Checks if a local branch exists in a specified repository directory.

    :param local_branch: The name of the local branch to check.
    :param repo_dir: The path to the repository directory.
    :return: The output of the branch list command as a string.
    """
    print(f"Check if the local branch '{local_branch}' exists.")
    branch_list_cmd = f"git branch --list {local_branch}"
    return run(branch_list_cmd.split(), cwd=repo_dir, capture_output=True, text=True).stdout


def pull_from_remote_branch(local_branch: str, remote_branch: str, repo_dir: str):
    """
    Pulls changes from a remote branch to an existing local branch in a specified repository directory.

    :param local_branch: The name of the existing local branch.
    :param remote_branch: The name of the remote branch to pull changes from.
    :param repo_dir: The path to the repository directory.
    :return: None
    """
    print(f"Local branch '{local_branch}' already exists.")
    run(f"git switch {local_branch}".split(), cwd=repo_dir)
    print(f"Pulling changes for branch '{remote_branch}' ...")
    if local_branch and remote_branch == "master":
        run(f"git pull".split(), cwd=repo_dir)
    else:
        run(f"git pull origin {remote_branch}".split(), cwd=repo_dir)


def create_local_backport_release_branches(sprint_numbers: list, ticket_number: str, repo_dir: str = None):
    """
    Creates local backport release branches for the given sprint numbers and ticket number.

    :param sprint_numbers: A list of sprint numbers for which the backport release branches need to be created.
    :param ticket_number: The ticket number for which the backport release branches are being created.
    :param repo_dir: The current repository directory where the branches need to be created. Defaults to None.
    :return: None
    """
    for sprint in sprint_numbers:
        release_branch_name = f"release/sprint_{sprint}"
        backport_branch_name = f"{ticket_number}_backport_for_sprint_{sprint}"
        if local_branch_exist(backport_branch_name, repo_dir):
            pull_from_remote_branch(backport_branch_name, release_branch_name, repo_dir)
        else:
            create_local_branch(backport_branch_name, release_branch_name, repo_dir)
            pull_from_remote_branch(backport_branch_name, release_branch_name, repo_dir)


def collecting_commit_hashes_from_local_branch(local_branch: str, author: str, repo_dir: str) -> list:
    """
    Collects commit hashes from a local branch authored by a specific author in a specified repository directory.

    :param local_branch: The name of the local branch.
    :param author: The name of the author whose commits will be collected.
    :param repo_dir: The path to the repository directory.
    :return: A list of commit hashes.
    """
    git_log_cmd = f"git log master..{local_branch} --format=%H --author={author} --no-merges"
    result = run(git_log_cmd.split(), cwd=repo_dir, stdout=PIPE, text=True)
    return result.stdout.split()


def cherry_pick_and_push(sprint_numbers: list, commit_hashes: list, ticket_number: str, repo_dir: str):
    """
    Cherry-picks and pushes commits to a backport branch for each sprint number.

    :param sprint_numbers: A list of sprint numbers.
    :param commit_hashes: A list of commit hashes to cherry-pick.
    :param ticket_number: The ticket number associated with the backport.
    :param repo_dir: The path to the repository directory.
    :return: None
    """
    for sprint in sprint_numbers:
        backport_branch_name = f"{ticket_number}_backport_for_sprint_{sprint}"
        if local_branch_exist(backport_branch_name, repo_dir):
            run(f"git switch {backport_branch_name}".split(), cwd=repo_dir)
            for commit in commit_hashes[::-1]:
                run(f"git cherry-pick -n {commit}".split(), cwd=repo_dir)
                run(f"git add --all".split(), cwd=repo_dir)
            run(f"git commit -m 'backporting_{ticket_number}_for_sprint_{sprint}'".split(), cwd=repo_dir)
            run(f"git push origin {backport_branch_name}".split(), cwd=repo_dir)
