#What’s a version control system?
A version control system, or VCS, tracks the history of changes as people and teams collaborate on projects together. As the project evolves, teams can run tests, fix bugs, and contribute new code with the confidence that any version can be recovered at any time. Developers can review project history to find out:
 
*  Which changes were made?
*  Who made the changes?
*  When were the changes made?
*  Why were changes needed?

#What’s a distributed version control system?
Git is an example of a __distributed version control system (DVCS)__ commonly used for open source and commercial software development. DVCSs allow full access to every file, branch, and iteration of a project, and allows every user access to a full and self-contained history of all changes. Unlike once popular centralized version control systems, DVCSs like Git don’t need a constant connection to a central repository. Developers can work anywhere and collaborate asynchronously from any time zone.

Without version control, team members are subject to redundant tasks, slower timelines, and multiple copies of a single project. To eliminate unnecessary work, Git and other VCSs give each contributor a unified and consistent view of a project, surfacing work that’s already in progress. Seeing a transparent history of changes, who made them, and how they contribute to the development of a project helps team members stay aligned while working independently.

#What’s a repository?
A repository, or Git project, encompasses the entire collection of files and folders associated with a project, along with each file’s revision history. The file history appears as snapshots in time called commits, and the commits exist as a linked-list relationship, and can be organized into multiple lines of development called branches. Because Git is a DVCS, repositories are self-contained units and anyone who owns a copy of the repository can access the entire codebase and its history. Using the command line or other ease-of-use interfaces, a git repository also allows for: interaction with the history, cloning, creating branches, committing, merging, comparing changes across versions of code, and more.

Working in repositories keeps development projects organized and protected. Developers are encouraged to fix bugs, or create fresh features, without fear of derailing mainline development efforts. Git facilitates this through the use of topic branches: lightweight pointers to commits in history that can be easily created and deprecated when no longer needed.

Through platforms like GitHub, Git also provides more opportunities for project transparency and collaboration. Public repositories help teams work together to build the best possible final product.


#What are the most popular cloud git repositories?

https://github.com/

https://bitbucket.org/

#Basic Git commands
To use Git, developers use specific commands to copy, create, change, and combine code. These commands can be executed directly from the command line or by using an application like GitHub Desktop or Git Kraken. Here are some common commands for using Git:

* `git init` initializes a brand new Git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.

* `git clone` creates a local copy of a project that already exists remotely. The clone includes all the project’s files, history, and branches.

* `git add` stages a change. Git tracks changes to a developer’s codebase, but it’s necessary to stage and take a snapshot of the changes to include them in the project’s history. This command performs staging, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project’s history. Staging and committing separately gives developers complete control over the history of their project without changing how they code and work.

* `git commit` saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that’s been staged with git add will become a part of the snapshot with git commit.

* `git status` shows the status of changes as untracked, modified, or staged.

* `git branch` shows the branches being worked on locally.

* `git merge` merges lines of development together. This command is typically used to combine changes made on two distinct branches. For example, a developer would merge when they want to combine changes from a feature branch into the master branch for deployment.

* `git pull` updates the local line of development with updates from its remote counterpart. Developers use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment.

* `git push` updates the remote repository with any commits made locally to a branch.


# Typical Dev Procedure

## Branch out and commit your changes

i) Let us suppose master is our main branch (we also have staging branch and prod branch) and we would like to make some changes on the master branch.
```
# check current status of the git folder
git status

# check current branch
git branch

# (optional) stash any uncommited changes
git stash

# pull the latest updates from remote
git pull
```

iia) If you have created the branch via Jira ticket, checkout to that branch
```
# branch should be named under the following naming convention 
# issue/<jira_ticket_shorthand>-<title> or 
# bugfix/<jira_ticket_shorthand>-<title> or 
# feature/<jira_ticket_shorthand>-<title>

git checkout <branch_name> 
```

iib) Or simply create a new one with `-b` on your local git and checkout to that branch
```
git checkout -b <branch_name>
```

iii) Now, code, CRUD files 

iv) Commit to your local git client
```
# check current status of the git folder
git status

# add all the files
git add -A

# (Alternative) only add the files that already exist in the remote server  
git add -u 

# (Alternative) if you need to remove a code
git rm <file_name>

# add the commit message
git commit -m "<jira_ticket_shorthand> <a concise summary>"

# push the local change to the remote server
git push

# 
git push origin <branch_name>
# A pull request link will pop up
```
## Check History and diff

```
# use this command to checkout the author, date and summary of others commit
git log

# use this command to see what has been changed against the master branch
git diff

```

## Resovle conflicts
Pull the most recent version of the repository from Bitbucket.
```
$ git pull
```

Checkout the source branch.

```
$ git checkout <feature_branch>
```

Pull the destination branch into the source branch. At this point, pulling the destination will try to merge it with the source and reveal all the conflicts.
```
$ git pull origin <destination_branch>
```
For example, if your destination branch is master, the result will look something like this:
```
computer:my-repository emmap$ git pull origin master
 * branch            master     -> FETCH_HEAD
Auto-merging team_contact_info.txt
CONFLICT (content): Merge conflict in team_contact_info.txt
Automatic merge failed; fix conflicts and then commit the result.
```
![Alt text](images/mergeconflict_git_branches.png?raw=true)
* A. The beginning of the change in the HEAD branch. In this case, HEAD represents the active branch into which you're merging.
* B. The end of the change in the active branch and the beginning of the change in the non-active branch.
* C. The end of the change in the non-active branch.


Fix the file, add and commit the change.
```
$ git add <filename>
$ git commit -m'commit message'
```
Push the change to the remote.
```
git push origin <feature_branch>
```

## Visualisation
http://git-school.github.io/visualizing-git/


## Manage multiple git accounts on your local machine
Under each git repo, you can set the local git account by
```
git config user.name <User Name>
git config user.email <User Email>
```


# Interview Questions:
## Difference between git fetch and git pull?
* `git fetch` is the command that tells your local git to retrieve the latest meta-data info from the original (yet doesn't do any file transfering. It's more like just checking to see if there are any changes available).
* `git pull` on the other hand does that AND brings (copy) those changes from the remote repository.

## What is the benefits of fast forward merge?

## What does rebase do?