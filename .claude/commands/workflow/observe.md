---
name: workflow.observe
description: Analyze current state and identify next actionable tasks (EPIC - Observe phase)
parameters: []
tools:
  - Bash
  - Read
  - Glob
  - Grep
---

# /workflow.observe

Analyze the current feature implementation state and identify the next actionable task following EPIC methodology.

## Usage

```
/workflow.observe
```

## EPIC Methodology

**EPIC** = **O**bserve → **A**ct → **V**erify → **L**oop

This command implements the **Observe** phase:
- Analyze current progress
- Compare implemented vs planned
- Identify next actionable task
- Provide context and guidance

## Behavior

This command performs comprehensive progress analysis:

1. **Determine current feature**:
   - Extract feature number from current git branch
   - Or detect from current directory (if in `specs/{number}-{name}/`)
   - Or prompt user to specify feature number

2. **Load specification files**:
   - Read `specs/{number}-{name}/spec.md`
   - Read `specs/{number}-{name}/plan.md` (if exists)
   - Read `specs/{number}-{name}/tasks.md` (if exists)
   - Extract requirements (FR-NNN) and success criteria (SC-NNN)

3. **Analyze implemented code**:
   - Use Glob to find all files in `src/` and `tests/`
   - Use Grep to search for requirement IDs (FR-NNN) in:
     - Code comments
     - Docstrings
     - Test function names
     - Module documentation

4. **Compare progress**:
   - **Completed tasks**: Tasks marked as done in tasks.md or implemented in code
   - **In-progress tasks**: Partially implemented features
   - **Pending tasks**: Not yet started
   - **Requirements coverage**: Which FR-NNN are implemented vs missing

5. **Identify next task**:
   - Select highest-priority pending task from tasks.md
   - Or identify logical next step based on dependencies
   - Ensure task is actionable and well-defined

6. **Generate analysis report**:
   - Current progress summary (percentage complete)
   - Completed requirements and tasks
   - Next recommended task with context
   - Implementation guidance
   - Dependencies and prerequisites

## Examples

Example 1: Observe at start of feature (no code yet)
```
/workflow.observe
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Observe Phase
════════════════════════════════════════════════════════════════════════════

Feature: 002-claude-code-commands-setup
Branch: 002-claude-code-commands-setup
Status: In Progress

Progress Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Requirements:  0/60 implemented (0%)
  Success Criteria: 0/15 achieved (0%)
  Tasks: 0/60 completed (0%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Implementation Status:
  ✓ Phase 1: Directory Structure (Complete)
  → Phase 2: Spec Commands (In Progress)
  ○ Phase 3: Workflow Commands (Not Started)
  ○ Phase 4: Utility Commands (Not Started)
  ○ Phase 5: Dash Commands (Not Started)

Completed Requirements: None yet

Next Recommended Task:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Task: T007 - Implement /spec.create command
Type: Command Implementation
Size: Medium (1-3 hours)
Priority: High
Dependencies: T001-T006 (Complete ✓)

Description:
Create .claude/commands/spec/create.md following the command file format.
Implement logic to auto-increment feature numbers, create spec directories,
and populate spec.md from template.

Addresses Requirements:
- FR-001: Slash command support for spec.create
- FR-006: Auto-increment feature numbers
- FR-011: Spec template generation

Context:
- Directory structure is ready (.claude/commands/spec/ exists)
- Template should be at specs/templates/spec-template.md
- Follow format defined in plan.md

Implementation Guidance:
1. Use TDD: Write tests first in tests/commands/test_spec_create.py
2. Create command file with YAML frontmatter
3. Document usage, behavior, examples
4. Ensure constitutional alignment check

Tools Needed: Write, Read, Glob, Bash
Skills: spec-kit-workflow (auto-activates)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Step: /workflow.act Implement /spec.create command

════════════════════════════════════════════════════════════════════════════
```

