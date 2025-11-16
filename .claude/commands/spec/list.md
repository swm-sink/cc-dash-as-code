---
name: spec.list
description: List all specifications with status, priority, and dependencies
parameters: []
tools:
  - Glob
  - Read
---

# /spec.list

Display a comprehensive list of all feature specifications with their current status, priority, and dependencies.

## Usage

```
/spec.list
```

## Behavior

This command provides an overview of all specifications in the project:

1. **Scan for specifications**:
   - Use Glob with pattern `specs/*/spec.md`
   - Exclude `specs/memory/` and `specs/templates/` directories

2. **Extract metadata** from each spec.md:
   - Feature number (from directory name)
   - Feature name (from directory name or spec header)
   - Status (**Status**: Draft | Approved | Implemented | etc.)
   - Priority (**Priority**: P0, P1, P2, P3)
   - Implementation phase (if present)
   - Dependencies (**Dependencies**: List of spec numbers)

3. **Sort specifications**:
   - Primary sort: Feature number (ascending)
   - Secondary sort: Priority (P0 > P1 > P2 > P3)

4. **Format output**:
   - Table format for clarity
   - Color coding by status (if terminal supports it):
     - Draft: Yellow
     - Approved: Green
     - Implemented: Blue
   - Highlight dependencies

5. **Summary statistics**:
   - Total specifications
   - Count by status
   - Count by priority

## Examples

Example 1: List all specifications
```
/spec.list
```

Output:
```
Feature Specifications

┌──────┬────────────────────────────────────┬──────────────┬──────────┬────────────────┐
│ #    │ Feature Name                       │ Status       │ Priority │ Dependencies   │
├──────┼────────────────────────────────────┼──────────────┼──────────┼────────────────┤
│ 001  │ Dashboard Foundation               │ Approved     │ P2       │ 002, 003, 004  │
│ 002  │ Claude Code Commands Setup         │ Approved     │ P1       │ None           │
│ 003  │ Agent Skills - Development         │ Approved     │ P1       │ 002            │
│ 004  │ Agent Skills - Production          │ Approved     │ P1       │ 002            │
│ 005  │ MCP Integration                    │ Approved     │ P3       │ None           │
│ 006  │ Sales Analytics Dashboard          │ Draft        │ P2       │ 001            │
└──────┴────────────────────────────────────┴──────────────┴──────────┴────────────────┘

Summary:
- Total: 6 specifications
- Status: 5 Approved, 1 Draft
- Priority: 0 P0, 4 P1, 2 P2, 1 P3

Implementation Order:
1. Spec 002 (Phase 1) - Commands Setup
2. Spec 003 (Phase 2) - Development Skills
3. Spec 004 (Phase 3) - Production Skills
4. Spec 005 (Phase 4) - MCP Integration (optional)
5. Spec 001 (Phase 5) - Dashboard Foundation
6. Spec 006 (Phase 6) - Sales Analytics

Next Actions:
- Complete Spec 002 implementation (currently in progress)
- Begin Spec 003 after 002 is done
```

Example 2: Filter by status (conceptual - for future enhancement)
```
/spec.list --status=Draft
```

Output:
```
Feature Specifications (Draft only)

┌──────┬────────────────────────────────────┬──────────────┬──────────┬────────────────┐
│ #    │ Feature Name                       │ Status       │ Priority │ Dependencies   │
├──────┼────────────────────────────────────┼──────────────┼──────────┼────────────────┤
│ 006  │ Sales Analytics Dashboard          │ Draft        │ P2       │ 001            │
└──────┴────────────────────────────────────┴──────────────┴──────────┴────────────────┘

Summary: 1 Draft specification
```

## Output

**Table Columns**:
- **#**: Feature number (3-digit zero-padded)
- **Feature Name**: Human-readable feature name
- **Status**: Current status (Draft, Approved, Implemented, etc.)
- **Priority**: Implementation priority (P0-P3)
- **Dependencies**: Comma-separated list of dependent spec numbers

**Summary Section**:
- Total count
- Breakdown by status
- Breakdown by priority

**Implementation Order**:
- Suggested implementation sequence based on dependencies
- Highlights current phase

**Next Actions**:
- Recommendations for what to work on next

## Implementation Notes

**Metadata Extraction**:
The command reads spec.md files to extract metadata. Expected format:

```markdown
**Feature #**: 002
**Feature Name**: Claude Code Commands Setup
**Status**: Approved
**Priority**: P1
**Dependencies**: None
```

If metadata is not in expected format, the command attempts to:
- Extract feature number from directory name (`002-feature-name`)
- Extract feature name from directory name
- Default status to "Unknown"
- Default priority to "Unspecified"

**Dependency Resolution**:
Dependencies are parsed from the spec.md Dependencies section:
```markdown
## Dependencies
- **Spec 002**: Claude Code Commands Setup (must be complete first)
- **Spec 003**: Agent Skills - Development (required for skill activation)
```

## See Also

- `/spec.create` - Create new specification
- `/spec.validate` - Validate specification
- `/spec.show [number]` - Display specific specification
- `/spec.branch [number]` - Create feature branch
- `specs/WORKFLOW.md` - Specification workflow documentation
