---
name: workflow.checkpoint
description: Create a git commit with a descriptive message following Conventional Commits format
parameters:
  - name: message
    description: Commit message (type: subject format, or full message)
    required: true
    type: string
tools:
  - Bash
---

# /workflow.checkpoint

Create a git commit with a descriptive message following Conventional Commits specification.

## Usage

```
/workflow.checkpoint [message]
```

**Arguments**:
- `message`: Commit message in Conventional Commits format

## Purpose

This command provides manual commit control within the EPIC workflow:
- Alternative to `/workflow.loop` for granular commits
- Useful for checkpointing work in progress
- Enforces Conventional Commits format
- Does not automatically identify next task (unlike `/workflow.loop`)

## Behavior

This command creates a git commit:

1. **Parse Commit Message**:
   - Accept message parameter
   - Validate format: `type(scope): subject`
   - Ensure proper structure

2. **Validate Message Format**:
   - **Type** must be one of:
     - `feat`: New feature
     - `fix`: Bug fix
     - `docs`: Documentation only
     - `style`: Formatting, white-space, etc.
     - `refactor`: Code restructuring
     - `perf`: Performance improvement
     - `test`: Test additions/changes
     - `build`: Build system changes
     - `ci`: CI configuration changes
     - `chore`: Maintenance tasks
   - **Scope** (optional): Component or module affected
   - **Subject**: Brief description in imperative mood

3. **Check Git Status**:
   - Run `git status` to verify changes exist
   - Warn if working directory is clean (nothing to commit)
   - List modified, new, and deleted files

4. **Stage Changes**:
   - Run `git add .` to stage all changes
   - Or accept specific files (enhancement)

5. **Create Commit**:
   - Run `git commit -m "message"`
   - Capture commit hash
   - Handle commit errors (e.g., pre-commit hooks fail)

6. **Output Summary**:
   - Commit hash
   - Files changed
   - Next steps

## Examples

Example 1: Feature commit
```
/workflow.checkpoint "feat(components): Add sales filter dropdown"
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Git Checkpoint
════════════════════════════════════════════════════════════════════════════

Validating commit message...
  Format: ✓ Valid Conventional Commits format
  Type: feat (New feature)
  Scope: components
  Subject: Add sales filter dropdown

Checking git status...
  Modified:  2 files
  New:       3 files
  Deleted:   0 files

Files to commit:
  M  src/components/sales_filter.py
  M  tests/unit/components/test_sales_filter.py
  A  src/components/__init__.py
  A  tests/unit/components/filters/__init__.py
  A  tests/unit/components/filters/test_sales_filter.py

Staging files...
  ✓ Staged 5 files

Creating commit...
  [002-claude-code-commands-setup a7f3d91] feat(components): Add sales filter dropdown
   5 files changed, 178 insertions(+)

  ✓ Commit created: a7f3d91

Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Commit: a7f3d91
  Branch: 002-claude-code-commands-setup
  Files changed: 5
  Insertions: 178 lines

Next Steps:
  - Continue work: /workflow.act [next task]
  - Check progress: /workflow.status
  - Complete EPIC cycle: /workflow.verify then /workflow.loop
  - Push to remote: git push

════════════════════════════════════════════════════════════════════════════
```

Example 2: Bug fix commit
```
/workflow.checkpoint "fix(data): Handle null values in CSV loader"
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Git Checkpoint
════════════════════════════════════════════════════════════════════════════

Validating commit message...
  Format: ✓ Valid Conventional Commits format
  Type: fix (Bug fix)
  Scope: data
  Subject: Handle null values in CSV loader

[... file staging ...]

Creating commit...
  [001-dashboard-foundation c9d2e82] fix(data): Handle null values in CSV loader
   2 files changed, 23 insertions(+), 5 deletions(-)

  ✓ Commit created: c9d2e82

[... summary ...]
════════════════════════════════════════════════════════════════════════════
```

Example 3: Refactoring commit
```
/workflow.checkpoint "refactor: Extract common validation logic"
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Git Checkpoint
════════════════════════════════════════════════════════════════════════════

Validating commit message...
  Format: ✓ Valid Conventional Commits format
  Type: refactor (Code restructuring)
  Scope: (none - affects multiple modules)
  Subject: Extract common validation logic

[... commit process ...]
════════════════════════════════════════════════════════════════════════════
```

Example 4: Invalid commit message format
```
/workflow.checkpoint "Added new feature"
```

Output:
```
❌ Error: Invalid commit message format

Message: "Added new feature"
Format: Invalid (does not follow Conventional Commits)

Expected format:
  type(scope): subject

  - type: feat, fix, docs, style, refactor, perf, test, build, ci, chore
  - scope: (optional) component or module name
  - subject: brief description in imperative mood

Valid examples:
  ✓ feat(components): Add sales filter
  ✓ fix(data): Handle null values
  ✓ docs: Update README with usage examples
  ✓ refactor(utils): Extract validation logic

Invalid examples:
  ✗ Added new feature (no type)
  ✗ FEAT: Add filter (type must be lowercase)
  ✗ feat: added filter (use imperative: "add" not "added")

Try again with correct format.

See: https://www.conventionalcommits.org/
```

Example 5: No changes to commit
```
/workflow.checkpoint "feat(components): Add date picker"
```

