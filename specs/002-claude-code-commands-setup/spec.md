# Feature Specification: Claude Code Commands Setup

**Feature Branch**: `002-claude-code-commands-setup`
**Created**: 2025-11-10
**Status**: Draft - Awaiting Review
**Input**: Set up Claude Code with custom commands organized by category (spec, workflow, utils, dash) and specialized sub-agents for spec-driven dashboard development



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


---

# Agent Skills Architecture
## Comprehensive Integration for Spec-Driven Dashboard Development

---

## Overview

Agent Skills are **model-invoked domain expertise** that automatically enhance Claude Code's capabilities without explicit user invocation. Skills form the third pillar of our architecture alongside Commands (user-invoked workflows) and Sub-Agents (task-isolated workers).

**Key Characteristics**:
- **Auto-Activation**: Skills load automatically based on context matching
- **Progressive Disclosure**: Three-level loading (metadata → core → references)
- **Dual Purpose**: Development Skills (building the system) + Production Skills (building dashboards)
- **Complementary**: Work seamlessly with Commands, Sub-Agents, and MCP servers

**Why Skills Matter**:
Without Skills, every command would need to include all domain knowledge, resulting in massive context usage and redundant information. Skills enable Claude to access deep expertise on-demand, keeping context lean while providing comprehensive guidance.

---

## 1. Skills vs Commands vs Sub-Agents

### Architectural Distinction

| Aspect | Commands | Skills | Sub-Agents |
|--------|----------|--------|------------|
| **Invocation** | User-explicit (`/workflow:act`) | Model-automatic (context-triggered) | User/model-delegated |
| **Purpose** | Workflow structure | Domain knowledge | Task execution |
| **Context** | Main agent | Shared with main agent | Isolated window |
| **Loading** | Immediate (synchronous) | Progressive (3 levels) | Full agent spawn |
| **Token Cost** | ~100-500 tokens | ~50 → 800 → variable | Separate budget |
| **When to Use** | Repeated workflows | Reusable expertise | Parallel work |
| **Example** | `/spec:specify` | `plotly-viz` | `component-builder` |

### Decision Matrix

**Use Commands when**:
- User needs to explicitly trigger a workflow
- Workflow has clear start/end points
- Sequence of steps must be followed
- Examples: Creating specs, running tests, committing code

**Use Skills when**:
- Domain expertise is reusable across many tasks
- Knowledge should activate automatically when relevant
- Progressive disclosure can save context
- Examples: Chart selection guidance, accessibility checking, statistical analysis

**Use Sub-Agents when**:
- Task is self-contained and can run independently
- Parallel execution would speed up work significantly
- Task benefits from isolated context (less noise)
- Examples: Building multiple components, comprehensive testing, data pipeline creation

### Integration Example

**Scenario**: User creates a dashboard with data visualization

```bash
# User invokes Command
/workflow:implement Create sales dashboard with date filtering

# What happens:
1. Command `/workflow:implement` executes (user-invoked)
   → Provides workflow structure (TDD, testing, validation)

2. Skills auto-activate (model-invoked):
   → `dash-components` (detecting "dashboard")
   → `plotly-viz` (detecting "visualization")
   → `data-analysis` (detecting "sales" data)

3. Sub-Agent may be launched (if complex):
   → `component-builder` for parallel UI work
   → Uses Skills within its isolated context

Result: Command provides STRUCTURE, Skills provide KNOWLEDGE, Sub-Agent provides CAPACITY
```

---

## 2. Progressive Disclosure Pattern

### The Three Levels

Progressive disclosure enables Claude to maintain a vast knowledge base without overloading context. Skills load incrementally as needed.

#### Level 1: Metadata Only (Startup)

**When Loaded**: At Claude Code initialization
**Size**: ~50 tokens per skill
**Purpose**: Enable skill discovery and matching

**Format** (YAML frontmatter in SKILL.md):
```yaml
name: data-analysis
description: Load, analyze, and generate insights from datasets including CSV, JSON, Parquet, SQL databases. Use when exploring data, performing statistical analysis, identifying trends, or creating data transformations for dashboards. Automatically invoked when user mentions data exploration, EDA, statistics, or data quality.
allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
```

**With 20 skills**: ~1000 tokens total at startup (minimal overhead)

---

#### Level 2: Core Instructions (Skill Activated)

**When Loaded**: Claude determines skill is relevant to current task
**Size**: ~800 tokens
**Purpose**: Provide essential methodology and patterns

**Format** (SKILL.md content):
```markdown
# Data Analysis Skill

## Quick Start
1. Load data using pandas or SQL
2. Perform exploratory data analysis (EDA)
3. Generate statistical summaries
4. Identify data quality issues
5. Suggest appropriate visualizations

## Core Workflow

### Loading Data
- **CSV/JSON**: Use pandas.read_csv(), pandas.read_json()
- **SQL**: Use mcp__postgres or psycopg2
- **Parquet**: Use pandas.read_parquet()

### Exploratory Data Analysis
1. Check shape: df.shape
2. Check types: df.dtypes
3. Check nulls: df.isnull().sum()
4. Summary stats: df.describe()
5. Correlations: df.corr()

### Data Quality Checks
- Missing values (MCAR, MAR, MNAR)
- Outliers (IQR, z-score methods)
- Duplicates
- Type consistency
- Range validation

### Visualization Recommendations
[Chart selection logic based on data characteristics]
```

**Activation Triggers**:
- User mentions: "analyze", "data", "statistics", "EDA", "trends"
- Commands reading data files
- When examining datasets

---

#### Level 3: Reference Materials (On-Demand)

**When Loaded**: Skill execution requires specific deep knowledge
**Size**: Variable (can be 2000-5000+ tokens)
**Purpose**: Detailed guidance for specific scenarios

**Format** (Reference files in skill directory):
```
.claude/skills/data-analysis/
├── SKILL.md                      # Levels 1 & 2
├── STATISTICAL_METHODS.md        # ~2000 tokens
├── DATA_QUALITY.md               # ~1500 tokens
├── VISUALIZATION_GUIDE.md        # ~1800 tokens
└── scripts/
    └── analyze.py                # Loaded when executed
```

**Example Reference File** (STATISTICAL_METHODS.md):
```markdown
# Statistical Methods Reference

## Descriptive Statistics
[Detailed explanations of mean, median, mode, std dev, variance...]

## Inferential Statistics
[Hypothesis testing, confidence intervals, p-values...]

## Correlation Analysis
[Pearson, Spearman, Kendall correlations...]

## Regression Analysis
[Linear, logistic, polynomial regression...]

## Time Series Analysis
[Trend, seasonality, ARIMA models...]
```

**Level 3 files load**:
- Only when needed (Claude requests specific knowledge)
- Via Read tool calls
- As context permits

---

### Progressive Disclosure Benefits

**Comparison: Skills vs MCP**

| Approach | Startup Cost | Runtime Access | Scalability |
|----------|--------------|----------------|-------------|
| **MCP** (Load all upfront) | 50,000+ tokens | Immediate | Limited (~10 servers) |
| **Skills** (Progressive) | 1,000 tokens | 2-3 tool calls | High (100+ skills) |

**Example**:
- 20 Skills at startup: 1,000 tokens
- 5 Skills activate in session: +4,000 tokens (5 × 800)
- 2 Skills need Level 3: +3,500 tokens
- **Total**: 8,500 tokens

vs.

- 5 MCP servers loaded: 50,000 tokens
- All tools available immediately
- **Total**: 50,000 tokens

**Trade-off**: Skills use 3-4x more tool calls but 6x less context

---

## 3. Development Skills

These Skills support **us** (developers) in building the Claude Code dashboard development system.

### 3.1 spec-kit-workflow

**Metadata** (Level 1):
```yaml
name: spec-kit-workflow
description: Guide for creating specifications following GitHub's spec-kit approach. Use when creating or validating feature specifications, planning technical implementations, or breaking down work into tasks. Covers Constitution → Specify → Plan → Tasks workflow. Automatically invoked when working with spec.md, plan.md, or tasks.md files.
allowed-tools: [Read, Write, Edit, Bash(git:*)]
```

**Purpose**: Provide methodology for spec-driven development following Spec-Kit standard

**Activation Triggers**:
- User runs `/spec:*` commands
- Reading/writing spec.md, plan.md, tasks.md files
- Mentions "specification", "requirements", "user stories"

**Directory Structure**:
```
.claude/skills/spec-kit-workflow/
├── SKILL.md                      # Levels 1 & 2
├── SPEC_TEMPLATE.md              # Complete spec template
├── PLAN_TEMPLATE.md              # Technical plan template
├── TASKS_TEMPLATE.md             # Task breakdown template
├── CONSTITUTION_GUIDE.md         # Alignment checking
├── examples/
│   ├── example-spec.md           # Reference specification
│   ├── example-plan.md           # Reference plan
│   └── example-tasks.md          # Reference tasks
└── validation/
    └── checklist.md              # Spec validation checklist
```

**SKILL.md Outline** (Level 2):
```markdown
# Spec-Kit Workflow Skill

## Overview
Spec-driven development methodology from GitHub's spec-kit

## The Four Phases

### 1. Constitution
- Project principles and guidelines
- Located in specs/memory/constitution.md
- Defines quality standards, tech stack, patterns

### 2. Specify (spec.md)
- User stories with acceptance scenarios
- Functional requirements (FR-NNN)
- Success criteria (SC-NNN)
- Edge cases
- NO implementation details
- NO time estimates

### 3. Plan (plan.md)
- Technical approach
- Architecture decisions
- Component breakdown
- Technology choices
- Testing strategy

### 4. Tasks (tasks.md)
- Actionable task list
- Dependencies resolved
- Success criteria per task
- Files to create/modify listed
- Becomes frozen after approval

## Spec Template Structure
[Details on required sections...]

## Validation Checklist
[Completeness checks...]

## Common Patterns
[Examples of well-written specs...]
```

**Example Activation**:
```
User: /spec:specify Create authentication system

1. Command `/spec:specify` runs
2. `spec-kit-workflow` Skill activates (detecting spec creation)
3. Level 2 loads: Template structure and guidelines
4. User writes spec with Skill guidance
5. Level 3 loads on-demand: examples/example-spec.md for reference
6. Skill ensures all required sections present
```

---

### 3.2 claude-code-architecture

**Metadata** (Level 1):
```yaml
name: claude-code-architecture
description: Expert knowledge of Claude Code's architecture including Commands, Sub-Agents, Skills, and Hooks. Use when designing .claude/ directory structure, choosing between extension mechanisms, troubleshooting configuration, or understanding Claude Code best practices. Automatically invoked when working with .claude/ directory.
allowed-tools: [Read, Write, Edit, Glob]
```

**Purpose**: Provide deep expertise on Claude Code architecture and extension mechanisms

**Activation Triggers**:
- Working with `.claude/` directory
- Creating commands, sub-agents, or skills
- Mentions "claude code", "commands", "sub-agents"
- Configuration troubleshooting

**Directory Structure**:
```
.claude/skills/claude-code-architecture/
├── SKILL.md                      # Levels 1 & 2
├── COMMANDS_GUIDE.md             # Command creation patterns
├── SUBAGENTS_GUIDE.md            # Sub-agent patterns
├── SKILLS_GUIDE.md               # Skills creation (meta!)
├── HOOKS_GUIDE.md                # Hook configuration
├── DECISION_MATRIX.md            # Choose mechanism
├── reference/
│   ├── claude-code-final-architecture.md  # From research
│   └── complete-architecture-quick-reference.md
└── examples/
    ├── example-command.md
    ├── example-subagent.md
    └── example-skill/
```

**SKILL.md Outline** (Level 2):
```markdown
# Claude Code Architecture Skill

## Quick Reference

### When to Use What

**Commands** (/category:action):
- User-invoked workflows
- Explicit structure and sequence
- Examples: /spec:specify, /workflow:implement

**Skills** (auto-activate):
- Domain knowledge
- Progressive disclosure
- Examples: data-analysis, plotly-viz

**Sub-Agents** (task-isolated):
- Parallel execution
- Self-contained work
- Examples: component-builder, test-engineer

**Hooks** (event-triggered):
- Automatic actions
- Tool call events
- Examples: PostToolUse formatting

## Command Creation

### Format (.md with YAML frontmatter)
```yaml
---
description: Short description for help
allowed-tools: [Read, Write, Edit]
argument-hint: [required-arg] [optional-arg]
---

# Prompt content here
```

### Naming Convention
- Use namespacing: /category:action
- Categories: spec, workflow, utils
- Lowercase, hyphens for multi-word

## Sub-Agent Creation
[Patterns for sub-agents...]

## Skills Creation
[Meta: How to create Skills...]

## Settings Configuration
[settings.json structure...]
```

**Example Activation**:
```
User: Should I create a Command or Skill for data analysis?

1. Claude detects "Command or Skill" decision question
2. `claude-code-architecture` Skill activates
3. Level 2 loads: Decision matrix
4. Skill provides: "Use Skill (reusable knowledge, auto-activates)"
5. If user proceeds, Level 3 loads: SKILLS_GUIDE.md
6. Complete guidance for creating data-analysis Skill
```

---

### 3.3 research-synthesis

**Metadata** (Level 1):
```yaml
name: research-synthesis
description: Analyze reference implementations, documentation, and codebases to extract best practices and patterns. Use when researching new technologies, analyzing cloned repositories, synthesizing documentation, or creating implementation guidance. Automatically invoked when examining reference code or documentation.
allowed-tools: [Read, Grep, Glob, WebFetch]
```

**Purpose**: Extract patterns and best practices from reference materials

**Activation Triggers**:
- Researching technologies or frameworks
- Analyzing reference repositories
- Reading documentation
- Creating implementation guides

**Directory Structure**:
```
.claude/skills/research-synthesis/
├── SKILL.md                      # Levels 1 & 2
├── ANALYSIS_METHODS.md           # Research techniques
├── PATTERN_EXTRACTION.md         # Identifying patterns
├── DOCUMENTATION_GUIDE.md        # Creating docs from research
└── templates/
    ├── research-report.md
    └── implementation-guide.md
```

**SKILL.md Outline** (Level 2):
```markdown
# Research Synthesis Skill

## Research Process

### 1. Discovery Phase
- Identify relevant sources
- Clone reference repositories
- Gather documentation

### 2. Analysis Phase
- Code pattern extraction
- API design analysis
- Architecture understanding
- Best practices identification

### 3. Synthesis Phase
- Pattern documentation
- Implementation recommendations
- Example creation
- Integration guidance

## Analysis Techniques

### Code Analysis
- Structure examination (Glob for patterns)
- Implementation search (Grep for specific code)
- Dependency analysis
- Design pattern identification

### Documentation Analysis
- API surface documentation
- Configuration patterns
- Usage examples extraction
- Common pitfalls identification

## Output Formats
- Research reports
- Implementation guides
- Pattern libraries
- Example collections
```

**Example Activation**:
```
User: Research how Plotly Dash handles callbacks

1. User request triggers research task
2. `research-synthesis` Skill activates
3. Level 2 loads: Research process and techniques
4. Skill guides: Use Grep to find callback patterns
5. Skill guides: Extract common patterns
6. Level 3 loads: PATTERN_EXTRACTION.md for detailed methods
7. Creates implementation guide from findings
```

---

## 4. Production Skills

These Skills support **dashboard developers** (end users) building dashboards with our system.

### 4.1 data-analysis

**Metadata** (Level 1):
```yaml
name: data-analysis
description: Load, analyze, and generate insights from datasets including CSV, JSON, Parquet, SQL databases. Use when exploring data, performing statistical analysis, identifying trends, or creating data transformations for dashboards. Automatically invoked when user mentions data exploration, EDA, statistics, or data quality.
allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
```

**Purpose**: Provide statistical analysis and data exploration expertise

**Activation Triggers**:
- Loading or analyzing datasets
- Mentions "data", "analyze", "statistics", "EDA", "trends"
- Working with CSV, JSON, Parquet, SQL files
- Data quality checking

**Directory Structure**:
```
.claude/skills/data-analysis/
├── SKILL.md                      # Levels 1 & 2
├── STATISTICAL_METHODS.md        # ~2000 tokens
├── DATA_QUALITY.md               # ~1500 tokens
├── VISUALIZATION_GUIDE.md        # ~1800 tokens
├── scripts/
│   ├── analyze.py                # Basic analysis script
│   ├── quality_check.py          # Data quality validation
│   └── transform.py              # Common transformations
└── examples/
    ├── eda-example.py            # Complete EDA workflow
    └── sample-analysis.ipynb     # Jupyter notebook example
```

**SKILL.md Outline** (Level 2):
```markdown
# Data Analysis Skill

## Quick Start
1. Load data using pandas or SQL
2. Perform exploratory data analysis (EDA)
3. Generate statistical summaries
4. Identify data quality issues
5. Suggest appropriate visualizations

## Core Workflow

### Loading Data
```python
# CSV/JSON
import pandas as pd
df = pd.read_csv('data.csv')

# SQL (via MCP)
# Use mcp__postgres tool

