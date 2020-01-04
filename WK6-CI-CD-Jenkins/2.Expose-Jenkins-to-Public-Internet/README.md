# Description

This is to demo how to expose a server inside the firewall to public internet via ngrok

# Pre-requisite

- A server to expose (Jenkins in this example)


# Steps
## Step #1: Login to ngrok via Github or Google
https://dashboard.ngrok.com/login

![Alt text](images/expose-jenkins-to-public-internet-01.png?raw=true)


## Step #2: Follow docs to install ngrok client and setup authtoken
```
ngrok authtoken xxx
```
![Alt text](images/expose-jenkins-to-public-internet-02.png?raw=true)


## Step #3: Expose Jenkins to public internet
```
ngrok http 80
```
![Alt text](images/expose-jenkins-to-public-internet-03.png?raw=true)


## Step #4: You should be able to access Jenkins in the public internet
![Alt text](images/expose-jenkins-to-public-internet-04.png?raw=true)


## Step #5: Change "Jenkins URL" to the public URL.
![Alt text](images/expose-jenkins-to-public-internet-05.png?raw=true)
