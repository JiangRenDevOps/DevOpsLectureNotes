# Description

This is a brief guideline on setting up CI/CD for our CMS project.

# Tasks

## Task #1: Run a Jenkins in Kubernetes Cluster

## Task #2: Add a service account to jenkins
So Jenkins will have permission to create pods dynamically as Jenkins slave.
```
kubectl apply -f https://raw.githubusercontent.com/jenkinsci/kubernetes-plugin/master/src/main/kubernetes/service-account.yml
```

Add "serviceAccountName: jenkins" to Jenkins in workloads.
![Alt text](images/CI_CD_CMS_01.png?raw=true)

## Task #3: Install Kubernetes plugin and configure Kubernetes in Jenkins
```
jenkins-1-jenkins-agents-connector:50000
```
![Alt text](images/CI_CD_CMS_02.png?raw=true)

## Task #4: Configure Credentials for Jenkins pipeline
As required in this file: https://github.com/davisliu11/jrcms/blob/master/Jenkinsfile

## Task #5: Create Elastic Beanstalk environments in AWS
You will need to update the `Jenkinsfile` and files under `deployment` folder accordingly.
![Alt text](images/CI_CD_CMS_03.png?raw=true)

## Task #6: Setup Github integration
https://github.com/JiangRenDevOps/DevOpsLectureNotes/tree/master/WK6-CI-CD-Jenkins/4.Integrate-with-Github-Org

## Task #7: Play around
Make changes and test the auto deployment
