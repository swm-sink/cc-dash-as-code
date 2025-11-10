# Hybrid Workflow Architecture

**Date**: 2025-11-10
**Status**: Approved Architecture
**Purpose**: Define the two-process workflow for spec-driven dashboard development

---

## Overview

Our development workflow combines **two distinct processes**:

1. **Spec-Kit Process** (Planning) - Defines WHAT to build
2. **Claude Code Process** (Execution) - Defines HOW to build it

The handoff point is **tasks.md** - a frozen, approved task list that execution follows.

---

## The Two Processes

### Process 1: Spec-Kit (Planning)

**Purpose**: Define WHAT needs to be built
**Commands**: `/spec:*`
**Output**: Approved tasks.md file

```
Constitution (Project Principles)
    ↓
Specify (spec.md) - User stories, requirements, success criteria
    ↓
Plan (plan.md) - Technical approach, architecture, components
    ↓
Tasks (tasks.md) - Actionable task list with dependencies
    ↓
[APPROVAL GATE] ← Human review and approval required
    ↓
tasks.md (FROZEN*)
```

**Key Characteristics**:
- Human-driven (requires approval at each phase)
- Revision cycles within planning (can iterate spec → plan → tasks until approved)
- Output is stable, documented, traceable
- Focus on completeness and correctness

**Flexibility Rule**: After approval, minor task edits allowed:
- ✅ Typo corrections
- ✅ Clarifications (make task clearer without changing scope)
- ❌ Scope changes (adding/removing/reordering tasks requires re-approval)

---

### Process 2: Claude Code Execution (Building)

**Purpose**: Define HOW to build what was specified
**Commands**: `/workflow:*`
**Input**: Approved tasks.md file

```
For Each Task in tasks.md:
    ↓
Research - Understand task, examine codebase, load relevant Skills
    ↓
Implement - Write tests first (TDD), then implementation
    ↓
Verify - Run tests, linters, type checkers
    ↓
[PASS?]
    ↓           ↓
   YES          NO → [Correction Loop]
    ↓                Max 3 attempts
    ↓                Then escalate
    ↓           ↓
Mark Complete  Human Review
    ↓
Next Task
```

**Key Characteristics**:
- Agent-driven (autonomous execution with agentic corrections)
- Correction loops within task scope (fix bugs, improve code)
- Continuous progress without approval gates
- Focus on working, tested code

**Correction Loop Limits**:
- Max 3 verify attempts per task
- After 3 failures: Escalate to human review
- Human decides: Fix task definition, update spec, or provide guidance

---

## Handoff Mechanism

### The Interface: tasks.md

**Format**:
```markdown
# Tasks for [Feature Name]

## Task 1: Create data loader for sales data
**Dependencies**: None
**Success Criteria**:
- Loads CSV and PostgreSQL data
- Handles missing values
- Tests achieve 80%+ coverage

**Files**:
- src/data/sales_loader.py
- tests/unit/test_sales_loader.py

## Task 2: Create bar chart component
**Dependencies**: Task 1
**Success Criteria**:
- Displays sales by region
- Accessible (WCAG 2.1 AA)
- Tests achieve 80%+ coverage

**Files**:
- src/components/sales_chart.py
- tests/unit/test_sales_chart.py
```

**Requirements for tasks.md**:
- ✅ Actionable: Clear what to do
- ✅ Testable: Clear success criteria
- ✅ Ordered: Dependencies resolved
- ✅ Atomic: Each task is self-contained
- ✅ Tracked: Files to create/modify listed

---

## Command Structure

### Spec-Kit Commands (`.claude/commands/spec/`)

| Command | Purpose | Output |
|---------|---------|--------|
| `/spec:specify` | Create feature specification | spec.md |
| `/spec:plan` | Create implementation plan | plan.md |
| `/spec:tasks` | Generate actionable tasks | tasks.md |
| `/spec:validate` | Check spec completeness | Validation report |
| `/spec:review` | Run approval checklist | Review status |

### Claude Code Commands (`.claude/commands/workflow/`)

