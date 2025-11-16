# Architectural Decisions Log

**Last Updated**: 2025-11-13
**Purpose**: Record significant architectural decisions with rationale, alternatives considered, and date

---

## Overview

This file documents important architectural decisions made during the project. Each decision follows the ADR (Architecture Decision Record) lightweight format.

**Format**:
- **Title**: Short descriptive title
- **Date**: When decision was made
- **Status**: Proposed | Accepted | Deprecated | Superseded
- **Context**: The situation requiring a decision
- **Decision**: What was decided
- **Rationale**: Why this decision was made
- **Alternatives**: Other options considered
- **Consequences**: Expected outcomes (positive and negative)

---

## ADR-001: Use Spec-Kit Methodology for Feature Development

**Date**: 2025-11-10
**Status**: Accepted

### Context

The project needs a structured approach to feature development that ensures:
- Requirements are clearly defined before implementation
- All stakeholders align on scope and goals
- Implementation can be validated against specifications
- Development follows a consistent process

### Decision

Adopt GitHub's spec-kit methodology for all feature development:
1. Create specification (spec.md) first
2. Define technical plan (plan.md)
3. Break down into tasks (tasks.md)
4. Implement following spec-driven workflow

### Rationale

- **Clarity**: Specs force clear thinking about requirements before coding
- **Alignment**: Stakeholders can review and approve specs before implementation
- **Validation**: Success criteria provide objective acceptance tests
- **Industry-proven**: GitHub uses this for their own development

### Alternatives Considered

1. **Code-first**: Start coding, document later
   - Rejected: Leads to unclear requirements and scope creep

2. **Traditional PRD**: Product requirements documents
   - Rejected: Too heavyweight, less developer-friendly

3. **User stories only**: Just write user stories
   - Rejected: Lacks technical detail and success criteria

### Consequences

**Positive**:
- Clearer requirements and expectations
- Reduced rework from misunderstandings
- Better documentation
- Measurable success criteria

**Negative**:
- Upfront time investment in spec writing
- Requires discipline to write specs first
- Learning curve for spec-kit format

---

## ADR-002: Use Claude Code for Development, Agent SDK for Production

**Date**: 2025-11-10
**Status**: Accepted

### Context

Need development environment that:
- Supports spec-driven workflow
- Provides AI assistance
- Enables rapid iteration
- Deploys to production reliably

### Decision

Use two-environment approach:
- **Development**: Claude Code with custom commands, skills, sub-agents
- **Production**: Claude Agent SDK for deployment and orchestration

### Rationale

- **Development**: Claude Code provides AI-native development experience
- **Production**: Agent SDK provides reliable, scalable deployment
- **Separation**: Clear boundary between dev and prod environments
- **Integration**: Both from Anthropic, designed to work together

### Alternatives Considered

1. **Traditional IDE + manual deployment**
   - Rejected: Loses AI assistance benefits

2. **Claude Code for both dev and prod**
   - Rejected: Not designed for production hosting

3. **Different AI tools**
   - Rejected: Claude Code is most mature for spec-driven development

### Consequences

**Positive**:
- Best-in-class development experience
- Production-grade deployment
- Clear dev/prod separation
- AI-assisted development

**Negative**:
- Dependency on Anthropic tools
- Need to learn both environments
- Potential future migration if tools evolve

---

## ADR-003: Implement EPIC Workflow (Observe → Act → Verify → Loop)

**Date**: 2025-11-13
**Status**: Accepted

### Context

Spec 002 (Claude Code Commands Setup) defines an EPIC methodology for iterative development. Need to decide whether to use EPIC or a simpler linear workflow.

### Decision

Implement EPIC workflow as core development pattern:
- **Observe**: Analyze current state, identify next task
- **Act**: Implement task with TDD
- **Verify**: Run tests, quality checks
- **Loop**: Checkpoint and continue

Commands: `/workflow.observe`, `/workflow.act`, `/workflow.verify`, `/workflow.loop`

