#Description
This guide is to help you set up virtualenv and virtualenvwrapper


#Prerequiste

Installed Python3

Installed Pip3

#Steps
```
 pip3 install virtualenv
 pip3 install virtualenvwrapper
```
Open `~/.bashrc` file
```
 subl ~/.bashrc
```
Add these lines
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```

Now, feel free to create new project
```
# First time create a project's virtualenv
mkvirtualenv my_awesome_new_project

# Exit the virtualenv
deactivate

# -----------------------------------------------
# Not the first time entering the virtualenv
workon my_awesome_new_project

# Exit the virtualenv
deactivate

```
