# Claude Code Setup for Dashboard Development

This file documents the custom Claude Code configuration for spec-driven dashboard development with Plotly Dash.

## Overview

This project uses Claude Code with custom slash commands, agent skills, and specialized sub-agents to accelerate dashboard development following the spec-kit methodology.

**Key Capabilities:**
- Custom slash commands for spec-driven workflow
- Specialized agent skills for domain tasks
- Sub-agents for parallel development
- MCP integration for data access
- Agent memory for context persistence
- Seamless Agent SDK deployment

## Quick Start

### 1. Initialize a Feature

```bash
/dashboard.spec Create a sales analytics dashboard with date filtering
```

### 2. Create Implementation Plan

```bash
/dashboard.plan Use Plotly Dash with Pandas. PostgreSQL database. Docker deployment.
```

### 3. Generate Tasks

```bash
/dashboard.tasks
```

### 4. Implement

```bash
/dashboard.implement
```

### 5. Test & Deploy

```bash
/dashboard.test
/dashboard.deploy
```

## Custom Slash Commands

All commands follow the `/dashboard.<action>` pattern.

### Core Workflow Commands

#### `/dashboard.spec [description]`

Create a new feature specification following spec-kit methodology.

**Usage:**
```
/dashboard.spec Build a customer analytics dashboard with filters for region and date range
```

**What it does:**
- Generates unique feature number
- Creates specification directory
- Populates spec template
- Creates git branch
- Reviews constitution for alignment

**Output:**
- `.specify/specs/{number}-{name}/spec.md`
- Git branch: `{number}-{name}`

**Next step:** `/dashboard.plan`

---

#### `/dashboard.plan [tech details]`

Create technical implementation plan with architecture and tech stack.

**Usage:**
```
/dashboard.plan Dash 2.14+ with Pandas for data. FastAPI backend. PostgreSQL database. Docker Compose.
```

**What it does:**
- Reviews specification
- Defines technology stack
- Creates architecture design
- Specifies components and APIs
- Plans testing strategy
- Researches latest versions

**Output:**
- `.specify/specs/{feature}/plan.md`
- `.specify/specs/{feature}/research.md` (optional)
- `.specify/specs/{feature}/data-model.md` (optional)

**Next step:** `/dashboard.tasks`

---

#### `/dashboard.tasks`

Generate detailed task breakdown from implementation plan.

**Usage:**
```
/dashboard.tasks
```

**What it does:**
- Parses implementation plan
- Breaks down into granular tasks
- Identifies dependencies
- Marks parallel tasks [P]
- Orders for optimal execution

**Output:**
- `.specify/specs/{feature}/tasks.md`

**Next step:** `/dashboard.implement`

---

#### `/dashboard.implement`

Execute implementation tasks following TDD and quality gates.

**Usage:**
```
/dashboard.implement
```

**What it does:**
- Loads spec, plan, and tasks
- Executes tasks in order
- Writes code and tests (TDD)
- Runs quality checks
- Creates git commits
- Validates checkpoints

**Output:**
- Source code in `src/`
- Tests in `tests/`
- Git commits at milestones
- Coverage reports

**Next step:** `/dashboard.test` or `/dashboard.review`

---

### Quality & Analysis Commands

#### `/dashboard.analyze`

Perform cross-artifact consistency analysis.

**Usage:**
```
/dashboard.analyze
```

**What it does:**
- Checks spec-code alignment
- Validates requirement coverage
- Identifies gaps and inconsistencies
- Verifies success criteria

**Output:**
- Analysis report
- Gap identification
- Recommendations

---

#### `/dashboard.test`

Run comprehensive test suite with coverage reporting.

**Usage:**
```
/dashboard.test
```

**What it does:**
- Runs unit, integration, e2e tests
- Generates coverage report
- Checks accessibility
- Validates performance

**Output:**
- Test results
- Coverage report (HTML)
- Performance metrics
- Accessibility report

---

#### `/dashboard.review`

Perform automated code quality review.

**Usage:**
```
/dashboard.review
```

**What it does:**
- Runs Black formatter
- Runs Ruff linter
- Runs mypy type checker
- Checks security (Bandit)
- Reviews code patterns

**Output:**
- Quality report
- Issues identified
- Auto-fixes applied
- Recommendations

---

### Deployment Commands

#### `/dashboard.deploy`

Configure Claude Agent SDK deployment.

**Usage:**
```
/dashboard.deploy
```

**What it does:**
- Generates Agent SDK configs
- Creates deployment manifests
- Configures environments
- Sets up health checks
- Prepares for production

**Output:**
- `agents/` directory with configs
- Docker files
- Deployment scripts
- Environment templates

---

## Agent Skills

Skills are specialized capabilities invoked automatically by Claude Code.

### data-analysis