| Command | Purpose | Loops |
|---------|---------|-------|
| `/workflow:research` | Understand task, examine code | No |
| `/workflow:implement` | Write tests + code (TDD) | No |
| `/workflow:verify` | Run tests, validate | Yes (max 3) |
| `/workflow:next` | Mark complete, move to next | No |
| `/workflow:status` | Show progress against tasks.md | No |

### Utility Commands (`.claude/commands/utils/`)

| Command | Purpose |
|---------|---------|
| `/utils:test` | Run pytest with coverage |
| `/utils:lint` | Run Black, Ruff, mypy |
| `/utils:format` | Auto-format code |
| `/utils:diff` | Show changes since branch |

---

## Agentic Corrections

### Within-Task Corrections (Allowed Freely)

During `/workflow:verify`, if tests fail:

```
Attempt 1:
  Run tests → FAIL (AssertionError in test_sales_loader)
  Analyze failure
  Fix code

Attempt 2:
  Run tests → FAIL (Missing edge case)
  Add edge case handling
  Fix code

Attempt 3:
  Run tests → PASS ✓
  Run linter → PASS ✓
  Coverage check → 85% ✓

→ Task complete
```

**Correction Types**:
- ✅ Fix failing tests
- ✅ Fix linter errors
- ✅ Improve coverage
- ✅ Handle edge cases discovered during testing
- ✅ Refactor for better code quality

### Escalation (After 3 Attempts)

If after 3 verify attempts task still fails:

```
/workflow:verify
→ Attempt 1: FAIL
→ Attempt 2: FAIL
→ Attempt 3: FAIL

[ESCALATION]
→ Stop execution
→ Create escalation report:
  - What was attempted
  - What failed
  - Potential causes
  - Suggested fixes
→ Notify human for review

Human Actions:
  Option 1: Provide guidance, retry
  Option 2: Clarify task in tasks.md (minor edit)
  Option 3: Update spec (major change, requires re-approval)
```

---

## Feedback Loops

### Normal Flow (No Feedback to Planning)

```
Planning: Specify → Plan → Tasks → [Approved]
                                      ↓
Execution: Research → Implement → Verify → Complete
           (corrections within task scope only)
```

**90% of cases**: Execution completes without planning changes

### Exception Flow (Feedback Required)

