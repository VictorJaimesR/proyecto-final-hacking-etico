# Proyecto Final Hacking Ético

## Tema

Análisis, explotación y mitigación de vulnerabilidades en APIs REST usando Damn Vulnerable RESTaurant API Game.

## Objetivo

Configurar, analizar, explotar y mitigar vulnerabilidades presentes en una API REST vulnerable, documentando evidencias técnicas y relacionando los hallazgos con OWASP API Security Top 10.

## Integrantes y responsabilidades

- Integrante 1: Configuración del entorno, documentación técnica y evidencias del despliegue.
- Integrante 2: Identificación y explotación de vulnerabilidades.
- Integrante 3: Mitigación, validación y extensión del sistema vulnerable.

## Entorno utilizado

- Sistema operativo: Kali Linux 2026.1
- Virtualización: Oracle VirtualBox
- Editor: Visual Studio Code / terminal de Kali
- Contenedores: Docker
- Orquestación: Docker Compose V2
- API vulnerable: Damn Vulnerable RESTaurant API Game
- Base de datos: PostgreSQL
- Puerto de la API: 8091

## Ejecución del entorno vulnerable

Para levantar el entorno:

```bash
cd src/Damn-Vulnerable-RESTaurant-API-Game
sudo ./start_app.sh

## Para verificar los contenedores activos:
sudo docker ps

## URLs principales

- Swagger: http://localhost:8091/docs
- Redoc: http://localhost:8091/redoc
- OpenAPI JSON: http://localhost:8091/openapi.json

## Validación del entorno 

El entorno fue validado mediante:

- Servicio Docker en estado active (running).
- Contenedores de API y PostgreSQL en ejecución.
- Swagger funcionando correctamente en http://localhost:8091/docs.
- Redoc validado mediante curl, obteniendo respuesta HTTP/1.1 200 OK

## Estructura del repositorio

proyecto-final-hacking-etico/
├── evidencias/
│   ├── entorno/
│   ├── mitigaciones/
│   ├── vulnerabilidad-1-bola/
│   ├── vulnerabilidad-2-bfla/
│   └── vulnerabilidad-3-mass-assignment/
├── informe/
├── scripts/
└── src/
    └── Damn-Vulnerable-RESTaurant-API-Game/
