# /dashboard.spec - Create Feature Specification

Create a new feature specification following the spec-kit methodology for dashboard development.

## Command Usage

```
/dashboard.spec [feature description]
```

## Arguments

- `feature description` (required): Brief description of the feature to be built

## Behavior

When this command is executed, Claude Code should:

1. **Parse the feature description** from the user
2. **Generate a unique feature number** (e.g., 003, 004) by checking existing specs in `.specify/specs/`
3. **Create a feature directory** at `.specify/specs/{number}-{kebab-case-name}/`
4. **Copy the spec template** from `.specify/templates/spec-template.md`
5. **Populate the template** with:
   - Feature name derived from description
   - Feature branch name (format: `{number}-{kebab-case-name}`)
   - Current date
   - User description in the "Input" field
   - Initial user stories based on the description (prioritized)
   - Functional requirements (numbered FR-001, FR-002, etc.)
   - Success criteria (numbered SC-001, SC-002, etc.)
   - Edge cases
   - Key entities
6. **Review the constitution** (`.specify/memory/constitution.md`) to ensure alignment
7. **Save the specification** to `spec.md` in the feature directory
8. **Create a feature branch** in git with the name `{number}-{kebab-case-name}`
9. **Output a summary** showing what was created and next steps

## Example

```
User: /dashboard.spec Create a sales analytics dashboard with filtering by date range and product category

Claude Code:
✓ Generated feature number: 003
✓ Created directory: .specify/specs/003-sales-analytics-dashboard/
✓ Created specification: .specify/specs/003-sales-analytics-dashboard/spec.md
✓ Created git branch: 003-sales-analytics-dashboard

Next steps:
1. Review the generated specification
2. Refine user stories and requirements
3. Run /dashboard.plan to create implementation plan
```

## Specification Quality Checklist

The generated specification should include:

- [ ] Prioritized user stories (P1, P2, P3)
- [ ] Each user story is independently testable
- [ ] Functional requirements with unique IDs (FR-001, FR-002, ...)
- [ ] Success criteria with unique IDs (SC-001, SC-002, ...)
- [ ] Edge cases documented
- [ ] Key entities identified
- [ ] Review & acceptance checklist included

## Constitution Alignment

The specification must align with project principles from `.specify/memory/constitution.md`:

- Technology-agnostic (focus on WHAT and WHY, not HOW)
- Measurable success criteria
- Security and privacy considerations
- Performance targets
- Accessibility requirements (WCAG 2.1 AA)
- Testing expectations (80% coverage)

## Error Handling

If the command fails, provide clear error messages:

- **Missing .specify/ directory**: "This doesn't appear to be a spec-driven project. Run the project initialization first."
- **Invalid feature description**: "Please provide a feature description. Usage: /dashboard.spec [description]"
- **Duplicate feature number**: "Feature number already exists. Generated next available number."

## Related Commands

- `/dashboard.plan` - Create implementation plan (next step)
- `/dashboard.tasks` - Generate task breakdown
- `/dashboard.analyze` - Analyze specification quality

---

*This command initiates the spec-driven development workflow for dashboard features.*
