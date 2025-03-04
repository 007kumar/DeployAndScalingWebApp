import boto3
import base64

ec2_client = boto3.client('ec2')

# Define the user data script
user_data_script = """#!/bin/bash
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker

docker network create --driver bridge backend-network

# Authenticate Docker with AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 975050024946.dkr.ecr.us-east-1.amazonaws.com

# Pull the latest backend image from ECR
docker pull 975050024946.dkr.ecr.us-east-1.amazonaws.com/mern-backend:latest

# Run the container, exposing it on port 80
docker run -d -p 80:5000 --name backend-app 975050024946.dkr.ecr.us-east-1.amazonaws.com/mern-backend:latest
"""


user_data_encoded = base64.b64encode(user_data_script.encode("utf-8")).decode("utf-8")


response = ec2_client.create_launch_template(
    LaunchTemplateName='BackendShivkumar',
    LaunchTemplateData={
        'ImageId': 'ami-04b4f1a9cf54c11d0',  # Ensure this AMI is valid
        'InstanceType': 't2.micro',
        'KeyName': 'jenki',  # Ensure this key pair exists in AWS
        'SecurityGroupIds': ['sg-03f6debda4a4ed902'],  # Ensure this Security Group exists
        'IamInstanceProfile': {'Name': 'EC2FullAccessShivkumar'},  # Ensure the IAM role is attached
        'UserData': user_data_encoded  # Base64 encoded UserData
    }
)

print("🚀 Launch Template Created Successfully!")
