# ADR-0003: Test Driven Development

Status: Accepted

## Context

Thermal Brain will implement mathematical and physical models.
Regressions are difficult to detect without automated tests.

## Decision

Development follows a test-first approach whenever practical.

Rules:

- New features require tests.
- Bugs require a regression test.
- Domain logic must be testable without Home Assistant.
- Physics before optimisation.

## Consequences

The project will prioritize correctness over implementation speed.
