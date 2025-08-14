# Brandbold Wave

**Brandbold Wave** es un sistema de streaming de contenido multimedia, que permite administrar, transmitir y consumir contenido desde un cliente web. Está construido como un **monorepo de microservicios**, usando Flask, Spring Boot y React.

## Arquitectura

- `flask-microservice` → Admin: Subida, gestión y administración de contenido.
- `spring-microservice` → Streaming: Servicio encargado de la transmisión del contenido a los clientes.
- `react-client` → Cliente: Interfaz web donde los usuarios pueden explorar y reproducir contenido.
- `docker-compose.yml` → Orquestación de todos los servicios con Docker.
- `nginx.conf` → Configuración de Nginx para reverse proxy y streaming.

## Características

- Subida y gestión de contenido multimedia desde un panel de administración.
- Streaming eficiente con microservicio dedicado.
- Cliente web moderno en React para navegación y reproducción.
- Orquestación mediante Docker Compose.
- Posibilidad de escalar servicios de manera independiente.

## Instalación
