import boto3

def listar_instancias():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | Estado: {instance['State']['Name']}")

if __name__ == "__main__":
    import sys

if len(sys.argv) > 2 and sys.argv[1] == "start":
    iniciar_instancia(sys.argv[2])
else:
    listar_instancias()

def iniciar_instancia(instance_id):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Iniciando instancia {instance_id}")
