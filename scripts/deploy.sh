#!/bin/bash

ACCION=$1
INSTANCE_ID=$2
DIRECTORIO=$3
BUCKET=$4

echo "Acción: $ACCION"
echo "Instance ID: $INSTANCE_ID"
echo "Directorio: $DIRECTORIO"
echo "Bucket: $BUCKET"

echo "Ejecutando script EC2..."

python3 ec2/gestionar_ec2.py $ACCION $INSTANCE_ID

