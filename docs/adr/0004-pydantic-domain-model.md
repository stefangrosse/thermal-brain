# ADR-0004: Pydantic Domain Model

Status: Accepted

## Decision
Thermal Brain uses Pydantic v2 for all public domain models.

## Rationale
- Strong typing
- Validation
- Serialization
- Immutability support
- Excellent IDE support
- Stable API between integrations

Business logic SHALL NOT live inside Pydantic models.
