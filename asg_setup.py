import boto3

client = boto3.client('autoscaling')

def create_asg():
    response = client.create_auto_scaling_group(
        AutoScalingGroupName='ShivBatch8ASG',
        LaunchTemplate={'BackendLaunchTemplate'},
        MinSize=2,
        MaxSize=5,
        DesiredCapacity=3,
        VPCZoneIdentifier='subnet-001f1bee6f6f48a70',
        TargetGroupARNs=['arn:aws:elasticloadbalancing:us-east-1:975050024946:targetgroup/batch8shiv/85343662cfe8acf7']
    )
    print('Auto Scaling Group Created')
    
if __name__ == "__main__":
    create_asg()

