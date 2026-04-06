# Proyecto DevOps - Automatización en AWS

## Descripción del proyecto

Este proyecto implementa un flujo básico de DevOps utilizando servicios de AWS como EC2 y S3. Se desarrollaron scripts en Python y Bash para automatizar la gestión de infraestructura y respaldos, integrados mediante un script de orquestación que simula un pipeline de CI/CD.

---

## Instrucciones de uso

### 1. Clonar repositorio

```bash
git clone https://github.com/AreliPerdue/actividad2-devops.git
cd actividad2-devops
```

### 2. Ejecutar script principal

```bash
./scripts/deploy.sh list
```

---

## Flujo Git

El flujo de trabajo implementado fue:

1. Creación de branch feature
2. Desarrollo de funcionalidades
3. Commits pequeños y descriptivos
4. Push al repositorio remoto
5. Integración de cambios

Ejemplo:

```bash
git checkout -b feature/ec2-script
git add .
git commit -m "feat: listar instancias EC2"
git push origin feature/ec2-script
```

---

## Ejemplos de uso

### Gestión de EC2

```bash
python3 ec2/gestionar_ec2.py list
python3 ec2/gestionar_ec2.py start <instance_id>
python3 ec2/gestionar_ec2.py stop <instance_id>
```

### Script de respaldo en S3

```bash
bash s3/backup_s3.sh . nombre-bucket
```

### Script de orquestación

```bash
./scripts/deploy.sh list
```

---

## Tecnologías utilizadas

* AWS EC2
* AWS S3
* Python (boto3)
* Bash scripting
* Git y GitHub

---

## Notas

Se implementaron buenas prácticas de DevOps como:

* Separación de configuración mediante archivo config.env
* Uso de logs
* Automatización de procesos
* Exclusión de archivos temporales mediante .gitignore

