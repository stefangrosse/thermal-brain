# ADR-0005: Strongly Typed Value Objects

Status: Accepted

## Decision
Primitive values with domain meaning SHALL be represented by value objects.

Examples:
- Temperature
- Energy
- Power
- Percentage
- Duration

## Motivation
Prevent unit mixups, improve readability and provide a stable domain API.
