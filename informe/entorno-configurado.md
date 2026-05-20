# Configuración del Entorno

## Responsable

VictorJaimesR

## Objetivo

Configurar el entorno vulnerable del proyecto final de Hacking Ético para permitir el análisis, explotación y mitigación de vulnerabilidades en una API REST.

## Entorno utilizado

- Kali Linux 2026.1
- Oracle VirtualBox
- Docker
- Docker Compose V2
- Git
- Curl
- Swagger
- Damn Vulnerable RESTaurant API Game
- PostgreSQL

## Actividades realizadas

Se instaló y validó Docker en Kali Linux. Posteriormente, se clonó el proyecto Damn Vulnerable RESTaurant API Game y se ejecutó mediante el script `start_app.sh`.

La ejecución del entorno generó dos contenedores principales:

- `damn-vulnerable-restaurant-api-game-web-1`: servicio web de la API vulnerable.
- `damn-vulnerable-restaurant-api-game-db-1`: base de datos PostgreSQL.

La API quedó disponible en el puerto `8091`.

## Validación

El entorno fue validado mediante:

- `sudo systemctl status docker`
- `sudo docker ps`
- `http://localhost:8091/docs`
- `curl -i http://localhost:8091/docs`
- `curl -i http://localhost:8091/redoc`

Swagger cargó correctamente en:

```text
http://localhost:8091/docs

Redoc respondió correctamente por terminal con estado HTTP/1.1 200 OK, aunque no renderizó visualmente en el navegador debido a un recurso externo de JavaScipt no disponible.

## Evidencias

Las evidencias se encuentran en:

evidencias/entorno/

Incluyen capturas de Docker activo, contenedores en ejecución, Swagger funcionando, pruebas con curl y estructura del repositorio.

## Conclusión

El entorno vulnerable fue configurado correctamente y quedó listo para que el equipo continúe con las fases de identificación, explotación, mitigación y validación de vulnerabilidades.

