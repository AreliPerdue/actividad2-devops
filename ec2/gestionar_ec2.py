import boto3

def listar_instancias():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']} | Estado: {instance['State']['Name']}")

def iniciar_instancia(instance_id):
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Iniciando instancia {instance_id}")

def detener_instancia(instance_id):
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Deteniendo instancia {instance_id}")

def terminar_instancia(instance_id):
    ec2 = boto3.client('ec2')
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminando instancia {instance_id}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Uso:")
        print("python gestionar_ec2.py list")
        print("python gestionar_ec2.py start <instance_id>")
        print("python gestionar_ec2.py stop <instance_id>")
        print("python gestionar_ec2.py terminate <instance_id>")
        sys.exit(1)

    comando = sys.argv[1]

    if comando == "list":
        listar_instancias()
    elif comando == "start" and len(sys.argv) == 3:
        iniciar_instancia(sys.argv[2])
    elif comando == "stop" and len(sys.argv) == 3:
        detener_instancia(sys.argv[2])
    elif comando == "terminate" and len(sys.argv) == 3:
        terminar_instancia(sys.argv[2])
    else:
        print("Parámetros inválidos")