### Rationale

- **Iterative**: Small, frequent cycles reduce risk
- **Quality**: Built-in verification at each step
- **Clarity**: Always know what to do next (observe tells you)
- **Flexible**: Can adapt based on verification results

### Alternatives Considered

1. **Linear workflow**: spec → plan → tasks → implement all → test
   - Rejected: Big-bang implementation is riskier

2. **Ad-hoc**: No structured process
   - Rejected: Inconsistent, hard to track progress

3. **Kanban only**: Just move tasks across board
   - Rejected: Lacks built-in quality gates

### Consequences

**Positive**:
- Reduced risk (small iterations)
- Continuous quality (verify each cycle)
- Clear next steps (observe provides guidance)
- Easy to pause and resume

**Negative**:
- More checkpoints (potentially slower initial perception)
- Requires discipline to follow cycle
- Learning curve for EPIC methodology

---

## ADR-004: Use Progressive Disclosure for Skills (3-Level Loading)

**Date**: 2025-11-10
**Status**: Accepted

### Context

Agent Skills need to provide deep expertise without overwhelming the context window. Need balance between comprehensive guidance and lean context.

### Decision

Implement 3-level progressive disclosure for all Skills:
- **Level 1 (Metadata)**: 40-60 tokens - Basic description
- **Level 2 (Core)**: 600-1000 tokens - Essential guidance
- **Level 3 (References)**: Variable - Detailed docs, examples, scripts (loaded on-demand)

### Rationale

- **Context efficiency**: Load only what's needed
- **Scalability**: Can add extensive L3 content without context bloat
- **Performance**: Faster activation (L1 → L2 loaded quickly)
- **Flexibility**: Can expand L3 without affecting L1/L2 budgets

### Alternatives Considered

1. **Single-level**: All content loaded at once
   - Rejected: Context window explosion

2. **Two-level**: Metadata + everything else
   - Rejected: Still too much context for complex skills

3. **On-demand only**: Load everything lazily
   - Rejected: Too many round trips, poor UX

### Consequences

**Positive**:
- 70%+ reduction in context usage
- Can include extensive documentation
- Fast skill activation
- Scalable to many skills

**Negative**:
- Complexity in skill structure
- Need to carefully allocate content across levels
- Token budget enforcement required

---

## ADR-005: Make MCP Integration Optional (P3 Priority)

**Date**: 2025-11-10
**Status**: Accepted

### Context

Model Context Protocol (MCP) servers provide standardized data access (PostgreSQL, files, APIs). Need to decide if MCP is required or optional.

### Decision

Make MCP integration optional enhancement (Spec 005, P3 priority):
- Dashboards can use direct access (psycopg2, pandas.read_csv(), requests)
- MCP provides optimization and standardization
- Skills provide fallback patterns when MCP unavailable

### Rationale

- **Flexibility**: Developers can choose direct access or MCP
- **Simplicity**: Don't force MCP for simple cases
- **Gradual adoption**: Can add MCP later if needed
- **Fallback**: Skills work with or without MCP

### Alternatives Considered

1. **MCP required**: Force all data access through MCP
   - Rejected: Too restrictive for simple cases

2. **No MCP at all**: Only direct access
   - Rejected: Loses standardization benefits

3. **MCP for specific sources only**: E.g., only for databases
   - Rejected: Inconsistent, confusing

### Consequences

**Positive**:
- Flexibility in data access approach
- Lower barrier to entry (no MCP setup required)
- Can add MCP when beneficial

**Negative**:
- Need to maintain both patterns (MCP + direct)
- Potential inconsistency across projects
- Skills must handle both cases

---

## ADR-006: Prioritize Accessibility (WCAG 2.1 AA) from Start

**Date**: 2025-11-10
**Status**: Accepted

### Context

Dashboards must be accessible to users with disabilities. Need to decide when to address accessibility (during development or after).

### Decision