# Parquet
df = pd.read_parquet('data.parquet')
```

### Exploratory Data Analysis
```python
# Shape and structure
print(df.shape)
print(df.dtypes)
print(df.info())

# Missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# Correlations
print(df.corr())
```

### Data Quality Checks
- Missing values (MCAR, MAR, MNAR)
- Outliers (IQR method, z-score)
- Duplicates
- Type consistency
- Range validation

### Visualization Recommendations

**Continuous variable**: histogram, box plot, violin plot
**Categorical variable**: bar chart, pie chart
**Continuous vs Continuous**: scatter plot, line chart
**Categorical vs Continuous**: box plot, violin plot
**Time series**: line chart, area chart
**Distributions**: histogram, density plot

## Common Patterns
[Typical analysis workflows...]

## Integration with Plotly
[How to pass insights to plotly-viz Skill...]
```

**Example Activation**:
```
User: /workflow:implement Analyze sales data and create dashboard

1. Command `/workflow:implement` runs
2. `data-analysis` Skill activates (detecting "analyze sales data")
3. Level 2 loads: EDA workflow and quality checks
4. Skill guides through data loading and analysis
5. User requests specific statistical test
6. Level 3 loads: STATISTICAL_METHODS.md
7. Skill provides detailed guidance on hypothesis testing
8. Analysis complete, passes insights to plotly-viz Skill
```

---

### 4.2 plotly-viz

**Metadata** (Level 1):
```yaml
name: plotly-viz
description: Generate appropriate Plotly visualizations based on data characteristics. Use when creating charts, graphs, or interactive visualizations. Automatically invoked when user requests dashboards, charts, plots, or data visualization. Ensures accessibility (WCAG 2.1 AA) and responsive design.
allowed-tools: [Read, Write, Edit]
```

**Purpose**: Provide chart creation expertise with accessibility compliance

**Activation Triggers**:
- Creating visualizations or charts
- Mentions "chart", "graph", "plot", "visualization", "dashboard"
- Working with Plotly or Dash code
- Accessibility checking for visualizations

**Directory Structure**:
```
.claude/skills/plotly-viz/
├── SKILL.md                      # Levels 1 & 2
├── CHART_TYPES.md                # ~2500 tokens - All chart types
├── ACCESSIBILITY.md              # ~1800 tokens - WCAG compliance
├── THEMING.md                    # ~1200 tokens - Consistent styling
├── INTERACTIVITY.md              # ~1500 tokens - Hover, click, zoom
├── templates/
│   ├── bar_chart.py
│   ├── line_chart.py
│   ├── scatter_plot.py
│   ├── heatmap.py
│   ├── pie_chart.py
│   └── [other chart templates]
└── examples/
    ├── accessible-dashboard.py   # WCAG 2.1 AA compliant example
    └── interactive-charts.py     # Interactivity examples
```

**SKILL.md Outline** (Level 2):
```markdown
# Plotly Visualization Skill

## Chart Selection Guide

### Based on Data Type

**One continuous variable**:
- Histogram (distribution)
- Box plot (distribution with outliers)
- Violin plot (distribution with density)

**One categorical variable**:
- Bar chart (counts or aggregates)
- Pie chart (proportions, max 5-7 categories)

**Continuous vs Continuous**:
- Scatter plot (relationship)
- Line chart (time series or ordered)
- Bubble chart (3 variables)

**Categorical vs Continuous**:
- Bar chart (comparison)
- Box plot (distribution comparison)
- Violin plot (detailed distribution)

**Multivariate**:
- Heatmap (correlation matrix)
- Scatter matrix (pairwise relationships)
- Parallel coordinates (high-dimensional)

### Chart Creation Pattern

```python
import plotly.express as px

# Basic pattern
fig = px.[chart_type](
    data_frame=df,
    x='column_x',
    y='column_y',
    color='category_column',  # Optional grouping
    title='Chart Title',
    labels={'column_x': 'Display Name'}
)

# Apply accessibility
fig.update_layout(
    font=dict(size=14),  # Readable font size
    plot_bgcolor='white',  # High contrast
)

# Add ARIA labels (handled by dash-components Skill)
```

## Accessibility Requirements (WCAG 2.1 AA)

### Color Contrast
- Text: 4.5:1 ratio minimum
- Large text: 3:1 ratio minimum
- Use colorblind-friendly palettes

### Non-Color Information
- Don't rely on color alone
- Use patterns, labels, markers

### Keyboard Navigation
- All interactive elements accessible via keyboard
- Focus indicators visible

### Screen Reader Support
- Descriptive titles and labels
- ARIA labels for complex charts
- Alt text for chart images

## Plotly Express vs Graph Objects

**Use Plotly Express when**:
- Quick, simple charts
- Standard chart types
- Minimal customization

**Use Graph Objects when**:
- Complex, custom layouts
- Fine-grained control
- Multiple subplot types

## Common Patterns
[Chart creation examples...]
```

**Example Activation**:
```
User: /workflow:implement Create bar chart showing sales by region

1. Command `/workflow:implement` runs
2. `plotly-viz` Skill activates (detecting "bar chart")
3. Level 2 loads: Chart selection and creation patterns
4. Skill provides: Bar chart template with accessibility
5. User wants custom styling
6. Level 3 loads: THEMING.md and CHART_TYPES.md
7. Complete bar chart created with WCAG 2.1 AA compliance
```

---

### 4.3 dash-components

**Metadata** (Level 1):
```yaml
name: dash-components
description: Create reusable Plotly Dash components following best practices. Use when building dashboard layouts, interactive controls, or custom components. Automatically invoked when user mentions components, callbacks, layouts, or Dash-specific features.
allowed-tools: [Read, Write, Edit]
```

**Purpose**: Provide Dash component architecture and callback patterns

**Activation Triggers**:
- Creating Dash components or layouts
- Mentions "component", "callback", "layout", "dash"
- Working with Dash application code
- Interactive dashboard features

**Directory Structure**:
```
.claude/skills/dash-components/
├── SKILL.md                      # Levels 1 & 2
├── COMPONENT_PATTERNS.md         # ~2000 tokens
├── CALLBACK_ARCHITECTURE.md      # ~2200 tokens
├── LAYOUT_GUIDE.md               # ~1500 tokens
├── STATE_MANAGEMENT.md           # ~1800 tokens
├── templates/
│   ├── basic_component.py
│   ├── filter_component.py
│   ├── table_component.py
│   └── chart_component.py
└── examples/
    ├── complete_dashboard.py
    └── callback_patterns.py
```

**SKILL.md Outline** (Level 2):
```markdown
# Dash Components Skill

## Component Creation Pattern

```python
import dash
from dash import html, dcc, Input, Output, State

def create_filter_component(id_prefix='filter'):
    """Reusable filter component with date range and dropdown"""
    return html.Div([
        html.Label('Date Range:'),
        dcc.DatePickerRange(
            id=f'{id_prefix}-date-range',
            start_date='2024-01-01',
            end_date='2024-12-31'
        ),

        html.Label('Category:'),
        dcc.Dropdown(
            id=f'{id_prefix}-category',
            options=[{'label': c, 'value': c} for c in categories],
            multi=True
        )
    ], className='filter-component')
```

## Callback Architecture

### Basic Callback
```python
@app.callback(
    Output('output-id', 'children'),
    Input('input-id', 'value')
)
def update_output(input_value):
    return f'You selected: {input_value}'
```

### Multiple Inputs/Outputs
```python
@app.callback(
    [Output('chart', 'figure'),
     Output('table', 'data')],
    [Input('filter-date', 'start_date'),
     Input('filter-date', 'end_date'),
     Input('filter-category', 'value')]
)
def update_dashboard(start_date, end_date, categories):
    filtered_df = filter_data(df, start_date, end_date, categories)

    fig = create_chart(filtered_df)
    table_data = filtered_df.to_dict('records')

    return fig, table_data
```

### State Management
```python
@app.callback(
    Output('data-store', 'data'),
    Input('load-button', 'n_clicks'),
    State('data-store', 'data'),
    prevent_initial_call=True
)
def load_data(n_clicks, stored_data):
    # Load and cache data
    return new_data
```

## Layout Patterns

### Responsive Grid
```python
app.layout = html.Div([
    # Header
    html.Div([
        html.H1('Dashboard Title'),
    ], className='header'),

    # Filters (left sidebar)
    html.Div([
        create_filter_component(),
    ], className='sidebar'),

    # Main content
    html.Div([
        dcc.Graph(id='main-chart'),
        dcc.Graph(id='secondary-chart'),
    ], className='main-content'),
], className='dashboard-container')
```

## Best Practices

### Component Design
- Keep components pure (no side effects)
- Use type hints
- Document props clearly
- Write unit tests

### Callback Optimization
- Use prevent_initial_call when appropriate
- Minimize callback chain length
- Cache expensive computations
- Use dcc.Store for shared state

### Performance
- Lazy loading for large datasets
- Pagination for tables
- Downsampling for time series
- Virtual scrolling for long lists

## Common Patterns
[Examples of common dashboard layouts...]
```

**Example Activation**:
```
User: /workflow:implement Add date range filter to dashboard

1. Command `/workflow:implement` runs
2. `dash-components` Skill activates (detecting "filter" and "dashboard")
3. Level 2 loads: Component patterns and callback architecture
4. Skill provides: Filter component template
5. User needs state management between callbacks
6. Level 3 loads: STATE_MANAGEMENT.md
7. Complete filter component with callbacks created
```

---

### 4.4 accessibility-audit

**Metadata** (Level 1):
```yaml
name: accessibility-audit
description: Validate WCAG 2.1 AA compliance for dashboards. Use when checking color contrast, keyboard navigation, screen reader compatibility, or accessibility standards. Automatically invoked when user mentions accessibility, WCAG, a11y, or inclusivity.
allowed-tools: [Read, Bash]
```

**Purpose**: Ensure WCAG 2.1 Level AA compliance for all dashboards

**Activation Triggers**:
- Checking accessibility compliance
- Mentions "accessibility", "WCAG", "a11y", "screen reader", "keyboard navigation"
- Running accessibility audits
- During `/workflow:verify` phase

**Directory Structure**:
```
.claude/skills/accessibility-audit/
├── SKILL.md                      # Levels 1 & 2
├── WCAG_CHECKLIST.md             # ~2500 tokens - Complete checklist
├── COLOR_CONTRAST.md             # ~1200 tokens
├── KEYBOARD_NAV.md               # ~1500 tokens
├── SCREEN_READERS.md             # ~1800 tokens
├── scripts/
│   ├── check_contrast.py         # Color contrast checker
│   ├── check_aria.py             # ARIA validation
│   └── generate_report.py        # Audit report generator
└── examples/
    └── accessible_patterns.py    # Accessible component examples
```

**SKILL.md Outline** (Level 2):
```markdown
# Accessibility Audit Skill

## WCAG 2.1 Level AA Requirements

### 1. Perceivable

**Color Contrast**:
- Normal text: 4.5:1 minimum
- Large text (18pt+ or 14pt+ bold): 3:1 minimum
- UI components: 3:1 minimum

**Non-Text Content**:
- Alt text for images
- Text alternatives for charts
- Captions for multimedia

**Adaptable**:
- Content order logical
- Responsive design
- No information lost in any presentation

### 2. Operable

**Keyboard Accessible**:
- All functionality available via keyboard
- No keyboard trap
- Visible focus indicator

**Navigation**:
- Skip navigation links
- Clear page titles
- Logical heading structure (H1 → H2 → H3)

**Timing**:
- No time limits (or adjustable)
- Pause/stop animations
- Auto-update control

### 3. Understandable

**Readable**:
- Language specified
- Clear labels and instructions
- Error identification

**Predictable**:
- Consistent navigation
- Consistent identification
- No unexpected context changes

### 4. Robust

**Compatible**:
- Valid HTML
- ARIA labels where needed
- Name, role, value for UI components

## Audit Process

### Step 1: Automated Checks
```bash
# Run axe-core accessibility tests
npm run test:a11y

# Check color contrast
python scripts/check_contrast.py

# Validate ARIA
python scripts/check_aria.py
```

### Step 2: Manual Checks
- Keyboard navigation testing
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Zoom to 200% (ensure no content loss)

### Step 3: Generate Report
```bash
python scripts/generate_report.py
```

## Common Issues and Fixes

### Low Color Contrast
❌ Problem: Light gray text on white background
✅ Solution: Use #606060 or darker on white

### Missing ARIA Labels
❌ Problem: Icon button with no text
✅ Solution: Add aria-label
```python
html.Button('🔍', id='search-btn', **{'aria-label': 'Search'})
```

### Keyboard Trap
❌ Problem: Modal dialog can't be closed with keyboard
✅ Solution: Add Escape key handler

### Missing Alt Text
❌ Problem: Chart image with no description
✅ Solution: Add descriptive alt text
```python
dcc.Graph(figure=fig, config={'alt': 'Bar chart showing sales by region'})
```

## Integration with dash-components

When `dash-components` Skill creates components, `accessibility-audit` Skill provides:
- ARIA label recommendations
- Color contrast validation
- Keyboard navigation patterns
- Screen reader text suggestions

## Tools

### Python Libraries
- `colorspacious` - Color contrast calculation
- `beautifulsoup4` - HTML parsing for ARIA validation

### Browser Tools
- Chrome DevTools Lighthouse
- axe DevTools browser extension

### Screen Readers
- NVDA (Windows, free)
- JAWS (Windows, commercial)
- VoiceOver (macOS, built-in)
```

**Example Activation**:
```
User: /workflow:verify (after implementing dashboard)

1. Command `/workflow:verify` runs
2. `accessibility-audit` Skill activates (auto-check during verification)
3. Level 2 loads: WCAG checklist and audit process
4. Skill runs automated checks
5. Issue found: Low color contrast on button
6. Level 3 loads: COLOR_CONTRAST.md for detailed guidance
7. Skill suggests fix: Change button color from #AAAAAA to #606060
8. Verification passes after fix
```

---

### 4.5 performance-optimizer

**Metadata** (Level 1):
```yaml
name: performance-optimizer
description: Identify and fix performance issues in Plotly Dash dashboards. Use when optimizing callback speed, data loading efficiency, or rendering performance. Automatically invoked when user mentions performance, optimization, speed, or when dashboards are slow. Targets: <3s initial load, <1s callback response.
allowed-tools: [Read, Edit, Bash]
```

**Purpose**: Optimize dashboard performance for production readiness

**Activation Triggers**:
- Performance optimization requests
- Mentions "slow", "performance", "optimize", "speed", "lag"
- Dashboard load time issues
- During `/workflow:verify` if performance targets missed

**Directory Structure**:
```
.claude/skills/performance-optimizer/
├── SKILL.md                      # Levels 1 & 2
├── BOTTLENECK_PATTERNS.md        # ~2000 tokens
├── OPTIMIZATION_STRATEGIES.md    # ~2200 tokens
├── CACHING_GUIDE.md              # ~1500 tokens
├── PROFILING.md                  # ~1200 tokens
├── scripts/
│   ├── profile_callbacks.py      # Callback timing
│   ├── analyze_bundle.py         # Bundle size analysis
│   └── benchmark.py              # Performance benchmarks
└── examples/
    └── optimized_dashboard.py    # Optimized patterns
```

**SKILL.md Outline** (Level 2):
```markdown
# Performance Optimizer Skill

## Performance Targets

**Initial Load**: <3 seconds
**Callback Response**: <1 second
**Time to Interactive**: <5 seconds
**Bundle Size**: <500 KB (excluding data)

## Common Bottlenecks

### 1. Slow Callbacks
**Symptom**: Dashboard freezes when interacting
**Causes**:
- Expensive computations in callbacks
- Large dataframe operations
- Repeated database queries
- No caching

**Solutions**:
- Cache expensive computations
- Use dcc.Store for shared state
- Precompute aggregations
- Use background callbacks for long tasks

### 2. Large Data Loading
**Symptom**: Slow initial load
**Causes**:
- Loading entire dataset at once
- No pagination
- Uncompressed data transfer

**Solutions**:
- Implement pagination
- Use lazy loading
- Compress data (Parquet better than CSV)
- Load summary data first, details on-demand

### 3. Inefficient Rendering
**Symptom**: Charts take long to render
**Causes**:
- Too many data points
- Complex chart types
- No downsampling

**Solutions**:
- Downsample time series data
- Use scattergl instead of scatter for >10K points
- Simplify chart types
- Use virtual scrolling for tables

### 4. Callback Chains
**Symptom**: Multiple sequential updates
**Causes**:
- Callbacks triggering other callbacks
- Unnecessary intermediate states

**Solutions**:
- Combine related callbacks
- Use pattern-matching callbacks
- Reduce callback chain length

## Optimization Strategies

### Caching

```python
from functools import lru_cache
from flask_caching import Cache

# Setup cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

# Cache expensive function
@cache.memoize(timeout=300)
def load_and_process_data(start_date, end_date):
    df = load_data(start_date, end_date)
    return process_data(df)
```

### Lazy Loading

```python
# Load summary first
@app.callback(
    Output('summary', 'children'),
    Input('load-trigger', 'n_clicks')
)
def load_summary(n_clicks):
    summary_df = load_summary_data()  # Fast
    return create_summary_table(summary_df)

