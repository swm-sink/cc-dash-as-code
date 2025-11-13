# Claude Code Setup for Dashboard Development

This file documents the custom Claude Code configuration for spec-driven dashboard development with Plotly Dash.

**Last Updated**: 2025-11-13
**Aligned with**: Spec 002 (Claude Code Commands Setup) - Approved

---

## Overview

This project uses Claude Code with custom slash commands, agent skills, and specialized sub-agents to accelerate dashboard development following the spec-kit methodology and EPIC workflow.

**Key Capabilities:**
- Custom slash commands for spec-driven workflow
- EPIC methodology (Observe → Act → Verify → Loop)
- Specialized agent skills for domain tasks
- Sub-agents for parallel development
- MCP integration for data access (optional)
- Agent memory for context persistence
- Seamless Agent SDK deployment

---

## Quick Start

### 1. Create a Feature Specification

```bash
/spec.create Create a sales analytics dashboard with date filtering
```

### 2. Begin Implementation (EPIC Workflow)

```bash
/workflow.observe    # Analyze current state, identify next tasks
/workflow.act        # Implement the identified task
/workflow.verify     # Run tests, lint, type check
/workflow.loop       # Checkpoint and continue
```

### 3. Utilities

```bash
/utils.test          # Run test suite
/utils.lint          # Check code quality
/utils.format        # Auto-format code
```

---

## Custom Slash Commands

Commands are organized into 4 categories following Spec 002 architecture.

### Specification Workflow Commands (`/spec.*`)

These commands help create and manage feature specifications following the spec-kit methodology.

---

#### `/spec.create [description]`

Create a new feature specification with unique feature number.

**Usage:**
```
/spec.create Build a customer analytics dashboard with filters for region and date range
```

**What it does:**
- Generates unique feature number (auto-increments)
- Creates `specs/{number}-{feature-name}/` directory
- Populates `spec.md` from template
- Initializes README and directory structure
- Reviews constitution for alignment

**Output:**
- `specs/{number}-{feature-name}/spec.md`
- Directory structure ready for plan.md and tasks.md

**Next step:** Manually create `plan.md` and `tasks.md`, then `/workflow.observe`

---

#### `/spec.validate`

Check specification completeness and constitutional alignment.

**Usage:**
```
/spec.validate
```

**What it does:**
- Validates spec.md structure (all required sections present)
- Checks requirements have unique IDs (FR-NNN format)
- Verifies success criteria are measurable
- Checks alignment with constitution.md
- Reports missing or incomplete sections

**Output:**
- Validation report with issues and recommendations

---

#### `/spec.list`

Show all specifications with their current status.

**Usage:**
```
/spec.list
```

**What it does:**
- Lists all specs in specs/ directory
- Shows status (draft, approved, implemented, etc.)
- Displays feature numbers, names, priorities
- Shows dependencies between specs

**Output:**
- Table of all specifications with metadata

---

#### `/spec.show [feature-number]`

Display full specification content.

**Usage:**
```
/spec.show 003
```

**What it does:**
- Reads and displays spec.md for given feature
- Shows user stories, requirements, success criteria
- Displays dependencies and clarifications

**Output:**
- Full specification content

---

#### `/spec.branch [feature-number]`

Create git feature branch from approved spec.

**Usage:**
```
/spec.branch 003
```

**What it does:**
- Creates git branch: `{number}-{feature-name}`
- Switches to new branch
- Prepares for implementation

**Output:**
- New git branch
- Ready for `/workflow.observe`

---

### EPIC Workflow Commands (`/workflow.*`)

These commands implement the EPIC methodology (Observe → Act → Verify → Loop) for feature development.

**EPIC** = **E**xecute, **P**lan, **I**mprove, **C**ontinue (iterative development)

---

#### `/workflow.observe`

Analyze current state and identify next tasks.

**Usage:**
```
/workflow.observe
```

**What it does:**
- Reads spec.md, plan.md, tasks.md
- Analyzes what's been implemented (reads src/, tests/)
- Identifies next actionable task
- Provides context and guidance

**Output:**
- Current progress summary
- Next recommended task
- Context for implementation

**Next step:** `/workflow.act`

---

#### `/workflow.act [task]`

Implement a task following TDD (Test-Driven Development).

**Usage:**
```
/workflow.act Implement sales filter component
```

**What it does:**
- Writes failing test first (TDD red phase)
- Implements code to make test pass (TDD green phase)
- Refactors if needed (TDD refactor phase)
- Follows best practices (type hints, docstrings)
- Integrates with relevant Skills (data-analysis, plotly-viz, etc.)

**Output:**
- New/modified code in src/
- New/modified tests in tests/
- Implementation ready for verification

**Next step:** `/workflow.verify`

---

#### `/workflow.verify`

