# Overview Section (Revised)
## For Spec 002 - Claude Code Commands Setup

---

## Overview

This specification defines the Claude Code configuration for spec-driven Plotly Dash development using a **hybrid workflow architecture**. The setup integrates three complementary extension mechanisms—Commands (user-invoked workflows), Agent Skills (model-invoked expertise), and Sub-Agents (task-isolated workers)—to create a complete development environment.

**Core Architecture**: Two distinct but integrated processes:

1. **Spec-Kit Process** (Planning): Constitution → Specify → Plan → Tasks → Approval
   - Defines WHAT needs to be built
   - Human-driven with approval gates
   - Commands: `/spec:*`
   - Skills: Development Skills (spec-kit-workflow, claude-code-architecture, research-synthesis)

2. **Claude Code Process** (Execution): Research → Implement → Verify → Next
   - Defines HOW to build it
   - Agent-driven with agentic corrections
   - Commands: `/workflow:*`, `/utils:*`
   - Skills: Production Skills (data-analysis, plotly-viz, dash-components, accessibility-audit, performance-optimizer)

**Handoff Mechanism**: tasks.md file (frozen after approval, minor edits allowed)

---

### Key Principles

#### 1. Spec-First Workflow
All work begins with approved specifications. No implementation without documented requirements, technical plans, and actionable tasks. This principle is **enforced** by Commands that check for approved specs before allowing implementation.

#### 2. Hybrid Workflow Architecture
Two processes working together:
- **Spec-Kit** (planning) creates clear, approved tasks
- **Claude Code** (execution) implements with autonomous corrections
- Handoff via tasks.md (frozen but allows minor clarifications)
- Feedback loops managed through escalation thresholds

See `specs/WORKFLOW.md` for complete architecture documentation.

#### 3. Namespaced Commands
Commands organized by category using namespace syntax:
- `/spec:*` - Specification management (specify, plan, tasks, validate, review)
- `/workflow:*` - Implementation workflow (research, implement, verify, next, status)
- `/utils:*` - Developer utilities (test, lint, format, diff)

Format: `/category:action` (e.g., `/spec:specify`, `/workflow:implement`)

#### 4. Agent Skills - Progressive Disclosure
Skills provide domain expertise through three-level loading:
- **Level 1** (Metadata): ~50 tokens per skill at startup
- **Level 2** (Core): ~800 tokens when skill activates
- **Level 3** (References): Variable size, loaded on-demand

This enables 100+ skills to be available with minimal context overhead.

**Development Skills** (for building this system):
- `spec-kit-workflow` - Spec-driven development methodology
- `claude-code-architecture` - Commands/Skills/Sub-Agents expertise
- `research-synthesis` - Reference documentation analysis

**Production Skills** (for dashboard developers):
- `data-analysis` - Statistical analysis, EDA, data quality
- `plotly-viz` - Chart generation, accessibility, theming
- `dash-components` - Component patterns, callbacks, layouts
- `accessibility-audit` - WCAG 2.1 AA compliance checking
- `performance-optimizer` - Bottleneck detection, optimization

Skills auto-activate based on context, enhancing Commands without replacing them.

#### 5. Specialized Sub-Agents
Task-isolated workers for parallel execution:
- `component-builder` - Create reusable Dash UI components
- `data-pipeline` - Build data loaders and transformers
- `test-engineer` - Write comprehensive test suites

Sub-Agents have isolated context windows and coordinate via file locking or queue-based systems to avoid conflicts.

#### 6. Agentic Corrections
During execution (`/workflow:verify`), Claude can autonomously correct issues:
- **Within-task corrections**: Unlimited (fix bugs, improve code, handle edge cases)
- **Max 3 verify attempts**: After 3 failures, escalate to human review
- **Escalation triggers**: Technical impossibility, incorrect dependencies, unclear requirements

This enables high-quality output without constant human intervention.

---

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Hybrid Workflow                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Process 1: Spec-Kit (Planning)                            │
│  ┌─────────────────────────────────────────────┐           │
│  │ Constitution → Specify → Plan → Tasks       │           │
│  │    ↓            ↓         ↓       ↓         │           │
│  │ Commands:   /spec:specify /spec:plan        │           │
│  │             /spec:tasks                      │           │
│  │    ↓                                         │           │
│  │ Skills:   spec-kit-workflow                 │           │
│  │           claude-code-architecture           │           │
│  │           research-synthesis                 │           │
│  │    ↓                                         │           │
│  │ [APPROVAL GATE]                              │           │
│  │    ↓                                         │           │
│  │ tasks.md (FROZEN*)                           │           │
│  └─────────────────────────────────────────────┘           │
│                      ↓                                      │
│                   Handoff                                   │
│                      ↓                                      │
│  Process 2: Claude Code (Execution)                        │
│  ┌─────────────────────────────────────────────┐           │
│  │ For Each Task in tasks.md:                  │           │
│  │   Research → Implement → Verify → Next      │           │
│  │      ↓          ↓           ↓                │           │
│  │ Commands:   /workflow:research               │           │
│  │             /workflow:implement              │           │
│  │             /workflow:verify (max 3 attempts)│           │
│  │             /workflow:next                   │           │
│  │      ↓                                       │           │
│  │ Skills:   data-analysis                     │           │
│  │           plotly-viz                         │           │
│  │           dash-components                    │           │
│  │           accessibility-audit                │           │
│  │           performance-optimizer              │           │
│  │      ↓                                       │           │
│  │ Sub-Agents: component-builder               │           │
│  │             data-pipeline                    │           │
│  │             test-engineer                    │           │
│  └─────────────────────────────────────────────┘           │
│                                                             │
└─────────────────────────────────────────────────────────────┘

