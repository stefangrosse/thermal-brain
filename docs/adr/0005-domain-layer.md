# ADR-0005: Domain Layer Structure

Status: Accepted

## Decision

The domain is split into:

- entities
- value_objects
- interfaces

The separation keeps the public API stable and prevents business logic from leaking into data models.
