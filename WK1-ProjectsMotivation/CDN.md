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

7. In "Minimum TTL", input "3600" which stands for one hour

8. In "Compress Objects Automatically", select "yes"

9. Click "Create Distribution" button in the bottom right to create a Cloudfront distribution

10. Wait util the distribution status is "Deployed" (it takes about 10 minutes)

11. Open the domain name "e.g. xxx.cloudfront.net" to confirm you can get a jiangren website. 

# Task 2: Test the speed of jiangren.com.au website

1. Open https://www.dotcom-tools.com/website-speed-test.aspx in 3 browser tabs.

2. Test "jiangren.com.au" in all of the 3 browser tabs. It will run test across 25 locations in the world.

# Task 3: Test the speed of the CDN website

1. Open https://www.dotcom-tools.com/website-speed-test.aspx in 3 browser tabs.

2. Test your CDN site "e.g. xxx.cloudfront.net" in all of the 3 browser tabs. It will run test across 25 locations in the world.

