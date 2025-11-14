---
name: workflow.loop
description: Complete the EPIC cycle by committing changes and identifying the next task (EPIC - Loop phase)
parameters: []
tools:
  - Bash
  - Read
---

# /workflow.loop

Complete the EPIC cycle: commit changes, update progress, and identify the next task.

## Usage

```
/workflow.loop
```

## EPIC Methodology

**EPIC** = Observe → Act → Verify → **L**oop

This command implements the **Loop** phase:
- Verify all quality checks passed
- Create git commit with descriptive message
- Update progress tracking
- Re-run Observe to identify next task
- Present continuation options

## Behavior

This command completes the EPIC cycle and prepares for the next iteration:

1. **Check Verification Status**:
   - Ensure `/workflow.verify` was run recently
   - Confirm all quality checks passed
   - **Block if verification failed**: Cannot loop until quality standards met

2. **Create Git Commit**:
   - Run `git status` to see changes
   - Stage relevant files with `git add`
   - Generate commit message following Conventional Commits format:
     - Type: feat, fix, refactor, test, docs, chore
     - Scope: Component or module affected
     - Subject: Brief description (imperative mood)
     - Body: Details including requirement references (FR-NNN)
   - Execute `git commit`
   - Output commit hash

3. **Update Progress Tracking**:
   - Mark completed task in tasks.md (if using checklist)
   - Update requirement status in tracking system
   - Log completion in progress file

4. **Re-run Observe**:
   - Automatically call `/workflow.observe` internally
   - Analyze new state after commit
   - Identify next actionable task

5. **Present Continuation Options**:
   - **Continue**: Move to next task immediately
   - **Pivot**: Choose different task (if priorities changed)
   - **Pause**: Stop for review or break
   - **Complete**: Mark feature as done (if all requirements met)

6. **Output Summary**:
   - Commit details
   - Progress update
   - Next recommended task
   - Continuation options

## Examples

Example 1: Successful loop with next task
```
/workflow.loop
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Loop Phase
════════════════════════════════════════════════════════════════════════════

Checking verification status...
  ✅ All quality checks passed

Creating git commit...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Git status:
  Modified:  2 files
  New:       4 files

Files to commit:
  M  src/components/sales_filter.py
  M  tests/unit/components/test_sales_filter.py
  A  src/components/__init__.py
  A  tests/unit/components/__init__.py

Generating commit message...

Commit message:
  feat(components): Add sales filter dropdown component

  Implement region filter dropdown with accessibility support:
  - Created sales filter component with dcc.Dropdown
  - Added ARIA labels for screen readers
  - Implemented input validation
  - Comprehensive test coverage (100%)

  Addresses:
  - FR-023: Filter components
  - SC-008: WCAG 2.1 AA compliance

Committing...
  [002-claude-code-commands-setup a7f3d91] feat(components): Add sales filter dropdown component
   4 files changed, 145 insertions(+)

  ✅ Commit created: a7f3d91

Progress Update
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature: 002-claude-code-commands-setup
Completed: T023 - Implement sales filter component

Updated Progress:
  Requirements:  16/60 implemented (27%)
  Success Criteria: 7/15 achieved (47%)
  Tasks: 24/60 completed (40%)

Recent Completions:
  ✓ T021: Create component directory structure
  ✓ T022: Implement base component patterns
  ✓ T023: Implement sales filter component (just completed)

Analyzing Next Task...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Recommended Task: T024 - Implement date range picker component

Task Details:
  Type: Dash Component
  Size: Medium (1-3 hours)
  Priority: High
  Dependencies: T021-T023 (Complete ✓)

Description:
  Create date range picker component using dcc.DatePickerRange.
  Include input validation, default date range (last 30 days),
  and accessibility support (ARIA labels, keyboard navigation).

Addresses Requirements:
  - FR-024: Date filtering components
  - SC-009: Keyboard navigation support

Continuation Options
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Choose next action:

  1. Continue with recommended task:
     /workflow.act Implement date range picker component

  2. Pivot to different task:
     /workflow.observe (review all options)

  3. Pause for review:
     Review commit: git show a7f3d91
     View progress: /workflow.status

  4. Complete feature (if all requirements met):
     /workflow.status (check completion)

Recommendation: Continue with T024 to maintain momentum.

Next Step: /workflow.act Implement date range picker component

════════════════════════════════════════════════════════════════════════════
```

Example 2: Verification not run or failed
```
/workflow.loop
```

