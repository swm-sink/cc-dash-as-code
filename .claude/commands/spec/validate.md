---
name: spec.validate
description: Check specification completeness, format compliance, and constitutional alignment
parameters: []
tools:
  - Glob
  - Read
---

# /spec.validate

Validate a specification for completeness, format compliance, and alignment with project constitution.

## Usage

```
/spec.validate
```

Validates the specification in the current context (based on current directory or git branch).

## Behavior

This command performs comprehensive specification validation:

1. **Locate specification**:
   - Check current directory for spec.md
   - Or extract feature number from git branch name
   - Or prompt for specification to validate

2. **Load specification**: Read spec.md content

3. **Structure validation**:
   - Check all required sections are present:
     - Feature Metadata (Feature #, Name, Status, Priority, etc.)
     - Overview
     - User Scenarios & Testing
     - Functional Requirements
     - Success Criteria
     - Dependencies (if applicable)
     - Edge Cases & Clarifications
   - Verify section ordering and completeness

4. **Requirements validation**:
   - Check all requirements have unique IDs (FR-001, FR-002, etc.)
   - Verify FR-NNN format (3-digit zero-padded)
   - Ensure requirements are clear and actionable
   - Check for duplicate requirement IDs

5. **Success criteria validation**:
   - Check all criteria have unique IDs (SC-001, SC-002, etc.)
   - Verify criteria are measurable (contain numbers, percentages, time targets)
   - Examples of measurable criteria:
     - "80% test coverage"
     - "Load time < 3 seconds"
     - "WCAG 2.1 AA compliance"

6. **Constitutional alignment**:
   - Load `specs/memory/constitution.md`
   - Check spec references core principles
   - Verify quality standards are met:
     - 80% test coverage mentioned
     - WCAG 2.1 AA compliance for UI features
     - Performance targets specified (<3s load, <1s callbacks)
     - Security considerations documented

7. **Generate validation report**:
   - Summary (pass/fail)
   - Detailed findings
   - Missing or incomplete sections
   - Non-compliant requirements
   - Recommendations for improvement

## Examples

Example 1: Validate current specification
```
/spec.validate
```

Output (passing):
```
✓ Specification Validation Report

Specification: 002-claude-code-commands-setup
Status: PASS

Checks:
  ✓ All required sections present (7/7)
  ✓ Requirements format valid (60 requirements, FR-001 to FR-060)
  ✓ Success criteria measurable (15 criteria, SC-001 to SC-015)
  ✓ Constitutional alignment verified
    - References Core Principles 1, 2, 10
    - Quality standards defined (80% coverage, WCAG 2.1 AA)
    - Testing requirements specified

Recommendations: None

The specification is complete and ready for implementation.
```

Example 2: Validate with issues
```
/spec.validate
```

Output (failing):
```
✗ Specification Validation Report

Specification: 007-analytics-dashboard
Status: FAIL (3 issues found)

Issues:

1. CRITICAL: Missing required section "Success Criteria"
   Location: Expected after "Functional Requirements"
   Fix: Add "## Success Criteria" section with measurable targets

2. WARNING: Requirements missing IDs
   Location: Lines 45-52 (8 requirements)
   Format: Requirements must have format "FR-001:", "FR-002:", etc.
   Fix: Add unique FR-NNN identifiers to all requirements

3. INFO: Success criteria not measurable
   Location: SC-003, SC-007
   Examples: "Dashboard should be fast" → "Dashboard loads in <3s"
   Fix: Add specific numbers, percentages, or time targets

4. WARNING: No constitutional alignment
   Missing: Reference to Core Principles
   Fix: Add "## Constitutional Alignment" section or reference principles in Overview

Recommendations:
- Complete all required sections
- Add FR-NNN IDs to all requirements
- Make success criteria measurable
- Reference constitution.md principles

Run /spec.validate again after addressing these issues.
```

## Output

**Validation Report Structure**:
- Header: Specification name and overall status (PASS/FAIL)
- Checks: List of validation checks with pass/fail indicators
- Issues: Detailed list of problems found (if any)
  - CRITICAL: Missing required sections
  - WARNING: Format violations, missing IDs
  - INFO: Suggestions for improvement
- Recommendations: Next steps to resolve issues
- Footer: Status message

**Pass Criteria**:
A specification passes validation when:
- All required sections are present
- All requirements have unique FR-NNN IDs
- All success criteria have unique SC-NNN IDs
- Success criteria are measurable
- Constitutional principles are referenced

## See Also

- `/spec.create` - Create new specification
- `/spec.list` - List all specifications
- `/spec.show` - Display full specification
- `specs/memory/constitution.md` - Project principles and standards
- `specs/templates/spec-template.md` - Specification template