Validate implementation (tests, lint, type check, accessibility, performance).

**Usage:**
```
/workflow.verify
```

**What it does:**
- Runs full test suite (`pytest`)
- Checks coverage (must meet 80% minimum)
- Runs linter (`ruff`)
- Runs type checker (`mypy`)
- Runs accessibility audit (if applicable)
- Checks performance targets (<3s load, <1s callbacks)

**Output:**
- Test results and coverage report
- Lint/type check results
- Accessibility compliance status
- Performance measurements
- Pass/fail status

**Next step:** If pass → `/workflow.loop`, If fail → fix and `/workflow.verify` again

---

#### `/workflow.loop`

Checkpoint progress and present next task options.

**Usage:**
```
/workflow.loop
```

**What it does:**
- Creates git commit with descriptive message
- Updates progress tracking
- Analyzes remaining tasks
- Presents next task options
- Decides: continue, pivot, or complete

**Output:**
- Git commit created
- Progress summary
- Next task recommendations

**Next step:** `/workflow.observe` (continue cycle) or done

---

#### `/workflow.status`

Show spec requirement completion progress.

**Usage:**
```
/workflow.status
```

**What it does:**
- Reads spec.md requirements (FR-NNN)
- Analyzes code coverage of requirements
- Shows which requirements are implemented
- Identifies gaps and missing requirements

**Output:**
- Requirement completion matrix
- Implementation coverage percentage
- Missing/incomplete requirements

---

#### `/workflow.checkpoint`

Create git commits with descriptive messages.

**Usage:**
```
/workflow.checkpoint Implement data loading with pandas
```

**What it does:**
- Runs git status
- Stages relevant changes
- Creates commit with message following Conventional Commits
- Ensures tests pass before committing

**Output:**
- Git commit created

---

### Utility Commands (`/utils.*`)

These commands provide development utilities for testing, linting, formatting, and dependency management.

---

#### `/utils.test [path]`

Run pytest with coverage reporting.

**Usage:**
```
/utils.test                    # Run all tests
/utils.test tests/unit/        # Run specific directory
/utils.test tests/test_foo.py  # Run specific file
```

**What it does:**
- Runs pytest with coverage plugin
- Generates coverage report (HTML and terminal)
- Shows passing/failing tests
- Identifies uncovered code

**Output:**
- Test results
- Coverage percentage
- HTML coverage report in `htmlcov/`

---

#### `/utils.lint`

Run Black, Ruff, and mypy and report issues.

**Usage:**
```
/utils.lint
```

**What it does:**
- Runs Black formatter (check mode)
- Runs Ruff linter
- Runs mypy type checker
- Reports all issues found

**Output:**
- Linting issues with file locations
- Type errors
- Formatting violations

**Next step:** `/utils.format` to auto-fix

---

#### `/utils.format`

Auto-format code with Black and Ruff.

**Usage:**
```
/utils.format
```

**What it does:**
- Runs Black formatter (write mode)
- Runs Ruff with --fix flag
- Applies automatic fixes

**Output:**
- Formatted code files
- Summary of changes applied

---

#### `/utils.check-deps`

Validate and check dependencies for updates/vulnerabilities.

**Usage:**
```
/utils.check-deps
```

**What it does:**
- Validates requirements.txt
- Checks for package updates
- Scans for security vulnerabilities (using safety or pip-audit)
- Reports outdated or vulnerable packages

**Output:**
- Dependency status report
- Update recommendations
- Security warnings

---

#### `/utils.commit [message]`

Create git commit with conventional commit format.

**Usage:**
```
/utils.commit "feat: Add sales filter component"
```

**What it does:**
- Validates commit message format
- Stages changes
- Creates commit
- Follows Conventional Commits specification

**Output:**
- Git commit created

---

#### `/utils.diff [spec-number]`

Show changes since feature branch creation.

**Usage:**
```
/utils.diff 003
```

**What it does:**
- Shows git diff from feature branch base
- Highlights added/modified/deleted files
- Shows line-by-line changes

**Output:**
- Git diff output

---

### Dash-Specific Commands (`/dash.*`)

These commands help create Dash components, layouts, and callbacks following best practices.

---

#### `/dash.component [name] [type]`

Create Dash component with tests and documentation.

**Usage:**
```
/dash.component SalesFilter dropdown
/dash.component DataTable table
```

**What it does:**
- Creates component file in `src/components/`
- Generates component function with proper structure
- Creates unit test file in `tests/unit/components/`
- Adds type hints and docstrings
- Follows accessibility guidelines

**Output:**
- `src/components/{name}.py`
- `tests/unit/components/test_{name}.py`

---

#### `/dash.layout [name]`

Create responsive dashboard layout.

**Usage:**
```
/dash.layout sales_dashboard
```

