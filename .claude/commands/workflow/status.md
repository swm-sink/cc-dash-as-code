---
name: workflow.status
description: Display feature requirement completion progress and implementation coverage
parameters: []
tools:
  - Read
  - Grep
  - Glob
---

# /workflow.status

Display comprehensive progress report for the current feature, showing requirement completion and implementation coverage.

## Usage

```
/workflow.status
```

## Purpose

This command provides a high-level view of feature implementation progress:
- Which requirements are complete
- Which requirements are in progress
- Which requirements are missing
- Overall completion percentage
- Success criteria achievement

## Behavior

This command analyzes implementation progress:

1. **Determine Current Feature**:
   - Extract feature number from git branch
   - Or detect from current directory
   - Or prompt for feature number

2. **Load Specification**:
   - Read `specs/{number}-{name}/spec.md`
   - Extract all functional requirements (FR-NNN)
   - Extract all success criteria (SC-NNN)
   - Note requirement priorities

3. **Search Codebase for Requirements**:
   - Use Grep to search for requirement IDs in:
     - Source code comments: `# FR-023`
     - Docstrings: `"""... Implements FR-023 ..."""`
     - Test names: `def test_fr023_filter_validation():`
     - Module documentation
   - Use Glob to find all relevant files in `src/` and `tests/`

4. **Categorize Requirements**:
   - **Implemented**: Found in code with passing tests
   - **In Progress**: Found in code but tests failing or incomplete
   - **Missing**: Not found in codebase

5. **Verify Success Criteria**:
   - Check if measurable targets are met
   - Examples:
     - "80% test coverage" → Check pytest coverage report
     - "Load time <3s" → Check performance test results
     - "WCAG 2.1 AA" → Check accessibility audit results

6. **Generate Completion Report**:
   - Overall progress (percentage)
   - Requirement-by-requirement status
   - Success criteria achievement
   - Recommendations for next steps

## Examples

