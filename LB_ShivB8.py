import boto3

elb_client = boto3.client('elbv2')

response = elb_client.create_load_balancer(
    Name="ShivB8-ELB",
    Subnets=[
        "subnet-0dbb43b345d9f2093",
        "subnet-001f1bee6f6f48a70"
    ],
    SecurityGroups=["sg-03f6debda4a4ed902"],
    Scheme="internet-facing",
    Type="application",
    IpAddressType="ipv4"
)

print("Load Balancer Created:", response)