Example 2: Observe mid-implementation (some tasks complete)
```
/workflow.observe
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Observe Phase
════════════════════════════════════════════════════════════════════════════

Feature: 001-dashboard-foundation
Branch: 001-dashboard-foundation
Status: In Progress

Progress Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Requirements:  15/39 implemented (38%)
  Success Criteria: 6/23 achieved (26%)
  Tasks: 23/58 completed (40%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recent Completions:
  ✓ FR-012: Data loading from CSV (implemented in src/data/loaders.py)
  ✓ FR-013: DataFrame validation (implemented in src/data/validators.py)
  ✓ SC-003: Load 1M rows in <5s (test passing at 3.2s)

In Progress:
  → FR-014: Data transformation pipeline (partially implemented)
    Status: Core pipeline exists, missing error handling
    Files: src/data/transformers.py (65% complete)

Missing Requirements (High Priority):
  ○ FR-015: Data caching strategy
  ○ FR-016: Cache invalidation logic
  ○ FR-017: Filter component creation

Next Recommended Task:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Task: T024 - Complete data transformation error handling
Type: Enhancement
Size: Small (<1 hour)
Priority: High
Dependencies: T021-T023 (Complete ✓)

Description:
Add comprehensive error handling to data transformation pipeline:
- Validate input data types
- Handle missing columns gracefully
- Add transformation failure recovery
- Log all errors with context

Addresses Requirements:
- FR-014: Data transformation pipeline (completion)
- FR-018: Error handling (partial)

Context:
- Core transformation logic exists in src/data/transformers.py:45-120
- Add error handling around lines 67, 89, 105
- Follow error handling patterns from specs/memory/patterns.md

Implementation Guidance:
1. Add try/except blocks with specific exceptions
2. Create custom TransformationError exception class
3. Add tests for error scenarios
4. Ensure all edge cases from spec.md are covered

Files to Modify:
- src/data/transformers.py (add error handling)
- src/data/exceptions.py (create new file for custom exceptions)
- tests/unit/data/test_transformers.py (add error test cases)

Estimated Time: 45-60 minutes
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Step: /workflow.act Complete data transformation error handling

════════════════════════════════════════════════════════════════════════════
```

Example 3: No current feature detected
```
/workflow.observe
```

Output:
```
Error: No feature context detected

Current branch: main
Current directory: /home/user/cc-dash-as-code

To use /workflow.observe, you must be:
1. On a feature branch (e.g., 002-claude-code-commands-setup)
2. Or in a spec directory (e.g., specs/002-claude-code-commands-setup/)

Options:
- Create feature branch: /spec.branch [feature-number]
- Switch to existing branch: git checkout [branch-name]
- List available specs: /spec.list

Available feature branches:
  - 002-claude-code-commands-setup
  - 001-dashboard-foundation
```

## Output

**Progress Summary**:
- Requirements coverage (implemented vs total)
- Success criteria achievement
- Task completion percentage

**Status Breakdown**:
- Completed tasks/requirements
- In-progress items
- Pending items

**Next Task Details**:
- Task ID and description
- Type, size, priority
- Dependencies (with status)
- Requirements addressed
- Implementation guidance
- Files to create/modify
- Estimated time

**Navigation**:
- Suggested next command (`/workflow.act`)
- Links to relevant files
- Context for decision-making

## Integration with EPIC Workflow

**Observe** is the first step in the EPIC cycle:

```
Observe ───→ Act ───→ Verify ───→ Loop
   ↑                                 │
   └─────────────────────────────────┘
```

**Flow**:
1. `/workflow.observe` - Analyze and identify task
2. `/workflow.act` - Implement the task
3. `/workflow.verify` - Validate implementation
4. `/workflow.loop` - Commit and repeat (calls observe again)

## Analysis Algorithm

The command uses a sophisticated analysis algorithm:

1. **Requirement Tracking**:
   - Searches code for `# FR-NNN` comments
   - Searches docstrings for requirement references
   - Matches test names to requirements

2. **Task Completion Detection**:
   - Checks tasks.md for checkboxes: `- [x] Task description`
   - Verifies implementation files exist
   - Confirms tests are passing

3. **Dependency Resolution**:
   - Parses task dependencies from tasks.md
   - Ensures prerequisites are complete before recommending tasks
   - Respects parallel vs sequential task ordering

4. **Priority Calculation**:
   - High priority: Blocking tasks or critical path items
   - Medium priority: Non-blocking enhancements
   - Low priority: Nice-to-have features

## See Also

- `/workflow.act` - Implement identified task (next step)
- `/workflow.verify` - Validate implementation
- `/workflow.loop` - Complete cycle and continue
- `/workflow.status` - View overall requirement completion
- `/spec.show [number]` - View specification details
- `specs/{number}-{name}/plan.md` - Technical plan
- `specs/{number}-{name}/tasks.md` - Task breakdown
