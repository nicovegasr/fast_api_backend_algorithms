# Make a script in bash to git add and commit all files in a directory with a message from the command line
# Usage: ./git_dev "Commit message"
git add . && git commit -m "$1"
