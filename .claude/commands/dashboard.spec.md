---
allowed-tools: Read, Write, Bash(git:*), Glob
description: Create a new feature specification following spec-kit methodology
argument-hint: <feature description>
---

# Create Feature Specification

You are creating a new feature specification for a Plotly Dash dashboard following the spec-kit methodology.

## Current Project Context

- Project Constitution: !`cat .specify/memory/constitution.md`
- Existing Specifications: !`ls -1 .specify/specs/ 2>/dev/null || echo "No specs yet"`
- Current Branch: !`git branch --show-current`

## Your Task

**Input**: $ARGUMENTS (feature description from user)

**Steps to Execute:**

1. **Generate unique feature number**
   - Check existing specs in `.specify/specs/`
   - Assign next available number (e.g., 003, 004, 005)

2. **Create feature directory**
   - Format: `.specify/specs/{number}-{kebab-case-name}/`
   - Example: `.specify/specs/003-sales-analytics-dashboard/`

3. **Copy and populate spec template**
   - Source: `.specify/templates/spec-template.md`
   - Destination: `.specify/specs/{feature}/spec.md`
   - Fill in:
     - Feature name (derived from description)
     - Feature branch name
     - Current date
     - User description in "Input" field
     - Initial user stories (prioritized P1, P2, P3)
     - Functional requirements (FR-001, FR-002, ...)
     - Success criteria (SC-001, SC-002, ...)
     - Edge cases
     - Key entities

4. **Review constitution alignment**
   - Ensure specification follows project principles
   - Technology-agnostic (WHAT and WHY, not HOW)
   - Measurable success criteria
   - Security, performance, accessibility requirements
   - Testing expectations (80% coverage)

5. **Create git branch**
   - Branch name: `{number}-{kebab-case-name}`
   - Example: `003-sales-analytics-dashboard`
   - Switch to the new branch

6. **Output summary**
   - Feature number assigned
   - Directory created
   - Spec file created
   - Git branch created
   - Next steps

## Quality Checklist

The generated specification MUST include:
- [ ] Prioritized user stories (P1, P2, P3)
- [ ] Each user story is independently testable
- [ ] Functional requirements with unique IDs (FR-001, FR-002, ...)
- [ ] Success criteria with unique IDs (SC-001, SC-002, ...)
- [ ] Edge cases documented
- [ ] Key entities identified
- [ ] Review & acceptance checklist included

## Next Steps for User

After completing this command, inform the user:
1. Review the generated specification
2. Refine user stories and requirements as needed
3. Run `/dashboard.plan` to create implementation plan

## Error Handling

- If `.specify/` doesn't exist: "This doesn't appear to be a spec-driven project. Initialize project first."
- If no description provided: "Please provide a feature description as an argument."
- If duplicate feature number: Generate next available number automatically

---

**Note**: This command creates the specification only. Implementation planning comes next with `/dashboard.plan`.
