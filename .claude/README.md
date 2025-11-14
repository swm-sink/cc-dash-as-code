# Claude Code Configuration

This directory contains custom Claude Code configuration for spec-driven dashboard development with Plotly Dash.

**Specification**: Spec 002 - Claude Code Commands Setup (Approved)
**Last Updated**: 2025-11-13
**Version**: 1.0.0

---

## Directory Structure

```
.claude/
├── commands/           # Custom slash commands (16 total)
│   ├── spec/          # Specification workflow (5 commands)
│   ├── workflow/      # EPIC methodology (6 commands)
│   ├── utils/         # Development utilities (6 commands)
│   └── dash/          # Dash component creation (3 commands)
├── agents/            # Sub-agent definitions (3 agents)
├── skills/            # Agent skills (auto-activate based on context)
│   ├── development/   # Development skills (Spec 003) - 3 skills
│   └── production/    # Production skills (Spec 004) - 5 skills
├── settings.json      # Configuration and permissions
└── README.md          # This file
```

---

## Commands

### Specification Workflow (`/spec.*`)

Commands for managing feature specifications following spec-kit methodology:

- **`/spec.create [description]`** - Create new feature specification with unique number
- **`/spec.validate`** - Check specification completeness and constitutional alignment
- **`/spec.list`** - Show all specifications with their current status
- **`/spec.show [feature-number]`** - Display full specification content
- **`/spec.branch [feature-number]`** - Create git feature branch from approved spec

### EPIC Workflow (`/workflow.*`)

Commands implementing the EPIC methodology (Observe → Act → Verify → Loop):

- **`/workflow.observe`** - Analyze current state and identify next tasks
- **`/workflow.act [task]`** - Implement task following TDD (Test-Driven Development)
- **`/workflow.verify`** - Validate implementation (tests, lint, type check, accessibility)
- **`/workflow.loop`** - Checkpoint progress and present next task options
- **`/workflow.status`** - Show spec requirement completion progress
- **`/workflow.checkpoint [message]`** - Create git commits with descriptive messages

### Development Utilities (`/utils.*`)

Commands for testing, linting, formatting, and dependency management:

- **`/utils.test [path]`** - Run pytest with coverage reporting
- **`/utils.lint`** - Run Black, Ruff, and mypy and report issues
- **`/utils.format`** - Auto-format code with Black and Ruff
- **`/utils.check-deps`** - Validate and check dependencies for updates/vulnerabilities
- **`/utils.commit [message]`** - Create git commit with conventional commit format
- **`/utils.diff [spec-number]`** - Show changes since feature branch creation

### Dash Component Creation (`/dash.*`)

Commands for creating Dash components, layouts, and callbacks:

- **`/dash.component [name] [type]`** - Create Dash component with tests and documentation
- **`/dash.layout [name]`** - Create responsive dashboard layout
- **`/dash.callback [description]`** - Create Dash callback with tests

---

## Sub-Agents

Specialized agents for parallel work on different aspects of implementation:

### component-builder
- **Specialization**: Autonomous UI component creation
- **Coordination**: File locking
- **Responsibilities**: Build components, write tests, generate docs, apply theming

### data-pipeline
- **Specialization**: Data infrastructure development
- **Coordination**: Queue-based (for database operations)
- **Responsibilities**: Data loaders, transformations, validators, query optimization, caching

### test-engineer
- **Specialization**: Comprehensive testing infrastructure
- **Coordination**: Independent (test files separate from implementation)
- **Responsibilities**: Unit tests, integration tests, e2e tests, fixtures, CI/CD config

---

## Skills

Skills are specialized capabilities that auto-activate based on context. They provide domain expertise without explicit invocation.

### Development Skills (`skills/development/`)

Support building the Claude Code system itself (Spec 003):

1. **spec-kit-workflow** - Guide specification creation
2. **claude-code-architecture** - Commands/Skills/Sub-Agents expertise
3. **research-synthesis** - Analyze reference implementations

**Status**: Placeholder (to be implemented in Spec 003 - Phase 2)

### Production Skills (`skills/production/`)

Support dashboard developers using the system (Spec 004):

1. **data-analysis** - Statistical analysis, EDA, data quality
2. **plotly-viz** - Chart generation with WCAG 2.1 AA compliance
3. **dash-components** - Component patterns, callback architecture
4. **accessibility-audit** - WCAG 2.1 Level AA validation
5. **performance-optimizer** - Bottleneck detection, optimization (<3s load, <1s callbacks)

**Status**: Placeholder (to be implemented in Spec 004 - Phase 3)

---

## Configuration

### settings.json

Central configuration file defining:
- **Permissions**: Allowed tools and file access paths
- **Code Quality**: Formatter, linter, type checker settings (80% coverage minimum)
- **Workflow**: Branch patterns, commit message format (Conventional Commits)
- **Security**: Secret scanning enabled
- **Skills**: Token budgets (Level 1: 60, Level 2: 1000)

See `settings.json` for complete configuration.

---

## EPIC Workflow

The EPIC methodology provides iterative feature development:

```
Observe → Act → Verify → Loop
   ↓       ↓       ↓       ↓
Identify  Implement  Validate  Checkpoint
next task  with TDD    quality   & continue
```

**Example workflow**:
```bash
/workflow.observe     # Identifies: "Create sales filter component"
/workflow.act Create sales filter component  # Implements with TDD
/workflow.verify      # Runs tests, lint, type check
/workflow.loop        # Commits and shows next task
```

---

## Usage Examples

### Creating a New Feature

```bash
# 1. Create specification
/spec.create Build a revenue dashboard with year-over-year comparison

# 2. Edit spec.md, add plan.md and tasks.md manually

# 3. Create feature branch
/spec.branch 006

# 4. Begin EPIC workflow
/workflow.observe
/workflow.act <identified task>
/workflow.verify
/workflow.loop
```

### Creating Dash Components

```bash
# Create a filter component
/dash.component RegionFilter dropdown

# Create a layout
/dash.layout revenue_dashboard

# Create callback
/dash.callback Update chart when region filter changes
```

### Running Quality Checks

```bash
# Run tests
/utils.test

# Fix formatting
/utils.format

# Check all quality metrics
/utils.lint
```

---

## Implementation Status

### Phase 1: Directory Structure ✅ Complete
- All directories created
- Placeholder READMEs for skills
- This README created

### Phase 2: Commands 🔄 Next
- Implement 16 slash commands
- Test each command category
- Integration testing

### Phase 3: Sub-Agents & Settings 📋 Planned
- Define 3 sub-agents
- Create settings.json
- Test coordination strategies

### Phase 4-5: Skills 📋 Future
- Spec 003: Development Skills (Phase 2)
- Spec 004: Production Skills (Phase 3)

---

## Documentation

- **User Guide**: See `CLAUDE.md` in project root
- **Specification**: See `specs/002-claude-code-commands-setup/spec.md`
- **Technical Plan**: See `specs/002-claude-code-commands-setup/plan.md`
- **Task Breakdown**: See `specs/002-claude-code-commands-setup/tasks.md`

---

## Support

For issues or questions:
1. Check `CLAUDE.md` for usage examples
2. Review Spec 002 for requirements
3. Check `specs/memory/constitution.md` for project principles
4. Review `IMPLEMENTATION_PLAN.md` for overall timeline

---

**Version**: 1.0.0 (Phase 1 Complete)
**Specification**: Spec 002 - Claude Code Commands Setup (Approved)
**Last Updated**: 2025-11-13
