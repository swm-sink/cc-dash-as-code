---
name: spec.show
description: Display the full content of a specification by feature number
parameters:
  - name: feature-number
    description: Three-digit feature number (e.g., 001, 002, 006)
    required: true
    type: string
tools:
  - Glob
  - Read
---

# /spec.show

Display the complete content of a feature specification.

## Usage

```
/spec.show [feature-number]
```

**Arguments**:
- `feature-number`: Three-digit feature number (e.g., 001, 002, 006)

## Behavior

This command retrieves and displays a complete specification:

1. **Validate input**:
   - Check feature-number format (must be 3 digits: 001-999)
   - Sanitize input to prevent path traversal

2. **Locate specification**:
   - Use Glob to find `specs/{number}-*/spec.md`
   - Handle cases where multiple matches found (error)
   - Handle cases where no match found (error)

3. **Load specification**:
   - Read complete spec.md content

4. **Format output**:
   - Display full specification with syntax highlighting (if supported)
   - Optionally highlight key sections:
     - Feature metadata header
     - User scenarios
     - Functional requirements (FR-NNN)
     - Success criteria (SC-NNN)
     - Dependencies
     - Edge cases

5. **Add navigation hints**:
   - Show file path for reference
   - Suggest related commands
   - If spec has plan.md or tasks.md, mention them

## Examples

Example 1: Show Spec 002
```
/spec.show 002
```

Output:
```
═══════════════════════════════════════════════════════════════════════════════
Specification: 002-claude-code-commands-setup
Location: specs/002-claude-code-commands-setup/spec.md
═══════════════════════════════════════════════════════════════════════════════

# Feature Specification: Claude Code Commands Setup

**Feature #**: 002
**Feature Name**: Claude Code Commands Setup
**Status**: Approved
**Priority**: P1 (Phase 1 - Implement FIRST)
**Estimated Effort**: 40 hours (1 week)
**Dependencies**: None
**Related Specs**: 003 (Agent Skills - Development), 004 (Agent Skills - Production)

## Overview

Configure Claude Code with custom slash commands, sub-agents, and configuration
files to accelerate dashboard development following the spec-kit methodology and
EPIC workflow.

[... full spec.md content continues ...]

═══════════════════════════════════════════════════════════════════════════════
Related Files:
  - Plan: specs/002-claude-code-commands-setup/plan.md
  - Tasks: specs/002-claude-code-commands-setup/tasks.md
  - README: specs/002-claude-code-commands-setup/README.md

Next Actions:
  - Validate: /spec.validate
  - Create branch: /spec.branch 002
  - List all specs: /spec.list
═══════════════════════════════════════════════════════════════════════════════
```

Example 2: Show spec that doesn't exist
```
/spec.show 099
```

Output:
```
Error: Specification 099 not found

Searched: specs/099-*/spec.md
Found: No matches

Available specifications:
  - 001: Dashboard Foundation
  - 002: Claude Code Commands Setup
  - 003: Agent Skills - Development
  - 004: Agent Skills - Production
  - 005: MCP Integration

Use /spec.list to see all specifications.
```

Example 3: Show spec without plan.md
```
/spec.show 006
```

Output:
```
═══════════════════════════════════════════════════════════════════════════════
Specification: 006-sales-analytics-dashboard
Location: specs/006-sales-analytics-dashboard/spec.md
═══════════════════════════════════════════════════════════════════════════════

# Feature Specification: Sales Analytics Dashboard

[... spec.md content ...]

═══════════════════════════════════════════════════════════════════════════════
Note: This specification is missing plan.md and tasks.md

Next Actions:
  1. Create plan.md with technical implementation approach
  2. Create tasks.md with granular task breakdown
  3. Run /spec.validate to check completeness
  4. Update Status to "Approved" when ready
  5. Create feature branch: /spec.branch 006

See: specs/templates/ for plan and task templates
═══════════════════════════════════════════════════════════════════════════════
```

## Output

**Main Content**:
- Header with spec metadata
- Full spec.md content
- Footer with related files and next actions

**Error Messages**:
- Feature number not found
- Invalid feature number format
- File read errors

**Navigation Hints**:
- Related files (plan.md, tasks.md)
- Suggested next commands
- Links to templates if files missing

## Advanced Features

**Section Highlighting** (optional enhancement):
When displaying the spec, the command can optionally highlight key sections:
- Requirements (FR-NNN) in one color
- Success criteria (SC-NNN) in another color
- Dependencies in bold
- Status and priority emphasized

**Quick Summary** (optional parameter for future):
```
/spec.show 002 --summary
```
Would show only:
- Metadata
- Overview
- Requirements count
- Success criteria count
- Status

## See Also

- `/spec.create` - Create new specification
- `/spec.validate` - Validate specification
- `/spec.list` - List all specifications
- `/spec.branch [number]` - Create feature branch
- `specs/{number}-{name}/plan.md` - Technical plan (if exists)
- `specs/{number}-{name}/tasks.md` - Task breakdown (if exists)
