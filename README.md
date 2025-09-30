# DataScience
Study material for data scientist
--------------------------------------------------------------------------------------
# 1. Initialize & link
git init
git remote add origin https://github.com/username/repo.git

# 2. Create branch & work
git checkout -b feature/basic
# (edit files...)

# 3. Add & commit
git add .
git commit -m "Initial commit on basic branch"

# 4. Sync remote (if exists)
git pull origin feature/basic --rebase

# 5. Push branch
git push -u origin feature/basic
---------------------------------------------------------------------------------------
Git imp commands:
# Check Git version (to confirm installation)
git --version

# Configure your Git identity (required only once per machine)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# Initialize a new Git repository in your current folder
git init

# Add remote repository (replace URL with your repo)
git remote add origin https://github.com/username/repo.git

# Verify remote
git remote -v

# If you need to change remote
git remote remove origin
git remote add origin https://github.com/username/repo.git

# See current file status
git status

# Add all files
git add .

# OR add specific file
git add filename.ext

# Commit with a message
git commit -m "Your commit message"

# List all local branches
git branch

# List remote branches
git branch -r

# List all (local + remote)
git branch -a

# Create a new branch and switch to it
git checkout -b branch-name

# Switch to an existing branch
git checkout branch-name

# Delete a local branch
git branch -d branch-name

# Delete a remote branch
git push origin --delete branch-name

# First-time push of a new branch
git push -u origin branch-name

# Regular push after upstream is set
git push

# Pull latest changes from remote
git pull

# Pull + rebase (cleaner history)
git pull --rebase

# Pull from specific branch
git pull origin branch-name --rebase

# Fetch all remote branches and updates (no merge)
git fetch

# View difference between local and remote branches
git diff branch-name origin/branch-name

# Rebase local changes on top of remote branch
git pull origin branch-name --rebase

# Show commit history (compact)
git log --oneline

# Show commit history with branches graph
git log --oneline --graph --all

# Show detailed log
git log

# Show changes in last commit
git show

# Unstage a file (keep changes)
git reset filename.ext

# Undo last commit but keep changes staged
git reset --soft HEAD~1

# Undo last commit and unstaged changes
git reset --mixed HEAD~1

# Discard all local changes (dangerous!)
git reset --hard HEAD

# Revert a specific commit (creates new commit)
git revert <commit-id>

# Rename a branch (local)
git branch -m old-name new-name

# Rename a branch (remote)
git push origin :old-name new-name
git push -u origin new-name

# Stash changes (temporarily save without commit)
git stash

# List stashes
git stash list

# Apply last stash
git stash pop

