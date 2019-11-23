# Description
This runbook shows you the basic about how to create a repo, add file and raise a PR via bitbucket

# Pre-requisite
* Bitbucket Account
* (Optional) Jira Software Site

# Create Repo Steps
1. Once login to https://bitbucket.org/dashboard/overview, click __Create Repository__
![Alt text](images/bb_create_repo_1.png?raw=true)
2. You will see the following page and please fill in the repo name __MyTestRepo__ and then click __Create repository__
![Alt text](images/bb_create_repo_2.png?raw=true)

3. Now you will see a page like this with a detailed README page
![Alt text](images/bb_create_repo_3.png?raw=true)

4. Congrats! __MyTestRepo__ repo has been created

# (Optional) Link Bitbucket to Jira
1. Since you already have a bitbucket account, you don't need to register again for Jira. Simply pick a site name and signup
![Alt text](images/jira_create_site_1.png?raw=true)

2. Let us skip the most but use a tight schedule for our work
![Alt text](images/jira_onboarding_1.png?raw=true)

3. Jira will suggest you to use scrum board, click __select__
![Alt text](images/jira_onboarding_2.png?raw=true)

4. Create a project by naming it and click create
![Alt text](images/jira_create_project_1.png?raw=true)

5. You will see a backlog; now, type __what needs to be done?__ and hits enter
![Alt text](images/jira_backlog_1.png?raw=true)

6. Once you have created a ticket, click on it will show you the details of the ticket. Let us click __create sprint__ to create a sprint
![Alt text](images/jira_backlog_2.png?raw=true)

7. Drag the ticket to the new sprint and hit __start sprint__
![Alt text](images/jira_backlog_3.png?raw=true)

8. Fill in how long would you like the sprint to be
![Alt text](images/jira_start_sprint_1.png?raw=true)

9. Viola! Now we lands on our sprint board
![Alt text](images/jira_sprint_board_1.png?raw=true)

# Connect your bitbucket to your Jira
1. Click __Settings__ -->  __Jira__ --> __Connect__
![Alt text](images/bb_settings_1.png?raw=true)

2. __Grant Access__ --> __OK__
![Alt text](images/bb_settings_2.png?raw=true)

3. Go back to bitbucket and click __Add file__
![Alt text](images/bb_add_file_1.png?raw=true)

4. Fill in the details and click __commit__
![Alt text](images/bb_add_file_2.png?raw=true)

5. Rename the commit message with the ticket name and the branch name with issue/<ticket_name>+anything
![Alt text](images/bb_add_file_3.png?raw=true)

6. Now the ticket is linked to the title; click the link and see what happens
![Alt text](images/bb_add_file_4.png?raw=true)
