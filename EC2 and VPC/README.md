# Virtual Private Cloud (VPC)
VPC is a service that lets you launch AWS resources in a logically isolated (secure) virtual network that you define. Services, such as EC2 instances, can be launched into the VPC.

### Benefits of VPC
* **Secure and monitored network connections** - inbound and outbound filtering can be performed at the instance and subnet level.
* **Customisable virtual network** - IP address ranges, subnets, and route tables can be configured to any available gateways.

## EC2
Elastic Compute Cloud provides scalable computing capacity in the AWS cloud. Effectively running virtual computing environments (instances) on the cloud. Some benefits:
* **Scalable** - can scale up or down based on changes in requirements
* **No need for hardware up front** - can develop and deploy applications faster
* **Secure** - has security configurations with security groups

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
