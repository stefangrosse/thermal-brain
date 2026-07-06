# AGENTS.md

# Thermal Brain

Welcome to the Thermal Brain project.

This document defines the engineering principles, architecture and development workflow for both humans and AI coding agents.

---

# Project Mission

Thermal Brain is a framework-independent Building Intelligence Engine.

The goal is **not** to automate heating systems.

The goal is to understand buildings.

Thermal Brain continuously learns the thermal behaviour of a building and uses this knowledge to:

- analyse
- predict
- simulate
- recommend
- optimise

Home Assistant is only the first integration.

The Core must remain independent from every automation platform.

---

# Vision

Thermal Brain should become the reference Open Source library for thermal building intelligence.

The project should support multiple integrations including:

- Home Assistant
- openHAB
- ioBroker
- MQTT
- Node-RED
- CLI
- Jupyter

---

# Architecture

Monorepo

```
thermal-brain/

packages/
    thermal_brain_core/

integrations/
    homeassistant/

docs/

tests/

examples/

benchmarks/
```

Business logic belongs exclusively inside:

```
packages/thermal_brain_core/
```

Integrations must never contain business logic.

---

# Architecture Principles

- Architecture First
- Domain Driven Design
- SOLID
- Clean Architecture
- Test Driven Development
- Explainable Algorithms
- Physics before AI
- Local First
- Vendor Independent
- Open Source First

---

# Development Workflow

Before implementing any feature:

1. Read the relevant ADRs.
2. Read `docs/ROADMAP.md`.
3. Reuse existing abstractions.
4. Avoid breaking changes.
5. Prefer extending over rewriting.

---

# Coding Rules

Always

- write production-ready code
- use explicit typing
- write unit tests
- document public APIs
- keep functions small
- keep classes focused
- prefer composition over inheritance
- follow existing architecture

Never

- generate placeholder implementations
- add TODOs
- duplicate logic
- introduce unnecessary dependencies
- redesign existing architecture unless explicitly requested

---

# Technology Stack

Python 3.12+

Pydantic v2

Pytest

Ruff

MyPy

uv

GitHub Actions

---

# Domain Rules

Primitive values representing physical quantities should not be passed through the domain model.

Use Value Objects.

Examples:

- Temperature
- Energy
- Power
- Percentage
- Duration
- Identifier

The domain model must remain platform independent.

---

# Architecture Decision Records

Architecture changes require an ADR.

Current ADRs:

- ADR-0001 Building First
- ADR-0002 Framework Independent Core
- ADR-0003 Test Driven Development
- ADR-0004 Pydantic Domain Models
- ADR-0005 Strongly Typed Value Objects
- ADR-0006 Domain uses Value Objects

---

# Testing

Every new feature requires tests.

Every bug requires a regression test.

Domain logic must be testable without Home Assistant.

---

# Commit Rules

Use Conventional Commits.

Examples:

feat(domain):
feat(statistics):
fix(core):
refactor(domain):
docs(roadmap):
test(core):
ci:
build:

Every commit must:

- compile
- pass tests
- pass Ruff
- pass MyPy

---

# Milestone Workflow

Development follows the project roadmap.

Each milestone must result in:

- mergeable code
- tests
- documentation
- commit message
- ADR if architecture changes

---

# Review

After implementation perform a self review.

Verify:

- Architecture
- API consistency
- Ruff
- MyPy
- Pytest
- Documentation

Review findings should be reported separately.

Do not modify the implementation during review.

---

# Documentation

Public documentation is written in English.

Source code is written in English.

Commit messages are written in English.

ADRs are written in English.

Discussion with the project owner may be in German.

---

# Long-Term Goal

Every design decision should support the creation of a reusable Building Intelligence Engine.

The project should remain understandable, maintainable and extensible for many years.