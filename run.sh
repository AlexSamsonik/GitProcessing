#!/bin/sh

export REPO_DIR=
export REPO_URL=

author="user_email@gmal.com"
sprints="10.11.12"

ticket="TEST-757"
branch="TEST-757_login_test_for_example"

# Example of usage: python3 main.py -s 10.11.12 -t TEST-757 -a user_email@gmal.com -b TEST-757_login_test_for_example
python3 main.py -s "$sprints" -t "$ticket" -a "$author" -b "$branch"