**Triggers**:
- Task technically impossible (API doesn't exist)
- Dependencies incorrect (Task B needs Task C first)
- Task fundamentally underspecified (unclear what to build)

**Process**:
```
Execution discovers blocker
    ↓
Flag task as BLOCKED
    ↓
Create spec revision request:
  - Describe blocker
  - Suggest spec change
  - Impact analysis
    ↓
Return to Planning Process:
  Update spec.md
  Update plan.md
  Regenerate tasks.md
  Re-approve
    ↓
Resume Execution with updated tasks.md
```

**Governance**: Major blockers only, requires justification

---

## Skills Integration

Skills auto-invoke during both processes:

### Planning Process Skills

- **spec-kit-workflow**: Guides specification creation
- **claude-code-architecture**: Helps design technical approach
- **research-synthesis**: Analyzes reference implementations

### Execution Process Skills

- **data-analysis**: Auto-loads when processing data
- **plotly-viz**: Auto-loads when creating visualizations
- **dash-components**: Auto-loads when building components
- **accessibility-audit**: Auto-loads when checking WCAG
- **performance-optimizer**: Auto-loads when optimizing

**Integration**: Skills enhance both processes automatically without explicit invocation

---

## Example: Complete Workflow

### Scenario: Build Sales Dashboard

#### Phase 1: Planning (Spec-Kit Process)

```bash
# Step 1: Specify
/spec:specify "Sales dashboard with date and region filtering"

Output: specs/003-sales-dashboard/spec.md
- 5 user stories
- 25 functional requirements
- 15 success criteria
- WCAG 2.1 AA requirement

# Step 2: Plan
/spec:plan

Output: specs/003-sales-dashboard/plan.md
- Technical stack: Dash 2.14, Plotly Express, PostgreSQL
- Architecture: Component-based, callback-driven
- 8 components identified
- Data flow documented

# Step 3: Tasks
/spec:tasks

Output: specs/003-sales-dashboard/tasks.md
- 15 tasks generated
- Dependencies resolved
- Success criteria per task
- Files to create listed

# Step 4: Review & Approve
/spec:review

Output: Approval checklist completed
- ✓ Spec complete
- ✓ Plan feasible
- ✓ Tasks actionable
- ✓ Constitutional alignment

[APPROVAL GATE]
→ Mark spec as "Approved"
→ tasks.md is now FROZEN
```

#### Phase 2: Execution (Claude Code Process)

```bash
# Task 1: Create sales data loader

/workflow:research
→ Examines existing loaders
→ data-analysis Skill auto-loads
→ Identifies pandas + psycopg2 pattern

/workflow:implement
→ Writes test first: test_sales_loader.py
  - test_load_from_csv()
  - test_load_from_postgres()
  - test_handle_missing_values()
→ Writes implementation: sales_loader.py

/workflow:verify
→ Attempt 1:
  - Run pytest: FAIL (missing import)
  - Fix: Add pandas import
→ Attempt 2:
  - Run pytest: FAIL (edge case not handled)
  - Fix: Handle empty dataset
→ Attempt 3:
  - Run pytest: PASS ✓
  - Run ruff: PASS ✓
  - Coverage: 87% ✓
→ Task complete

/workflow:next
→ Mark Task 1 complete
→ Move to Task 2

# Task 2: Create bar chart component

/workflow:research
→ plotly-viz Skill auto-loads
→ dash-components Skill auto-loads

/workflow:implement
→ Writes test: test_sales_chart.py
→ Writes component: sales_chart.py

/workflow:verify
→ Attempt 1:
  - Run pytest: PASS ✓
  - Accessibility check: FAIL (missing ARIA labels)
  - Fix: Add aria-label attributes
→ Attempt 2:
  - Run pytest: PASS ✓
  - Accessibility check: PASS ✓
  - Coverage: 82% ✓
→ Task complete

/workflow:next
→ Continue through remaining tasks...
```

#### Phase 3: Exception Handling

```bash
# Task 8: Integrate with Salesforce API

/workflow:research
→ Discovers: Salesforce requires OAuth setup not in spec

/workflow:implement
→ Cannot proceed without OAuth credentials

[ESCALATION]
→ Task BLOCKED
→ Escalation Report:
  - Blocker: OAuth setup required
  - Not specified in spec
  - Suggests adding OAuth task

→ Return to Planning:

  Update spec.md:
    Add FR-26: System MUST support OAuth authentication

  Update plan.md:
    Add OAuth Setup section

  Regenerate tasks.md:
    Insert Task 7.5: Set up OAuth for Salesforce

  Re-approve changes

→ Resume Execution:
  Execute Task 7.5 (OAuth setup)
  Then execute Task 8 (Salesforce integration)
```

---

## Success Metrics

### Planning Process (Spec-Kit)

- **Spec Completeness**: All required sections filled
- **Plan Feasibility**: Technical approach validated
- **Task Quality**: Tasks are actionable, testable, atomic
- **Approval Speed**: Review completes within 2 days

### Execution Process (Claude Code)

- **Task Completion Rate**: 95%+ tasks complete without escalation
- **First-Pass Success**: 70%+ tasks pass verify on attempt 1
- **Escalation Rate**: <5% tasks require spec revision
- **Code Quality**: 100% pass linting, 90%+ achieve 80% coverage
- **Agentic Efficiency**: Average 1.8 verify attempts per task

### Overall Workflow

- **Planning Accuracy**: <10% spec revisions during execution
- **Execution Efficiency**: 0.8 hours per task average
- **Quality**: 0 production bugs from completed tasks
- **Velocity**: 10-15 tasks per week steady state

---

## Governance & Controls

### What Requires Re-Approval

**Major Changes** (Full re-approval required):
- Add/remove tasks from tasks.md
- Change task scope significantly
- Reorder tasks (affects dependencies)
- Change success criteria substantially
- Modify core architecture in plan.md

### What Doesn't Require Re-Approval

**Minor Changes** (Allowed during execution):
- Fix typos in task descriptions
- Clarify ambiguous wording
- Add implementation notes
- Update file paths (if discovered wrong)
- Add edge cases to success criteria

### Escalation Thresholds

**Automatic Escalation**:
- 3 verify failures on same task
- Task blocked by technical impossibility
- Dependencies discovered incorrect

**Optional Escalation**:
- Task takes >4 hours (complexity underestimated)
- Unclear success criteria during implementation
- Test coverage can't reach 80% (need guidance)

---

## Documentation Requirements

### Planning Phase Documentation

- **spec.md**: Complete, approved before execution
- **plan.md**: Technical details, approved before execution
- **tasks.md**: Frozen after approval, minor edits only

### Execution Phase Documentation

- **Code Comments**: Explain non-obvious logic
- **Docstrings**: All functions, classes documented
- **CHANGELOG.md**: Updated per task completion
- **Test Documentation**: Complex test scenarios explained

### Synchronization

**Process**: After each task completion:
1. Update CHANGELOG.md
2. Update component documentation
3. Update inline command help if command changed
4. Flag any documentation drift for review

**Frequency**: Continuous during execution

---

## Troubleshooting

### Problem: Tasks unclear during execution

**Symptom**: Repeated confusion about what task requires

**Solution**:
1. Check if minor clarification sufficient (allowed)
2. If major scope issue, escalate for spec revision
3. Document learnings to improve future task generation

### Problem: Excessive verify failures

**Symptom**: Many tasks hitting 3-attempt limit

**Root Causes**:
- Tasks too ambitious (should split smaller)
- Success criteria too strict
- Insufficient test infrastructure

**Solution**:
1. Review task size in planning phase
2. Adjust success criteria if unrealistic
3. Add infrastructure tasks to plan.md

### Problem: Frequent spec revisions during execution

**Symptom**: >10% tasks trigger spec changes

**Root Causes**:
- Planning phase rushed (insufficient research)
- Technical constraints not discovered
- Requirements changed during execution

**Solution**:
1. Increase research time in planning
2. Create proof-of-concept tasks for risky areas
3. Freeze requirements during execution sprint

---

## Tools & Configuration

### Command Files

```
.claude/commands/
├── spec/
│   ├── specify.md     # Constitution → Specify phase
│   ├── plan.md        # Specify → Plan phase
│   ├── tasks.md       # Plan → Tasks phase
│   ├── validate.md    # Check completeness
│   └── review.md      # Approval checklist
│
├── workflow/
│   ├── research.md    # Understand task
│   ├── implement.md   # Write code (TDD)
│   ├── verify.md      # Validate (max 3 attempts)
│   ├── next.md        # Mark complete, continue
│   └── status.md      # Show progress
│
└── utils/
    ├── test.md        # Run pytest
    ├── lint.md        # Run quality checks
    └── format.md      # Auto-format code
```

### Skills Integration

Skills auto-invoke during appropriate phases:

**Planning Skills** (`.claude/skills/development/`):
- spec-kit-workflow/
- claude-code-architecture/
- research-synthesis/

**Execution Skills** (`.claude/skills/production/`):
- data-analysis/
- plotly-viz/
- dash-components/
- accessibility-audit/
- performance-optimizer/

### Settings

`.claude/settings.json`:
```json
{
  "workflow": {
    "max_verify_attempts": 3,
    "allow_minor_task_edits": true,
    "escalation_timeout_hours": 4
  },
  "permissions": {
    "allow": ["Read(*)", "Write(*)", "Edit(*)", "Bash(git:*)"],
    "deny": ["Bash(rm -rf:*)", "Bash(sudo:*)"]
  }
}
```

---

## Summary

**Two Processes, One Goal**:
- **Spec-Kit**: Plans thoroughly, documents completely, approves carefully
- **Claude Code**: Executes autonomously, corrects intelligently, validates continuously

**Handoff Point**: tasks.md (frozen after approval, minor edits allowed)

**Correction Philosophy**:
- Within-task corrections: Unlimited (fix bugs, improve code)
- Cross-task changes: Escalate for approval (scope changes)

**Success Formula**:
- Good planning → Clear tasks → Smooth execution
- Agentic corrections → High quality → Minimal escalations
- Continuous validation → Early issue detection → Rapid fixes

---

**Status**: This workflow architecture is approved and will be used for all feature development.

**Next**: Implement this workflow in spec 001-claude-code-commands-setup.

**Version**: 1.0.0
**Last Updated**: 2025-11-10
