import boto3

elb_client = boto3.client('elbv2')

response = elb_client.create_load_balancer(
    Name='BackendELB',
    Subnets=['subnet-001f1bee6f6f48a70', 'subnet-037aad25cf1334572'],
    SecurityGroups=['sg-03f6debda4a4ed902'],
    Scheme='internet-facing',
    Type='application'
)
lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
print(f"Load Balancer Created: {lb_arn}")
