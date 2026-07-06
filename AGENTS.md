# AGENTS.md

# Thermal Brain

Welcome to the Thermal Brain project.

This document defines the engineering principles, architecture and development workflow for both humans and AI coding agents.

---

# Project Mission

Thermal Brain is a framework-independent **Building Intelligence Engine**.

The goal is **not** to automate heating systems.

The goal is to understand buildings.

Thermal Brain continuously learns the thermal behaviour of a building and uses this knowledge to

- analyse
- predict
- simulate
- recommend
- optimise

Home Assistant is only the first integration.

The Core must remain independent from every automation platform.

---

# Vision

Thermal Brain aims to become the leading Open Source library for thermal building intelligence.

The project should support multiple integrations including

- Home Assistant
- openHAB
- ioBroker
- MQTT
- Node-RED
- CLI
- Jupyter

---

# Repository Structure

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

All business logic belongs to

```
packages/thermal_brain_core/
```

Integrations are adapters only.

They must never contain business logic.

---

# Architecture Principles

- Architecture First
- Domain Driven Design
- SOLID
- Clean Architecture
- Test Driven Development
- Physics before AI
- Explainable Algorithms
- Local First
- Vendor Independent
- Open Source First

---

# Technology Stack

- Python 3.12+
- Pydantic v2
- Pytest
- Ruff
- MyPy
- uv
- GitHub Actions

---

# Domain Rules

Physical quantities shall not be represented by primitive types.

Always use Value Objects.

Examples

- Temperature
- Energy
- Power
- Percentage
- Duration
- Identifier

The Core domain must remain completely independent of Home Assistant.

---

# Development Workflow

Every repository change must originate from exactly one GitHub Issue.

Development must always start from the latest `main` branch.

AI agents must never implement changes while on `main`.

Every GitHub Issue must be implemented inside its own feature branch.

Workflow

1. Switch to `main`.
2. Pull the latest changes.
3. Create a dedicated feature branch for the issue.
4. Verify the current branch is not `main`.
5. Implement the assigned GitHub Issue.
6. Run Ruff, MyPy and Pytest.
7. Commit using Conventional Commits.
8. Push the feature branch.
9. Open a Pull Request.
10. Do not merge the Pull Request.

---

# Branch Naming

Features

```
feature/<issue-number>-<short-description>
```

Example

```
feature/12-observation-engine
```

Bug Fixes

```
fix/<issue-number>-<short-description>
```

Refactoring

```
refactor/<short-description>
```

---

# Commits

Use Conventional Commits.

Examples

```
feat(observation): implement observation engine

feat(statistics): add heating degree day calculation

fix(core): validate percentage range

docs(domain): update observation model

refactor(domain): simplify observation API
```

---

# Pull Requests

Every Pull Request must address exactly one GitHub Issue.

Every feature branch must be pushed and submitted as a Pull Request.

AI agents must never merge Pull Requests automatically.

All CI checks must pass before a Pull Request can be merged.

Before opening a Pull Request verify

- Ruff passes
- MyPy passes
- Pytest passes
- Documentation updated
- ADR added if architecture changed

Merge Strategy

**Squash and Merge**

Delete the feature branch after merging.

---

# Coding Rules

Always

- write production-ready code
- use explicit typing
- write tests
- document public APIs
- keep functions small
- keep classes focused
- prefer composition over inheritance
- reuse existing abstractions

Never

- generate placeholder code
- generate pseudo code
- add TODOs
- duplicate logic
- redesign existing architecture without an ADR
- commit directly to main

---

# ADR Rules

Architecture changes require an ADR.

Current ADRs

- ADR-0001 Building First
- ADR-0002 Framework Independent Core
- ADR-0003 Test Driven Development
- ADR-0004 Pydantic Domain Models
- ADR-0005 Strongly Typed Value Objects
- ADR-0006 Domain uses Value Objects

---

# Testing

Every feature requires tests.

Every bug requires a regression test.

Domain logic must be testable without Home Assistant.

---

# Documentation

Public documentation is written in English.

Source code is written in English.

Commit messages are written in English.

ADRs are written in English.

Discussions with the project owner may be in German.

---

# Development Process for AI Agents

Before implementing a GitHub Issue

1. Read AGENTS.md
2. Read docs/ROADMAP.md
3. Read all relevant ADRs
4. Create a feature branch
5. Implement the issue
6. Write tests
7. Update documentation
8. Run Ruff
9. Run MyPy
10. Run Pytest
11. Commit using Conventional Commits
12. Open a Pull Request

Never merge the Pull Request.

Never redesign the architecture unless explicitly requested.

---

# Review

After implementation perform a self review.

Verify

- Architecture
- API consistency
- Ruff
- MyPy
- Pytest
- Documentation

Report improvements separately.

Do not modify the implementation during the review.

---

# Long-Term Goal

Every design decision should support the creation of a reusable Building Intelligence Engine.

The project should remain understandable, maintainable and extensible for many years.
