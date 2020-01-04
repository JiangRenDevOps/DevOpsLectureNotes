# Description

This is to demo how to integrate Jenkins with a Github Orgnisation

# Pre-requisite

- Github Account
- Jenkins Server

# Task

## Step #1: New an item in Jenkins.
![Alt text](images/integrate-with-github-org-01.png?raw=true)


## Step #2: Enter item name.
Preferrablelly with your Github Organisation name.
![Alt text](images/integrate-with-github-org-02.png?raw=true)


## Step #3: Choose to add credential
![Alt text](images/integrate-with-github-org-03.png?raw=true)


## Step #4: Add your Github username/password
![Alt text](images/integrate-with-github-org-04.png?raw=true)
Note: the plugin doesn't support token yet.


## Step #5: Select the credential you have just added
![Alt text](images/integrate-with-github-org-05.png?raw=true)


## Step #6: Input your Github Organisation name to the "Owner" field, review other settings and save.

![Alt text](images/integrate-with-github-org-06.png?raw=true)


## Step #7: You should see this screen after the integration.
![Alt text](images/integrate-with-github-org-07.png?raw=true)


## Step #8: In github organisation, you should see a webhook created automatically.
This webhook will notify Jenkins when there is a push, PR or repository created.
![Alt text](images/integrate-with-github-org-08.png?raw=true)


## Step #9: Fork a repo with Jenkinsfile to your organisation
Fork https://github.com/davisliu11/hello-Jenkinsfile


## Step #10: In Jenkins, you should see a job is created automatically
![Alt text](images/integrate-with-github-org-10.png?raw=true)


## Step #11: Create a new branch
![Alt text](images/integrate-with-github-org-11.png?raw=true)


## Step #12: In Jenkins, you should see a new job is created automatically
![Alt text](images/integrate-with-github-org-12.png?raw=true)


## Step #13: Modify README.md or add a file to the repo.
![Alt text](images/integrate-with-github-org-13.png?raw=true)


## Step #14: In Jenkins, you should see a new build is triggerred
![Alt text](images/integrate-with-github-org-14.png?raw=true)


## Step #15: Create a PR
![Alt text](images/integrate-with-github-org-15.png?raw=true)


## Step #16: In Jenkins, you should see a new build is triggerred
![Alt text](images/integrate-with-github-org-16.png?raw=true)


## Step #17: Merge the PR
![Alt text](images/integrate-with-github-org-17.png?raw=true)


## Step #18: In Jenkins, you should see the PR build is going to be deleted
![Alt text](images/integrate-with-github-org-18.png?raw=true)


## Step #19: In Jenkins, you should see another build in master branch
![Alt text](images/integrate-with-github-org-19.png?raw=true)


## Step #20: Open "Blue Ocean"
![Alt text](images/integrate-with-github-org-20.png?raw=true)


## Step #21: You should see a new UI experience
![Alt text](images/integrate-with-github-org-21.png?raw=true)
