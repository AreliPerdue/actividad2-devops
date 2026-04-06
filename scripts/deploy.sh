#!/bin/bash

echo "Iniciando despliegue..."

# Listar instancias
python3 ec2/gestionar_ec2.py list

# Ejecutar backup (cambia esto después con tu bucket)
bash s3/backup_s3.sh . al03072223

echo "Despliegue finalizado"