**What it does:**
- Creates layout file in `src/layouts/`
- Generates responsive grid structure
- Includes header, sidebar, main content areas
- Applies theming and styling
- Follows accessibility guidelines

**Output:**
- `src/layouts/{name}.py`
- `tests/unit/layouts/test_{name}.py`

---

#### `/dash.callback [description]`

Create Dash callback with tests.

**Usage:**
```
/dash.callback Update chart when filter changes
```

**What it does:**
- Creates callback function in appropriate module
- Defines Input, Output, State
- Generates callback test
- Follows callback best practices (prevent_initial_call, etc.)

**Output:**
- Callback code with @app.callback decorator
- Test for callback logic

---

## Agent Skills

Skills are specialized capabilities that auto-activate based on context. You don't invoke them explicitly—they activate when needed.

### Development Skills (`.claude/skills/development/`)

These skills support building the Claude Code system itself.

1. **spec-kit-workflow**
   - **Purpose:** Guide specification creation following spec-kit methodology
   - **Activates when:** Working with spec.md files, creating requirements
   - **Provides:** Templates, requirement formats, success criteria patterns

2. **claude-code-architecture**
   - **Purpose:** Expertise on Commands, Skills, Sub-Agents, Hooks architecture
   - **Activates when:** Designing architecture, choosing between mechanisms
   - **Provides:** Decision matrices, architectural patterns, best practices

3. **research-synthesis**
   - **Purpose:** Analyze reference implementations and extract patterns
   - **Activates when:** Researching codebases, analyzing patterns
   - **Provides:** Analysis methods, pattern extraction techniques

### Production Skills (`.claude/skills/production/`)

These skills support dashboard developers building dashboards.

1. **data-analysis**
   - **Purpose:** Statistical analysis, EDA, data quality checking
   - **Activates when:** Loading .csv/.json/.parquet files, using pandas/SQL
   - **Provides:** EDA workflows, quality checks, visualization recommendations

2. **plotly-viz**
   - **Purpose:** Chart generation with WCAG 2.1 AA compliance
   - **Activates when:** Creating charts, mentions "visualization", "plot", "chart"
   - **Provides:** Chart selection guide, accessible color palettes, Plotly patterns

3. **dash-components**
   - **Purpose:** Component patterns, callback architecture
   - **Activates when:** Creating Dash components, writing callbacks
   - **Provides:** Component patterns, callback best practices, state management

4. **accessibility-audit**
   - **Purpose:** WCAG 2.1 Level AA compliance validation
   - **Activates when:** Running `/workflow.verify`, mentions "accessibility"
   - **Provides:** WCAG checklist, color contrast checking, keyboard nav testing

5. **performance-optimizer**
   - **Purpose:** Bottleneck detection and optimization
   - **Activates when:** Performance issues detected, mentions "slow", "optimize"
   - **Provides:** Bottleneck identification, caching strategies, profiling methods

---

## Sub-Agents

Specialized agents that can be launched for parallel work on different aspects of implementation.

### component-builder

**Specialization:** Autonomous UI component creation

**Responsibilities:**
- Build reusable Dash components
- Write component tests
- Generate component documentation
- Apply theming and styling

**Coordination:** File locking for component files

**When to use:** Creating multiple components in parallel

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

**When to use:** Building data loading and processing infrastructure

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

**When to use:** Generating comprehensive test coverage

---

## MCP Integration (Optional)

Model Context Protocol servers for standardized data access. These are **optional** - dashboards can use direct access methods without MCP.

**Configuration:** `.claude/mcp_config.json`

### Available MCP Servers

#### mcp__postgres
- **Purpose:** PostgreSQL database access
- **Connection:** `${POSTGRES_URL}` environment variable
- **Status:** Disabled by default (enable in config)

#### mcp__filesystem
- **Purpose:** Access CSV, JSON, Parquet files
- **Path:** `./data` (configurable)
- **Status:** Enabled

#### mcp__fetch
- **Purpose:** REST API access
- **Status:** Enabled

#### mcp__search
- **Purpose:** Search reference documentation
- **Path:** `./reference` (configurable)
- **Status:** Enabled

### Enabling MCP Servers

Edit `.claude/mcp_config.json`:
```json
{
  "mcpServers": {
    "postgres": {
      "enabled": true,
      "env": {
        "POSTGRES_URL": "${POSTGRES_URL}"
      }
    }
  }
}
```

---

## Workflow Examples

### Example 1: New Dashboard Feature (Full EPIC Cycle)

