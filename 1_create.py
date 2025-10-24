# Crear proyecto Python-Django desde cero
## 1. Instalar python3, venv, pip
## sudo apt install -y python3 python3-venv python3-pip

## 2. Dentro del proyecto, crear entorno virtual
## python3 -m venv .venv

## 3. Activar entorno virtual
## source .venv/bin/activate

## 4. Instalar dependencias
## pip install django dotenv

## 5. Crear proyecto
## django-admin startproject mysite .`

## 6. Migrar tablas base
## python manage.py migrate

## 7. Crear apps
## python manage.py startapp name

## 8. Generar migraciones
## python manage.py makemigrations

## 9. Aplicar migraciones
## python manage.py migrate

## 10. Crear super usuario
## python manage.py createsuperuser

## 11. Correr servidor
## python manage.py runserver

## 12. Desactivar entorno virtual
## `deactivate`

## 13. Adicional
## Guardar dependencias con `pip freeze > requirements.txt`

## Crear archivo `.gitignore` e ignorar:
## git ignore
## env/
## *.pyc
## __pycache__/
## db.sqlite3
## *.log
## *.sqlite3
## /staticfiles/
## /media/
## .DS_Store
## .env
## EOF

## Crear archivo `.env` con:
## DJANGO_SECRET_KEY='django-insecure...'

## Configurar Dotenv:
## settings.py
### from dotenv import load_dotenv
### import os
### load_dotenv()

### SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
