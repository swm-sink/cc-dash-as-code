---
name: spec.branch
description: Create and switch to a git feature branch from an approved specification
parameters:
  - name: feature-number
    description: Three-digit feature number (e.g., 001, 002, 006)
    required: true
    type: string
tools:
  - Glob
  - Read
  - Bash
---

# /spec.branch

Create a git feature branch from an approved specification.

## Usage

```
/spec.branch [feature-number]
```

**Arguments**:
- `feature-number`: Three-digit feature number (e.g., 001, 002, 006)

## Behavior

This command creates a feature branch following git-flow conventions:

1. **Validate feature number**:
   - Check format (3 digits: 001-999)
   - Use Glob to find matching spec directory

2. **Verify specification status**:
   - Read spec.md to check **Status** field
   - Ensure status is "Approved" (not "Draft")
   - Warn if plan.md or tasks.md are missing

3. **Extract feature name**:
   - Get kebab-case name from directory (e.g., `002-claude-code-commands-setup`)

4. **Check git status**:
   - Use `git status` to check for uncommitted changes
   - Warn if working directory is not clean
   - Confirm branch doesn't already exist

5. **Create and switch to branch**:
   - Branch naming format: `{number}-{kebab-case-name}`
   - Example: `002-claude-code-commands-setup`
   - Execute: `git checkout -b {branch-name}`

6. **Output success message**:
   - Confirm branch creation
   - Show next steps (typically `/workflow.observe`)

## Examples

Example 1: Create branch for approved spec
```
/spec.branch 002
```

Output:
```
Creating feature branch for Spec 002...

Specification: 002-claude-code-commands-setup
Status: Approved ✓
Plan: plan.md found ✓
Tasks: tasks.md found ✓

Checking git status...
Working directory clean ✓

Creating branch: 002-claude-code-commands-setup
Switched to a new branch '002-claude-code-commands-setup'

✓ Feature branch created successfully!

Next steps:
1. Begin EPIC workflow: /workflow.observe
2. Or review the plan: cat specs/002-claude-code-commands-setup/plan.md
3. Or review tasks: cat specs/002-claude-code-commands-setup/tasks.md

Ready to implement Spec 002!
```

Example 2: Attempt to create branch for draft spec
```
/spec.branch 006
```

Output:
```
Error: Cannot create branch for Draft specification

Specification: 006-sales-analytics-dashboard
Status: Draft ✗

A specification must be approved before creating a feature branch.

Next steps:
1. Complete the specification:
   - Add all requirements (FR-NNN)
   - Add success criteria (SC-NNN)
   - Create plan.md
   - Create tasks.md
2. Validate: /spec.validate
3. Update Status to "Approved" in spec.md
4. Try /spec.branch 006 again

Use /spec.show 006 to view the specification.
```

Example 3: Branch already exists
```
/spec.branch 002
```

Output:
```
Error: Branch already exists

Branch name: 002-claude-code-commands-setup
Status: Already exists locally

Options:
1. Switch to existing branch: git checkout 002-claude-code-commands-setup
2. Delete and recreate: git branch -D 002-claude-code-commands-setup && /spec.branch 002
3. Use different name: git checkout -b 002-claude-code-commands-v2

Current branch: main
```

Example 4: Uncommitted changes
```
/spec.branch 003
```

Output:
```
Warning: Uncommitted changes detected

Modified files:
  - specs/003-agent-skills-development/plan.md
  - .claude/commands/spec/create.md

Recommendation: Commit or stash changes before creating a feature branch.

Options:
1. Commit changes: git add . && git commit -m "..."
2. Stash changes: git stash
3. Proceed anyway (not recommended)

Proceed with branch creation? (This command will not proceed automatically)

Use /utils.commit or /workflow.checkpoint to commit changes.
```

Example 5: Missing plan.md or tasks.md
```
/spec.branch 007
```

Output:
```
Warning: Specification missing implementation files

Specification: 007-customer-segmentation
Status: Approved ✓

Missing files:
  ✗ plan.md - Technical implementation plan
  ✗ tasks.md - Task breakdown

Recommendation: Create plan.md and tasks.md before beginning implementation.

Proceed with branch creation anyway?
1. Yes - Create branch now (you can add plan/tasks later)
2. No - Cancel and create plan/tasks first

For most features, having a plan and task breakdown greatly improves implementation efficiency.
```

## Output

**Success Path**:
- Verification checks (status, files, git state)
- Branch creation confirmation
- Next steps (typically `/workflow.observe`)

**Error Conditions**:
- Spec not found
- Spec not approved (Status: Draft)
- Branch already exists
- Uncommitted changes (warning)
- Missing plan.md or tasks.md (warning)

**Warnings vs Errors**:
- **Error**: Blocks branch creation (e.g., Draft spec)
- **Warning**: Allows proceeding with confirmation (e.g., uncommitted changes)

## Branch Naming Convention

**Format**: `{number}-{kebab-case-name}`

**Examples**:
- `001-dashboard-foundation`
- `002-claude-code-commands-setup`
- `006-sales-analytics-dashboard`

**Rationale**:
- Number prefix allows sorting by implementation order
- Kebab-case matches directory naming
- Clear link between branch and specification
- Compatible with git-flow and CI/CD systems

## Constitutional Alignment

This command enforces Core Principle 1: Specification-driven development
- Only approved specifications can have feature branches
- Plan and tasks should be ready before implementation
- Clear link between specification and code

## See Also

- `/spec.create` - Create new specification
- `/spec.validate` - Validate specification
- `/spec.list` - List all specifications
- `/spec.show [number]` - Display specification
- `/workflow.observe` - Begin EPIC workflow (first step after branching)
- `/utils.commit` - Commit changes before branching
- `specs/WORKFLOW.md` - Git workflow documentation
