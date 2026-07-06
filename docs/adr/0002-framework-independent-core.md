# ADR-0002: Framework Independent Core

Status: Accepted

## Context

Home automation platforms should not contain business logic.

## Decision

Thermal Brain is split into:

- Core Engine
- Integration Layer

The Core Engine contains all domain logic, thermal models,
prediction and recommendation algorithms.

Integrations are responsible for:
- Data acquisition
- Scheduling
- Persistence
- User interaction

## Consequences

- Framework independent
- Reusable outside Home Assistant
- Easy unit testing
- Lower maintenance effort