**Purpose:** Load, analyze, and generate insights from datasets

**Capabilities:**
- Load CSV, JSON, Parquet, SQL data
- Exploratory data analysis (EDA)
- Statistical summaries
- Data quality assessment
- Visualization recommendations
- Transformation pipeline generation

**Invoked by:** `/dashboard.plan`, `/dashboard.implement`, data-pipeline sub-agent

**Configuration:** `.claude/skills/data-analysis.yaml`

---

### plotly-viz

**Purpose:** Generate appropriate Plotly visualizations

**Capabilities:**
- Auto-select chart types
- Generate Dash components
- Apply consistent theming
- Ensure accessibility (WCAG 2.1 AA)
- Optimize performance
- Add interactivity

**Chart types:** bar, line, scatter, histogram, box, heatmap, pie, area, funnel, sunburst

**Invoked by:** `/dashboard.implement`, component-builder sub-agent

**Configuration:** `.claude/skills/plotly-viz.yaml`

---

### dashboard-testing

**Purpose:** Generate comprehensive test suites

**Capabilities:**
- Unit test generation
- Integration test creation
- E2E test workflows
- Fixture management
- Mock data creation
- Coverage optimization

**Invoked by:** `/dashboard.implement`, test-engineer sub-agent

**Configuration:** `.claude/skills/dashboard-testing.yaml`

---

### accessibility-audit

**Purpose:** Validate WCAG compliance

**Capabilities:**
- Color contrast checking
- Keyboard navigation testing
- Screen reader compatibility
- Alt text validation
- ARIA label verification

**Standards:** WCAG 2.1 Level AA

**Invoked by:** `/dashboard.test`, `/dashboard.review`

**Configuration:** `.claude/skills/accessibility-audit.yaml`

---

### performance-optimizer

**Purpose:** Identify and fix performance issues

**Capabilities:**
- Bottleneck detection
- Callback optimization
- Data loading efficiency
- Rendering performance
- Caching strategies
- Resource usage analysis

**Targets:** < 3s load, < 1s callbacks

**Invoked by:** `/dashboard.review`, `/dashboard.implement`

**Configuration:** `.claude/skills/performance-optimizer.yaml`

---

### component-builder

**Purpose:** Create reusable Dash components

**Capabilities:**
- Component scaffolding
- Props definition
- Type hints
- Documentation
- Unit tests
- Storybook examples

**Invoked by:** component-builder sub-agent

**Configuration:** `.claude/skills/component-builder.yaml`

---

## Sub-Agents

Specialized agents for parallel work on different aspects.

### component-builder

**Specialization:** Autonomous UI component creation

**Responsibilities:**
- Build reusable Dash components
- Write component tests
- Generate component documentation
- Apply theming and styling

**Coordination:** File locking for component files

---

### data-pipeline

**Specialization:** Data infrastructure development

**Responsibilities:**
- Create data loaders
- Build transformation pipelines
- Write validators
- Optimize queries
- Set up caching

**Coordination:** Queue-based for database operations

---

### test-engineer

**Specialization:** Comprehensive testing infrastructure

**Responsibilities:**
- Write unit tests
- Create integration tests
- Build e2e test workflows
- Set up fixtures
- Configure CI/CD

**Coordination:** Independent (test files separate)

---

### documentation

**Specialization:** Documentation generation

**Responsibilities:**
- API documentation
- Component docs
- User guides
- Architecture diagrams
- README updates

**Coordination:** Independent (docs separate from code)

---

## MCP Integration

Model Context Protocol servers for data access.

### Configuration

File: `.claude/mcp_config.json`

### Available MCP Servers

#### filesystem
- **Purpose:** Access CSV, JSON, Parquet files
- **Path:** `./data`
- **Command:** `mcp-server-filesystem`

#### postgres
- **Purpose:** PostgreSQL database access
- **Connection:** `${POSTGRES_URL}` environment variable
- **Command:** `mcp-server-postgres`
- **Status:** Disabled by default

#### sqlite
- **Purpose:** Local SQLite database
- **Path:** `./data/local.db`
- **Command:** `mcp-server-sqlite`

#### fetch
- **Purpose:** REST API access
- **Command:** `mcp-server-fetch`

#### search
- **Purpose:** Search reference documentation
- **Path:** `./reference`
- **Command:** `mcp-server-search`

### Enabling MCP Servers

Edit `.claude/mcp_config.json` and set:
```json
{
  "mcpServers": {
    "postgres": {
      "enabled": true
    }
  }
}
```

---

## Agent Memory

Persistent context across sessions stored in `.specify/memory/`.

### Memory Files

#### constitution.md
Project principles and development guidelines (already exists)

#### patterns.md
Coding patterns and conventions learned during development

#### decisions.md
Architectural decisions with rationale and date

