# Description

This is to guide how to apply and set up a DNS name for a Cloudfront distribution.

# Pre-requisite

AWS Account


# Task 1: Create a route53 hosted zone

1. Login to AWS Route53 Console: https://console.aws.amazon.com/route53/home?region=us-east-1#hosted-zones:
2. Click "Created Hosted Zone" button, input your domain name ("your_name.jiangren.mooo.com") and then click "Create" button.
![Alt text](images/DNS1.png?raw=true)
You can find a hosted zone created.
![Alt text](images/DNS2.png?raw=true)
3. Click "Create Record Set" to create a DNS name. In the right panel, select "Alias" as "Yes", then select your Cloudfront distribution from the "Alias Target". Click "Create" button to create a DNS record.
![Alt text](images/DNS3.png?raw=true)

# Task 2: Add CNAME with Certification
1. Go back to AWS Cloudfront console: https://console.aws.amazon.com/cloudfront/home and select your Distribution.
![Alt text](images/DNS4_1.png?raw=true)
2. Click "Edit" button to continue edit.
![Alt text](images/DNS4.png?raw=true)
3. In the "Alternative Domain Names (CNAMEs)", input your Domain name. Then, click "Request or import a Certificate with ACM".
![Alt text](images/DNS5.png?raw=true)
4. Input your Domain Name.
![Alt text](images/DNS6.png?raw=true)
5. Select "DNS validation".
![Alt text](images/DNS7.png?raw=true)
6. Review the change.
![Alt text](images/DNS8.png?raw=true)
7. Expand your domain and then click "Create record in Route 53"
![Alt text](images/DNS9.png?raw=true)
You should get a successful result.
![Alt text](images/DNS11.png?raw=true)
8. After a minute, you will find your certificate is issued.
![Alt text](images/DNS12.png?raw=true)
9. Go back to the CDN distribution edit page and select the certification that you just created.
![Alt text](images/DNS13.png?raw=true)
10. Click "Yes, Edit" in the bottom right to save it. It should take 10 minutes or so to apply cloudfront changes to all the edge servers.
![Alt text](images/DNS14.png?raw=true)
# Step 3: Set up DNS Delegation
DNS and CDN are configured. The final step is to give your NS record to teacher via SSH so your DNS delegation will be set up.
1. Go back to Route53 console, copy your NS record info and save it to a file. 
![Alt text](images/DNS15.png?raw=true)
2. Upload the file to the server via: `scp your_name.jiangren.mooo.com ec2-user@54.206.36.48:/home/ec2-user`
3. Validate your NS record is updated via `dig NS your_name.jiangren.mooo.com`.
4. Now, you should be able to view the site.
![Alt text](images/DNS16.png?raw=true)