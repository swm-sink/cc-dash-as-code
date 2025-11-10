# /dashboard.plan - Create Technical Implementation Plan

Create a technical implementation plan specifying HOW to build a feature based on its specification.

## Command Usage

```
/dashboard.plan [technical details]
```

## Arguments

- `technical details` (required): Tech stack, architecture, and implementation approach

## Behavior

When this command is executed, Claude Code should:

1. **Identify the current feature** by checking git branch or prompting user
2. **Verify specification exists** at `.specify/specs/{feature}/spec.md`
3. **Review the specification** to understand requirements
4. **Review the constitution** for technical standards
5. **Copy the plan template** from `.specify/templates/plan-template.md`
6. **Populate the plan** with:
   - Technology stack details from user input
   - Architecture and design patterns
   - Component breakdown
   - Data model and schemas
   - API contracts (if applicable)
   - File structure
   - Dependencies and libraries
   - Testing strategy
   - Deployment approach
7. **Research latest versions** of specified technologies (if available online)
8. **Validate alignment** with constitutional requirements:
   - Python 3.11+
   - Plotly Dash
   - Type hints required
   - Black + Ruff + mypy for quality
   - 80% test coverage
   - WCAG 2.1 AA accessibility
9. **Save the plan** to `.specify/specs/{feature}/plan.md`
10. **Output a summary** with next steps

## Example

```
User: /dashboard.plan Use Plotly Dash with Pandas for data processing. PostgreSQL database. FastAPI for backend APIs. Docker deployment.

Claude Code:
✓ Found feature: 003-sales-analytics-dashboard
✓ Reviewed specification with 5 user stories
✓ Created implementation plan: .specify/specs/003-sales-analytics-dashboard/plan.md

Plan includes:
- Technology: Plotly Dash 2.14+, Pandas 2.1+, FastAPI 0.104+
- Database: PostgreSQL 15+ with SQLAlchemy ORM
- Architecture: 3-tier (frontend, API, database)
- Components: 8 Dash components, 4 API endpoints
- Testing: pytest, pytest-cov, Playwright for e2e
- Deployment: Docker Compose (dev), Agent SDK (prod)

Next steps:
1. Review the generated plan
2. Refine component design and API contracts
3. Run /dashboard.tasks to generate task breakdown
```

## Plan Quality Checklist

The generated plan should include:

- [ ] Complete technology stack with versions
- [ ] Architecture diagram or description
- [ ] Component breakdown with responsibilities
- [ ] Data model with entity relationships
- [ ] API contracts (OpenAPI spec if applicable)
- [ ] File/directory structure
- [ ] External dependencies list
- [ ] Testing strategy (unit, integration, e2e)
- [ ] Deployment approach (dev and prod)
- [ ] Performance considerations
- [ ] Security considerations

## Constitution Alignment

The plan must align with project standards:

- **Python 3.11+**: Minimum runtime version
- **Plotly Dash**: Primary framework for dashboards
- **Type hints**: All function signatures
- **Code quality**: Black, Ruff, mypy configured
- **Test coverage**: Minimum 80%
- **Accessibility**: WCAG 2.1 AA compliance
- **Performance**: < 3s load, < 1s callback response
- **Security**: No secrets in code, input validation

## Research Guidance

If technologies are rapidly changing (e.g., .NET Aspire, Dash latest features), Claude Code should:

1. Note which technologies need version verification
2. Search documentation if web access available
3. Document research findings in `research.md`
4. Flag any potential version compatibility issues

## Error Handling

- **No specification found**: "Cannot find specification for current feature. Create one with /dashboard.spec first."
- **Invalid technical details**: "Please provide technical details. Usage: /dashboard.plan [tech stack and architecture]"
- **Specification incomplete**: "Specification has unresolved [NEEDS CLARIFICATION] items. Resolve these before planning."

## Output Files

This command creates/updates:

- `.specify/specs/{feature}/plan.md` - Main implementation plan
- `.specify/specs/{feature}/research.md` - Optional research notes
- `.specify/specs/{feature}/data-model.md` - Optional detailed data models
- `.specify/specs/{feature}/contracts/` - Optional API specifications

## Related Commands

- `/dashboard.spec` - Create specification (prerequisite)
- `/dashboard.tasks` - Generate task breakdown (next step)
- `/dashboard.analyze` - Analyze plan completeness

---

*This command translates WHAT needs to be built into HOW it will be implemented.*
