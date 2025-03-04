import boto3

elb_client = boto3.client('elbv2')

response = elb_client.create_target_group(
    Name='BackendTG',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-019080b2921c6a0b1',
    TargetType='instance',
    HealthCheckProtocol='HTTP',
    HealthCheckPort='80',
    HealthCheckPath='/health',
    HealthCheckIntervalSeconds=30,
    HealthCheckTimeoutSeconds=5,
    HealthyThresholdCount=2,
    UnhealthyThresholdCount=2
)

tg_arn = response['TargetGroups'][0]['TargetGroupArn']
print(f"Target Group Created: {tg_arn}")

