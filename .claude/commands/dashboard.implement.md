# /dashboard.implement - Execute Implementation Tasks

Execute the implementation plan by working through tasks in the correct order, writing code, tests, and documentation.

## Command Usage

```
/dashboard.implement
```

## Arguments

None. The command uses the current feature's task breakdown.

## Behavior

When this command is executed, Claude Code should:

1. **Identify the current feature** from git branch
2. **Load prerequisites**:
   - Specification: `.specify/specs/{feature}/spec.md`
   - Plan: `.specify/specs/{feature}/plan.md`
   - Tasks: `.specify/specs/{feature}/tasks.md`
   - Constitution: `.specify/memory/constitution.md`
3. **Validate prerequisites exist** and are complete
4. **Parse the task list** from tasks.md
5. **Create a TodoWrite list** with all tasks
6. **Execute tasks in order**:
   - Mark task as "in_progress"
   - Read the task description and requirements
   - Check for dependencies (complete prerequisite tasks first)
   - Write implementation code
   - Write tests (TDD approach)
   - Run tests to verify functionality
   - Run code quality checks (Black, Ruff, mypy)
   - Fix any issues
   - Mark task as "completed"
7. **Handle parallel tasks** (marked with [P]):
   - Can be worked on simultaneously
   - Consider launching sub-agents for true parallelism
8. **Validate checkpoints**:
   - After each user story phase, run validation tests
   - Verify acceptance criteria from specification
9. **Update documentation** as code is written
10. **Create commits** at logical milestones
11. **Output progress** and completion summary

## Example

```
User: /dashboard.implement

Claude Code:
✓ Found feature: 003-sales-analytics-dashboard
✓ Loaded specification (5 user stories, 23 requirements)
✓ Loaded plan (Dash + Pandas + PostgreSQL)
✓ Loaded tasks (42 tasks across 5 phases)

Starting implementation...

[Phase 1: Data Model & Database]
✓ Task 1.1: Create SQLAlchemy models [COMPLETED]
✓ Task 1.2: Create database migrations [COMPLETED]
✓ Task 1.3: Write model tests [COMPLETED]
✓ Task 1.4: Validate database schema [COMPLETED]

[Phase 2: Data Loading & Processing]
⟳ Task 2.1: Create data loaders [IN PROGRESS]
  - Writing src/data/loaders.py...
  - Writing tests/unit/test_loaders.py...
  ...
```

## Implementation Strategy

### Test-Driven Development (TDD)

For each task:
1. Write failing test first
2. Implement minimum code to pass test
3. Refactor for quality
4. Verify all tests still pass

### Code Quality Gates

Before marking task as complete:
- [ ] Code is formatted with Black
- [ ] Code passes Ruff linting
- [ ] Code passes mypy type checking
- [ ] Tests are written and passing
- [ ] Coverage meets 80% threshold
- [ ] Documentation is updated

### Checkpoint Validation

After each user story phase:
1. Run full test suite
2. Verify acceptance criteria from spec
3. Check performance targets
4. Test accessibility (if UI changes)
5. Create git commit with summary

## Task Dependencies

Tasks may have dependencies indicated in tasks.md:
- **Sequential**: Must complete previous task first
- **Parallel** [P]: Can work simultaneously with other [P] tasks
- **Conditional**: Only if certain conditions met

Claude Code should respect dependencies and work in correct order.

## Sub-Agent Coordination

For parallel tasks, Claude Code may launch sub-agents:
- `component-builder`: Create UI components
- `data-pipeline`: Build data infrastructure
- `test-engineer`: Write comprehensive tests
- `documentation`: Generate docs

Sub-agents work independently and coordinate to avoid conflicts.

## Error Handling

- **No tasks found**: "Cannot find tasks.md. Run /dashboard.tasks first."
- **Prerequisites missing**: "Missing {file}. Complete the workflow: spec → plan → tasks → implement."
- **Test failures**: "Tests failing for task {X}. Fixing issues..." then retry
- **Quality gate failures**: "Code quality check failed. Applying automatic fixes..." then retry
- **Unresolvable errors**: Pause and request user guidance

## Progress Tracking

Claude Code maintains a TodoWrite list showing:
- Total tasks
- Completed tasks
- Current task (in_progress)
- Remaining tasks
- Estimated completion time

## Commit Strategy

Create commits at logical points:
- After each user story phase completes
- After all tasks in a phase complete
- When checkpoint validations pass

Commit messages follow format:
```
Implement {user story title}

- Task 1: Description
- Task 2: Description
- Task 3: Description

Tests: {X} tests, {Y}% coverage
Implements: .specify/specs/{feature}/spec.md#{user-story}
```

## Output

The command produces:
- **Source code**: In `src/` directory
- **Tests**: In `tests/` directory
- **Documentation**: Updated in `docs/` and docstrings
- **Git commits**: At logical milestones
- **Coverage report**: HTML report in `htmlcov/`
- **Quality reports**: Linting and type checking results

## Related Commands

- `/dashboard.spec` - Create specification
- `/dashboard.plan` - Create implementation plan
- `/dashboard.tasks` - Generate task breakdown (prerequisite)
- `/dashboard.test` - Run test suite
- `/dashboard.review` - Review code quality

---

*This command executes the entire implementation workflow autonomously, following TDD and meeting all quality gates.*
