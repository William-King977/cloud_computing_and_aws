# Cloud Computing and AWS
## What is cloud computing and why should we use it?
Cloud computing is the delivery of computing services (servers, storage, databases, networking etc.) over the Internet (the cloud) to offer faster innovation, flexible resources, and economies of scale. Cloud services are normally pay-as-you-go, which helps lower operating costs, run the infrastructure more efficiently and can scale as the business changes. The cloud is a secure storage that protects your data from potential security threats as well as being reliable for disaster recovery.

## What is Amazon Web Services?
Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform, offering 200 fully features services from data centres globally. Companies (from start-ups to large enterprises and leading government agencies, so it's flexible) use AWS to lower costs, become more agile, and innovate faster.

### Why do Companies use AWS?
Compared to other cloud services providers:
* **Most functionality** - AWS provides more services, and more features within those services, than any other cloud provider. This makes it faster, easier and more cost effective to move existing applications to the cloud.
* **Most secure** - AWS is architected to be the most flexible and secure cloud computing environment. Their core infrastructure is built to satisfy the security requirements for the military, global banks, and other high-sensitivity organisations.

## Cloud types
* **On premises/Private cloud (local machine etc.)** - everything is stored locally. Companies on premise are responsible for the security of the data. If you lose the data, it's gone forever.
* **Hybrid cloud** - Bridges the private cloud and public cloud. Sensitive information is kept in private cloud, everything else is stored in public cloud. Used by banks etc.

## Cloud scaling types
* **Autoscaling** - servers run based on the number of users. They scale up as more users use the service and scale down as less users use it.
* **Horizontal (Up)** - increase the size of the servers, or buying a larger server to accommodate the number of users.
* **Vertical (Out)** - increase number of servers, not good for maintenance costs.

## Architectures
### Monolithic
When all of the servers/instances are run from a single machine. Components of the program are interconnected and dependent on each other. If an update is made, the whole application has to re-run. Despite this, it's simpler to test than modular approaches (microservices), due to having fewer components as well as being simple to deploy. For example, running all vagrant virtual machines from a single Vagrantfile.

### Two tier
When the presentation layer (interface) runs on a client and a data layer/structure (database) gets stored on a server. Basically, when each instance is run on a separate machine. It separates these two components into different locations. Having separate layers can improve performance and scalability.

## EC2
Elastic Compute Cloud provides scalable computing capacity in the AWS cloud. Effectively running virtual computing environments (instances) on the cloud. Some benefits:
* **Scalable** - can scale up or down based on changes in requirements
* **No need for hardware up front** - can develop and deploy applications faster
* **Secure** - has security configurations with security groups

## Virtual Private Cloud (VPC)
VPC is a service that lets you launch AWS resources in a logically isolated (secure) virtual network that you define. Services, such as EC2 instances, can be launched into the VPC.

### Benefits of VPC
* **Secure and monitored network connections** - inbound and outbound filtering can be performed at the instance and subnet level.
* **Customisable virtual network** - IP address ranges, subnets, and route tables can be configured to any available gateways.

## Subnets
A subnet is a network inside a network. They make networks more efficient as network traffic can travel a shorter distance without passing through unnecessary routers to reach its destination. E.g. a subnet for teachers and another one for students.
* Public subnets have their traffic routed to an internet gateway. 
* Private subnets are not routed to an internet gateway, but its traffic is routed to a virtual private gateway for a Site-to-Site VPN connection (known as VPN-only subnet). Limits access from the internet.

## Internet gateway
An internet gateway is a horizontally scaled and highly available VPC component that allows communication between your VPC (and its components) and the internet.

## Route tables
A route table contains a set of rules, called routes, that are used to determine where network traffic from your subnet or gateway is directed.

## Security Group
Security group acts as a firewall that controls the traffic for your instance (server) on the machine. Other points:
* As mentioned, it operates at an instance level
* It's stateful - returning traffic is automatically allowed, regardless of the rules
* All rules are evaluated before deciding to allow traffic
* Supports allow rules only

## Network Access Control List (NACL)
A network access control list is an additional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. Other points:
* It operates at a subnet level - the rules apply to all the instances in the subnet (in addition to the SG rules applied to those instances).
* It's stateless - returning traffic must follow the rules
* Rules are processed in order, starting with the lowest numbered rule, when deciding to allow traffic
* Supports both allow and deny rules

## Ephemeral/Dynamic Ports
* Shortly lived ports, 'lives' for the duration of their use
* Automatically allocated based on the demand
* Range from 1024-65535

## Bastion Servers
A bastion server is a special purpose instance (EC2) designed to be the primary access point from the internet and acts as a proxy to your other EC2 instances (e.g. the database). Some benefits include:
* Provides access to a private network from an external network
* Acts as a 'jump server' that allows you to SSH into EC2 instances in private subnets
* Acts as a (secure) bridge between the private instances and the internet

## AWS VPC configuration with Subnets
### Step 1: Create the VPC
1. Click `Your VPCs`, then `Create VPC`
2. Change the VPC nametag to `Eng84_william_vpc`
3. Change IPv4 CIDR block to `0.0.0.0/16` where the first 2 numbers are unique e.g. `59.84.0.0/16`
4. Click `Create VPC`

### Step 2: Create the Internet Gateway and Attach to VPC
This needs to be done, so that your VPC can connect to the internet.
1. Click `Internet Gateways`, then `Create internet gateway`
2. Change the nametag to `Eng84_william_ig`
3. Click `Create Internet Gatway`
4. Click `Actions`, then `Attach to VPC`
5. Select the VPC you created, then click `Attach internet gateway`

### Step 3: Create the Subnets
1. Click `Subnets`, then `Create subnet`
2. Select your VPC
3. Add the Subnet name as `Eng84_william_public_subnet`
4. Availability zone to `1c`, but `No preference` is fine
5. IPv4 CIDR block to `59.84.1.0/24` as per the VPC IP
6. Click `Create Subnet`
7. Repeat the above steps for the Private Subnet, but with the applicable name and the third number of the IPv4 CIDR block must be unique.

### Step 4: Setting up Routing Tables
First, we'll find our route table and link the public subnet into it.
1. Go on `Routing Tables`
2. Click on the unnamed route tables until you find the one with your VPC
3. Rename it to `Eng84_william_public_rt`
4. With the route table selected, select the `Routes` tab
5. Click `Edit routes` and do the following:
   * Set the destination to `0.0.0.0/0`
   * Set the target to `Internet Gateway`, then select your internet gateway
   * Save the configurations
6. Select the `Subnet Associations` tab to link the Public Subnet
7. Click `Edit subnet associations` and do the following:
   * Select the public subnet you have created
   * Click `Save` 

Next, we'll create a separate route table for the private subnet.
1. Click `Create route table`, then do the following:
   * Set the Name tag to `Eng84_william_private_rt`
   * Select your VPC
   * Click `Create`
   * NOTE: This route table will not be connected to the internet.
2. With the new route table selected, select the `Subnet Associations` tab
3. Click `Edit subnet associations` and do the following:
   * Select the PRIVATE subnet you have created
   * Click `Save`

Both route tables are now set up!

### Step 5: Creating the EC2 instances
#### NOTE: Skip this step if you have created AMIs already.
First, we'll create the instance for the app.
1. Click `Launch Instance`
2. Choose `Ubuntu Server 16.04 LTS (HVM), SSD Volume Type` as the Amazon Machine Image (AMI)
3. Choose `t2.micro` as the instance type (the default)
4. On Configure Instance Details:
   * Change the VPC to your VPC
   * Change subnet to your public subnet
   * Enable `Auto-assign Public IP` for the app
5. Skip `Add Storage` (keep defaults)
6. Add a tag with the `Key` as `Name` and the value as shown below:
   * `Eng84_name_appType`
   * `Eng84_william_db`, `Eng84_william_app`, etc.
7. Security group name should be `Eng84_william_app_sg` for the app
   * For the SSH rule:
     * Set to Port 22
     * Source: My IP
     * Description: My IP
   * Add another rule for HTTP:
     * Set to Port 80
     * Custom Source: `0.0.0.0/0, ::/0` (default)
8. Review and Launch
9. Select the existing DevOpsStudent key:pair option for SSH

Now, we'll create an instance for the database.
1. Repeat steps 1 to 3 from the above
2. Repeat step 4, but change the subnet to your private one instead.
3. Repeat steps 5 and 6. Adjust the name applicable for step 6.
4. Repeat step 7, but replace the HTTP rule for All traffic:
   * Custom Source: `the public security group`
   * This only allows the app to access the database
5. Repeat steps 8 and 9 as normal

### Step 6: Connecting the EC2 instances
Let's start with the app and import the files.
1. Go to the directory before the app folder.
2. Execute this command: `scp -i ~/.ssh/DevOpsStudent.pem -r app/ ubuntu@app_ec2_public_ip:~/app/`
3. Change to the `~/.ssh`
4. Click `Connect`, then run the SSH command given from the `SSH client` instructions 
5. If you are asked for a finger print, type yes.
6. Create the provisions file and copy, paste the contents. Adjust the directories as needed (hint: use `pwd`).
7. Run the provision file using `./provision_file_name.sh`. Change permissions with `chmod` if needed.
8. Run the environment variable command, so the app can connect to the database: `echo "export DB_HOST=mongodb://db_private_ip:27017/posts" >> ~/.bashrc`
9. Do the following if you want to apply the reverse proxy manually:
   * Execute: `sudo nano /etc/nginx/sites-available/default`
   * Replace it all with the code below:
     ```
     server {
         listen 80;

         server_name _;

         location / {
             proxy_pass http://localhost:3000;
             proxy_http_version 1.1;
             proxy_set_header Upgrade $http_upgrade;
             proxy_set_header Connection 'upgrade';
             proxy_set_header Host $host;
             proxy_cache_bypass $http_upgrade;
         }
     }
     ```

Next, we'll connect to the database instance.
1. The database is not connected to the internet, so a proxy SSH is required.
2. First, we need the Public IPv4 address of our app.
3. Next, we need the Private IPv4 address of our database.
2. Execute this command to SSH into the database: `ssh -i ~/.ssh/DevOpsStudent.pem -o ProxyCommand="ssh -i ~/.ssh/DevOpsStudent.pem -W %h:%p ubuntu@app_public_ip" ubuntu@db_private_ip`

### Step 7: Updating the database instance
First, modify the security group.
1. Go on `Security`, then click the security group
2. Click `Edit inbound rules`
3. Add a HTTP rule and set the Source to `Anywhere`

Next, go to the VPC to modify the route table subnet associations.
1. Click `Route Tables`
2. Select your public route table
3. With your public route table selected, click the `Subnet Associations` tab
4. Edit the subnet associations, then select the private subnet.

The database instance is now accessible to the internet.
1. SSH into the database instance just like your app instance.
2. Create the provisions file and copy, paste the contents.
3. Run the provisions file
4. With the operations complete, remove the private subnet from the public route table.
5. Remove the HTTP rule from the security group.
7. Reconnect (SSH) into both instances.
8. NOTE: for the app, one will need to run `seed.js`

### Step 8: Creating a Public NACL for the VPC
Ensure that you are in the VPC section (not EC2).
1. Go to the `Network ACLs` section under `Security`
2. Click `Create network ACL`
3. Add the appropriate name and allocate the VPC, then create it

Next, lets set the inbound rules for the NACL.
1. With the NACL selected, click on the `Inbound rules` tab
2. Click `Edit inbound rules`
3. Remove the default rule and add the following rules:
   * 100: HTTP (80) with source `0.0.0.0/0` - this allows external HTTP traffic to enter the network
   * 110: SSH (22) with source your_IP_address/32 - allows SSH connections to the VPC
   * 120: Custom TCP with Port range `1024-65535` and source `0.0.0.0/0` - allows inbound return traffic from hosts on the internet that are responding to requests originating in the subnet
   * NOTE: All rules should be `Allow` rules

Now, lets set the outbound rules.
1. Select the `Outbound rules` tab
2. Click `Edit outbound rules`
3. There should be the following rules:
   * 100: HTTP (80) with source `0.0.0.0/0`
   * 110: Custom TCP with source private subnet CIDR block (`59.84.2.0/32` in this case) and port 27017 for outbound access to our MongoDB server in the private subnet
   * 120: Custom TCP with port `1024-65535` and source `0.0.0.0/0` -  allow short lived ports between 1024-65535
   * NOTE: All rules should be `Allow` rules

### Step 9: Creating a Private NACL for the VPC
Create the private NACL and lets set the inbound rules for the NACL.
1. With the NACL selected, click on the `Inbound rules` tab
2. Click `Edit inbound rules`
3. Remove the default rule and add the following rules:
   * 100: Custom TCP with source public subnet CIDR block (`59.84.1.0/32` in this case) - this allows the app subnet to access the database subnet
   * 110: SSH (22) with source your_IP_address/32 - allows SSH connections to the VPC
   * NOTE: All rules should be `Allow` rules

Now, lets set the outbound rules.
1. Select the `Outbound rules` tab
2. Click `Edit outbound rules`
3. There should be the following rules:
   * 100: All traffic with source `0.0.0.0/0` - allow all the traffic out
   * NOTE: All rules should be `Allow` rules

### Step 10: Assigning Subnets to NACLs
Finally, lets assign the subnets to the NACL.
1. Select the `Subnet associations` tab
2. Select the `Edit subnet associations` tab
3. Select the public/private subnet, depending on the NACL

## Creating Instance AMIs and New Instances (from those AMIs)
### Step 1: Create AMIs of the Instances
For each instance, do the following:
1. Select the instance
2. Select Action
3. Select Image and templates, create image
4. Enter name as instance with `_ami`
5. Click Create image

### Step 2: Create New Instances of the AMIs
For each instance, follow the steps from `Step 5: Creating the EC2 instances` in the `AWS VPC configuration with Subnets` instructions, but change the following:
1. When selecting your AMI, click on `My AMIs` on the side tab
2. Search for your AMI and select it
3. In the Security Group step, select the ones specific to your VPC IF you created them separately. Otherwise, create new ones.
4. NOTE: creating instances with these AMIs will have everything installed (and running, like MongoDB)

### Step 3: Connecting Everything
There are a few things to change in the APP to get these AMI instances to work:
1. Change the private database IP in the environment variable (in `~/.bashrc`) to the private database of the AMI.
2. Exit and re-SSH into the app instance to 'save' the changes
3. NOT SURE, but you may have to re-run `seed.js`
4. Now, everything should work when running `node app.js`!

### TOP TIP(s): 
* **First iteration:** When you spin up the AMIs, do it in the default VPC and subnets first.
* **Second iteration:** Spin up the AMIs in your own VPC and subnet

## AWS VPC Diagram
Below is a diagram of configuring a two tier architecture in a AWS VPC:

![image](https://user-images.githubusercontent.com/44005332/116392059-e2ef9b80-a817-11eb-8b14-c21d7aeddd8d.png)

### Security Group Inbound Rules
Public:
* 

Private:
*

### Security Group Outbound Rules
Public:
* 

Private:
*

### NACL Rules
Public:
*

Private:

### Route Table Rules


## Creating a Bastion Server
Even though we got *everything* working, we cannot SSH into our database instance because its in a private subnet. To solve this, we need to create a bastion server, also known as a jump box, so that we can log in to the bastion and then from there, access our database instance to perform updates.

Follow the following to create a bastion server:
1. Create a public subnet for the bastion server
2. Create a Linux instance that acts as the bastion server
   * Select your VPC and set the bastion subnet
   * Set the Security Group rule as SSH with source `My IP`
3. Change the following for the app and database instances:
   * In Security Group inbound rules, add SSH with source bastion security group (ID)
   * Add bastion subnet into the public route table (from the Subnet page)

Now, we need to make some configurations before the bastion can SSH into our app and database. Do the following on your host machine:
1. On the `~/.ssh` directory, execute `ssh-agent bash`
2. Execute `ssh-add pem_file`
3. Now, execute `ssh -A ubuntu@bastion_public_ip` to SSH into the bastion server (instance). NOTE: using this method of SSH will allow you to SSH into the app and database. The *regular* SSH method won't allow this.
4. NOTE: the above needs to be done each time you open a new GitBash/Terminal window.

Inside the bastion server, we need to add a `config` file in the `~/.ssh` directory:
1. Execute `cd ~/.ssh`
2. Execute `nano config`
3. Copy and paste the following contents and adjust where applicable:
   ```
   Host db
     Hostname db_private_ip
     User ubuntu
     Port 22
   Host app
     Hostname app_private_ip
     User ubuntu
     Port 22
   ```
4. Now, you can SSH into the app and database with `ssh app` and `ssh db` respectively.
5. NOTE: you *may* have to `exit` on the host machine to stop some additional processes.