Make WCAG 2.1 Level AA compliance a core requirement from the start:
- Build accessibility into Skills (plotly-viz enforces compliance)
- Automated checking in workflow (accessibility-audit skill)
- Verification in every EPIC cycle (/workflow.verify includes a11y)

Constitution requirement: SC-011 (WCAG 2.1 AA compliance)

### Rationale

- **Ethical**: Accessibility is a right, not a feature
- **Legal**: Many jurisdictions require accessibility
- **Quality**: Better UX for everyone, not just disabled users
- **Cheaper**: Easier to build in than bolt on later

### Alternatives Considered

1. **Accessibility as final step**: Add after features complete
   - Rejected: Expensive retrofits, often skipped

2. **Basic accessibility only**: Just color contrast
   - Rejected: Insufficient for real accessibility

3. **WCAG AAA**: Highest standard
   - Rejected: AA is widely accepted standard, AAA often impractical

### Consequences

**Positive**:
- Inclusive product from day one
- Legal compliance
- Better overall UX
- Easier to maintain (built in, not added)

**Negative**:
- Additional upfront effort
- Need accessibility expertise (Skills provide this)
- Some design constraints

---

## ADR-007: Enforce 80% Test Coverage Minimum

**Date**: 2025-11-10
**Status**: Accepted

### Context

Need to decide on quality gates for code. What test coverage threshold ensures quality without excessive burden?

### Decision

Enforce 80% code coverage minimum:
- Enforced in /workflow.verify
- Blocks merge to main if coverage below 80%
- Applies to unit, integration, and e2e tests combined

Constitution requirement: FR-024

### Rationale

- **Quality**: 80% is industry sweet spot (diminishing returns above)
- **Balanced**: High enough to catch issues, not so high as to be onerous
- **Pragmatic**: Allows for some untestable code (e.g., main entry points)

### Alternatives Considered

1. **100% coverage**: Perfect coverage
   - Rejected: Unrealistic, encourages gaming metrics

2. **50% coverage**: Lower bar
   - Rejected: Too low, allows gaps

3. **No minimum**: Trust developers
   - Rejected: Inconsistent quality

### Consequences

**Positive**:
- Consistent quality baseline
- Catches most issues
- Encourages testable design

**Negative**:
- May encourage writing tests just for coverage
- Some effort to reach 80% initially
- May block useful code that's hard to test

---

## ADR-008: Use Plotly Dash as Primary Dashboard Framework

**Date**: 2025-11-10
**Status**: Accepted

### Context

Need to choose dashboard framework for Python-based interactive dashboards.

### Decision

Use Plotly Dash as the primary dashboard framework:
- Dash 2.14+ required
- Plotly Express for standard charts
- Graph Objects for advanced customization

### Rationale

- **Python-native**: Pure Python, no JavaScript required
- **Powerful**: Full interactivity, callbacks, state management
- **Ecosystem**: Large community, many examples
- **Integration**: Works well with pandas, numpy, ML libraries
- **Accessibility**: Can achieve WCAG 2.1 AA compliance

### Alternatives Considered

1. **Streamlit**: Simpler Python framework
   - Rejected: Less flexible for complex dashboards

2. **Flask + custom JS**: Full control
   - Rejected: Requires JavaScript expertise

3. **Panel/Bokeh**: Alternative Python frameworks
   - Rejected: Smaller ecosystems

### Consequences

**Positive**:
- Fully Python-based development
- Rich interactive capabilities
- Large community and resources
- Good performance

**Negative**:
- Learning curve for Dash patterns
- Some limitations vs custom JS
- Deployment complexity (mitigated by Agent SDK)

---

## Future Decisions

Decisions to be made during implementation:

- [ ] Caching strategy (Redis vs in-memory)
- [ ] Authentication/authorization approach
- [ ] Logging framework selection
- [ ] Monitoring/observability tools
- [ ] CI/CD platform choice
- [ ] Container orchestration (if needed beyond Agent SDK)

---

**Note**: This is a living document. Add new ADRs as significant decisions are made.