#### preferences.md
Developer preferences, naming conventions, anti-patterns to avoid

### Memory Management

- **Auto-save:** Every 10 minutes
- **Max size:** 10 MB
- **Format:** Markdown
- **Editable:** Yes, manually edit any file

---

## Configuration Files

### .claude/agent_config.yaml

Main agent configuration file.

**Key settings:**
- Code quality: 80% coverage, Black, Ruff, mypy
- Testing: pytest, pytest-cov, Playwright
- Sub-agents: Max 4 concurrent
- Performance: Parallel execution enabled
- Security: Secret scanning enabled

### .claude/mcp_config.json

MCP server configuration.

**Key settings:**
- Enabled servers
- Connection strings
- Caching: Enabled, 1 hour TTL
- Security: Allowed/denied paths

---

## Workflow Examples

### Example 1: New Dashboard Feature

```bash
# Create specification
/dashboard.spec Build a revenue dashboard with year-over-year comparison

# Review and refine spec
# Edit .specify/specs/003-revenue-dashboard/spec.md

# Create plan
/dashboard.plan Use Dash with Plotly Express. Load from PostgreSQL. Cache with Redis.

# Review plan
# Edit .specify/specs/003-revenue-dashboard/plan.md

# Generate tasks
/dashboard.tasks

# Review tasks
# Edit .specify/specs/003-revenue-dashboard/tasks.md

# Implement
/dashboard.implement

# Test
/dashboard.test

# Review quality
/dashboard.review

# Deploy
/dashboard.deploy
```

### Example 2: Data Analysis Workflow

```bash
# Create spec
/dashboard.spec Analyze customer segmentation data and create interactive dashboard

# Plan with MCP
/dashboard.plan Use MCP postgres server for data access. Plotly Dash for visualization.

# During implementation, data-analysis skill automatically:
# - Connects to database via MCP
# - Performs EDA
# - Identifies segments
# - Suggests visualizations
# - Generates transformation code

/dashboard.implement
```

### Example 3: Parallel Development

```bash
# Start implementation
/dashboard.implement

# Claude Code launches sub-agents automatically:
# - component-builder: Creates UI components in parallel
# - data-pipeline: Builds data loaders concurrently
# - test-engineer: Writes tests alongside implementation
# - documentation: Generates docs as code is written

# All work coordinated to avoid conflicts
# Final integration happens automatically
```

---

## Customization

### Adding Custom Commands

1. Create `.claude/commands/dashboard.{action}.md`
2. Define command behavior and arguments
3. Document usage and examples
4. Update this file

### Adding Custom Skills

1. Create `.claude/skills/{skill-name}.yaml`
2. Define capabilities, inputs, outputs
3. Specify implementation guidelines
4. Test with sample scenarios
5. Update this file

### Configuring MCP Servers

1. Edit `.claude/mcp_config.json`
2. Add server configuration
3. Set environment variables for credentials
4. Enable the server
5. Test connection

---

## Troubleshooting

### Commands Not Found

- Verify `.claude/commands/` directory exists
- Check command file naming: `dashboard.{action}.md`
- Reload Claude Code configuration

### Skills Not Working

- Check `.claude/skills/` directory
- Validate YAML syntax
- Review skill configuration in agent_config.yaml

### MCP Connection Failures

- Verify server is running
- Check connection credentials
- Review mcp_config.json configuration
- Check allowed paths in security settings

### Sub-Agent Conflicts

- Review coordination strategy in agent_config.yaml
- Check for file locking issues
- Increase task timeout if needed
- Reduce max_concurrent sub-agents

---

## Performance Tips

1. **Enable Caching:** Speeds up repeated operations
2. **Use MCP:** Faster data access than manual file reading
3. **Parallel Tasks:** Mark independent tasks with [P] in tasks.md
4. **Sub-Agents:** Launch for truly parallel work
5. **Memory:** Keeps context, reduces repeated explanations

---

## Security Best Practices

1. **Never hardcode secrets:** Use environment variables
2. **Enable secret scanning:** Configured in agent_config.yaml
3. **MCP security:** Configure allowed/denied paths
4. **Review code:** Use `/dashboard.review` before commits
5. **Audit dependencies:** Run safety checks

---

## Support

For issues or questions:

1. Check `.specify/specs/002-claude-code-agent-setup/spec.md`
2. Review `.claude/README.md`
3. Consult `docs/REFERENCES.md` for learning resources
4. Review constitution: `.specify/memory/constitution.md`

---

## Version

- **Configuration Version:** 1.0.0
- **Last Updated:** 2025-11-10
- **Specification:** `.specify/specs/002-claude-code-agent-setup/spec.md`

---

*This setup enables rapid, high-quality dashboard development with Claude Code following spec-driven methodology and constitutional standards.*
