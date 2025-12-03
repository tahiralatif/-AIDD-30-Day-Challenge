---

description: "Task list for calculator-app feature implementation"
---

# Tasks: calculator-app

**Input**: Design documents from `/specs/001-calculator-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md, contracts/

**Tests**: Test tasks are included following the TDD approach as per the project constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize a new Python project with `uv` in the current directory (`.`): `uv init .`
- [x] T002 Create `src/calculator/` directory
- [x] T003 Create `src/calculator/__init__.py`
- [x] T004 Create `tests/` directory
- [x] T005 Create `tests/__init__.py`
- [x] T006 Add `pytest` as a development dependency in `pyproject.toml` using `uv add pytest --group dev`
- [x] T007 Generate `requirements.txt` from `pyproject.toml` using `uv pip compile --group dev -o requirements.txt`
- [x] T008 Install dependencies using `uv pip install -r requirements.txt`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T009 Define `Operation` dataclass in `src/calculator/operations.py`
- [x] T010 Implement basic arithmetic functions (`add`, `subtract`, `multiply`, `divide`) stubs in `src/calculator/operations.py`
- [x] T011 Create `test_operations.py` for `add` function in `tests/test_operations.py` (ensure it fails)
- [x] T012 Implement `add` function logic in `src/calculator/operations.py` to pass T011
- [x] T013 Create `test_operations.py` for `subtract` function in `tests/test_operations.py` (ensure it fails)
- [x] T014 Implement `subtract` function logic in `src/calculator/operations.py` to pass T013
- [x] T015 Create `test_operations.py` for `multiply` function in `tests/test_operations.py` (ensure it fails)
- [x] T016 Implement `multiply` function logic in `src/calculator/operations.py` to pass T015
- [x] T017 Create `test_operations.py` for `divide` function in `tests/test_operations.py` (ensure it fails)
- [x] T018 Implement `divide` function logic in `src/calculator/operations.py` to pass T017
- [x] T019 Implement division by zero error handling in `src/calculator/operations.py`
- [x] T020 Create `test_operations.py` for division by zero error handling in `tests/test_operations.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: The user can perform basic arithmetic operations using a command-line interface.

**Independent Test**: Running the CLI with various valid inputs for addition, subtraction, multiplication, and division produces correct outputs.

### Implementation for User Story 1

- [x] T021 [US1] Create `main.py` CLI entry point in `src/calculator/main.py`
- [x] T022 [US1] Implement argument parsing for CLI in `src/calculator/main.py` to extract operands and operator
- [x] T023 [US1] Integrate `operations.py` functions into `main.py` for calculation based on parsed arguments
- [x] T024 [US1] Implement handling for non-numeric input error in `src/calculator/main.py` (display message and exit)
- [x] T025 [US1] Implement handling for incorrect command format error in `src/calculator/main.py` (display message and exit)
- [x] T026 [US1] Create `test_main.py` with acceptance tests for basic arithmetic operations in `tests/test_main.py` (ensure it fails initially)
- [x] T027 [US1] Update `main.py` logic to pass acceptance tests in `tests/test_main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: Functional Requirement (FR-004) - Operation History

**Goal**: The calculator maintains a history of the last 5 operations.

**Independent Test**: Performing more than 5 operations and then querying the history shows only the last 5 operations.

### Implementation for Operation History

- [x] T028 [US1] Create `history.py` in `src/calculator/history.py`
- [x] T029 [US1] Implement `OperationHistory` class with a fixed-size storage (e.g., deque) for last 5 operations in `src/calculator/history.py`
- [x] T030 [US1] Create `test_history.py` for `OperationHistory` class in `tests/test_history.py` (ensure it fails)
- [x] T031 [US1] Implement adding operations to history in `src/calculator/history.py` to pass T030
- [x] T032 [US1] Implement history limit logic (last 5, remove oldest when full) in `src/calculator/history.py` to pass T030
- [x] T033 [US1] Integrate `history.py` into `main.py` to record each successfully completed operation
- [x] T034 [US1] Add a command-line option to `main.py` (e.g., `history`) to display the last 5 operations
- [x] T035 [US1] Create `test_main.py` for history display functionality in `tests/test_main.py`

**Checkpoint**: Operation history is functional and testable independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T036 Ensure type hints are comprehensive across all Python files in `src/calculator/`
- [x] T037 Review and refine code comments and docstrings for clarity and completeness
- [x] T038 Update `quickstart.md` in `specs/001-calculator-app/quickstart.md` with final usage instructions including history command
- [x] T039 Run all tests and ensure at least 80% code coverage (Principle 6)
- [x] T040 Final code quality check (adherence to SOLID, DRY, KISS principles)
- [x] T041 Update `pyproject.toml` with project entry point for CLI to allow direct execution (e.g., `calculator` command)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational phase completion
- **Operation History (Phase 4)**: Depends on Foundational phase completion and can be worked on in parallel with or after User Story 1. For sequential execution, it depends on User Story 1.
- **Polish (Phase 5)**: Depends on all other phases being functionally complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
- **Functional Requirement (FR-004) - Operation History**: Depends on core arithmetic operations being functional (from User Story 1 or Foundational). Can be integrated after core arithmetic is working.

### Within Each User Story / Phase

- Tests MUST be written and FAIL before implementation
- Logic for entities/data structures should precede integration into main flow
- Core implementation before error handling/edge cases

### Parallel Opportunities

- T001, T002, T003, T004, T005 in Phase 1 can be parallelized (setting up different files).
- Tasks T008, T010, T012, T014, T017 (creating initial test stubs) can be parallelized within Phase 2.
- Tasks T009, T011, T013, T015, T016 (implementing functions and error handling) can be parallelized within Phase 2, provided their respective test stubs are complete.
- For Phase 3, once T018-T020 are done, T021 and T022 (error handling) could potentially be parallel.
- For Phase 4, T025, T026 (creating history components) could be parallel. T027 (tests) is parallel to the implementation of T028 and T029.
- Tasks T033, T034 in Phase 5 are parallel.

---

## Parallel Example: Foundational Phase (Core Operations)

```bash
# Developer A: Implement Addition
- [x] T008 Create test for add function in tests/test_operations.py
- [x] T009 Implement add function logic in src/calculator/operations.py

# Developer B: Implement Subtraction
- [x] T010 Create test for subtract function in tests/test_operations.py
- [x] T011 Implement subtract function logic in src/calculator/operations.operations.py

# Developer C: Implement Multiplication
- [x] T012 Create test for multiply function in tests/test_operations.py
- [x] T013 Implement multiply function logic in src/calculator/operations.py

# Developer D: Implement Division
- [x] T014 Create test for divide function in tests/test_operations.py
- [x] T015 Implement divide function logic in src/calculator/operations.py

# Developer E: Implement Division by Zero Error (can be done once divide is functional)
- [x] T016 Implement division by zero error handling in src/calculator/operations.py
- [x] T017 Create test for division by zero error handling in tests/test_operations.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add Functional Requirement (FR-004) - Operation History → Test independently → Deploy/Demo
4. Complete Polish phase.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Basic Arithmetic)
   - Developer B: Functional Requirement (FR-004) - Operation History
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
