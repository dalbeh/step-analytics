import time
import boto3
import io

import warnings
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import paramiko



def lambda_handler(event, context):

    secrets_manager = boto3.client('secretsmanager')

    ec2 = boto3.resource('ec2', region_name='us-east-2')
    instance_id = secrets_manager.get_secret_value(SecretId='step-analytics/ec2-instance-id')
    instance = ec2.Instance(instance_id['SecretString'])


    print("----------------------------------------------------")
    print("Instance id - ", instance.id)
    print("Instance public IP - ", instance.public_ip_address)
    print("Instance private IP - ", instance.private_ip_address)
    print("Public dns name - ", instance.public_dns_name)
    print("----------------------------------------------------")


    pemkey = secrets_manager.get_secret_value(SecretId='step-analytics/pem') 

    privkey = paramiko.RSAKey.from_private_key(io.StringIO(pemkey['SecretString']))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        instance.public_dns_name, username='ec2-user', pkey=privkey
    )
    stdin, stdout, stderr = ssh.exec_command(
        'cd / && sudo aws s3 cp s3://deploy-code-sentiment-analysis/ /app/sentiment-analysis --recursive')
    stdin.flush()
    data = stdout.read().splitlines()
    for line in data:
        print(line)

    ssh.close()  