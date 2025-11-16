---
name: spec.create
description: Create a new feature specification with unique feature number following spec-kit methodology
parameters:
  - name: description
    description: Brief description of the feature to create (will be sanitized to kebab-case)
    required: true
    type: string
tools:
  - Glob
  - Bash
  - Read
  - Write
---

# /spec.create

Create a new feature specification with auto-incremented feature number following spec-kit methodology.

## Usage

```
/spec.create [description]
```

## Behavior

This command automates the creation of a new feature specification:

1. **Find existing specs**: Uses Glob to scan `specs/` directory for existing specifications
2. **Auto-increment feature number**: Extracts the highest feature number and increments by 1 (e.g., 005 → 006)
3. **Sanitize name**: Converts description to kebab-case for directory naming
4. **Create directory**: Creates `specs/{number}-{kebab-case-name}/` directory structure
5. **Load template**: Reads `specs/templates/spec-template.md` (if exists) or generates from standard structure
6. **Populate spec.md**: Creates `specs/{number}-{name}/spec.md` with:
   - Feature metadata (number, name, status: Draft)
   - Standard sections (Overview, User Scenarios, Requirements, Success Criteria, Edge Cases)
   - Placeholder content for manual completion
7. **Create README**: Generates `specs/{number}-{name}/README.md` with overview
8. **Constitutional review**: Reads `specs/memory/constitution.md` and checks alignment
9. **Output**: Success message with file path and next steps

## Examples

Example 1: Create a sales dashboard specification
```
/spec.create Build a sales analytics dashboard with regional filters
```

Output:
```
Created Spec 006: Build a sales analytics dashboard with regional filters

Location: specs/006-sales-analytics-dashboard-with-regional-filters/spec.md

Next steps:
1. Edit spec.md to complete all sections:
   - Add user scenarios and testing details
   - Define functional requirements (FR-001, FR-002, etc.)
   - Define measurable success criteria (SC-001, SC-002, etc.)
   - Document edge cases and clarifications
2. Create plan.md with technical implementation approach
3. Create tasks.md with task breakdown
4. Run /spec.validate to check completeness
5. Mark spec.md Status as "Approved" when ready
6. Run /spec.branch 006 to create feature branch
```

Example 2: Create a data integration specification
```
/spec.create Integrate PostgreSQL data source for customer analytics
```

## Output

**Success**:
- New directory created: `specs/{number}-{name}/`
- `spec.md` file with template structure
- `README.md` file with overview
- Success message with next steps

**Error Conditions**:
- Invalid description (empty or too short)
- File system errors
- Missing templates directory (will generate default structure)

## Related Sections

**Constitution Alignment**:
The command automatically checks that the specification outline aligns with:
- Core Principle 1: Specification-driven development
- Core Principle 10: Documentation-first approach

**Spec-Kit Methodology**:
Follows GitHub's spec-kit approach:
1. Specification defines the "what" and "why"
2. Plan defines the "how" (technical approach)
3. Tasks define the "when" (granular steps)

## See Also

- `/spec.validate` - Validate specification completeness
- `/spec.list` - List all specifications
- `/spec.show` - Display full specification content
- `/spec.branch` - Create feature branch from spec
- `specs/templates/spec-template.md` - Specification template
- `specs/memory/constitution.md` - Project principles