Example 1: Mid-implementation progress
```
/workflow.status
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Feature Implementation Status
════════════════════════════════════════════════════════════════════════════

Feature: 002-claude-code-commands-setup
Branch: 002-claude-code-commands-setup
Status: In Progress

Overall Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Functional Requirements: 25/60 implemented (42%)
  ████████████████░░░░░░░░░░░░░░░░░░░░

  Success Criteria: 8/15 achieved (53%)
  █████████████████████░░░░░░░░░░░░░░░░░░

  Tasks: 28/60 completed (47%)
  ██████████████████░░░░░░░░░░░░░░░░░░░░

Functional Requirements Breakdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Implemented (25 requirements)

  Directory Structure (5/5):
    ✓ FR-001: .claude/ directory creation
    ✓ FR-002: commands/ subdirectories
    ✓ FR-003: agents/ directory
    ✓ FR-004: skills/ directory structure
    ✓ FR-005: README documentation

  Spec Commands (5/5):
    ✓ FR-006: /spec.create command
    ✓ FR-007: /spec.validate command
    ✓ FR-008: /spec.list command
    ✓ FR-009: /spec.show command
    ✓ FR-010: /spec.branch command

  Workflow Commands (6/6):
    ✓ FR-011: /workflow.observe command
    ✓ FR-012: /workflow.act command
    ✓ FR-013: /workflow.verify command
    ✓ FR-014: /workflow.loop command
    ✓ FR-015: /workflow.status command
    ✓ FR-016: /workflow.checkpoint command

  Utility Commands (6/6):
    ✓ FR-017: /utils.test command
    ✓ FR-018: /utils.lint command
    ✓ FR-019: /utils.format command
    ✓ FR-020: /utils.check-deps command
    ✓ FR-021: /utils.commit command
    ✓ FR-022: /utils.diff command

  Dash Commands (3/3):
    ✓ FR-023: /dash.component command
    ✓ FR-024: /dash.layout command
    ✓ FR-025: /dash.callback command

🔶 In Progress (8 requirements)

  Sub-Agents (3/3):
    → FR-026: component-builder agent (file created, needs testing)
    → FR-027: data-pipeline agent (file created, needs testing)
    → FR-028: test-engineer agent (file created, needs testing)

  Settings & Configuration (5/10):
    → FR-029: settings.json creation (structure defined)
    → FR-030: permissions configuration (in progress)
    ○ FR-031: code quality settings (not started)
    ○ FR-032: workflow settings (not started)
    ○ FR-033: security settings (not started)

⭕ Missing (27 requirements)

  Command Implementation Details (10/30):
    ○ FR-034: Auto-increment feature numbers (spec.create)
    ○ FR-035: Template population (spec.create)
    ○ FR-036: Constitutional validation (spec.validate)
    ○ FR-037: Dependency parsing (spec.list)
    ○ FR-038: Git integration (spec.branch)
    ○ FR-039: Task analysis (workflow.observe)
    ○ FR-040: TDD workflow (workflow.act)
    ○ FR-041: Multi-tool verification (workflow.verify)
    ○ FR-042: Commit automation (workflow.loop)
    ○ FR-043: Progress tracking (workflow.status)
    ... (20 more requirements)

Success Criteria Achievement
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Achieved (8 criteria)

  ✓ SC-001: All 16 commands created
    Status: Complete (16/16 command files exist)

  ✓ SC-002: Directory structure complete
    Status: Complete (all directories created)

  ✓ SC-003: YAML frontmatter valid
    Status: Complete (validated with parser)

  ✓ SC-004: Documentation complete
    Status: Complete (all sections present in commands)

  ✓ SC-005: Cross-references present
    Status: Complete ("See Also" sections in all commands)

  ✓ SC-006: Examples provided
    Status: Complete (avg 2.5 examples per command)

  ✓ SC-007: Error handling documented
    Status: Complete (error scenarios in all commands)

  ✓ SC-008: Workflow integration tested
    Status: Complete (TEST_RESULTS.md validates)

⭕ Not Yet Achieved (7 criteria)

  → SC-009: Sub-agents functional
    Status: Partial (files created, not tested)
    Target: All 3 sub-agents working
    Current: 0/3 tested

  ○ SC-010: Settings.json complete
    Status: Not started
    Target: All configuration sections present
    Current: 0/8 sections

  ○ SC-011: Skills integration ready
    Status: Not started (placeholder READMEs only)
    Target: Skill activation mechanisms defined
    Current: Directory structure only

  ○ SC-012: 80% test coverage
    Status: Not measured yet
    Target: ≥80% coverage for command logic
    Current: 0% (no tests written yet)

  ○ SC-013: Performance targets
    Status: Not measured
    Target: Command execution <2s
    Current: Not benchmarked

  ○ SC-014: Git integration tested
    Status: Not tested
    Target: Branch creation, commit automation working

  ○ SC-015: Documentation deployed
    Status: Not deployed
    Target: README.md and CLAUDE.md published

Implementation Timeline
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✅ Phase 1: Directory Structure (Complete - 100%)
  ✅ Phase 2: Spec Commands (Complete - 100%)
  ✅ Phase 3: Workflow Commands (Complete - 100%)
  ✅ Phase 4: Utility Commands (Complete - 100%)
  ✅ Phase 5: Dash Commands (Complete - 100%)
  → Phase 6: Sub-Agents (In Progress - 40%)
  ○ Phase 7: Settings (Not Started - 0%)
  ○ Phase 8: Integration & Validation (Not Started - 0%)

Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Immediate Next Steps:
  1. Complete Phase 6: Sub-Agents
     - Test component-builder agent
     - Test data-pipeline agent
     - Test test-engineer agent
     → Addresses: FR-026, FR-027, FR-028, SC-009

  2. Start Phase 7: Settings
     - Create settings.json with all sections
     - Define permissions and tool access
     - Configure code quality settings
     → Addresses: FR-029 to FR-033, SC-010

  3. Begin Phase 8: Integration Testing
     - Write tests for command logic
     - Benchmark performance
     - Validate git integration
     → Addresses: SC-012, SC-013, SC-014

Estimated Remaining Time: 8-12 hours (3-4 phases)

Next Command: /workflow.observe (to see specific next task)

════════════════════════════════════════════════════════════════════════════
```

