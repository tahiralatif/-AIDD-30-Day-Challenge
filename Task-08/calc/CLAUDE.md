# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Install Dependencies**: `uv pip install -r requirements.txt`
- **Run All Tests**: `pytest`
- **Run a Single Test**: `pytest <path_to_test_file>::<test_name>`

## Code Architecture and Structure

This is a Python project using `uv` for dependency management and `pytest` for testing. The primary application logic is expected to reside within the `src/` directory. Tests are located in the `tests/` directory. `pyproject.toml` is used for project configuration.