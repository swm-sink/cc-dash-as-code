---
name: utils.commit
description: Create git commit with Conventional Commits format (alias for /workflow.checkpoint)
parameters:
  - name: message
    description: Commit message in Conventional Commits format
    required: true
    type: string
tools:
  - Bash
---

# /utils.commit

Create a git commit following Conventional Commits specification.

**Note**: This is functionally equivalent to `/workflow.checkpoint`. Use either command.

## Usage

```
/utils.commit [message]
```

## Purpose

Quick git commits with proper formatting:
- Enforces Conventional Commits format
- Validates message structure
- Creates commit with staged changes

## Behavior

1. **Validate message format**: `type(scope): subject`
2. **Check for changes**: `git status`
3. **Stage changes**: `git add .`
4. **Create commit**: `git commit -m "message"`
5. **Output commit hash**

## Examples

```
/utils.commit "feat(data): Add CSV loader with validation"
```

Output:
```
✓ Commit created: a7f3d91
```

## Message Format

```
type(scope): subject
```

**Types**: feat, fix, docs, style, refactor, perf, test, build, ci, chore

## See Also

- `/workflow.checkpoint` - Same functionality with more detail
- `/workflow.loop` - Commit as part of EPIC cycle
- Conventional Commits: https://www.conventionalcommits.org/
