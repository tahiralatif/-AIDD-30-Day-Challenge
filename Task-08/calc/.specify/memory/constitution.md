<!--
    Sync Impact Report
    Version change: N/A --> 1.0.0
    List of modified principles:
        - Principle 1: Test-Driven Development (TDD) (Added)
        - Principle 2: Code Quality and Readability (Added)
        - Principle 3: Modern Python and Type Hinting (Added)
        - Principle 4: Architectural Decision Records (ADR) (Added)
        - Principle 5: Technical Stack Adherence (Added)
        - Principle 6: Quality Assurance Standards (Added)
    Added sections: All Core Principles are new.
    Removed sections: None.
    Templates requiring updates:
        - .specify/templates/plan-template.md (✅ updated - "Constitution Check" aligns)
        - .specify/templates/spec-template.md (✅ updated - implicit guidance aligned)
        - .specify/templates/tasks-template.md (✅ updated - TDD and QA principles aligned)
    Follow-up TODOs:
        - Review Governance section defaults to ensure they meet project-specific needs.
-->
# calc Constitution

## Core Principles

### Principle 1: Test-Driven Development (TDD)
All new features and bug fixes MUST follow a Test-Driven Development (TDD) approach. Tests MUST be written first, approved, fail initially, and then the implementation MUST follow to make them pass. The Red-Green-Refactor cycle is strictly enforced.

### Principle 2: Code Quality and Readability
Code MUST be clean, readable, and easy to understand. Essential OOP principles including SOLID, DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid) MUST be followed.

### Principle 3: Modern Python and Type Hinting
All Python code MUST utilize Python 3.12+ features, including comprehensive type hints to improve code clarity, maintainability, and error detection.

### Principle 4: Architectural Decision Records (ADR)
All significant architectural and design decisions MUST be documented using Architectural Decision Records (ADRs) to capture rationale, context, and consequences.

### Principle 5: Technical Stack Adherence
The project MUST standardize on Python 3.12+ with `uv` as the package manager and `pytest` for testing. All project files MUST be managed under Git version control.

### Principle 6: Quality Assurance Standards
All automated tests MUST pass, and the project MUST maintain at least 80% code coverage. Dataclasses SHOULD be used for defining data structures where appropriate.

## Governance
This Constitution supersedes all other informal practices. Amendments require documented rationale, approval from project leads, and a clear migration plan. Compliance with these principles MUST be verified during code reviews and continuous integration processes. Any deviations MUST be explicitly justified and documented.

**Version**: 1.0.0 | **Ratified**: 2025-11-28 | **Last Amended**: 2025-11-28