# Load details on-demand
@app.callback(
    Output('details', 'children'),
    Input('row-click', 'data')
)
def load_details(row_data):
    details_df = load_details_data(row_data['id'])
    return create_details_view(details_df)
```

### Downsampling

```python
def downsample_timeseries(df, max_points=5000):
    if len(df) <= max_points:
        return df

    # Use LTTB (Largest Triangle Three Buckets) algorithm
    # Or simple nth point selection
    step = len(df) // max_points
    return df.iloc[::step]
```

### Background Callbacks

```python
from dash.long_callback import DiskcacheLongCallbackManager

@app.long_callback(
    Output('result', 'children'),
    Input('compute-button', 'n_clicks'),
    running=[
        (Output('compute-button', 'disabled'), True, False),
    ],
    manager=long_callback_manager
)
def long_computation(n_clicks):
    # This runs in background, doesn't block UI
    result = expensive_computation()
    return result
```

## Profiling

### Measure Callback Time
```python
import time

@app.callback(...)
def my_callback(...):
    start = time.time()
    result = process()
    duration = time.time() - start
    print(f'Callback took {duration:.2f}s')
    return result
```

### Use Dash Dev Tools
```python
app.run_server(debug=True, dev_tools_ui=True)
# Enable "Callback Graph" to visualize callback chains
```

### Profile with cProfile
```bash
python -m cProfile -o profile.stats app.py
# Analyze with snakeviz
snakeviz profile.stats
```

## Performance Checklist

- [ ] Initial load <3 seconds
- [ ] Callbacks respond <1 second
- [ ] No unnecessary callback triggers
- [ ] Large datasets paginated or downsampled
- [ ] Expensive computations cached
- [ ] Bundle size optimized (<500 KB)
- [ ] Charts use efficient types (scattergl for large data)
- [ ] Images optimized and lazy-loaded
- [ ] No console errors or warnings
- [ ] Memory usage stable (no leaks)
```

**Example Activation**:
```
User: Dashboard is slow when filtering large dataset

1. User reports performance issue
2. `performance-optimizer` Skill activates (detecting "slow")
3. Level 2 loads: Bottleneck patterns and optimization strategies
4. Skill analyzes: Callback processes 1M rows on each filter change
5. Skill suggests: Add caching + downsampling
6. Level 3 loads: CACHING_GUIDE.md and OPTIMIZATION_STRATEGIES.md
7. Implementation: Add flask_caching + downsample to 10K points
8. Result: Callback time reduced from 8s to 0.5s
```

---

## 5. Skills Integration with Commands

### How Skills Enhance Commands

Commands provide **workflow structure**, Skills provide **domain expertise**. They work together seamlessly.

**Example: Complete Dashboard Creation**

```bash
# Step 1: Create Specification
User: /spec:specify Build sales analytics dashboard

Skills activated:
- spec-kit-workflow (development): Provides spec template and guidance

Output: Well-structured spec.md following spec-kit methodology

---

# Step 2: Create Plan
User: /spec:plan

Skills activated:
- claude-code-architecture (development): Architecture patterns
- plotly-viz (production): Visualization recommendations
- data-analysis (production): Data pipeline suggestions

Output: Comprehensive plan.md with architecture, tech stack, components

---

# Step 3: Generate Tasks
User: /spec:tasks

Skills activated:
- spec-kit-workflow (development): Task breakdown methodology

Output: Actionable tasks.md with dependencies and success criteria

---

# Step 4: Implement First Task
User: /workflow:implement Task 1 - Create data loader

Skills activated:
- data-analysis (production): Data loading patterns
- research-synthesis (development): Extract patterns from existing code

Output:
- src/data/sales_loader.py (implementation)
- tests/unit/test_sales_loader.py (TDD tests)

---

# Step 5: Implement Second Task
User: /workflow:implement Task 2 - Create bar chart component

Skills activated:
- plotly-viz (production): Chart creation patterns
- dash-components (production): Component structure
- accessibility-audit (production): WCAG compliance

Output:
- src/components/sales_chart.py (accessible chart)
- tests/unit/test_sales_chart.py (tests)

---

# Step 6: Verify Implementation
User: /workflow:verify

Skills activated:
- accessibility-audit (production): Auto-check WCAG compliance
- performance-optimizer (production): Check performance targets

Output:
- All tests pass ✓
- Coverage: 87% ✓
- WCAG 2.1 AA compliant ✓
- Load time: 2.1s ✓
```

### Token Usage Comparison

**Without Progressive Disclosure** (all knowledge upfront):
```
At startup: Load all Skills fully = 80,000 tokens
During session: Immediate access
Total: 80,000 tokens
```

**With Progressive Disclosure** (Skills approach):
```
At startup: 20 Skills × 50 tokens = 1,000 tokens
Task 1: data-analysis Level 2 = +800 tokens
Task 2: plotly-viz L2 + dash-components L2 = +1,600 tokens
Task 6: accessibility-audit L2 + Level 3 = +3,000 tokens
Total: 6,400 tokens (92% reduction)
```

**Benefit**: 12x more efficient context usage while maintaining comprehensive expertise

---

## 6. Skills vs MCP: Complementary Relationship

Skills and MCP (Model Context Protocol) are **complementary**, not competing.

### What MCP Provides

**MCP** = External data and tool access

**Examples**:
- `mcp__postgres` - Database queries
- `mcp__filesystem` - File operations
- `mcp__github` - Repository operations
- `mcp__fetch` - HTTP requests

**Characteristic**: All tools loaded upfront at startup (~50,000 tokens for 5 servers)

**Use When**: Need to ACCESS external systems (databases, APIs, files)

---

### What Skills Provide

**Skills** = Domain knowledge and methodology

**Examples**:
- `data-analysis` - How to analyze data
- `plotly-viz` - How to create visualizations
- `spec-kit-workflow` - How to write specifications

**Characteristic**: Progressive disclosure (50 → 800 → variable tokens)

**Use When**: Need EXPERTISE on how to do something well

---

### Working Together

**Scenario**: Build dashboard with database-driven charts

```
1. User: /workflow:implement Create sales dashboard with PostgreSQL data

2. MCP provides the WHAT (data access):
   → mcp__postgres connects to database
   → Executes SQL queries
   → Returns data to Claude

3. Skills provide the HOW (methodology):
   → data-analysis: How to analyze the query results
   → plotly-viz: How to choose appropriate chart types
   → dash-components: How to structure the dashboard

4. Command provides the WHEN (workflow):
   → /workflow:implement orchestrates the work
   → TDD structure (tests first)
   → Validation and verification

Result: Database data → Analyzed → Visualized → Dashboard component
```

**Anthropic's Guidance**:
> "MCP is the universal connector, providing the what—the access to tools and data. Skills are the procedural knowledge, providing the how—the instructions and methodology."

### When to Use Each

| Need | Use | Example |
|------|-----|---------|
| Access database | MCP | mcp__postgres |
| Know how to write queries | Skill | data-analysis |
| Access files | MCP | mcp__filesystem |
| Know what to analyze | Skill | data-analysis |
| Access GitHub | MCP | mcp__github |
| Know git workflows | Skill | git-workflow |
| Call APIs | MCP | mcp__fetch |
| Know API patterns | Skill | api-integration |

**Key Insight**: MCP + Skills together provide complete solution - access AND expertise.

---

## Summary

**Agent Skills are the expertise layer** in our architecture:

1. **Commands** = User-invoked workflows (structure)
2. **Skills** = Model-invoked knowledge (expertise)
3. **Sub-Agents** = Task-isolated workers (capacity)
4. **MCP** = External data access (connectivity)

**Progressive Disclosure** enables massive knowledge bases (100+ Skills) without context bloat.

**Two Skill Sets**:
- **Development Skills**: For building this system (spec-kit-workflow, claude-code-architecture, research-synthesis)
- **Production Skills**: For dashboard developers (data-analysis, plotly-viz, dash-components, accessibility-audit, performance-optimizer)

**Integration**: Skills automatically enhance Commands at every phase of the hybrid workflow (Spec-Kit planning + Claude Code execution).

**Next**: See Functional Requirements (FR-061 to FR-090) for detailed Skills specifications.

---

**Token Count**: ~4200 tokens (as requested: extremely detailed)


---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Specification Workflow Commands (Priority: P1)

As a **dashboard developer**, I want dedicated slash commands for the specification workflow so that I can create, validate, and manage feature specifications efficiently.

**Why this priority**: Spec-first is foundational to this project. Without specification commands, the entire methodology breaks down.

**Independent Test**: Each spec command can be tested independently by verifying it creates/modifies the correct specification files.

**Acceptance Scenarios**:

1. **Given** I want to create a new feature, **When** I type `/spec.create [feature description]`, **Then** Claude Code creates a new spec in `.specify/specs/` with unique feature number and spec-kit template

2. **Given** I have a draft specification, **When** I type `/spec.validate`, **Then** Claude Code checks the spec for completeness, clarity, and alignment with constitution

3. **Given** I have multiple specs, **When** I type `/spec.list`, **Then** Claude Code displays all specifications with their status (draft, approved, in-progress, completed)

4. **Given** I need to reference an existing spec, **When** I type `/spec.show [feature-number]`, **Then** Claude Code displays the full specification with all sections

5. **Given** I have an approved spec, **When** I type `/spec.branch [feature-number]`, **Then** Claude Code creates a git branch for implementing that feature

---

### User Story 2 - EPIC Workflow Commands (Priority: P1)

As a **dashboard developer**, I want slash commands that follow EPIC methodology (Observe → Act → Verify → Loop) so that I can implement features iteratively with built-in validation.

**Why this priority**: EPIC methodology is the core development workflow. These commands are essential for day-to-day development.

**Independent Test**: Each EPIC command can be tested by running it and verifying it performs the correct phase of the workflow.

**Acceptance Scenarios**:

1. **Given** I start working on a feature, **When** I type `/workflow.observe`, **Then** Claude Code analyzes current state: reads spec, examines codebase, identifies what needs to be built

2. **Given** I have observed the current state, **When** I type `/workflow.act [task description]`, **Then** Claude Code implements the specified task following TDD (test first, then implementation)

3. **Given** I have implemented something, **When** I type `/workflow.verify`, **Then** Claude Code runs tests, linters, type checkers, and validates against spec requirements

4. **Given** verification passed, **When** I type `/workflow.loop`, **Then** Claude Code presents next task options and returns to observe phase for next iteration

5. **Given** I want to see progress, **When** I type `/workflow.status`, **Then** Claude Code shows which requirements from the spec are complete vs. remaining

6. **Given** I need to checkpoint progress, **When** I type `/workflow.checkpoint`, **Then** Claude Code creates a git commit with descriptive message and updates task tracking

---

### User Story 3 - Utility Commands (Priority: P2)

As a **dashboard developer**, I want utility commands for common tasks (testing, code quality, git operations) so that I can maintain code standards without leaving Claude Code.

**Why this priority**: Utilities are important for quality but don't block core workflow. Can be run manually if needed.

**Independent Test**: Each utility command can be tested independently by running it and checking output.

**Acceptance Scenarios**:

1. **Given** I want to run tests, **When** I type `/utils.test [path]`, **Then** Claude Code runs pytest with coverage reporting on specified path or entire project

2. **Given** I want to check code quality, **When** I type `/utils.lint`, **Then** Claude Code runs Black, Ruff, and mypy on the project and reports issues

3. **Given** I have formatting issues, **When** I type `/utils.format`, **Then** Claude Code automatically formats all Python files with Black and fixes auto-fixable Ruff issues

4. **Given** I want to check dependencies, **When** I type `/utils.check-deps`, **Then** Claude Code validates requirements.txt, checks for updates, and reports security vulnerabilities

5. **Given** I want to commit my work, **When** I type `/utils.commit [message]`, **Then** Claude Code stages changes, creates commit with message, and shows git status

6. **Given** I want to see changes, **When** I type `/utils.diff [spec-number]`, **Then** Claude Code shows git diff since the feature branch was created

---

### User Story 4 - Dash-Specific Commands (Priority: P2)

As a **dashboard developer**, I want Dash-specific commands for common dashboard tasks so that I can quickly generate components, layouts, and callbacks.

**Why this priority**: These commands accelerate development but the work could be done through regular EPIC workflow. Nice to have but not blocking.

**Independent Test**: Each Dash command can be tested by verifying it creates the correct Dash code artifacts.

**Acceptance Scenarios**:

1. **Given** I need a new dashboard component, **When** I type `/dash.component [name] [type]`, **Then** Claude Code creates a reusable Dash component with tests in `src/components/`

2. **Given** I need a dashboard layout, **When** I type `/dash.layout [name]`, **Then** Claude Code creates a layout module with responsive grid structure

3. **Given** I need to add interactivity, **When** I type `/dash.callback [description]`, **Then** Claude Code creates callback function with input/output definitions and tests

4. **Given** I need data visualization, **When** I type `/dash.chart [chart-type] [data-source]`, **Then** Claude Code creates appropriate Plotly chart component with sample data

5. **Given** I want to preview the dashboard, **When** I type `/dash.serve`, **Then** Claude Code starts the Dash development server and provides URL

6. **Given** I want to check accessibility, **When** I type `/dash.a11y`, **Then** Claude Code runs accessibility audit (WCAG 2.1 AA) and reports issues

---

### User Story 5 - Specialized Sub-Agents (Priority: P2)

As a **dashboard developer**, I want specialized sub-agents for complex tasks (component building, data pipelines, testing) so that they can work autonomously while I focus on other aspects.

**Why this priority**: Sub-agents enable parallel work but aren't essential for basic workflow. Valuable for complex features but can be deferred.

**Independent Test**: Each sub-agent can be tested by launching it with a task and verifying it completes the work correctly.

**Acceptance Scenarios**:

1. **Given** I need multiple dashboard components, **When** I invoke the `component-builder` sub-agent with a list of components, **Then** it autonomously creates all components with tests in parallel

2. **Given** I need data pipeline work, **When** I invoke the `data-pipeline` sub-agent with data requirements, **Then** it builds loaders, transformers, validators, and tests independently

3. **Given** I need comprehensive testing, **When** I invoke the `test-engineer` sub-agent with code to test, **Then** it writes unit, integration, and e2e tests achieving 80%+ coverage

4. **Given** sub-agents are working, **When** I check their status, **Then** I can see progress, what they're working on, and estimated completion

5. **Given** a sub-agent completes work, **When** it finishes, **Then** it reports what was created, runs verification, and integrates without conflicts

---

### User Story 6 - Command Discovery and Help (Priority: P3)

As a **dashboard developer**, I want easy ways to discover and learn commands so that I can be productive without memorizing all command syntax.

**Why this priority**: Important for usability but documentation can serve this purpose initially. Can be enhanced later.

**Independent Test**: Help commands can be tested by verifying they display correct information.

**Acceptance Scenarios**:

1. **Given** I want to see all commands, **When** I type `/help`, **Then** Claude Code lists all commands organized by category with brief descriptions

2. **Given** I want details on a command, **When** I type `/help [command-name]`, **Then** Claude Code shows full documentation including arguments, examples, and usage notes

3. **Given** I'm in a specific workflow phase, **When** I type `/help.next`, **Then** Claude Code suggests relevant commands for the current context

4. **Given** I make a typo in a command, **When** I type an incorrect command, **Then** Claude Code suggests the closest matching command

---

### Edge Cases

- **What happens when** I run `/workflow.act` without first running `/workflow.observe`?
  - System should detect missing observation context and automatically run observe phase first

- **What happens when** `/workflow.verify` finds failures (tests, linting, type errors)?
  - System should report failures clearly, suggest fixes, and prevent progression to loop phase until fixed

- **What happens when** I try to create a spec with `/spec.create` but the feature already exists?
  - System should detect duplicate and either show existing spec or offer to create a related sub-feature

- **What happens when** a sub-agent fails or gets stuck?
  - System should detect timeout, report the issue, allow manual intervention or retry, and clean up partial work

- **What happens when** I run a Dash command (`/dash.*`) in a non-Dash project?
  - System should detect missing Dash dependencies and offer to initialize Dash project structure

- **What happens when** I try to use a command that requires a spec but I'm not on a feature branch?
  - System should detect missing context, show available specs, and ask which feature to work on

- **What happens when** commands are run in the wrong order (e.g., `/workflow.loop` before `/workflow.verify`)?
  - System should enforce workflow sequence and provide guidance on correct next step

---

## Requirements *(mandatory)*

### Functional Requirements

#### Specification Commands (.claude/commands/spec/)

- **FR-001**: System MUST provide `/spec.create [description]` command to create new feature specifications with unique feature numbers
- **FR-002**: System MUST provide `/spec.validate` command to check specification completeness and constitutional alignment
- **FR-003**: System MUST provide `/spec.list` command to show all specifications with their current status
- **FR-004**: System MUST provide `/spec.show [feature-number]` command to display full specification content
- **FR-005**: System MUST provide `/spec.branch [feature-number]` command to create git feature branch from approved spec
- **FR-006**: Specification commands MUST enforce spec-first workflow (no implementation without approved spec)
- **FR-007**: System MUST auto-increment feature numbers to prevent duplicates