Output:
```
Warning: No changes to commit

Git status shows working directory is clean.

Did you make changes?
  - If yes: Changes might already be committed
  - If no: Make changes first, then commit

Current status:
  Modified:  0 files
  New:       0 files
  Deleted:   0 files

Options:
  1. Check recent commits: git log -3 --oneline
  2. View current branch: git branch -v
  3. Make changes: /workflow.act [task]

No commit created.
```

Example 6: Commit with body and footer
```
/workflow.checkpoint "feat(components): Add customer analytics dashboard

Implement complete dashboard with:
- Sales filter dropdown (FR-023)
- Date range picker (FR-024)
- Interactive charts (FR-025)
- Real-time data updates (FR-026)

All components include WCAG 2.1 AA compliance.
Test coverage: 95%

Closes #42"
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Git Checkpoint
════════════════════════════════════════════════════════════════════════════

Validating commit message...
  Format: ✓ Valid Conventional Commits format (with body and footer)
  Type: feat
  Scope: components
  Subject: Add customer analytics dashboard
  Body: Present (detailed description)
  Footer: Closes #42

[... staging ...]

Creating commit with detailed message...
  [001-dashboard-foundation f1a3b45] feat(components): Add customer analytics dashboard
   12 files changed, 567 insertions(+), 23 deletions(-)

  ✓ Commit created: f1a3b45

[... summary ...]
════════════════════════════════════════════════════════════════════════════
```

Example 7: Pre-commit hook failure
```
/workflow.checkpoint "feat(data): Add CSV loader"
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Git Checkpoint
════════════════════════════════════════════════════════════════════════════

Validating commit message... ✓
Staging files... ✓

Creating commit...
  ❌ Commit failed: Pre-commit hook returned non-zero exit

Hook output:
  Checking Python AST..........................................Failed
  - hook id: check-ast
  - exit code: 1

  src/data/csv_loader.py:45:12: E999 SyntaxError: invalid syntax

  Linting with Ruff............................................Failed
  - hook id: ruff
  - exit code: 1

  src/data/csv_loader.py:67:5: F841 local variable 'result' is assigned but never used

Recommendations:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. Fix syntax error in csv_loader.py:45
  2. Remove or use unused variable in csv_loader.py:67
  3. Run: /utils.lint to see all issues
  4. Fix issues, then try commit again

Pre-commit hooks protect code quality. Fix issues before committing.

No commit created.
════════════════════════════════════════════════════════════════════════════
```

## Output

**Validation**:
- Commit message format check
- Type, scope, subject validation

**File Status**:
- Modified files list
- New files list
- Deleted files list

**Commit Result**:
- Commit hash
- Files changed count
- Line changes (insertions/deletions)

**Next Steps**:
- Suggestions for what to do next

**Errors**:
- Format validation errors
- Git errors
- Pre-commit hook failures

## Conventional Commits Format

### Basic Format

```
type(scope): subject

body

footer
```

### Type Values

| Type | Description | Example |
|------|-------------|---------|
| feat | New feature | `feat(auth): Add login page` |
| fix | Bug fix | `fix(data): Handle null values` |
| docs | Documentation | `docs: Update README` |
| style | Formatting | `style: Format with Black` |
| refactor | Restructuring | `refactor: Extract validation` |
| perf | Performance | `perf(data): Cache results` |
| test | Tests | `test(utils): Add unit tests` |
| build | Build system | `build: Update dependencies` |
| ci | CI/CD | `ci: Add GitHub Actions` |
| chore | Maintenance | `chore: Clean up imports` |

### Scope

Optional but recommended. Examples:
- `components`: UI components
- `data`: Data processing
- `layouts`: Dashboard layouts
- `utils`: Utility functions
- `config`: Configuration
- `tests`: Test infrastructure

### Subject

- Use imperative mood: "Add" not "Added" or "Adds"
- Don't capitalize first letter
- No period at end
- Brief (50 characters or less)

### Body (Optional)

- Detailed description
- Explain what and why, not how
- Wrap at 72 characters
- Can reference requirements (FR-NNN)

### Footer (Optional)

- Breaking changes: `BREAKING CHANGE: ...`
- Issue references: `Closes #42`, `Fixes #123`

## Difference from /workflow.loop

| Feature | /workflow.checkpoint | /workflow.loop |
|---------|---------------------|----------------|
| Creates commit | ✓ Yes | ✓ Yes |
| Validates quality | ✗ No | ✓ Yes (requires /workflow.verify) |
| Identifies next task | ✗ No | ✓ Yes (runs /workflow.observe) |
| Manual control | ✓ Yes | ✗ No (automated) |
| Use case | Work-in-progress | Complete task cycle |

**When to use /workflow.checkpoint**:
- Checkpointing work in progress
- Multiple small commits during implementation
- Manual commit control needed

**When to use /workflow.loop**:
- Completing EPIC cycle
- Automated workflow continuation
- Enforcing quality standards

## See Also

- `/workflow.loop` - Complete EPIC cycle with commit
- `/workflow.verify` - Validate before committing
- `/utils.commit` - Similar functionality (alias)
- `specs/memory/patterns.md` - Commit message patterns
- https://www.conventionalcommits.org/ - Specification