```bash
# 1. Create specification
/spec.create Build a revenue dashboard with year-over-year comparison

# 2. Manually edit spec.md, add plan.md and tasks.md

# 3. Create feature branch
/spec.branch 006

# 4. Begin EPIC workflow
/workflow.observe
# → Analyzes spec, identifies first task: "Create project structure"

/workflow.act Create src/dashboards/revenue/ directory structure
# → Creates directories and __init__.py files

/workflow.verify
# → Tests pass (no code yet), linting passes

/workflow.loop
# → Commits changes, shows next task

/workflow.observe
# → Identifies next task: "Implement data loading"

/workflow.act Load revenue data from PostgreSQL
# → data-analysis skill activates
# → Implements data loader with pandas
# → Creates tests

/workflow.verify
# → Tests pass, coverage 85%, linting passes

/workflow.loop
# → Commits, continues

# ... continue cycle until all requirements implemented ...

/workflow.status
# → Shows FR-001 to FR-015 all implemented

# 5. Final verification
/utils.test
/utils.lint
/workflow.verify

# 6. Ready for deployment (handled separately via Agent SDK)
```

---

### Example 2: Quick Testing and Formatting

```bash
# Run tests
/utils.test

# Fix formatting
/utils.format

# Check all quality metrics
/utils.lint
```

---

### Example 3: Creating Components

```bash
# Create a filter component
/dash.component RegionFilter dropdown

# Create a layout
/dash.layout revenue_dashboard

# Create callback
/dash.callback Update revenue chart when region filter changes
```

---

## Configuration Files

### .claude/mcp_config.json

MCP server configuration (optional).

**Key settings:**
- Enabled servers
- Connection strings (via environment variables)
- Security (allowed/denied paths)
- Caching (TTL settings)

### specs/memory/constitution.md

Project principles and development guidelines (required).

**Contains:**
- 10 core principles
- Code quality standards (80% coverage, WCAG 2.1 AA, <3s load)
- Testing requirements
- Security standards

### specs/memory/patterns.md

Coding patterns and conventions (to be created).

### specs/memory/decisions.md

Architectural decisions log (to be created).

### specs/memory/preferences.md

Developer preferences and anti-patterns (to be created).

---

## Troubleshooting

### Commands Not Found

- Verify `.claude/commands/` directory exists
- Check command file naming matches Spec 002
- Reload Claude Code configuration

### Skills Not Activating

- Check `.claude/skills/` directory structure
- Validate SKILL.md files exist
- Review activation keywords in context

### MCP Connection Failures

- Verify server is running
- Check connection credentials in environment variables
- Review `mcp_config.json` configuration
- Check allowed paths in security settings

### Sub-Agent Conflicts

- Review coordination strategy (file locking, queue-based)
- Check for file access conflicts
- Increase task timeout if needed
- Reduce max_concurrent sub-agents

---

## Performance Tips

1. **Use EPIC workflow** - Small, iterative cycles are faster than big implementations
2. **Enable MCP caching** - Speeds up repeated data operations
3. **Leverage Skills** - They provide expertise automatically
4. **Parallel Sub-Agents** - Use for independent work
5. **Keep context lean** - Progressive disclosure in Skills keeps context small

---

## Security Best Practices

1. **Never hardcode secrets** - Use environment variables
2. **Enable secret scanning** - Configured in settings
3. **MCP security** - Configure allowed/denied paths
4. **Review code** - Use `/utils.lint` before commits
5. **Audit dependencies** - Run `/utils.check-deps` regularly

---

## Implementation Order

Per Spec 002 and approved specs:

```
Phase 1: Spec 002 - Claude Code Commands Setup (this configuration)
  ↓
Phase 2: Spec 003 - Development Skills (3 skills)
  ↓
Phase 3: Spec 004 - Production Skills (5 skills)
  ↓
Phase 4: Spec 005 - MCP Integration (optional)
  ↓
Phase 5: Spec 001 - Dashboard Foundation (application code)
```

**Current Status:** Phase 1 (Spec 002) in planning - need to create plan.md and tasks.md

---

## Support

For issues or questions:

1. Check Spec 002: `specs/002-claude-code-commands-setup/spec.md`
2. Review constitution: `specs/memory/constitution.md`
3. Check workflow: `specs/WORKFLOW.md`
4. Review implementation plan: `IMPLEMENTATION_PLAN.md`

---

## Version

- **Configuration Version:** 2.0.0 (Aligned with Spec 002)
- **Last Updated:** 2025-11-13
- **Specification:** `specs/002-claude-code-commands-setup/spec.md` (Approved)
- **Changes from 1.0.0:**
  - Updated command namespace from `/dashboard.*` to match Spec 002
  - Added EPIC workflow (Observe → Act → Verify → Loop)
  - Aligned all commands with Spec 002 requirements
  - Added Dash-specific commands
  - Clarified Skills activation patterns
  - Updated MCP as optional enhancement

---

*This setup enables rapid, high-quality dashboard development with Claude Code following spec-driven methodology, EPIC workflow, and constitutional standards.*