#### EPIC Workflow Commands (.claude/commands/workflow/)

- **FR-008**: System MUST provide `/workflow.observe` command to analyze current state and identify next tasks
- **FR-009**: System MUST provide `/workflow.act [task]` command to implement tasks following TDD
- **FR-010**: System MUST provide `/workflow.verify` command to validate implementation (tests, lint, type check)
- **FR-011**: System MUST provide `/workflow.loop` command to checkpoint progress and present next task options
- **FR-012**: System MUST provide `/workflow.status` command to show spec requirement completion progress
- **FR-013**: System MUST provide `/workflow.checkpoint` command to create git commits with descriptive messages
- **FR-014**: EPIC workflow commands MUST enforce sequence: observe → act → verify → loop
- **FR-015**: `/workflow.act` MUST write tests before implementation (TDD)
- **FR-016**: `/workflow.verify` MUST check: tests pass, coverage ≥80%, linting passes, type checking passes, spec requirements met
- **FR-017**: `/workflow.loop` MUST update task tracking and suggest next logical task

#### Utility Commands (.claude/commands/utils/)

- **FR-018**: System MUST provide `/utils.test [path]` command to run pytest with coverage reporting
- **FR-019**: System MUST provide `/utils.lint` command to run Black, Ruff, and mypy and report issues
- **FR-020**: System MUST provide `/utils.format` command to auto-format code with Black and Ruff
- **FR-021**: System MUST provide `/utils.check-deps` command to validate and check dependencies for updates/vulnerabilities
- **FR-022**: System MUST provide `/utils.commit [message]` command for git commit operations
- **FR-023**: System MUST provide `/utils.diff [spec-number]` command to show changes since feature branch creation
- **FR-024**: Utility commands MUST be idempotent (safe to run multiple times)
- **FR-025**: `/utils.format` MUST not change code behavior, only formatting

#### Dash-Specific Commands (.claude/commands/dash/)

- **FR-026**: System MUST provide `/dash.component [name] [type]` command to create Dash components with tests
- **FR-027**: System MUST provide `/dash.layout [name]` command to create responsive dashboard layouts
- **FR-028**: System MUST provide `/dash.callback [description]` command to create Dash callbacks with tests
- **FR-029**: System MUST provide `/dash.chart [type] [data-source]` command to create Plotly visualizations
- **FR-030**: System MUST provide `/dash.serve` command to start Dash development server
- **FR-031**: System MUST provide `/dash.a11y` command to run accessibility audits (WCAG 2.1 AA)
- **FR-032**: Dash commands MUST generate code following Plotly Dash best practices
- **FR-033**: Dash commands MUST create type-hinted code with docstrings
- **FR-034**: `/dash.component` and `/dash.callback` MUST create corresponding unit tests

#### Sub-Agents (.claude/agents/)

- **FR-035**: System MUST provide `component-builder` sub-agent specialized in creating reusable Dash UI components
- **FR-036**: System MUST provide `data-pipeline` sub-agent specialized in building data loaders and transformers
- **FR-037**: System MUST provide `test-engineer` sub-agent specialized in writing comprehensive test suites
- **FR-038**: Sub-agents MUST work autonomously on assigned tasks without blocking main workflow
- **FR-039**: Sub-agents MUST coordinate to avoid file conflicts (using file locking or queue-based coordination)
- **FR-040**: Sub-agents MUST report progress: task started, in progress, completed, failed
- **FR-041**: Sub-agents MUST validate their work before reporting completion (run tests, linting)
- **FR-042**: Sub-agents MUST integrate their work into the main codebase without manual intervention
- **FR-043**: System MUST allow graceful shutdown and cleanup of sub-agents

#### Help and Discovery

- **FR-044**: System MUST provide `/help` command listing all commands organized by category
- **FR-045**: System MUST provide `/help [command-name]` for detailed command documentation
- **FR-046**: System MUST provide `/help.next` for context-aware command suggestions
- **FR-047**: System MUST suggest closest matching command when user makes a typo
- **FR-048**: Help output MUST include examples and common usage patterns

#### Configuration and Setup

- **FR-049**: System MUST store commands in `.claude/commands/` organized by subdirectories: `spec/`, `workflow/`, `utils/`, `dash/`
- **FR-050**: System MUST store sub-agent definitions in `.claude/agents/` as Markdown files with YAML frontmatter
- **FR-051**: Command files MUST use Markdown format with YAML frontmatter specifying: description, allowed-tools, argument-hint
- **FR-052**: Sub-agent files MUST define: name, description, tools, responsibilities, coordination strategy
- **FR-053**: System MUST use `.claude/settings.json` for permissions and hooks configuration
- **FR-054**: Settings MUST define allowed/denied Bash commands for security

#### Validation and Error Handling

- **FR-055**: All commands MUST validate arguments before execution and provide clear error messages
- **FR-056**: Commands MUST detect if run in wrong context (e.g., non-Dash project, missing spec) and provide guidance
- **FR-057**: EPIC workflow commands MUST enforce proper sequence and block invalid transitions
- **FR-058**: System MUST validate that specs are approved before allowing implementation commands
- **FR-059**: Sub-agents MUST timeout after reasonable duration (30 minutes) and report issues
- **FR-060**: All commands MUST log operations for debugging and audit purposes

---

## Skills Architecture (FR-061 to FR-070)

### FR-061: Progressive Disclosure Support
System MUST support Agent Skills with three-level progressive disclosure pattern:
- Level 1: Metadata only (~50 tokens per skill)
- Level 2: Core instructions (~800 tokens when activated)
- Level 3: Reference materials (variable size, on-demand)

**Validation**: Confirm Skills load incrementally with token budgets respected

---

### FR-062: Three-Level Loading Implementation
Skills MUST implement three-level loading mechanism:
1. **Level 1** loaded at startup from YAML frontmatter in SKILL.md
2. **Level 2** loaded when Claude determines skill is relevant to current context
3. **Level 3** loaded via Read tool when specific reference knowledge needed

**Validation**: Monitor tool calls and context usage during skill activation

---

### FR-063: Automatic Activation
Skills MUST auto-activate based on context matching:
- Description matching (keywords in user input or file content)
- File type detection (e.g., working with .md files triggers spec-kit-workflow)
- Command integration (e.g., /workflow:implement triggers production skills)
- No explicit user invocation required

**Validation**: Skills activate correctly 95%+ of time based on context

---

### FR-064: Directory Organization
Skills MUST be organized by process in `.claude/skills/`:
```
.claude/skills/
├── development/          # Skills for building this system
│   ├── spec-kit-workflow/
│   ├── claude-code-architecture/
│   └── research-synthesis/
└── production/           # Skills for dashboard developers
    ├── data-analysis/
    ├── plotly-viz/
    ├── dash-components/
    ├── accessibility-audit/
    └── performance-optimizer/
```

**Validation**: Directory structure matches specification

---

### FR-065: SKILL.md Format
Each Skill MUST have SKILL.md file with:
- **YAML frontmatter**: name, description, allowed-tools
- **Level 2 content**: Core instructions and patterns
- **File size**: ~1000-1500 tokens total (frontmatter + content)

**Format**:
```yaml
---
name: skill-name
description: Skill description that triggers activation (40-60 tokens)
allowed-tools: [Read, Write, Edit, Bash, mcp__*]
---

# Skill Name

## Quick Start
[Essential workflow...]

## Core Patterns
[Common use cases...]
```

**Validation**: All SKILL.md files parse correctly, follow format

---

### FR-066: Allowed Tools Declaration
Skills MUST declare allowed-tools in YAML frontmatter:
- Restricts which tools skill can reference
- Prevents inappropriate tool usage
- Documents skill capabilities

**Examples**:
- `data-analysis`: [Read, Bash, mcp__postgres, mcp__filesystem]
- `plotly-viz`: [Read, Write, Edit]
- `accessibility-audit`: [Read, Bash]

**Validation**: Skills only reference declared tools

---

### FR-067: Level 1 Token Budget
System MUST load Level 1 (metadata) at startup with budget:
- **Per skill**: ~50 tokens (name + description + allowed-tools)
- **20 skills**: ~1000 tokens total
- **100 skills**: ~5000 tokens (still manageable)

**Validation**: Measure actual token usage at startup

---

### FR-068: Level 2 Token Budget
System MUST load Level 2 (core) when skill activates with budget:
- **Target**: ~800 tokens per skill
- **Range**: 500-1000 tokens acceptable
- **Content**: Essential workflow and patterns only

**Validation**: SKILL.md content stays within token budget

---

### FR-069: Level 3 On-Demand Loading
System MUST load Level 3 (references) only when needed:
- Claude explicitly reads reference file via Read tool
- Variable size (1000-5000+ tokens per file)
- Multiple reference files per skill supported

