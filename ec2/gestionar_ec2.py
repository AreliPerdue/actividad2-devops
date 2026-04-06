import boto3

def listar_instancias():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | Estado: {instance['State']['Name']}")

if __name__ == "__main__":
    listar_instancias()