Example 2: Feature complete
```
/workflow.status
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Feature Implementation Status
════════════════════════════════════════════════════════════════════════════

Feature: 002-claude-code-commands-setup
Branch: 002-claude-code-commands-setup
Status: ✅ Complete

Overall Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Functional Requirements: 60/60 implemented (100%)
  ████████████████████████████████████████

  Success Criteria: 15/15 achieved (100%)
  ████████████████████████████████████████

  Tasks: 60/60 completed (100%)
  ████████████████████████████████████████

🎉 All Requirements Implemented! 🎉

Functional Requirements: All 60 requirements complete
Success Criteria: All 15 criteria achieved

Implementation Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✅ Phase 1: Directory Structure (100%)
  ✅ Phase 2: Spec Commands (100%)
  ✅ Phase 3: Workflow Commands (100%)
  ✅ Phase 4: Utility Commands (100%)
  ✅ Phase 5: Dash Commands (100%)
  ✅ Phase 6: Sub-Agents (100%)
  ✅ Phase 7: Settings (100%)
  ✅ Phase 8: Integration & Validation (100%)

Quality Metrics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✓ Test Coverage: 87% (target: 80%)
  ✓ WCAG 2.1 AA: Compliant
  ✓ Command Performance: <2s (target: <2s)
  ✓ Documentation: Complete
  ✓ Git Integration: Tested and working

Next Steps
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. Final validation: /workflow.verify
  2. Push to remote: git push -u origin 002-claude-code-commands-setup
  3. Create pull request
  4. Move to next feature: /spec.list

Congratulations! Feature 002 is complete! 🎊

════════════════════════════════════════════════════════════════════════════
```

Example 3: Early in development
```
/workflow.status
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Feature Implementation Status
════════════════════════════════════════════════════════════════════════════

Feature: 001-dashboard-foundation
Branch: 001-dashboard-foundation
Status: Just Started

Overall Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Functional Requirements: 2/39 implemented (5%)
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

  Success Criteria: 0/23 achieved (0%)
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

  Tasks: 3/58 completed (5%)
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

You're just getting started! Keep going! 💪

Functional Requirements Breakdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Implemented (2 requirements)

  Setup (2/5):
    ✓ FR-001: Project directory structure created
    ✓ FR-002: requirements.txt populated

⭕ Missing (37 requirements)

  Setup (3/5):
    ○ FR-003: pytest configuration
    ○ FR-004: Black/Ruff configuration
    ○ FR-005: Git hooks setup

  ... (34 more requirements across 8 categories)

Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Focus Areas:
  1. Complete setup phase (FR-003 to FR-005)
  2. Begin data infrastructure (FR-006 to FR-012)
  3. Set up testing infrastructure (FR-013 to FR-015)

Estimated Remaining Time: 35-40 hours

Next Command: /workflow.observe

════════════════════════════════════════════════════════════════════════════
```

## Output

**Overall Progress**:
- Requirements percentage with progress bar
- Success criteria percentage with progress bar
- Tasks percentage with progress bar

**Requirements Breakdown**:
- **Implemented**: Complete list with checkmarks
- **In Progress**: Partial implementations
- **Missing**: Not yet started

**Success Criteria**:
- **Achieved**: Met with measurements
- **Not Achieved**: Missing with targets and current values

**Timeline**:
- Phase completion status
- Current phase indicator

**Recommendations**:
- Immediate next steps
- Focus areas
- Estimated remaining time

## Use Cases

1. **Daily standup**: Quick progress summary
2. **Sprint planning**: Identify what's left
3. **Code review**: Verify requirement coverage
4. **Stakeholder updates**: Progress reporting
5. **Debugging**: Find missing requirements

## See Also

- `/workflow.observe` - Identify next task
- `/workflow.act` - Implement requirements
- `/workflow.verify` - Validate quality
- `/workflow.loop` - Continue development
- `/spec.show [number]` - View full specification
- `specs/{number}-{name}/spec.md` - Specification details