**Reference file types**:
- Detailed guides (STATISTICAL_METHODS.md)
- Complete documentation (WCAG_CHECKLIST.md)
- Code templates (templates/*.py)
- Example scripts (scripts/*.py)

**Validation**: Reference files load only when Read tool called

---

### FR-070: No Conflicts
Skills MUST NOT conflict with Commands or Sub-Agents:
- Skills provide knowledge, Commands provide structure
- Skills auto-activate, Commands user-invoked
- Skills in shared context, Sub-Agents isolated
- Clear architectural distinction maintained

**Validation**: Integration testing shows no conflicts

---

## Development Skills (FR-071 to FR-075)

### FR-071: Spec-Kit Workflow Skill
System MUST provide `spec-kit-workflow` Skill with:
- **Description**: Spec-driven development methodology guide
- **Activation triggers**: Working with spec.md, plan.md, tasks.md files
- **Level 2 content**: Spec-Kit phases (Constitution → Specify → Plan → Tasks)
- **Reference files**: Templates, examples, validation checklist

**Directory structure**:
```
spec-kit-workflow/
├── SKILL.md
├── SPEC_TEMPLATE.md
├── PLAN_TEMPLATE.md
├── TASKS_TEMPLATE.md
├── CONSTITUTION_GUIDE.md
├── examples/
└── validation/
```

**Validation**: Skill activates during spec creation, provides correct templates

---

### FR-072: Claude Code Architecture Skill
System MUST provide `claude-code-architecture` Skill with:
- **Description**: Commands, Skills, Sub-Agents, Hooks expertise
- **Activation triggers**: Working with .claude/ directory, architectural decisions
- **Level 2 content**: Decision matrix (when to use what)
- **Reference files**: Complete guides for each mechanism

**Directory structure**:
```
claude-code-architecture/
├── SKILL.md
├── COMMANDS_GUIDE.md
├── SUBAGENTS_GUIDE.md
├── SKILLS_GUIDE.md
├── HOOKS_GUIDE.md
├── DECISION_MATRIX.md
├── reference/
└── examples/
```

**Validation**: Skill provides correct architectural guidance

---

### FR-073: Research Synthesis Skill
System MUST provide `research-synthesis` Skill with:
- **Description**: Analyze reference implementations and extract patterns
- **Activation triggers**: Research tasks, documentation analysis
- **Level 2 content**: Research process (discovery, analysis, synthesis)
- **Reference files**: Analysis methods, pattern extraction techniques

**Directory structure**:
```
research-synthesis/
├── SKILL.md
├── ANALYSIS_METHODS.md
├── PATTERN_EXTRACTION.md
├── DOCUMENTATION_GUIDE.md
└── templates/
```

**Validation**: Skill aids in analyzing reference codebases

---

### FR-074: Development Skills Activation
Development Skills MUST activate during planning commands:
- `spec-kit-workflow` → During `/spec:*` commands
- `claude-code-architecture` → When working with `.claude/` directory
- `research-synthesis` → During research and documentation tasks

**Validation**: Development Skills auto-activate in appropriate contexts

---

### FR-075: Development Skills References
Development Skills MUST include reference documentation:
- Spec templates and examples
- Architecture guides and decision matrices
- Research methodologies and analysis techniques
- All references properly structured for Level 3 loading

**Validation**: Reference files exist, properly formatted, loadable

---

## Production Skills (FR-076 to FR-085)

### FR-076: Data Analysis Skill
System MUST provide `data-analysis` Skill with:
- **Description**: Statistical analysis, EDA, data quality checking
- **Activation triggers**: Data loading, analysis, "data", "statistics", "EDA"
- **Level 2 content**: Loading workflow, EDA process, quality checks
- **Reference files**: Statistical methods, data quality guide, visualization recommendations
- **Allowed tools**: Read, Bash, mcp__postgres, mcp__filesystem

**Directory structure**:
```
data-analysis/
├── SKILL.md
├── STATISTICAL_METHODS.md
├── DATA_QUALITY.md
├── VISUALIZATION_GUIDE.md
├── scripts/
│   ├── analyze.py
│   ├── quality_check.py
│   └── transform.py
└── examples/
```

**Validation**: Skill provides correct statistical guidance, integrates with MCP

---

### FR-077: Plotly Visualization Skill
System MUST provide `plotly-viz` Skill with:
- **Description**: Chart generation, accessibility, responsive design
- **Activation triggers**: "chart", "visualization", "plot", Plotly code
- **Level 2 content**: Chart selection guide, creation patterns, accessibility basics
- **Reference files**: Detailed chart types guide, WCAG compliance, theming, interactivity
- **Allowed tools**: Read, Write, Edit

**Directory structure**:
```
plotly-viz/
├── SKILL.md
├── CHART_TYPES.md
├── ACCESSIBILITY.md
├── THEMING.md
├── INTERACTIVITY.md
├── templates/
│   ├── bar_chart.py
│   ├── line_chart.py
│   ├── scatter_plot.py
│   └── [others]
└── examples/
```

**Validation**: Skill selects appropriate charts, ensures accessibility

---

### FR-078: Dash Components Skill
System MUST provide `dash-components` Skill with:
- **Description**: Component patterns, callback architecture, layouts
- **Activation triggers**: "component", "callback", "layout", Dash code
- **Level 2 content**: Component creation pattern, callback basics, layout patterns
- **Reference files**: Component patterns, callback architecture, state management
- **Allowed tools**: Read, Write, Edit

**Directory structure**:
```
dash-components/
├── SKILL.md
├── COMPONENT_PATTERNS.md
├── CALLBACK_ARCHITECTURE.md
├── LAYOUT_GUIDE.md
├── STATE_MANAGEMENT.md
├── templates/
└── examples/
```

**Validation**: Skill creates proper Dash components with callbacks

---

### FR-079: Accessibility Audit Skill
System MUST provide `accessibility-audit` Skill with:
- **Description**: WCAG 2.1 Level AA compliance validation
- **Activation triggers**: "accessibility", "WCAG", "a11y", during `/workflow:verify`
- **Level 2 content**: WCAG requirements, audit process, common issues
- **Reference files**: Complete WCAG checklist, detailed guidance per criterion
- **Allowed tools**: Read, Bash

**Directory structure**:
```
accessibility-audit/
├── SKILL.md
├── WCAG_CHECKLIST.md
├── COLOR_CONTRAST.md
├── KEYBOARD_NAV.md
├── SCREEN_READERS.md
├── scripts/
│   ├── check_contrast.py
│   ├── check_aria.py
│   └── generate_report.py
└── examples/
```

**Validation**: Skill detects accessibility violations, suggests fixes

---

### FR-080: Performance Optimizer Skill
System MUST provide `performance-optimizer` Skill with:
- **Description**: Bottleneck detection, optimization strategies
- **Activation triggers**: "slow", "performance", "optimize", performance issues
- **Level 2 content**: Common bottlenecks, optimization strategies
- **Reference files**: Detailed guides for caching, profiling, optimization
- **Allowed tools**: Read, Edit, Bash
- **Targets**: <3s initial load, <1s callback response

**Directory structure**:
```
performance-optimizer/
├── SKILL.md
├── BOTTLENECK_PATTERNS.md
├── OPTIMIZATION_STRATEGIES.md
├── CACHING_GUIDE.md
├── PROFILING.md
├── scripts/
│   ├── profile_callbacks.py
│   ├── analyze_bundle.py
│   └── benchmark.py
└── examples/
```

**Validation**: Skill identifies bottlenecks, improves performance

---

### FR-081: Production Skills Activation
Production Skills MUST activate during workflow commands:
- `data-analysis` → When loading/analyzing data
- `plotly-viz` → When creating visualizations
- `dash-components` → When building Dash components
- `accessibility-audit` → During `/workflow:verify` phase
- `performance-optimizer` → When performance issues detected

**Validation**: Production Skills auto-activate in appropriate contexts

---

### FR-082: Plotly-Viz Accessibility Compliance
`plotly-viz` Skill MUST ensure WCAG 2.1 Level AA compliance:
- Color contrast: 4.5:1 for normal text, 3:1 for large text
- Non-color information encoding (patterns, labels, markers)
- Keyboard navigation support
- ARIA labels and descriptive titles

**Validation**: Charts generated with skill pass accessibility audit

---

### FR-083: Data Analysis Formats
`data-analysis` Skill MUST support multiple data formats:
- CSV files (pandas.read_csv)
- JSON files (pandas.read_json)
- Parquet files (pandas.read_parquet)
- SQL databases (via mcp__postgres or psycopg2)

**Validation**: Skill provides guidance for each format

---

### FR-084: Accessibility Audit Checks
`accessibility-audit` Skill MUST check:
- **Color contrast**: Using WCAG formulas
- **Keyboard navigation**: All interactive elements accessible
- **ARIA labels**: Proper labeling for screen readers
- **Semantic HTML**: Correct use of headings, landmarks
- **Focus indicators**: Visible focus states

**Validation**: Skill detects 90%+ of common violations

---

### FR-085: Performance Optimizer Targets
`performance-optimizer` Skill MUST target:
- **Initial load**: <3 seconds
- **Callback response**: <1 second
- **Time to interactive**: <5 seconds
- **Bundle size**: <500 KB (excluding data)

**Validation**: Optimizations achieve targets 80%+ of time

---

## Skills Integration (FR-086 to FR-090)

### FR-086: Skills Enhance Commands
Skills MUST enhance Commands without replacing them:
- Commands provide workflow structure
- Skills provide domain expertise
- Integration is seamless (no explicit skill invocation)
- Commands benefit from Skills automatically

**Example**: `/workflow:implement` command benefits from `plotly-viz` and `dash-components` Skills

**Validation**: Commands produce better output with Skills than without

---

### FR-087: Skills Discovery
Skills MUST be discoverable via description matching:
- Claude reads skill descriptions (Level 1)
- Matches description keywords to current context
- Activates relevant skills automatically
- No user intervention required

**Validation**: Correct skills activate based on context 95%+ of time

---

### FR-088: Skills + MCP Complementary
Skills MUST work seamlessly with MCP servers:
- **MCP** provides data access (what to access)
- **Skills** provide methodology (how to use data)
- **Example**: mcp__postgres (access) + data-analysis (expertise)
- No conflicts or redundancy

**Validation**: Skills reference MCP tools in allowed-tools, use correctly

---

### FR-089: Example Activation Scenarios
Each Skill MUST include example activation scenarios in documentation:
- User action that triggers skill
- How skill activates (context matching)
- What skill provides (Level 2/3 content)
- Expected outcome

**Validation**: All Skills have documented activation examples

---

### FR-090: Version Control
Skills MUST be version-controlled in repository:
- Located in `.claude/skills/` directory
- Committed to git with code
- Team members get Skills on git pull
- Changes tracked through git history

**Validation**: Skills directory in git, .gitignore excludes nothing

---

## Summary

**30 new requirements** covering:
- Skills architecture and progressive disclosure (FR-061 to FR-070)
- Development Skills for building the system (FR-071 to FR-075)
- Production Skills for dashboard development (FR-076 to FR-085)
- Skills integration with Commands and MCP (FR-086 to FR-090)

These requirements ensure Skills are properly implemented, documented, and integrated into the hybrid workflow architecture.

**Next**: Success Criteria (SC-031 to SC-045) define measurable outcomes for Skills effectiveness.

---

### Key Entities

- **Specification Command**: Command for managing feature specifications
  - Attributes: command name, feature number, spec content, approval status
  - Relationships: Creates specs, validates specs, manages spec lifecycle

- **EPIC Workflow Command**: Command implementing EPIC methodology phase
  - Attributes: command name, phase (observe/act/verify/loop), current context
  - Relationships: Follows sequence, updates task tracking, enforces TDD

- **Utility Command**: General-purpose developer utility
  - Attributes: command name, tool invoked (pytest, ruff, git), options
  - Relationships: Operates on codebase, reports results

- **Dash Command**: Dashboard-specific generator
  - Attributes: command name, artifact type (component/layout/callback), template
  - Relationships: Creates Dash code, generates tests, follows Dash patterns

- **Sub-Agent**: Autonomous specialist agent
  - Attributes: agent name, specialization, task queue, status, tools
  - Relationships: Receives tasks, works independently, reports completion, coordinates with other agents

- **Command Definition File**: Markdown file defining a command
  - Attributes: file path, YAML frontmatter, instruction content, examples
  - Relationships: Located in `.claude/commands/`, parsed by Claude Code

- **Sub-Agent Definition File**: Markdown file defining a sub-agent
  - Attributes: file path, YAML frontmatter, system prompt, responsibilities
  - Relationships: Located in `.claude/agents/`, instantiated by Claude Code



- **Agent Skill**: Domain knowledge provider with progressive disclosure
  - Attributes: name, description, directory structure, loading levels (1-3), allowed-tools, token budgets
  - Relationships: Auto-activates during Commands, complements MCP, distinct from Sub-Agents, benefits both planning and execution

- **Skill Level**: Progressive disclosure tier
  - Attributes: level number (1-3), token budget, content type (metadata/core/references)
  - Relationships: Belongs to Skill, loads sequentially based on need

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

#### Specification Workflow

- **SC-001**: Developers can create a new specification in under 3 minutes using `/spec.create`
- **SC-002**: Specification validation (`/spec.validate`) completes in under 10 seconds
- **SC-003**: 100% of implementations start with an approved specification (spec-first enforced)
- **SC-004**: Feature branch creation (`/spec.branch`) succeeds 100% of the time for valid spec numbers

#### EPIC Workflow

- **SC-005**: Complete observe → act → verify → loop cycle completes in under 15 minutes for typical tasks
- **SC-006**: `/workflow.verify` catches 90%+ of issues before manual review
- **SC-007**: EPIC workflow sequence violations are caught and reported 100% of the time
- **SC-008**: `/workflow.act` enforces TDD (test first) in 100% of cases
- **SC-009**: `/workflow.status` accurately reflects spec requirement completion within 5% margin

#### Code Quality

- **SC-010**: Code generated by commands passes all quality checks (Black, Ruff, mypy) 95%+ of the time
- **SC-011**: Generated tests achieve 80%+ coverage 90%+ of the time
- **SC-012**: `/utils.format` successfully formats code without errors 100% of the time
- **SC-013**: No regressions introduced by commands (existing tests continue to pass)

#### Dash Commands

- **SC-014**: `/dash.component` generates components that follow Plotly Dash best practices 95%+ of the time
- **SC-015**: `/dash.callback` generates working callbacks with correct input/output signatures 90%+ of the time
- **SC-016**: `/dash.a11y` detects 90%+ of WCAG 2.1 AA violations
- **SC-017**: `/dash.serve` successfully starts development server 100% of the time

#### Sub-Agents

- **SC-018**: Sub-agents complete assigned tasks successfully 90%+ of the time
- **SC-019**: File conflicts between sub-agents occur less than 5% of the time
- **SC-020**: Sub-agents reduce implementation time by 30%+ compared to sequential work
- **SC-021**: Sub-agent timeout and error recovery works correctly 100% of the time

#### Usability

- **SC-022**: Developers can discover and use commands without referring to external documentation 80%+ of the time
- **SC-023**: Command typos result in helpful suggestions 90%+ of the time
- **SC-024**: Developer satisfaction with command interface: 4.0/5.0 or higher
- **SC-025**: Developer onboarding to command usage: under 30 minutes

#### Performance

- **SC-026**: Specification commands execute in under 10 seconds
- **SC-027**: EPIC workflow commands execute in under 30 seconds
- **SC-028**: Utility commands execute in under 60 seconds
- **SC-029**: Dash commands execute in under 30 seconds
- **SC-030**: Sub-agent launch time: under 10 seconds

---

## Skills Effectiveness (SC-031 to SC-035)

### SC-031: Correct Activation Rate
Skills activate correctly based on context **95%+ of the time**

**Measurement**:
- Track skill activations during development sessions
- Verify activation was appropriate for context
- Count false positives (inappropriate activation)
- Count false negatives (should have activated but didn't)

**Target**:
- False positives: <5%
- False negatives: <5%

**Example**:
- User works on data analysis → `data-analysis` skill activates ✓
- User creates chart → `plotly-viz` skill activates ✓
- User writes tests → Data skills don't activate (correct non-activation) ✓

---

### SC-032: Context Efficiency
Progressive disclosure reduces context usage by **60%+ vs. loading all content upfront**

**Measurement**:
- Baseline: Load all 8 Skills Level 2+3 content = ~80,000 tokens
- With progressive disclosure:
  - Startup: 8 Skills × 50 tokens = 400 tokens
  - Typical session: 3-4 Skills activate Level 2 = +2,400-3,200 tokens
  - Occasional Level 3: 1-2 reference files = +2,000-4,000 tokens
  - Total: ~5,000-8,000 tokens

**Target**: 60-90% reduction in context usage
**Calculation**: (80,000 - 8,000) / 80,000 = 90% reduction ✓

**Benefit**: Can support 100+ skills with minimal overhead

---

### SC-033: Development Efficiency
Development Skills reduce spec creation time by **40%+ vs. without Skills**

**Measurement**:
- **Without Skills**: Manually reference templates, examples, guidelines
  - Average spec creation: 60 minutes
- **With spec-kit-workflow Skill**: Auto-provides templates, examples, validation
  - Average spec creation: 35 minutes
  - Reduction: (60 - 35) / 60 = 42% ✓

**Target**: 40%+ reduction in time
**Secondary benefit**: Higher quality specs (fewer missing sections)

---

### SC-034: Code Quality Improvement
Production Skills improve code quality across multiple dimensions:

**Accessibility** (`accessibility-audit` Skill):
- **Without Skill**: 60% of dashboards WCAG compliant
- **With Skill**: 95%+ of dashboards WCAG compliant
- **Improvement**: +35 percentage points

**Performance** (`performance-optimizer` Skill):
- **Without Skill**: 50% of dashboards meet <3s load target
- **With Skill**: 85%+ of dashboards meet <3s load target
- **Improvement**: +35 percentage points

**Test Coverage** (Skills guide TDD approach):
- **Without Skill**: Average 65% coverage
- **With Skill**: Average 82% coverage
- **Improvement**: +17 percentage points

**Target**: 30%+ improvement in quality metrics

---

### SC-035: Skill Activation Latency
Skills activate and load content quickly: **<2 seconds for Level 2 load**

**Measurement**:
- Time from context match to Level 2 content available
- Includes: File read, parsing, context loading

**Breakdown**:
- Read SKILL.md file: ~0.3s
- Parse and process: ~0.2s
- Context integration: ~0.5s
- Total: ~1.0s ✓

**Target**: <2 seconds (avg <1.5s)
**User impact**: Imperceptible delay

---

## Skills Adoption (SC-036 to SC-038)

### SC-036: Transparent Usage
Dashboard developers use Skills without explicit invocation **90%+ of the time**

**Measurement**:
- Track user sessions: Do users mention skills explicitly?
- **Desired**: "Create a chart" → plotly-viz activates automatically
- **Undesired**: "Use the plotly-viz skill to create a chart"

**Target**:
- 90%+ of skill activations are automatic (no user mention)
- 10% or less require explicit guidance

**Benefit**: Skills feel like native Claude expertise, not external tools

---

### SC-037: Documentation Clarity
Skills documentation receives **4.5/5.0+ rating** for clarity

**Measurement**:
- User surveys after first month
- Questions:
  - "How clear is the Skills documentation?"
  - "Can you understand when each Skill activates?"
  - "Are the directory structures well-documented?"
- Scale: 1-5 (1=very unclear, 5=very clear)

**Target**: Average ≥4.5/5.0

**Focus areas**:
- SKILL.md readability
- Activation trigger clarity
- Integration examples

---

### SC-038: Output Quality with Skills
Skill-enhanced commands produce better output **80%+ of the time**

**Measurement**:
- A/B comparison: Same task with/without Skills
- Quality dimensions:
  - Code correctness
  - Following best practices
  - Accessibility compliance
  - Performance optimization
  - Test coverage

**Example**:
- Task: "Create sales bar chart"
- **Without plotly-viz**: Basic chart, no accessibility, default colors
- **With plotly-viz**: Accessible chart, WCAG compliant, proper labels, responsive
- **Result**: With Skills is better ✓

**Target**: 80%+ of comparisons favor Skills-enhanced output

---

## Skills Maintenance (SC-039 to SC-041)

### SC-039: Token Budget Compliance
Skills remain under token budgets **95%+ of the time**

**Budgets**:
- **Level 1** (metadata): 50 tokens per skill
- **Level 2** (core): 800 tokens per skill
- **Level 3** (references): Variable, but documented

**Measurement**:
- Automated token counting in CI/CD
- Check SKILL.md file sizes
- Verify frontmatter + content ≤ target

**Target**:
- 95%+ of Skills meet Level 1 budget (40-60 tokens)
- 95%+ of Skills meet Level 2 budget (600-1000 tokens)
- Level 3 budgets documented and justified

**Enforcement**: CI checks fail if budgets exceeded

---

### SC-040: Update Without Breakage
Skills updates don't break existing workflows **98%+ of the time**

**Measurement**:
- Track Skill changes in git
- Run regression tests after each Skill update
- Monitor for workflow disruptions

**Target**:
- 98%+ of Skill updates don't cause failures
- 2% breakage acceptable if documented and fixed within 24 hours

**Protection**:
- Integration tests cover Skill activation
- Backward compatibility maintained
- Version documentation in SKILL.md

---

### SC-041: Low Conflict Rate
Skill conflicts (inappropriate activation, interference) occur **<1% of time**

**Conflict Types**:
1. **Activation conflict**: Multiple skills activate when one appropriate
2. **Content conflict**: Skills provide contradictory guidance
3. **Tool conflict**: Skill references unavailable tool

**Measurement**:
- Track user reports of conflicts
- Automated detection where possible
- Total conflicts / total skill activations

**Target**: <1% conflict rate

**Example of acceptable conflict**:
- `data-analysis` and `plotly-viz` both activate for "create chart from data"
- This is complementary (analyze then visualize), not conflicting ✓

---

## Integration Metrics (SC-042 to SC-045)

### SC-042: Commands + Skills Synergy
Commands with Skills complete tasks **30%+ faster** than Commands alone

**Measurement**:
- Baseline: Commands without Skills
- Enhanced: Commands with Skills auto-activating
- Measure: Time to complete typical tasks

**Example Tasks**:
1. Create spec for new feature
2. Implement data visualization component
3. Fix accessibility issues
4. Optimize slow dashboard

**Results Expected**:
- Spec creation: 60min → 35min (42% faster) ✓
- Visualization: 45min → 30min (33% faster) ✓
- Accessibility: 30min → 18min (40% faster) ✓
- Optimization: 50min → 35min (30% faster) ✓

**Overall Target**: 30%+ average improvement

---

### SC-043: MCP + Skills Integration
MCP and Skills integration works seamlessly **100% of the time**

**Integration Points**:
1. `data-analysis` Skill references `mcp__postgres` in allowed-tools
2. Skill provides guidance on using MCP tools
3. No conflicts between MCP and Skills

**Measurement**:
- All tasks requiring data access complete successfully
- Skills correctly guide MCP usage
- No "tool not found" or "permission denied" errors

**Target**: 100% success rate (zero integration failures)

**Example**:
```
User: Analyze sales data from PostgreSQL
→ mcp__postgres connects to database (access)
→ data-analysis Skill guides analysis (methodology)
→ plotly-viz Skill creates chart (visualization)
Result: Complete workflow, zero failures ✓
```

---

### SC-044: Sub-Agents Benefit from Skills
Sub-Agents successfully leverage Skills when applicable **90%+ of the time**

**Scenario**:
- Sub-Agent `component-builder` creates Dash components
- Within Sub-Agent context, `dash-components` and `plotly-viz` Skills available
- Sub-Agent benefits from Skills' expertise

**Measurement**:
- Sub-Agent output quality with Skills vs. without
- Skills activate within Sub-Agent context appropriately
- No context isolation issues

**Target**: 90%+ of Sub-Agent tasks benefit from Skills

**Note**: Sub-Agents have isolated context, but Skills should still be available

---

### SC-045: Efficient Discovery
Skills load only when needed: **0 Skills loaded when unnecessary**

**Measurement**:
- Session without data work: `data-analysis` should NOT load Level 2 ✓
- Session without charts: `plotly-viz` should NOT load Level 2 ✓
- Session without accessibility checks: `accessibility-audit` should NOT load ✓

**Efficient Discovery Means**:
- Level 1 (metadata) always loaded (~1000 tokens for 20 skills)
- Level 2 only when skill is relevant
- Level 3 only when specifically needed

**Target**:
- No false positive Level 2 loads
- No unnecessary Level 3 loads
- Context stays lean when skills not needed

**Example Measurement**:
- Simple spec editing session:
  - Loaded: spec-kit-workflow (Level 2) = +800 tokens
  - NOT loaded: All production skills = 0 tokens
  - Efficient ✓

---

## Summary Dashboard

| Category | Metrics | Targets |
|----------|---------|---------|
| **Effectiveness** | 5 metrics | 95% activation rate, 60% context reduction, 40% time savings, 30% quality improvement, <2s latency |
| **Adoption** | 3 metrics | 90% transparent usage, 4.5/5.0 clarity rating, 80% better output |
| **Maintenance** | 3 metrics | 95% budget compliance, 98% update success, <1% conflicts |
| **Integration** | 4 metrics | 30% faster with Commands, 100% MCP integration, 90% Sub-Agent benefit, 0 unnecessary loads |

**Total**: 15 new success criteria measuring Skills from all angles

---

## Measurement Plan

### Automated Metrics
- Token usage tracking (SC-032, SC-035, SC-039, SC-045)
- Activation logging (SC-031, SC-036, SC-041)
- Performance benchmarks (SC-042)
- Integration tests (SC-043, SC-044)

### User Surveys
- Documentation clarity (SC-037)
- Output quality comparison (SC-038)

### Development Tracking
- Time tracking for tasks (SC-033, SC-042)
- Quality metrics (SC-034)
- Breakage monitoring (SC-040)

### Review Cadence
- **Daily**: Automated metrics in CI/CD
- **Weekly**: Development time tracking analysis
- **Monthly**: User surveys and quality assessments
- **Quarterly**: Comprehensive Skills effectiveness review

---

**Integration with Core Success Criteria**:
- SC-001 to SC-030: Commands, workflow, code quality
- SC-031 to SC-045: Skills effectiveness and integration
- **Together**: Complete picture of system success

**Next**: Clarifications section (Q6-Q10) explains Skills concepts in detail

---

## Non-Functional Requirements

### Performance
- Command execution: < 30 seconds (excluding long-running operations like full test suites)
- Sub-agent launch: < 10 seconds
- Help command response: < 2 seconds

### Usability
- Commands use clear, intuitive naming following pattern `/category.action`
- Error messages are actionable with examples
- Help documentation is comprehensive and includes examples
- Command arguments use clear, descriptive names

### Reliability
- Commands succeed 95%+ of the time with valid inputs
- Sub-agents recover from failures automatically when possible
- No data loss on command failure (atomic operations)
- Graceful degradation when optional features unavailable

### Maintainability
- Command definitions are human-readable Markdown
- Sub-agent definitions are clear and well-documented
- Configuration uses standard formats (JSON, YAML, Markdown)
- Commands are modular and testable in isolation

### Security
- Bash command restrictions enforce security boundaries
- No hardcoded credentials in command definitions
- Commands validate and sanitize user inputs
- Sub-agents operate with least privilege necessary

## Technology Stack

### Required
- **Claude Code**: Development environment with custom command support
- **Python 3.11+**: Runtime environment
- **Plotly Dash 2.14+**: Dashboard framework
- **Git**: Version control

### Development Tools
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **Black**: Code formatting
- **Ruff**: Fast Python linter
- **mypy**: Static type checker

### File Formats
- **Markdown**: Command and sub-agent definitions
- **YAML**: Frontmatter in definition files
- **JSON**: Settings and configuration

## Out of Scope

The following are explicitly **not** included in this specification:

- Visual command builder or GUI (CLI-based only)
- Commands for non-Dash frameworks (Flask, FastAPI, etc.)
- Automatic code generation without specifications (spec-first required)
- Real-time collaboration between developers
- Integration with non-Claude AI tools
- Cloud deployment automation (Agent SDK deployment is separate feature)
- Database migration commands (handled in individual feature specs)
- Performance monitoring and APM integration

---

## Clarifications

### Q1: How does EPIC methodology map to commands?
**A**: EPIC is implemented as four sequential workflow commands:
- **Observe** (`/workflow.observe`): Read spec, analyze codebase, identify next task
- **Act** (`/workflow.act`): Implement task using TDD (test first, then code)
- **Verify** (`/workflow.verify`): Run tests, lint, type check, validate against spec
- **Loop** (`/workflow.loop`): Checkpoint progress (git commit), present next task options, return to observe

### Q2: When should I use sub-agents vs. regular workflow commands?
**A**: Use sub-agents when:
- Task is large and self-contained (e.g., "build 5 dashboard components")
- Task can proceed independently without constant user decisions
- Parallel work would significantly speed up development

Use regular workflow commands when:
- Task requires user decisions or clarifications
- You're learning the codebase or exploring options
- Task is small and quick (< 15 minutes)

### Q3: What's the difference between utility commands and workflow commands?
**A**:
- **Workflow commands** implement EPIC methodology and are used for feature development (observe → act → verify → loop)
- **Utility commands** are standalone tools for specific tasks (testing, formatting, git operations) that can be run anytime

### Q4: Can commands be customized or extended?
**A**: Yes. Commands are defined in Markdown files in `.claude/commands/`. Developers can:
- Modify existing command definitions
- Add new commands by creating new `.md` files
- Create custom sub-agents by adding `.md` files to `.claude/agents/`

All definitions use human-readable Markdown with YAML frontmatter.

### Q5: How do commands enforce spec-first workflow?
**A**: Implementation commands (`/workflow.act`, `/dash.*` generators) check for:
1. Current git branch matches a feature branch created by `/spec.branch`
2. Corresponding spec file exists in `.specify/specs/`
3. Spec status is "approved" (not "draft")

If any check fails, the command blocks and guides user to create/approve spec first.

---

## Q6: What's the difference between Skills and Commands?

**A**: Skills and Commands serve fundamentally different purposes and are complementary, not competing.

### Commands (User-Invoked)

**Invocation**: User explicitly types command (e.g., `/workflow:implement`)

**Purpose**: Provide workflow structure and sequence

**Example**:
```bash
User: /workflow:implement Create sales dashboard

Command does:
1. Sets up TDD workflow (tests first)
2. Structures implementation process
3. Enforces quality gates (testing, linting)
4. Manages git operations
```

**Characteristic**: Synchronous, predictable, user-controlled

---

### Skills (Model-Invoked)

**Invocation**: Claude automatically activates based on context

**Purpose**: Provide domain expertise and methodology

**Example**:
```bash
# Same task, but showing Skills

User: /workflow:implement Create sales dashboard

Skills auto-activate:
- dash-components (detecting "dashboard")
- plotly-viz (will create charts)
- accessibility-audit (ensure WCAG compliance)

Skills provide:
- Component structure patterns
- Chart selection guidance
- Accessibility requirements
```

**Characteristic**: Asynchronous, context-driven, automatic

---

### Integration Example

**Complete workflow showing both**:

```
User: /workflow:implement Task 5 - Create bar chart component

1. COMMAND `/workflow:implement` provides STRUCTURE:
   ✓ Read task from tasks.md
   ✓ Create test file first (TDD)
   ✓ Create implementation file
   ✓ Run verification
   ✓ Commit if successful

2. SKILLS provide EXPERTISE (auto-activated):
   ✓ plotly-viz: "For bar chart, use plotly.express.bar()..."
   ✓ plotly-viz: "Ensure WCAG 2.1 AA: contrast ratio 4.5:1..."
   ✓ dash-components: "Structure component with dcc.Graph()..."
   ✓ accessibility-audit: "Add aria-label: 'Bar chart showing...'"

3. RESULT: Command completes with Skill-enhanced quality
   ✓ Test file created: test_sales_chart.py
   ✓ Implementation: sales_chart.py (accessible, optimized)
   ✓ Tests pass, coverage 85%
   ✓ WCAG compliant
```

**Key Insight**: Command says "WHAT to do" (implement task), Skills say "HOW to do it well" (with accessibility, best practices, optimization).

---

### Decision Guide

**Use Commands when you want to**:
- Trigger a specific workflow
- Follow a defined sequence
- Have explicit control

**Use Skills when you want to**:
- Provide reusable knowledge
- Activate based on context
- Scale expertise across many tasks

**In our setup**: We use BOTH together for maximum effectiveness.

---

## Q7: What's the difference between Skills and Sub-Agents?

**A**: Skills and Sub-Agents have different architectural patterns and use cases.

### Comparison Table

| Aspect | Skills | Sub-Agents |
|--------|--------|------------|
| **Context** | Shared with main agent | Isolated context window |
| **Invocation** | Automatic (context-based) | Manual/delegated |
| **Purpose** | Domain knowledge | Task execution |
| **Parallelism** | No (sequential) | Yes (true parallel work) |
| **Tool Calls** | 3-4x more (progressive) | Fewer (dedicated context) |
| **Best For** | Reusable expertise | Self-contained work |
| **Example** | `plotly-viz` | `component-builder` |

---

### Skills: Shared Context, Progressive Knowledge

**Pattern**:
```
Main Agent Context (200K tokens)
├── User conversation
├── Task information
├── Skill: spec-kit-workflow (Level 2 loaded: +800 tokens)
├── Skill: plotly-viz (Level 2 loaded: +800 tokens)
└── Skill: accessibility-audit (activated when needed)
```

**Characteristics**:
- Skills share context with main agent
- Progressive disclosure (load incrementally)
- More tool calls (reading skill files)
- Knowledge benefits all subsequent tasks

**Use When**:
- Expertise is reusable across tasks
- Context sharing important
- Sequential work preferred

---

### Sub-Agents: Isolated Context, Parallel Execution

**Pattern**:
```
Main Agent Context
└── Delegates task

    Sub-Agent: component-builder (Isolated 200K context)
    ├── Task: "Create 3 dashboard components"
    ├── Skills available in Sub-Agent context too!
    │   ├── dash-components
    │   └── plotly-viz
    └── Works independently

    Main Agent continues other work in parallel
```

**Characteristics**:
- Sub-Agents have separate context windows
- Can work in true parallel
- Less context noise (focused on task)
- Complete task then return results

**Use When**:
- Task is self-contained
- Parallel execution helps
- Context isolation beneficial

---

### Working Together

**Scenario**: Build dashboard with 5 components + data pipeline

**Option 1: Main Agent + Skills** (Sequential)
```
Main Agent:
1. Create component 1 (plotly-viz & dash-components Skills help)
2. Create component 2 (same Skills help)
3. Create component 3 (same Skills help)
4. Create data pipeline (data-analysis Skill helps)
5. Create component 4 (Skills help)
6. Create component 5 (Skills help)

Time: ~90 minutes (sequential)
```

**Option 2: Main Agent + Sub-Agents + Skills** (Parallel)
```
Main Agent:
1. Launch component-builder Sub-Agent: "Create components 1-5"
   → Sub-Agent uses dash-components and plotly-viz Skills
2. Launch data-pipeline Sub-Agent: "Create data loaders"
   → Sub-Agent uses data-analysis Skill
3. While Sub-Agents work, prepare integration

Sub-Agents complete independently, then integrate

Time: ~35 minutes (parallel)
```

**Best Approach**: Use Sub-Agents for parallel work, and Skills enhance BOTH main agent AND Sub-Agents.

---

### Example: Skills Working in Sub-Agent

```python
# Sub-Agent: component-builder

# Task: Create sales chart component

# Skills activate WITHIN Sub-Agent context:
# - plotly-viz (chart creation)
# - dash-components (component structure)
# - accessibility-audit (WCAG compliance)

# Result: Sub-Agent creates high-quality component using Skills
```

**Key Insight**: Skills are available everywhere (main agent and Sub-Agents). Sub-Agents provide parallel capacity, Skills provide expertise.

---

## Q8: How does progressive disclosure actually work?

**A**: Progressive disclosure is a three-level loading pattern that keeps context lean while providing deep expertise.

### The Three Levels Explained

---

#### Level 1: Metadata Only (~50 tokens)

**When Loaded**: At Claude Code startup (before any user interaction)

**Content**: YAML frontmatter from SKILL.md
```yaml
---
name: data-analysis
description: Load, analyze, and generate insights from datasets including CSV, JSON, Parquet, SQL databases. Use when exploring data, performing statistical analysis, identifying trends, or creating data transformations for dashboards. Automatically invoked when user mentions data exploration, EDA, statistics, or data quality.
allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
---
```

**Token Count**: ~50 tokens (name ~2, description ~40, allowed-tools ~8)

**Purpose**:
- Help Claude discover which skills exist
- Match skill descriptions to current context
- Decide which skills to activate

**With 20 Skills**: 20 × 50 = 1,000 tokens at startup (minimal overhead)

---

#### Level 2: Core Instructions (~800 tokens)

**When Loaded**: Claude determines skill is relevant to current task

**Content**: Main SKILL.md content (after frontmatter)
```markdown
# Data Analysis Skill

## Quick Start
1. Load data using pandas or SQL
2. Perform exploratory data analysis (EDA)
3. Generate statistical summaries
4. Identify data quality issues
5. Suggest appropriate visualizations

## Core Workflow

### Loading Data
[Pandas patterns, SQL connection patterns...]

### Exploratory Data Analysis
[EDA process: shape, types, nulls, describe, correlations...]

### Data Quality Checks
[Missing values, outliers, duplicates, consistency...]

### Visualization Recommendations
[Chart selection based on data types...]

## Common Patterns
[Typical workflows...]
```

**Token Count**: ~800 tokens (500-1000 acceptable range)

**Purpose**:
- Provide essential methodology
- Cover 80% of common use cases
- Enable Claude to work effectively

**Loading Trigger**:
```
User: Analyze sales data

→ "Analyze" and "data" keywords match data-analysis description
→ Claude loads data-analysis Level 2
→ +800 tokens added to context
→ Claude now has EDA methodology available
```

---

#### Level 3: Reference Materials (Variable size)

**When Loaded**: Claude needs specific deep knowledge

**Content**: Separate reference files in skill directory
```
data-analysis/
├── SKILL.md                    # Levels 1 & 2
├── STATISTICAL_METHODS.md      # ~2000 tokens (Level 3)
├── DATA_QUALITY.md             # ~1500 tokens (Level 3)
├── VISUALIZATION_GUIDE.md      # ~1800 tokens (Level 3)
└── scripts/
    └── analyze.py              # Loaded when executed (Level 3)
```

**Token Count**: Variable per file (1000-5000+ tokens)

**Purpose**:
- Provide deep expertise for specific scenarios
- Detailed reference documentation
- Complex examples and templates

**Loading Trigger**:
```
Claude (internal): User needs hypothesis testing guidance

→ Claude uses Read tool: data-analysis/STATISTICAL_METHODS.md
→ +2000 tokens added to context
→ Now has detailed statistical methods available
→ Provides comprehensive guidance to user
```

**Important**: Level 3 files load **only when Claude explicitly reads them**, not automatically.

---

### Token Usage Comparison

**Scenario**: Session working with data, creating charts, checking accessibility

**Without Progressive Disclosure** (Load everything upfront):
```
At startup:
- All 8 Skills, full content loaded
- data-analysis: +3000 tokens
- plotly-viz: +3500 tokens
- dash-components: +3200 tokens
- accessibility-audit: +4000 tokens
- (and 4 more...)
Total: ~25,000 tokens before any work

During session:
- All knowledge immediately available
- No additional loading needed

Total session: 25,000 tokens (high context pressure)
```

**With Progressive Disclosure** (Our approach):
```
At startup:
- All 8 Skills, Level 1 only
- 8 × 50 = 400 tokens

During session:
- data-analysis activates (Level 2): +800 tokens
- plotly-viz activates (Level 2): +800 tokens
- accessibility-audit activates (Level 2): +800 tokens
- One Level 3 reference needed: +2000 tokens

Total session: 400 + 2400 + 2000 = 4,800 tokens

Savings: 25,000 - 4,800 = 20,200 tokens (81% reduction)
```

**Benefits**:
1. Can support 100+ skills (5,000 tokens at startup vs. impossible with full loading)
2. Context stays lean (more room for code, conversation)
3. Still get deep expertise when needed
4. Scales to large knowledge bases

**Trade-off**:
- More tool calls (Claude reads skill files)
- Slight latency for Level 2/3 loading (~1-2 seconds)
- Worth it for the context efficiency

---

### How Claude Decides What to Load

**Level 1 → Level 2 Decision**:
```
1. User input or file context contains keywords
2. Claude checks Level 1 descriptions (all loaded)
3. Finds matching keywords (e.g., "analyze data" matches data-analysis)
4. Activates skill: Reads SKILL.md content
5. Level 2 now available for this skill
```

**Level 2 → Level 3 Decision**:
```
1. Claude is using Level 2 knowledge
2. Encounters scenario needing deeper expertise
3. Claude explicitly uses Read tool on reference file
4. Level 3 content loaded
5. Provides detailed guidance
```

**Important**: All loading decisions are made by Claude based on context, not by user commands.

---

## Q9: What Skills should I create for my use case?

**A**: Skills depend on whether you're building the system (development) or using it (production).

### Development Skills (Building the System)

If you're setting up Claude Code for a new domain, create these types of skills:

#### 1. Methodology Skill

**Purpose**: Guide the development approach

**Example**: `spec-kit-workflow`
- Specification writing methodology
- Planning and task breakdown
- Quality gates and validation

**When to Create**: You have a defined development methodology to encode

---

#### 2. Architecture Skill

**Purpose**: Decisions about system structure

**Example**: `claude-code-architecture`
- When to use Commands vs Skills vs Sub-Agents
- Directory structure patterns
- Configuration best practices

**When to Create**: You're building something with architectural choices

---

#### 3. Domain Research Skill

**Purpose**: Analyze reference materials

**Example**: `research-synthesis`
- Extract patterns from reference repos
- Analyze documentation
- Create implementation guides

**When to Create**: You frequently reference existing implementations

---

### Production Skills (Using the System)

If you're building dashboards (or whatever your domain is), create these types:

#### 1. Data Processing Skill

**Purpose**: How to work with data

**Example**: `data-analysis`
- Data loading patterns
- Analysis methodology
- Quality checking

**When to Create**: Domain involves data processing

---

#### 2. Visualization Skill

**Purpose**: How to create visualizations

**Example**: `plotly-viz`
- Chart type selection
- Accessibility compliance
- Best practices

**When to Create**: Domain involves visual output

---

#### 3. Component/Framework Skill

**Purpose**: Framework-specific patterns

**Example**: `dash-components`
- Component structure
- Framework-specific patterns (callbacks, layouts)
- State management

**When to Create**: You use a specific framework extensively

---

#### 4. Quality Assurance Skill

**Purpose**: Automated quality checking

**Example**: `accessibility-audit`
- Compliance checking (WCAG, etc.)
- Automated validation
- Common issue detection

**When to Create**: You have specific quality standards to enforce

---

#### 5. Performance Skill

**Purpose**: Optimization guidance

**Example**: `performance-optimizer`
- Bottleneck patterns
- Optimization strategies
- Performance targets

**When to Create**: Performance is critical in your domain

---

### Creating Custom Skills

**Template**:
```
my-custom-skill/
├── SKILL.md                      # Required
│   └── YAML frontmatter + core content
├── REFERENCE_GUIDE.md            # Optional (Level 3)
├── EXAMPLES.md                   # Optional (Level 3)
├── scripts/                      # Optional (Level 3)
└── templates/                    # Optional (Level 3)
```

**SKILL.md Template**:
```markdown
---
name: my-custom-skill
description: Clear description with keywords that trigger activation. Mention use cases, when to use, what problem it solves. Keep to 40-60 tokens.
allowed-tools: [Read, Write, Edit, Bash]
---

# My Custom Skill

## Quick Start
[3-5 step workflow]

## Core Patterns
[Essential knowledge for 80% of use cases]

## Common Scenarios
[Examples of when this skill helps]

## Integration
[How this skill works with others]
```

**Best Practices**:
1. **Clear Description**: Include keywords that match when skill should activate
2. **Focused Scope**: One skill = one domain of expertise
3. **Progressive Disclosure**: Keep SKILL.md under 1000 tokens, detailed stuff in Level 3
4. **Examples**: Show activation scenarios
5. **Integration**: Document how skill works with Commands, other Skills

---

### Our Dashboard Development Skills

**Development Phase** (3 skills):
- `spec-kit-workflow` - How to write specs
- `claude-code-architecture` - How to structure .claude/
- `research-synthesis` - How to analyze references

**Production Phase** (5 skills):
- `data-analysis` - How to process data
- `plotly-viz` - How to create charts
- `dash-components` - How to build components
- `accessibility-audit` - How to ensure WCAG compliance
- `performance-optimizer` - How to optimize performance

**Total**: 8 skills covering full lifecycle

---

## Q10: How do Skills work with the hybrid workflow?

**A**: Skills enhance BOTH processes in the hybrid workflow architecture.

### Recap: Two-Process Model

**Process 1: Spec-Kit** (Planning)
- Constitution → Specify → Plan → Tasks → [Approval] → tasks.md

**Process 2: Claude Code** (Execution)
- For each task: Research → Implement → Verify → Next

**Handoff**: tasks.md file (frozen after approval)

See `specs/WORKFLOW.md` for complete documentation.

---

### Skills in Process 1: Spec-Kit Planning

**Commands**: `/spec:*`

**Skills Active**:
- `spec-kit-workflow` (development)
- `claude-code-architecture` (development)
- `research-synthesis` (development)

**Example Flow**:

```bash
# Step 1: Create Specification
User: /spec:specify Create sales analytics dashboard

Command /spec:specify:
- Creates specs/NNN-sales-dashboard/spec.md
- Prompts for user stories, requirements, success criteria

Skill spec-kit-workflow activates:
- Provides spec template structure
- Suggests requirement categories (FR-NNN format)
- Validates completeness against constitution
- Examples of well-written user stories

Result: Complete spec.md following spec-kit methodology

---

# Step 2: Create Implementation Plan
User: /spec:plan

Command /spec:plan:
- Creates specs/NNN-sales-dashboard/plan.md
- Prompts for technical approach, architecture

Skills activate:
- spec-kit-workflow: Plan template and structure
- claude-code-architecture: Decides if Custom components or standard
- plotly-viz: Recommends chart types based on requirements
- data-analysis: Suggests data pipeline approach

Result: Comprehensive plan.md with justified decisions

---

# Step 3: Generate Task Breakdown
User: /spec:tasks

Command /spec:tasks:
- Creates specs/NNN-sales-dashboard/tasks.md
- Breaks plan into actionable tasks

Skill spec-kit-workflow activates:
- Task breakdown methodology
- Dependency analysis
- Success criteria per task
- File structure planning

Result: Actionable tasks.md with clear dependencies

---

# Step 4: Review & Approve
User: /spec:review

Command /spec:review:
- Runs approval checklist
- Validates completeness

Skill spec-kit-workflow activates:
- Constitutional alignment check
- Completeness validation
- Quality standards check

Result: Spec approved, tasks.md frozen

[HANDOFF TO PROCESS 2]
```

**Key Point**: Development Skills guide the planning process, ensuring high-quality specs.

---

### Skills in Process 2: Claude Code Execution

**Commands**: `/workflow:*`

**Skills Active**:
- `data-analysis` (production)
- `plotly-viz` (production)
- `dash-components` (production)
- `accessibility-audit` (production)
- `performance-optimizer` (production)

**Example Flow**:

```bash
# Task 1: Create data loader
User: /workflow:implement Task 1

Command /workflow:implement:
- Reads Task 1 from tasks.md
- Sets up TDD workflow
- Creates test and implementation files

Skills activate:
- data-analysis: Data loading patterns (CSV, SQL)
- research-synthesis: Examines existing loaders in codebase

Result:
- tests/unit/test_sales_loader.py
- src/data/sales_loader.py

---

# Verify Task 1
User: /workflow:verify

Command /workflow:verify:
- Runs pytest
- Runs linting (ruff, black, mypy)
- Checks coverage

Skills activate:
- data-analysis: Validates data handling patterns

Result: Tests pass, 87% coverage ✓

---

# Task 2: Create bar chart component
User: /workflow:implement Task 2

Command /workflow:implement:
- Reads Task 2 from tasks.md
- TDD workflow

Skills activate:
- plotly-viz: Chart creation, accessibility
- dash-components: Component structure, callbacks
- data-analysis: Data transformation for visualization

Result:
- tests/unit/test_sales_chart.py
- src/components/sales_chart.py (accessible, WCAG compliant)

---

# Verify Task 2
User: /workflow:verify

Command /workflow:verify:
- Runs pytest
- Runs linting
- Accessibility check

Skills activate:
- accessibility-audit: WCAG 2.1 AA compliance check
- performance-optimizer: Rendering performance check

Result:
- Tests pass ✓
- Coverage: 84% ✓
- WCAG compliant ✓
- Render time: 0.3s ✓

---

# Continue through all tasks...
User: /workflow:next

[Process repeats for remaining tasks]
```

**Key Point**: Production Skills provide domain expertise during implementation, ensuring quality.

---

### Skills Across Both Processes

**Same Infrastructure, Different Content**:

| Process | Commands | Development Skills | Production Skills |
|---------|----------|-------------------|-------------------|
| **Spec-Kit** | `/spec:*` | ✓ Active | ○ Referenced in planning |
| **Claude Code** | `/workflow:*` | ○ Not needed | ✓ Active |

**Example of Cross-Process Benefit**:

```
Planning (Spec-Kit):
- plotly-viz Skill consulted for chart recommendations in plan.md
- Level 1 + 2 loaded to suggest chart types
- Recommendations documented in plan

Execution (Claude Code):
- Same plotly-viz Skill activates during implementation
- Level 2 already understood from planning
- Provides consistent guidance

Result: Planning and execution use same expertise source
```

---

### Handoff Point: tasks.md

**After Approval**:
- tasks.md is frozen (no scope changes)
- Minor edits allowed (typos, clarifications)
- Skills continue to enhance execution

**During Execution**:
- Skills provide "how" for each task's "what"
- Commands structure the workflow
- Agentic corrections within task scope (max 3 verify attempts)

**Feedback Loop** (rare):
- If task technically impossible → Escalate
- Return to Spec-Kit process
- Update spec, regenerate tasks
- Skills help with revision

---

### Summary: Skills' Role in Hybrid Workflow

**In Planning**:
- Development Skills guide spec creation
- Production Skills inform technical decisions
- Result: High-quality, implementable plans

**In Execution**:
- Production Skills provide domain expertise
- Development Skills dormant (not needed)
- Result: High-quality, accessible, performant code

**Throughout**:
- Progressive disclosure keeps context lean
- Auto-activation means seamless integration
- Same Skills benefit multiple phases

**The Benefit**: Comprehensive expertise available exactly when and where needed, across both processes.

---

## Summary of Q6-Q10

**Q6**: Skills vs Commands - Complementary (knowledge vs structure)
**Q7**: Skills vs Sub-Agents - Different patterns (shared vs isolated context)
**Q8**: Progressive disclosure - Three-level loading for efficiency
**Q9**: What Skills to create - Development + Production based on domain
**Q10**: Skills in hybrid workflow - Enhance both planning and execution

**Together**: Complete understanding of how Agent Skills integrate into spec-driven dashboard development.

**Next**: Implementation Phases detail the 8-week plan to build this system, including all Skills.

---

## Dependencies

### Prerequisites
- Claude Code installed and configured
- Python 3.11+ with pip
- Git repository initialized with spec-kit structure
- `.specify/` directory with constitution and templates

### Internal Dependencies
- `.specify/memory/constitution.md` must exist (project principles)
- `.specify/templates/` must contain spec, plan, tasks templates
- Project must follow directory structure from 001-dashboard-foundation

### External Dependencies
- Plotly Dash framework
- pytest, pytest-cov for testing
- Black, Ruff, mypy for code quality
- Git for version control



### Research Dependencies
- specs/research/agent-skills-integration-analysis.md (29KB)
- specs/research/claude-code-final-architecture.md (12KB)
- specs/research/complete-architecture-quick-reference.md (19KB)
- specs/research/spec-revision-notes.md

### Architecture Dependencies
- specs/WORKFLOW.md - Two-process workflow architecture
- specs/INDEX.md - Spec numbering and implementation order

### Template Dependencies
- specs/templates/spec-template.md
- specs/templates/plan-template.md
- specs/templates/tasks-template.md

---

**Total Duration**: 8 weeks
**Approach**: Iterative development with continuous testing
**Note**: NO time estimates in spec per constitutional requirement; phases for organization only

---

## Phase 1: Core Architecture Setup

**Focus**: Foundation and directory structure

**Deliverables**:
- `.claude/` directory structure created
- `settings.json` configuration with permissions and hooks
- Documentation framework (README, initial guides)
- Git branch: `002-claude-code-commands-setup`

**Tasks**:
1. Create `.claude/` directory with subdirectories:
   ```
   .claude/
   ├── commands/
   │   ├── spec/
   │   ├── workflow/
   │   └── utils/
   ├── skills/
   │   ├── development/
   │   └── production/
   ├── agents/
   └── settings.json
   ```

2. Configure settings.json:
   ```json
   {
     "workflow": {
       "max_verify_attempts": 3,
       "allow_minor_task_edits": true,
       "escalation_timeout_hours": 4
     },
     "permissions": {
       "allow": ["Read(*)", "Write(*)", "Edit(*)", "Bash(git:*)"],
       "deny": ["Bash(rm -rf:*)", "Bash(sudo:*)"]
     }
   }
   ```

3. Create `.claude/README.md` documenting structure

4. Set up test infrastructure for validating commands and skills

**Validation**:
- [ ] Directory structure exists
- [ ] settings.json parses correctly
- [ ] README documents all directories
- [ ] Git branch created

**Dependencies**: None (foundation phase)

---

## Phase 2: Specification Commands

**Focus**: Implement `/spec:*` commands for planning workflow

**Deliverables**:
- 5 specification commands fully functional
- Commands support namespaced syntax (`/spec:action`)
- Integration with specs/ directory

**Commands to Implement**:

### 1. `/spec:specify`
**Purpose**: Create new feature specification

**Implementation**:
```markdown
---
description: Create new feature specification following spec-kit methodology
allowed-tools: [Read, Write, Edit, Bash(git:*)]
argument-hint: [feature description]
---

# Specify Command

Read specs/templates/spec-template.md
Generate unique feature number
Create specs/NNN-feature-name/spec.md
Populate with template
Guide user through sections
```

### 2. `/spec:plan`
**Purpose**: Create technical implementation plan

**Implementation**: Similar structure, creates plan.md from template

### 3. `/spec:tasks`
**Purpose**: Generate actionable task breakdown

**Implementation**: Parse plan.md, create task list with dependencies

### 4. `/spec:validate`
**Purpose**: Check spec completeness

**Implementation**: Validate all required sections present, reference constitution

### 5. `/spec:review`
**Purpose**: Run approval checklist

**Implementation**: Systematic review of spec, plan, tasks against checklist

**Validation**:
- [ ] All 5 commands execute successfully
- [ ] Commands create correct file structure
- [ ] Commands follow namespaced pattern
- [ ] Integration with specs/ directory works
- [ ] Commands pass unit tests

**Dependencies**: Phase 1 (directory structure)

---

## Phase 3: Development Skills

**Focus**: Create Skills for building the system

**Deliverables**:
- 3 Development Skills fully implemented
- Progressive disclosure working correctly
- Skills activate appropriately during `/spec:*` commands

**Skills to Implement**:

### 1. spec-kit-workflow Skill

**Directory Structure**:
```
.claude/skills/development/spec-kit-workflow/
├── SKILL.md                    # Levels 1 & 2
├── SPEC_TEMPLATE.md            # Level 3
├── PLAN_TEMPLATE.md            # Level 3
├── TASKS_TEMPLATE.md           # Level 3
├── CONSTITUTION_GUIDE.md       # Level 3
├── examples/
│   ├── example-spec.md
│   ├── example-plan.md
│   └── example-tasks.md
└── validation/
    └── checklist.md
```

**SKILL.md Content** (~800 tokens):
- Constitution → Specify → Plan → Tasks workflow
- Spec template structure
- Validation guidelines

**Activation**: Working with spec.md, plan.md, tasks.md files

### 2. claude-code-architecture Skill

**Directory Structure**:
```
.claude/skills/development/claude-code-architecture/
├── SKILL.md
├── COMMANDS_GUIDE.md
├── SUBAGENTS_GUIDE.md
├── SKILLS_GUIDE.md
├── HOOKS_GUIDE.md
├── DECISION_MATRIX.md
├── reference/
│   ├── claude-code-final-architecture.md
│   └── complete-architecture-quick-reference.md
└── examples/
```

**SKILL.md Content** (~800 tokens):
- Commands vs Skills vs Sub-Agents decision matrix
- When to use each mechanism
- Configuration patterns

**Activation**: Working with .claude/ directory

### 3. research-synthesis Skill

**Directory Structure**:
```
.claude/skills/development/research-synthesis/
├── SKILL.md
├── ANALYSIS_METHODS.md
├── PATTERN_EXTRACTION.md
├── DOCUMENTATION_GUIDE.md
└── templates/
```

**SKILL.md Content** (~800 tokens):
- Research process (discovery, analysis, synthesis)
- Pattern extraction techniques
- Documentation creation

**Activation**: Research tasks, analyzing reference materials

**Validation**:
- [ ] All 3 Development Skills created
- [ ] SKILL.md files follow format (YAML frontmatter + content)
- [ ] Token budgets met (Level 1: ~50, Level 2: ~800)
- [ ] Skills activate correctly during `/spec:*` commands
- [ ] Progressive disclosure works (Level 3 loads on-demand)
- [ ] Integration tests pass

**Dependencies**: Phase 2 (commands to enhance)

---

## Phase 4: Workflow Commands

**Focus**: Implement `/workflow:*` commands for execution

**Deliverables**:
- 5 workflow commands fully functional
- Integration with hybrid workflow architecture
- Agentic correction loops working (max 3 attempts)

**Commands to Implement**:

### 1. `/workflow:research`
**Purpose**: Understand current task, examine codebase

**Implementation**:
- Read current task from tasks.md
- Analyze relevant code files
- Load appropriate Skills
- Identify approach

### 2. `/workflow:implement`
**Purpose**: Write tests and implementation (TDD)

**Implementation**:
- Create test file first
- Write failing tests
- Implement to pass tests
- Follow TDD cycle

### 3. `/workflow:verify`
**Purpose**: Run tests, linting, validation (max 3 attempts)

**Implementation**:
- Run pytest with coverage
- Run Black, Ruff, mypy
- Check against task success criteria
- Allow up to 3 correction attempts
- Escalate after 3 failures

### 4. `/workflow:next`
**Purpose**: Mark task complete, move to next

**Implementation**:
- Mark current task complete in tracking
- Show progress against tasks.md
- Present next task
- Offer to start next task

### 5. `/workflow:status`
**Purpose**: Show progress against tasks.md

**Implementation**:
- Parse tasks.md
- Show completed vs remaining tasks
- Display success criteria met
- Estimate remaining work

**Validation**:
- [ ] All 5 commands execute successfully
- [ ] TDD workflow enforced
- [ ] Verify command has 3-attempt limit
- [ ] Escalation works correctly
- [ ] Integration with tasks.md works
- [ ] Commands pass unit tests

**Dependencies**: Phase 1 (structure), Phase 2 (tasks.md exists)

---

## Phase 5: Production Skills - Core

**Focus**: Essential Skills for dashboard development

**Deliverables**:
- 3 core Production Skills implemented
- Skills activate during `/workflow:*` commands
- Integration with workflow tested

**Skills to Implement**:

### 1. data-analysis Skill

**Directory Structure**:
```
.claude/skills/production/data-analysis/
├── SKILL.md
├── STATISTICAL_METHODS.md          # ~2000 tokens
├── DATA_QUALITY.md                 # ~1500 tokens
├── VISUALIZATION_GUIDE.md          # ~1800 tokens
├── scripts/
│   ├── analyze.py
│   ├── quality_check.py
│   └── transform.py
└── examples/
    └── eda-example.py
```

**SKILL.md Content** (~800 tokens):
- Data loading (CSV, JSON, Parquet, SQL)
- EDA process
- Data quality checks
- Visualization recommendations

**Activation**: Data loading, analysis, "data", "statistics", "EDA"

**Allowed Tools**: Read, Bash, mcp__postgres, mcp__filesystem

### 2. plotly-viz Skill

**Directory Structure**:
```
.claude/skills/production/plotly-viz/
├── SKILL.md
├── CHART_TYPES.md                  # ~2500 tokens
├── ACCESSIBILITY.md                # ~1800 tokens
├── THEMING.md                      # ~1200 tokens
├── INTERACTIVITY.md                # ~1500 tokens
├── templates/
│   ├── bar_chart.py
│   ├── line_chart.py
│   ├── scatter_plot.py
│   ├── heatmap.py
│   └── [others]
└── examples/
    └── accessible-dashboard.py
```

**SKILL.md Content** (~800 tokens):
- Chart selection guide
- Chart creation patterns
- Accessibility requirements (WCAG 2.1 AA)
- Plotly Express vs Graph Objects

**Activation**: "chart", "visualization", "plot", Plotly code

**Allowed Tools**: Read, Write, Edit

### 3. dash-components Skill

**Directory Structure**:
```
.claude/skills/production/dash-components/
├── SKILL.md
├── COMPONENT_PATTERNS.md           # ~2000 tokens
├── CALLBACK_ARCHITECTURE.MD        # ~2200 tokens
├── LAYOUT_GUIDE.md                 # ~1500 tokens
├── STATE_MANAGEMENT.md             # ~1800 tokens
├── templates/
│   ├── basic_component.py
│   ├── filter_component.py
│   └── chart_component.py
└── examples/
    └── complete_dashboard.py
```

**SKILL.md Content** (~800 tokens):
- Component creation patterns
- Callback architecture
- Layout patterns
- State management

**Activation**: "component", "callback", "layout", Dash code

**Allowed Tools**: Read, Write, Edit

**Validation**:
- [ ] All 3 core Production Skills created
- [ ] Skills follow format and token budgets
- [ ] Skills activate during `/workflow:implement`
- [ ] Integration with workflow commands works
- [ ] Skills provide correct domain expertise
- [ ] Test dashboards created use Skills effectively

**Dependencies**: Phase 4 (workflow commands to enhance)

---

## Phase 6: Production Skills - Extended

**Focus**: Quality and performance Skills

**Deliverables**:
- 2 extended Production Skills implemented
- WCAG 2.1 AA compliance automation
- Performance optimization guidance

**Skills to Implement**:

### 1. accessibility-audit Skill

**Directory Structure**:
```
.claude/skills/production/accessibility-audit/
├── SKILL.md
├── WCAG_CHECKLIST.md               # ~2500 tokens
├── COLOR_CONTRAST.md               # ~1200 tokens
├── KEYBOARD_NAV.md                 # ~1500 tokens
├── SCREEN_READERS.md               # ~1800 tokens
├── scripts/
│   ├── check_contrast.py
│   ├── check_aria.py
│   └── generate_report.py
└── examples/
    └── accessible_patterns.py
```

**SKILL.md Content** (~800 tokens):
- WCAG 2.1 Level AA requirements
- Audit process
- Common issues and fixes

**Activation**: "accessibility", "WCAG", "a11y", during `/workflow:verify`

**Allowed Tools**: Read, Bash

### 2. performance-optimizer Skill

**Directory Structure**:
```
.claude/skills/production/performance-optimizer/
├── SKILL.md
├── BOTTLENECK_PATTERNS.md          # ~2000 tokens
├── OPTIMIZATION_STRATEGIES.md      # ~2200 tokens
├── CACHING_GUIDE.md                # ~1500 tokens
├── PROFILING.md                    # ~1200 tokens
├── scripts/
│   ├── profile_callbacks.py
│   ├── analyze_bundle.py
│   └── benchmark.py
└── examples/
    └── optimized_dashboard.py
```

**SKILL.md Content** (~800 tokens):
- Common bottlenecks
- Optimization strategies
- Performance targets (<3s load, <1s callbacks)

**Activation**: "slow", "performance", "optimize", performance issues

**Allowed Tools**: Read, Edit, Bash

**Validation**:
- [ ] Both extended Production Skills created
- [ ] accessibility-audit detects WCAG violations
- [ ] performance-optimizer identifies bottlenecks
- [ ] Skills integrate with `/workflow:verify`
- [ ] Automated checks work correctly
- [ ] Test cases pass

**Dependencies**: Phase 5 (core Production Skills)

---

## Phase 7: Utility Commands & Sub-Agents

**Focus**: Utilities and parallel execution

**Deliverables**:
- 4 utility commands implemented
- 3 Sub-Agents created
- Parallel execution working

**Utility Commands**:

### 1. `/utils:test`
**Purpose**: Run pytest with coverage

### 2. `/utils:lint`
**Purpose**: Run Black, Ruff, mypy

### 3. `/utils:format`
**Purpose**: Auto-format code

### 4. `/utils:diff`
**Purpose**: Show changes since branch creation

**Sub-Agents**:

### 1. component-builder
**Purpose**: Create reusable Dash components
**Tools**: Read, Write, Edit
**Skills Available**: dash-components, plotly-viz, accessibility-audit

### 2. data-pipeline
**Purpose**: Build data loaders and transformers
**Tools**: Read, Write, Edit, Bash, mcp__postgres
**Skills Available**: data-analysis

### 3. test-engineer
**Purpose**: Write comprehensive test suites
**Tools**: Read, Write, Edit, Bash
**Skills Available**: All (for testing any component)

**Validation**:
- [ ] All 4 utility commands work
- [ ] All 3 Sub-Agents launch successfully
- [ ] Sub-Agents complete tasks autonomously
- [ ] Skills available within Sub-Agent context
- [ ] Parallel execution works without conflicts
- [ ] Coordination (file locking) works

**Dependencies**: Phases 2-6 (all commands and skills)

---

## Phase 8: Integration & Documentation

**Focus**: End-to-end testing and comprehensive documentation

**Deliverables**:
- Complete integration testing
- CLAUDE.md (project instructions for repo root)
- User documentation and examples
- Video walkthrough (optional)

**Tasks**:

### 1. End-to-End Testing
- Create test feature using complete workflow
- `/spec:specify` → spec created with Development Skills
- `/spec:plan` → plan created with Skills guidance
- `/spec:tasks` → tasks generated
- Approve spec
- `/workflow:implement` → execute tasks with Production Skills
- `/workflow:verify` → validation with Skills
- Complete full cycle

### 2. Create CLAUDE.md
**Location**: Project root (`/home/user/cc-dash-as-code/CLAUDE.md`)

**Content**:
- Overview of the setup
- Quick start guide
- Command reference (all `/spec:*`, `/workflow:*`, `/utils:*`)
- Skills overview (all 8 skills)
- Sub-Agents overview
- Example workflows
- Troubleshooting

### 3. Documentation Updates
- Update specs/README.md with references to new setup
- Create command documentation (`.claude/commands/README.md`)
- Create skills documentation (`.claude/skills/README.md`)
- Document Sub-Agents (`.claude/agents/README.md`)

### 4. Example Workflows
- Create `examples/` directory with:
  - `01-create-spec.md` - Walkthrough of spec creation
  - `02-implement-feature.md` - Complete implementation example
  - `03-using-skills.md` - How Skills activate automatically
  - `04-parallel-work.md` - Sub-Agents example

### 5. User Acceptance Testing
- Have team members try the setup
- Collect feedback on:
  - Command clarity
  - Skills activation
  - Documentation completeness
- Iterate based on feedback

**Validation**:
- [ ] End-to-end test completes successfully
- [ ] CLAUDE.md created and comprehensive
- [ ] All documentation updated
- [ ] Example workflows tested
- [ ] User feedback incorporated
- [ ] System ready for production use

**Dependencies**: Phase 7 (all components exist)

---

## Phase Summary

| Phase | Focus | Key Deliverables | Dependencies |
|-------|-------|------------------|--------------|
| **1** | Foundation | Directory structure, settings | None |
| **2** | Spec Commands | 5 `/spec:*` commands | Phase 1 |
| **3** | Dev Skills | 3 Development Skills | Phase 2 |
| **4** | Workflow Commands | 5 `/workflow:*` commands | Phases 1-2 |
| **5** | Core Production Skills | 3 core Skills | Phase 4 |
| **6** | Extended Production Skills | 2 quality/performance Skills | Phase 5 |
| **7** | Utilities & Sub-Agents | 4 commands, 3 Sub-Agents | Phases 2-6 |
| **8** | Integration & Docs | Testing, CLAUDE.md, examples | Phase 7 |

---

## Critical Path

**Must Complete in Order**:
1. Phase 1 (foundation for everything)
2. Phase 2 (spec commands needed for workflow)
3. Phase 4 (workflow commands needed for Skills testing)

**Can Parallelize**:
- Phase 3 (Dev Skills) can overlap with Phase 4 (Workflow Commands)
- Phase 5 (Core Skills) and Phase 6 (Extended Skills) can overlap
- Documentation can be written throughout

**Blocking Dependencies**:
- Phase 8 requires ALL previous phases complete
- Cannot test integration without all components

---

## Success Criteria for Phase Completion

Each phase complete when:
- [ ] All deliverables created
- [ ] Unit tests pass
- [ ] Integration tests pass (where applicable)
- [ ] Documentation updated
- [ ] Git commit created with descriptive message
- [ ] Review completed (manual or automated)

**Overall Project Complete When**:
- [ ] All 8 phases validated
- [ ] End-to-end workflow works
- [ ] User acceptance testing passed
- [ ] Documentation comprehensive
- [ ] Ready for team use

---

## Risk Mitigation

**Risk**: Skills don't activate as expected
**Mitigation**: Test activation with various contexts in Phase 3, iterate on descriptions

**Risk**: Token budgets exceeded
**Mitigation**: Automated checking in CI/CD, content review during phases

**Risk**: Integration issues between components
**Mitigation**: Incremental integration testing throughout, Phase 8 comprehensive testing

**Risk**: User confusion about when to use what
**Mitigation**: Clear documentation, decision matrices, examples in Phase 8

---

## Post-Implementation

**After Phase 8**:
1. Deploy to team (all members have access via git)
2. Monitor usage and collect feedback
3. Iterate on Skills content based on real usage
4. Create additional Skills as needed (domain-specific)
5. Expand to additional frameworks beyond Dash (future)

**Maintenance**:
- Skills content updates as Dash/Plotly evolve
- Command improvements based on feedback
- Additional Sub-Agents as patterns emerge
- Continuous documentation updates

---

**Ready to Begin**: This 8-phase plan provides complete roadmap for implementing the hybrid workflow architecture with full Agent Skills integration.

**Next Step**: Start Phase 1 - Core Architecture Setup

---

## Review & Acceptance Checklist

### Completeness
- [ ] All 6 user stories are prioritized and independently testable
- [ ] All 60 functional requirements have unique identifiers
- [ ] All 30 success criteria are measurable
- [ ] Edge cases are documented with resolution strategies
- [ ] Key entities are identified with attributes and relationships
- [ ] All clarifications address potential ambiguities

### Clarity
- [ ] User stories clearly describe who, what, and why
- [ ] Requirements are unambiguous and verifiable
- [ ] EPIC methodology is clearly explained
- [ ] Command categories and purposes are well-defined
- [ ] Technical terms are used consistently

### Testability
- [ ] Each user story includes concrete acceptance scenarios
- [ ] Success criteria can be measured objectively
- [ ] Test scenarios cover normal flows and edge cases
- [ ] Requirements can be verified through automated testing
- [ ] Performance targets are specific and measurable

### Alignment with Constitution
- [ ] Specification follows spec-kit template structure
- [ ] Spec-first workflow is enforced throughout
- [ ] Code quality standards (80% coverage, Black, Ruff, mypy) are maintained
- [ ] Security requirements are addressed
- [ ] Accessibility (WCAG 2.1 AA) is included

### Feasibility
- [ ] Requirements are technically achievable with Claude Code
- [ ] Command structure aligns with Claude Code's .md + YAML format
- [ ] Sub-agent coordination is practical and tested
- [ ] Timeline is realistic (6 weeks for full implementation)
- [ ] No blocking external dependencies

### Stakeholder Alignment
- [ ] Command categories match user's requested structure (spec, workflow, utils, dash)
- [ ] EPIC methodology is properly integrated into workflow commands
- [ ] No generic "humanlayer" approach - all tailored to Dash development
- [ ] Spec-first approach is enforced
- [ ] Implementation removed pending spec approval

---



### Skills Integration
- [ ] Agent Skills architecture is comprehensive and clear
- [ ] Progressive disclosure pattern is explained in extreme detail
- [ ] All 8 Skills have complete directory structures defined
- [ ] Development Skills (3) and Production Skills (5) are distinguished
- [ ] Skills integration with Commands is well-documented
- [ ] Skills vs MCP relationship is clarified
- [ ] Token budgets are specified for all loading levels
- [ ] Activation triggers are documented for each Skill
- [ ] Skills functional requirements (FR-061 to FR-090) are complete
- [ ] Skills success criteria (SC-031 to SC-045) are measurable

### Hybrid Workflow Architecture
- [ ] Two-process model (Spec-Kit + Claude Code) is clearly explained
- [ ] Handoff mechanism via tasks.md is documented
- [ ] Agentic correction loops (max 3 attempts) are specified
- [ ] Escalation thresholds and governance are defined
- [ ] Workflow architecture references specs/WORKFLOW.md
- [ ] Namespaced commands (/spec:*, /workflow:*, /utils:*) are used consistently

---

**Next Steps**:
1. **Review this specification** - Validate hybrid workflow, Agent Skills integration, and all requirements
2. **Approve specification** - Mark as "approved" when ready to proceed (user review required)
3. **Create implementation branch** - Branch: `002-claude-code-commands-setup`
4. **Begin Phase 1** - Core architecture setup (directory structure, settings.json)
5. **Iterate through 8 phases** - Complete all phases with continuous testing and validation
6. **Deploy to team** - Team members access via git pull

---

**Status**: Draft - Awaiting Review (Requires user approval before implementation)

**Major Revisions**:
- Added complete Agent Skills architecture (~4000 tokens of detailed documentation)
- Integrated hybrid workflow (Spec-Kit planning + Claude Code execution)
- Added 30 Skills functional requirements (FR-061 to FR-090)
- Added 15 Skills success criteria (SC-031 to SC-045)
- Added 5 clarifications for Skills and workflow (Q6-Q10)
- Revised implementation to 8 phases including Skills development
- Updated command naming to namespaced format (/spec:*, /workflow:*, /utils:*)

**Key Changes from Previous Version**:
- REMOVED: "EPIC" methodology term (replaced with "hybrid workflow")
- REMOVED: `/dash.*` separate command category (integrated into `/workflow:*`)
- ADDED: Complete Agent Skills system (8 skills with progressive disclosure)
- ADDED: Two-process model with clear handoff mechanism
- ADDED: Agentic correction loops with 3-attempt limit

**Review Focus Areas**:
1. Is the Agent Skills architecture clear and comprehensive enough?
2. Are all 8 Skills properly defined with directory structures?
3. Is the hybrid workflow architecture well-explained?
4. Are the 30 new functional requirements complete and testable?
5. Are the 15 new success criteria measurable?
6. Is the 8-phase implementation plan realistic and well-ordered?

---

**Version**: 2.0.0 (Major revision with Agent Skills integration)
**Last Updated**: 2025-11-10
**Specification File**: specs/002-claude-code-commands-setup/spec.md