*Frozen = No scope changes allowed; typos/clarifications OK
```

---

### Extension Mechanisms Comparison

| Mechanism | Invocation | Purpose | Context | Example |
|-----------|-----------|---------|---------|---------|
| **Commands** | User-explicit | Workflow structure | Main agent | `/workflow:implement` |
| **Skills** | Model-automatic | Domain expertise | Shared | `plotly-viz` |
| **Sub-Agents** | Delegated | Task execution | Isolated | `component-builder` |
| **MCP Servers** | Tool calls | Data access | External | `mcp__postgres` |
| **Hooks** | Event-triggered | Automation | Main agent | PostToolUse |

All five mechanisms work together seamlessly to create a comprehensive development environment.

---

### Success Factors

**Good Planning → Clear Tasks → Smooth Execution**:
- Thorough Spec-Kit planning produces actionable tasks
- Clear tasks reduce execution errors and escalations
- Skills provide expertise that improves code quality
- Agentic corrections catch issues early

**Measurable Outcomes**:
- 95%+ task completion without escalation
- 70%+ tasks pass verification on first attempt
- <10% spec revisions required during execution
- 30%+ faster development with Skills vs. without

---

### What Makes This Setup Different

**vs. Generic Claude Code Setup**:
- Tailored to Plotly Dash dashboard development (not generic)
- Enforces spec-first methodology (not ad-hoc)
- Includes 8 specialized Skills (not just commands)
- Hybrid workflow with clear handoff point (not single process)

**vs. Manual Development**:
- Automated quality checks (testing, linting, accessibility)
- Domain expertise on-demand (Skills)
- Parallel work capability (Sub-Agents)
- Consistent patterns and standards enforced

**vs. Standard Dash Development**:
- Specification-driven (not code-first)
- Built-in accessibility compliance (WCAG 2.1 AA)
- Performance optimization guidance (<3s load, <1s callbacks)
- Comprehensive testing (80%+ coverage target)

---

### Integration with Project Ecosystem

**Constitution** (`specs/memory/constitution.md`):
- Defines project principles and quality standards
- Referenced during spec validation
- Ensures alignment across all work

**Workflow Architecture** (`specs/WORKFLOW.md`):
- Complete documentation of two-process model
- Handoff mechanisms and escalation rules
- Governance and controls

**Templates** (`specs/templates/`):
- `spec-template.md` - Feature specification structure
- `plan-template.md` - Technical implementation plan
- `tasks-template.md` - Actionable task breakdown

**Research** (`specs/research/`):
- Agent Skills integration analysis (29KB)
- Claude Code architecture documentation (12KB)
- Complete architecture quick reference (19KB)

---

### Scope Boundaries

**In Scope**:
- Namespaced commands for spec workflow and implementation
- 8 Agent Skills (3 development + 5 production)
- 3 specialized Sub-Agents for parallel work
- Hybrid workflow architecture implementation
- Configuration and settings management

**Out of Scope**:
- Visual command builder or GUI (CLI-based only)
- Commands for non-Dash frameworks
- Real-time collaboration features
- Cloud deployment automation (separate spec: 001-dashboard-foundation)
- Non-dashboard development workflows

---

### Prerequisites

**Required**:
- Claude Code installed and configured
- Python 3.11+ with pip
- Git repository initialized
- `specs/` directory with constitution and templates
- Plotly Dash 2.14+ installed

**Recommended**:
- pytest, pytest-cov for testing
- Black, Ruff, mypy for code quality
- Understanding of spec-driven development
- Familiarity with Plotly Dash framework

---

**Next Sections**:
- **Agent Skills Architecture**: Detailed documentation of all 8 Skills (~4000 tokens)
- **User Scenarios & Testing**: How users interact with Commands and Skills
- **Requirements**: 90 functional requirements (30 for Skills)
- **Success Criteria**: 45 measurable outcomes (15 for Skills)
- **Implementation Phases**: 8-week plan including Skills development

---

**Status**: Draft - Awaiting Review
**Dependencies**: specs/WORKFLOW.md, specs/research/agent-skills-integration-analysis.md
**Estimated Implementation**: 8 weeks (see Implementation Phases)
