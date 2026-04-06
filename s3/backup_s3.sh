#!/bin/bash

DIRECTORIO=$1
BUCKET=$2

echo "Directorio: $DIRECTORIO"
echo "Bucket: $BUCKET"

ARCHIVO="backup_$(date +%Y%m%d_%H%M%S).tar.gz"

tar -czf $ARCHIVO $DIRECTORIO

echo "Archivo comprimido: $ARCHIVO"
