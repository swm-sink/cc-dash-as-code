---
name: utils.diff
description: Show git diff since feature branch creation or from main branch
parameters:
  - name: spec-number
    description: Optional spec number to find branch base
    required: false
    type: string
tools:
  - Bash
---

# /utils.diff

Show changes since feature branch was created or since diverging from main.

## Usage

```
/utils.diff              # Diff from branch point
/utils.diff 002          # Diff for specific spec branch
```

## Purpose

View all changes in current feature:
- Files added/modified/deleted
- Line-by-line changes
- Summary statistics

## Behavior

1. **Find branch base**: `git merge-base main HEAD`
2. **Run git diff**: `git diff {base}...HEAD`
3. **Parse output**: Files changed, insertions, deletions
4. **Format display**: Summary + detailed diff

## Examples

```
/utils.diff
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Git Diff: Since Branch Creation
════════════════════════════════════════════════════════════════════════════

Branch: 002-claude-code-commands-setup
Base: main (commit 501d7a8)
HEAD: db809df

Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Files changed: 45
  Insertions: 3,842 lines
  Deletions: 23 lines

Files Changed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Added (42 files):
  A  .claude/README.md
  A  .claude/commands/spec/create.md
  A  .claude/commands/spec/validate.md
  ... (39 more)

Modified (3 files):
  M  CLAUDE.md
  M  specs/002-claude-code-commands-setup/spec.md
  M  specs/memory/decisions.md

Detailed Diff
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Full git diff output follows...]

════════════════════════════════════════════════════════════════════════════
```

## See Also

- `git diff` - Standard git diff command
- `/workflow.status` - See requirement completion progress
