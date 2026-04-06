#!/bin/bash

DIRECTORIO=$1
BUCKET=$2

echo "Directorio: $DIRECTORIO"
echo "Bucket: $BUCKET"

ARCHIVO="backup_$(date +%Y%m%d_%H%M%S).tar.gz"

tar -czf $ARCHIVO $DIRECTORIO

echo "Archivo comprimido: $ARCHIVO"

aws s3 cp $ARCHIVO s3://$BUCKET/

echo "Archivo subido a S3"

LOG="backup.log"

echo "$(date) - Backup creado: $ARCHIVO" >> $LOG
echo "$(date) - Subido a bucket: $BUCKET" >> $LOG
