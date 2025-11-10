# Claude Code Configuration

This directory contains configuration files for Claude Code, including custom slash commands, agent skills, and MCP server configurations.

## Directory Structure

```
.claude/
├── README.md                   # This file
├── commands/                   # Custom slash commands
│   ├── dashboard.spec.md      # Create feature specifications
│   ├── dashboard.plan.md      # Create implementation plans
│   ├── dashboard.tasks.md     # Generate task breakdowns
│   ├── dashboard.implement.md # Execute implementation
│   ├── dashboard.analyze.md   # Cross-artifact analysis
│   ├── dashboard.deploy.md    # Agent SDK deployment
│   ├── dashboard.test.md      # Run test suites
│   └── dashboard.review.md    # Code quality review
├── skills/                     # Agent skill definitions
│   ├── data-analysis.yaml     # Data analysis skill
│   ├── plotly-viz.yaml        # Visualization generation
│   ├── dashboard-testing.yaml # Test generation
│   ├── accessibility-audit.yaml # WCAG compliance checking
│   ├── performance-optimizer.yaml # Performance optimization
│   └── component-builder.yaml # Component creation
├── mcp_config.json            # MCP server configuration
└── agent_config.yaml          # Agent behavior settings
```

## Custom Slash Commands

All custom commands for the spec-driven dashboard workflow. Commands follow the naming pattern `/dashboard.<action>`.

### Core Workflow Commands

- `/dashboard.spec [description]` - Create a new feature specification
- `/dashboard.plan [tech details]` - Create a technical implementation plan
- `/dashboard.tasks` - Generate task breakdown from plan
- `/dashboard.implement` - Execute implementation tasks

### Quality & Deployment Commands

- `/dashboard.analyze` - Cross-artifact consistency analysis
- `/dashboard.test` - Run test suite with coverage
- `/dashboard.review` - Perform code quality review
- `/dashboard.deploy` - Configure Agent SDK deployment

## Agent Skills

Skills are specialized capabilities that Claude Code can invoke to perform domain-specific tasks. Each skill is defined in a YAML file with metadata and implementation guidelines.

### Available Skills

- **data-analysis**: Load, analyze, and visualize datasets
- **plotly-viz**: Generate appropriate Plotly visualizations
- **dashboard-testing**: Comprehensive test generation
- **accessibility-audit**: WCAG compliance checking
- **performance-optimizer**: Performance bottleneck identification
- **component-builder**: Create reusable Dash components

## MCP Configuration

The `mcp_config.json` file configures Model Context Protocol servers for accessing data sources (databases, files, APIs).

Example MCP servers:
- PostgreSQL database access
- Filesystem access (CSV, JSON, Parquet)
- REST API access
- Local documentation search

## Agent Configuration

The `agent_config.yaml` file configures agent behavior, preferences, and constraints.

Settings include:
- Code quality thresholds
- Testing requirements
- Memory persistence settings
- Sub-agent coordination rules

## Usage

### Creating a New Feature

```bash
# 1. Create specification
/dashboard.spec Build a sales analytics dashboard with filters

# 2. Create implementation plan
/dashboard.plan Use Plotly Dash with Pandas for data processing

# 3. Generate tasks
/dashboard.tasks

# 4. Implement
/dashboard.implement
```

### Testing and Quality

```bash
# Run tests
/dashboard.test

# Review code quality
/dashboard.review

# Analyze consistency
/dashboard.analyze
```

### Deployment

```bash
# Configure Agent SDK deployment
/dashboard.deploy
```

## Adding Custom Commands

To add a new custom command:

1. Create a new Markdown file in `.claude/commands/`
2. Name it `dashboard.<action>.md`
3. Define the command prompt and behavior
4. Document in this README

## Adding Custom Skills

To add a new skill:

1. Create a new YAML file in `.claude/skills/`
2. Define skill metadata (name, description, inputs, outputs)
3. Specify implementation guidelines
4. Document in this README

## Configuration Files

### mcp_config.json

Defines MCP servers for data access:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "mcp-server-postgres",
      "args": ["--connection-string", "$POSTGRES_URL"]
    },
    "filesystem": {
      "command": "mcp-server-filesystem",
      "args": ["--root-path", "./data"]
    }
  }
}
```

### agent_config.yaml

Configures agent behavior:

```yaml
code_quality:
  min_coverage: 80
  formatters:
    - black
    - ruff
  type_checking: strict

testing:
  frameworks:
    - pytest
  require_tests: true

memory:
  persist: true
  location: .specify/memory/

sub_agents:
  max_concurrent: 4
  coordination: file_locking
```

## Documentation

All commands and skills are automatically documented in `CLAUDE.md` at the project root.

For detailed specifications, see:
- `.specify/specs/002-claude-code-agent-setup/spec.md`

---

*This configuration enables spec-driven dashboard development with Claude Code and seamless production deployment via Claude Agent SDK.*
