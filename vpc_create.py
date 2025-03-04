import boto3

ec2 = boto3.client('ec2')

def create_vpc():
    response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = response['Vpc']['VpcId']
    print(f'VPC Created: {vpc_id}')
    return vpc_id

def create_subnet(vpc_id):
    response = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
    subnet_id = response['Subnet']['SubnetId']
    print(f'Subnet Created: {subnet_id}')
    return subnet_id

def create_security_group(vpc_id):
    response = ec2.create_security_group(
        GroupName='ShivBatch8SG',
        Description='Allow SSH and HTTP',
        VpcId=vpc_id
    )
    sg_id = response['GroupId']
    print(f'Security Group Created: {sg_id}')
    
    # Allow SSH and HTTP traffic
    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ]
    )
    return sg_id

if __name__ == "__main__":
    vpc_id = create_vpc()
    subnet_id = create_subnet(vpc_id)
    sg_id = create_security_group(vpc_id)

