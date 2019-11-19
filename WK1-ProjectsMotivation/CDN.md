# Description

This is the hands-on for the Jiangren CDN project.

# Pre-requisite

- AWS Account

# Task 1: Create a CDN

1. Login to your AWS Cloudfront console: https://console.aws.amazon.com/cloudfront/home

2. Click "Create Distribution" button.

3. Click "Get Started" in the "Web" section.

4. In "Origin Domain name", input "jiangren.com.au"

5. In "HTTPS Only", select "Origin Protocol Policy"

6. In "Object Caching", select "Customize"

7. In "Minimum TTL", input "86400" which stands for one day

8. In "Compress Objects Automatically", select "yes"

9. Click "Create Distribution" button in the bottom right to create a Cloudfront distribution

10. Wait util the distribution status is "Deployed" (it takes about 10 minutes)

11. Open the domain name "e.g. xxx.cloudfront.net" to confirm you can get a jiangren website

![Alt text](images/CDN1.png?raw=true)
![Alt text](images/CDN2.png?raw=true)


# Task 2: Test the speed of jiangren.com.au website across 25 locations in the world

1. Open https://www.dotcom-tools.com/website-speed-test.aspx in 3 browser tabs

2. Test "jiangren.com.au" in the first browser tabs

3. Wait for 10 seconds

4. Test "jiangren.com.au" in the second browser tabs

5. Wait for 10 seconds

6. Test "jiangren.com.au" in the third browser tabs

7. Wait until the test finishes and see if there is any trend among these three tests

# Task 3: Test the speed of the CDN website across 25 locations in the world

1. Open https://www.dotcom-tools.com/website-speed-test.aspx in 3 browser tabs.

2. Test your CDN site "e.g. xxx.cloudfront.net" in the first browser tabs

3. Wait for 10 seconds

4. Test your CDN site "e.g. xxx.cloudfront.net" in the second browser tabs

5. Wait for 10 seconds

6. Test your CDN site "e.g. xxx.cloudfront.net" in the third browser tabs

7. Wait until the test finishes and see if there is any trend among these three tests

# Task 4: Explore the "Reports & analytics" in Cloudfront console.
![Alt text](images/CDN3.png?raw=true)
Feel free to explore other menus in the "Reports & analytics" area.
