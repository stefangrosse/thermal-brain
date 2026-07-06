# ADR-0001: Building First

Status: Accepted

## Context

Most existing projects are tightly coupled to a specific heating technology.

## Decision

Thermal Brain models the building first.
Heating systems are represented through a generic Heat Source abstraction.

## Consequences

- Technology independent
- Easier testing
- Reusable thermal model
- Future support for multiple home automation platforms