Output:
```
❌ Error: Cannot loop - Verification required

The EPIC workflow requires passing verification before committing:

  Observe → Act → Verify → Loop
                    ↑
                 You are here

Status:
  Verification: Not run (or failed on last attempt)

Quality Standards:
  You must run /workflow.verify and ensure all checks pass:
    ✓ Tests pass (coverage ≥ 80%)
    ✓ Linting passes (zero errors)
    ✓ Type checking passes (zero errors)
    ✓ Formatting correct
    ✓ Accessibility compliant (if UI)
    ✓ Performance targets met (if applicable)

Next Steps:
  1. Run /workflow.verify
  2. If checks fail, fix issues
  3. Re-run /workflow.verify until all pass
  4. Then run /workflow.loop

Do not skip verification! It ensures code quality and prevents bugs.
```

Example 3: No changes to commit
```
/workflow.loop
```

Output:
```
Warning: No changes to commit

Git status shows working directory is clean.

Did you implement code?
  - If yes: Changes might already be committed
  - If no: Run /workflow.act to implement a task

Options:
  1. Check current progress: /workflow.status
  2. Implement next task: /workflow.observe then /workflow.act
  3. View recent commits: git log -3 --oneline

Working directory status:
  Modified:  0 files
  New:       0 files
  Deleted:   0 files

Current branch: 002-claude-code-commands-setup
Last commit: a7f3d91 feat(components): Add sales filter dropdown component
```

Example 4: Feature complete
```
/workflow.loop
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Loop Phase
════════════════════════════════════════════════════════════════════════════

Checking verification status...
  ✅ All quality checks passed

Creating git commit...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [... commit details ...]

  ✅ Commit created: b8e4f02

Progress Update
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Feature: 002-claude-code-commands-setup

Updated Progress:
  Requirements:  60/60 implemented (100%) ✨
  Success Criteria: 15/15 achieved (100%) ✨
  Tasks: 60/60 completed (100%) ✨

🎉 Feature Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

All requirements implemented and success criteria achieved!

Final Validation:
  ✅ All functional requirements (FR-001 to FR-060)
  ✅ All success criteria (SC-001 to SC-015)
  ✅ Test coverage: 87% (target: 80%)
  ✅ WCAG 2.1 AA compliant
  ✅ Performance targets met
  ✅ Documentation complete

Next Steps:
  1. Final verification:
     /workflow.verify (one last check)

  2. Push to remote:
     git push -u origin 002-claude-code-commands-setup

  3. Create pull request:
     gh pr create --title "Implement Spec 002: Claude Code Commands Setup"

  4. Deploy (if applicable):
     Follow deployment documentation

  5. Move to next spec:
     /spec.list (see what's next)

Congratulations on completing Feature 002! 🎊

════════════════════════════════════════════════════════════════════════════
```

## Output

**Verification Check**:
- Status (passed/failed)
- Block if failed

**Commit Details**:
- Files changed
- Commit message
- Commit hash

**Progress Update**:
- Requirements, success criteria, tasks percentages
- Recent completions

**Next Task** (if feature incomplete):
- Task ID and description
- Type, size, priority
- Requirements addressed

**Continuation Options**:
- Continue, Pivot, Pause, or Complete
- Recommended next command

**Feature Complete** (if 100%):
- Celebration message
- Final validation checklist
- Deployment next steps

## Commit Message Format

The command generates commit messages following Conventional Commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type**:
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code restructuring
- `test`: Test additions/changes
- `docs`: Documentation changes
- `chore`: Maintenance tasks

**Scope**: Component or module (e.g., components, data, layouts)

**Subject**: Brief description (imperative: "Add", "Fix", "Implement")

**Body**:
- Detailed description
- Requirement references (FR-NNN)
- Success criteria references (SC-NNN)

**Footer** (optional):
- Breaking changes
- Issue references

## Flow Control

The command provides intelligent flow control:

1. **Linear**: Continue with next sequential task
2. **Adaptive**: Suggest different task if priorities changed
3. **Blocked**: Identify if waiting on dependencies
4. **Complete**: Celebrate when feature is done

## Constitutional Alignment

This command enforces Core Principle 5: Iterative development
- Small, frequent commits
- Continuous integration
- Regular validation
- Steady progress

## See Also

- `/workflow.verify` - Validate quality (must pass before loop)
- `/workflow.observe` - Re-run to identify next task
- `/workflow.act` - Implement next task
- `/workflow.status` - View overall progress
- `/workflow.checkpoint` - Manual commit (alternative)
- `specs/memory/patterns.md` - Commit message patterns
