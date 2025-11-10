---
allowed-tools: Read, Write
description: Generate detailed task breakdown from implementation plan
---

# Generate Task Breakdown

You are generating a detailed, actionable task breakdown from an implementation plan.

## Current Context

- Specification: !`cat .specify/specs/$(git branch --show-current)/spec.md`
- Implementation Plan: !`cat .specify/specs/$(git branch --show-current)/plan.md`
- Current Branch: !`git branch --show-current`

## Your Task

Generate a comprehensive task breakdown that:

1. **Parses the implementation plan** into granular, actionable tasks
2. **Groups tasks by user story** from the specification
3. **Identifies dependencies** between tasks
4. **Marks parallel tasks** with [P] that can be worked on simultaneously
5. **Orders tasks** for optimal execution (dependencies first)
6. **Specifies file paths** where implementation occurs
7. **Includes test tasks** if TDD approach specified

## Task Format

```markdown
## Phase 1: [User Story Title]

### Tasks

- [ ] Task 1: Description
  - Files: `src/path/to/file.py`
  - Dependencies: None

- [ ] [P] Task 2: Description (can run in parallel)
  - Files: `src/another/file.py`
  - Dependencies: Task 1

- [ ] Task 3: Write tests for Task 1
  - Files: `tests/test_file.py`
  - Dependencies: Task 1

### Checkpoint

- [ ] All Phase 1 tests passing
- [ ] Phase 1 acceptance criteria met
```

## Quality Requirements

- Tasks are specific and actionable (not vague)
- Each task can be completed in < 4 hours
- Dependencies are clearly marked
- Parallel tasks identified with [P]
- File paths specified for each task
- Checkpoints defined after each phase

## Output

Save the task breakdown to `.specify/specs/{feature}/tasks.md`

## Next Steps

Inform the user:
1. Review the generated tasks
2. Adjust task granularity if needed
3. Run `/dashboard.implement` to execute tasks
