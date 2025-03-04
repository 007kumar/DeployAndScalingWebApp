import boto3

elb_client = boto3.client('elbv2')

response = elb_client.create_load_balancer(
    Name='BackendELB',
    Subnets=['subnet-xxxxxxxx'],
    SecurityGroups=['sg-xxxxxxxx'],
    Scheme='internet-facing',
    Type='application'
)
lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load Balancer Created: {lb_arn}")

# Create a Target Group
response = elb_client.create_target_group(
    Name='BackendTG',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-xxxxxxxx'
)
tg_arn = response['TargetGroups'][0]['TargetGroupArn']
print(f"Target Group Created: {tg_arn}")

# Register ASG with Target Group
asg_client = boto3.client('autoscaling')

asg_client.attach_load_balancer_target_groups(
    AutoScalingGroupName='BackendASG',
    TargetGroupARNs=[tg_arn]
)
print("ASG attached to Load Balancer Target Group")

