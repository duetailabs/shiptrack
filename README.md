# shiptrack

## Observability

This application is instrumented using OpenTelemetry for distributed tracing. This allows you to gain insights into the application's performance and behavior, especially in a microservices environment.

### Configuration

The following environment variables can be used to configure OpenTelemetry:

*   `OTEL_SERVICE_NAME`: Sets the service name for the application (e.g., `shipping-app`). This helps in identifying the application within your tracing backend.
*   `OTEL_EXPORTER_OTLP_ENDPOINT`: Specifies the OTLP (OpenTelemetry Protocol) endpoint where traces should be sent (e.g., `http://localhost:4318/v1/traces`). This is the address of your OpenTelemetry collector or tracing backend.