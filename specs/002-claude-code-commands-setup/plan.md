# Technical Implementation Plan: Claude Code Commands Setup

**Specification**: 002-claude-code-commands-setup
**Status**: Approved
**Plan Created**: 2025-11-13
**Implementation Priority**: P1 (Phase 1 - Implement FIRST)

---

## Overview

This plan defines the technical approach for implementing Spec 002: Claude Code Commands Setup. The goal is to configure Claude Code with custom slash commands, sub-agents, and configuration for spec-driven dashboard development using the EPIC workflow methodology.

**Key Deliverables**:
- `.claude/` directory with complete configuration
- 16 slash commands across 4 categories
- 3 sub-agent definitions
- Settings and configuration files
- Directory structure for Skills (implemented in Specs 003-004)

---

## Architecture

### Technology Stack

**Primary**:
- Claude Code (development environment)
- Markdown (command documentation format)
- YAML (frontmatter metadata)
- JSON (configuration files)

**No Additional Dependencies**: This phase uses only Claude Code features; no new packages needed.

---

### Directory Structure

```
.claude/
├── commands/
│   ├── spec/
│   │   ├── create.md
│   │   ├── validate.md
│   │   ├── list.md
│   │   ├── show.md
│   │   └── branch.md
│   ├── workflow/
│   │   ├── observe.md
│   │   ├── act.md
│   │   ├── verify.md
│   │   ├── loop.md
│   │   ├── status.md
│   │   └── checkpoint.md
│   ├── utils/
│   │   ├── test.md
│   │   ├── lint.md
│   │   ├── format.md
│   │   ├── check-deps.md
│   │   ├── commit.md
│   │   └── diff.md
│   └── dash/
│       ├── component.md
│       ├── layout.md
│       └── callback.md
├── agents/
│   ├── component-builder.md
│   ├── data-pipeline.md
│   └── test-engineer.md
├── skills/
│   ├── development/      # Placeholder (Spec 003)
│   └── production/       # Placeholder (Spec 004)
├── settings.json
└── README.md
```

**Rationale**:
- Commands organized by category (spec, workflow, utils, dash)
- Each command is a standalone .md file for clarity
- Agents defined as .md files following Claude Code conventions
- Skills directories created as placeholders (populated in Specs 003-004)

---

## Command File Format

### Standard Command Structure

All command files follow this structure:

```markdown
---
name: command-name
description: Brief description (1-2 sentences)
parameters:
  - name: param1
    description: Parameter description
    required: true/false
    type: string/number/boolean
tools:
  - tool-name-1
  - tool-name-2
---

# /category.command-name

Detailed description of what this command does.

## Usage

```
/category.command-name [param1] [param2]
```

## Behavior

Step-by-step description of command behavior:
1. Step 1
2. Step 2
3. Step 3

## Examples

Example 1:
```
/category.command-name example-value
```

## Output

Description of expected output.

## See Also

- Related commands
- Related documentation
```

**Rationale**:
- YAML frontmatter provides machine-readable metadata
- Markdown body provides human-readable documentation
- Consistent structure makes commands predictable
- Examples clarify usage

---

## Command Implementation Details

### Category 1: Spec Commands (`/spec.*`)

**Purpose**: Manage feature specifications following spec-kit methodology

#### `/spec.create [description]`

**Technical Approach**:
1. Use `Glob` tool to find existing specs, extract highest number
2. Auto-increment to get next feature number (e.g., 006)
3. Sanitize description to kebab-case for directory name
4. Use `Bash` tool to create directory: `specs/{number}-{name}/`
5. Use `Read` tool to load `specs/templates/spec-template.md`
6. Use `Write` tool to create `specs/{number}-{name}/spec.md` from template
7. Use `Read` tool to load `specs/memory/constitution.md`
8. Check specification outline aligns with constitution principles
9. Output success message with file path and next steps

**Tools**: `Glob`, `Bash`, `Read`, `Write`

**Validation**: Ensure unique feature number, valid directory name

---

#### `/spec.validate`

**Technical Approach**:
1. Use `Glob` to find current spec directory (based on git branch or pwd)
2. Use `Read` to load spec.md
3. Parse markdown to check for required sections:
   - Overview
   - User Scenarios & Testing
   - Requirements
   - Success Criteria
   - Edge Cases
4. Validate requirements have FR-NNN format
5. Validate success criteria are measurable (contain numbers, percentages, time targets)
6. Use `Read` to load constitution.md
7. Check alignment (principles referenced, quality standards met)
8. Generate validation report

**Tools**: `Glob`, `Read`

**Validation**: Report must list missing sections and non-compliant requirements

---

#### `/spec.list`

**Technical Approach**:
1. Use `Glob` with pattern `specs/*/spec.md`
2. For each spec, use `Read` to extract metadata:
   - Feature number
   - Feature name
   - Status (from **Status**: line)
   - Priority (if present)
3. Parse dependencies from spec.md
4. Format as table or list
5. Output sorted by feature number

**Tools**: `Glob`, `Read`

**Validation**: All specs in specs/ directory must be listed

---

#### `/spec.show [feature-number]`

**Technical Approach**:
1. Validate feature-number format (3 digits)
2. Use `Glob` to find `specs/{number}-*/spec.md`
3. Use `Read` to load complete spec.md
4. Output full content
5. Optionally highlight key sections (user stories, requirements, success criteria)

**Tools**: `Glob`, `Read`

**Validation**: Error message if feature number not found

---

#### `/spec.branch [feature-number]`

**Technical Approach**:
1. Validate feature-number format
2. Use `Glob` to find spec directory
3. Extract feature name from directory
4. Use `Bash` with git to:
   - Check current branch
   - Create new branch: `{number}-{feature-name}`
   - Switch to new branch
5. Output success message

**Tools**: `Glob`, `Bash`

**Validation**: Check spec is approved before creating branch

---

### Category 2: Workflow Commands (`/workflow.*`)

**Purpose**: Implement EPIC methodology (Observe → Act → Verify → Loop)

#### `/workflow.observe`

**Technical Approach**:
1. Determine current feature:
   - Use `Bash` git branch to get feature number
   - Or use pwd if in spec directory
2. Use `Read` to load spec.md, plan.md, tasks.md
3. Use `Glob` + `Read` to analyze implemented code in src/
4. Use `Grep` to search for requirement IDs (FR-NNN) in code
5. Compare implemented vs planned:
   - Which tasks are complete
   - Which requirements are implemented
   - What's next in tasks.md
6. Output analysis:
   - Current progress summary
   - Next recommended task
   - Context and guidance

**Tools**: `Bash`, `Read`, `Glob`, `Grep`

**Validation**: Must identify at least one actionable next task

---

#### `/workflow.act [task]`

**Technical Approach**:
1. Parse task description
2. Determine task type (component, callback, data loading, etc.)
3. TDD workflow:
   - **Red**: Write failing test first
     - Use `Write` to create test file in tests/
     - Use relevant Skills (dash-components, data-analysis)
   - **Green**: Implement code to pass test
     - Use `Write` to create implementation in src/
     - Use type hints, docstrings (per patterns.md)
   - **Refactor**: Improve code quality
     - Use `Edit` for improvements
4. Output files created and next step (/workflow.verify)

**Tools**: `Write`, `Edit`, `Read`

**Skills Integration**: Auto-activates relevant Skills based on task type

**Validation**: Both test and implementation files must be created

---

#### `/workflow.verify`

**Technical Approach**:
1. Run test suite:
   - Use `Bash` to execute `pytest --cov --cov-report=html`
   - Parse output for pass/fail, coverage percentage
2. Run linter:
   - Use `Bash` to execute `ruff check src/ tests/`
   - Parse output for violations
3. Run type checker:
   - Use `Bash` to execute `mypy src/`
   - Parse output for type errors
4. Run formatter check:
   - Use `Bash` to execute `black --check src/ tests/`
5. If Dash components involved, run accessibility checks (Skills-based)
6. Check performance targets if applicable
7. Aggregate results:
   - Pass/fail for each check
   - Overall verification status
8. Output comprehensive report

**Tools**: `Bash`, `Read`

**Skills Integration**: accessibility-audit, performance-optimizer Skills may activate

**Validation**: All checks must pass for overall verification to succeed

---

#### `/workflow.loop`

**Technical Approach**:
1. Check verification status (must pass before looping)
2. Create git commit:
   - Use `Bash` git status
   - Use `Bash` git add relevant files
   - Generate commit message (Conventional Commits format)
   - Use `Bash` git commit
3. Update progress tracking (if using checklist)
4. Re-run `/workflow.observe` to identify next task
5. Present options:
   - Continue with next task
   - Pivot to different task
   - Mark feature complete
6. Output progress summary and next steps

**Tools**: `Bash`, `Read`

**Validation**: Only loop if verification passed

---

#### `/workflow.status`

**Technical Approach**:
1. Load spec.md to get all requirements (FR-NNN)
2. Use `Grep` to search codebase for requirement IDs in:
   - Code comments
   - Docstrings
   - Test names
3. Calculate completion:
   - Requirements implemented (found in code)
   - Requirements missing (not found)
4. Generate completion matrix
5. Output:
   - Percentage complete
   - List of implemented requirements
   - List of missing requirements

**Tools**: `Read`, `Grep`

**Validation**: Must show both completed and missing requirements

---

#### `/workflow.checkpoint`

**Technical Approach**:
1. Accept commit message as parameter
2. Validate message format (Conventional Commits)
3. Use `Bash` to:
   - git status (check for changes)
   - git add . (or specified files)
   - git commit -m "message"
4. Output commit hash and summary

**Tools**: `Bash`

**Validation**: Commit message must follow format: `type(scope): subject`

---

### Category 3: Utility Commands (`/utils.*`)

**Purpose**: Development utilities for testing, linting, formatting

#### `/utils.test [path]`

**Technical Approach**:
1. Parse optional path parameter (default: tests/)
2. Activate venv if not already active
3. Use `Bash` to execute:
   ```bash
   source venv/bin/activate
   pytest {path} --cov=src --cov-report=html --cov-report=term
   ```
4. Parse output:
   - Test count (passed/failed/skipped)
   - Coverage percentage
   - Failed test details
5. Output results with path to HTML report

**Tools**: `Bash`

**Validation**: Must report coverage percentage and test pass rate

---

#### `/utils.lint`

**Technical Approach**:
1. Activate venv
2. Run checks in parallel (if possible):
   - Black: `black --check src/ tests/`
   - Ruff: `ruff check src/ tests/`
   - mypy: `mypy src/`
3. Aggregate results
4. Output all issues with file:line references
5. Suggest `/utils.format` if formatting issues found

**Tools**: `Bash`

**Validation**: Report must show all violations or "all checks passed"

---

#### `/utils.format`

**Technical Approach**:
1. Activate venv
2. Run formatters:
   - Black: `black src/ tests/`
   - Ruff: `ruff check --fix src/ tests/`
3. Capture changed files
4. Output summary of files modified

**Tools**: `Bash`

**Validation**: Must apply formatting and report changes

---

#### `/utils.check-deps`

**Technical Approach**:
1. Activate venv
2. Run dependency checks:
   - Validate requirements.txt format
   - Check for updates: `pip list --outdated`
   - Security scan: `pip-audit` or `safety check`
3. Parse results
4. Output:
   - Outdated packages with versions
   - Security vulnerabilities (if any)
   - Recommendations

**Tools**: `Bash`

**Validation**: Must report status of all dependencies

---

#### `/utils.commit [message]`

**Technical Approach**:
1. Validate commit message format
2. Use `Bash` git to:
   - Check for changes
   - Stage changes
   - Create commit
3. Output commit hash

**Tools**: `Bash`

**Validation**: Commit must be created with proper format

---

#### `/utils.diff [spec-number]`

**Technical Approach**:
1. Find feature branch base:
   - Use `Bash` git to find merge-base with main
2. Run git diff:
   - `git diff {base}...HEAD`
3. Parse and format diff output
4. Highlight key changes (files added/modified/deleted)
5. Output diff with summary

**Tools**: `Bash`

**Validation**: Must show changes since feature branch creation

---

### Category 4: Dash Commands (`/dash.*`)

**Purpose**: Create Dash components, layouts, and callbacks

#### `/dash.component [name] [type]`

**Technical Approach**:
1. Validate name (PascalCase) and type (dropdown, table, etc.)
2. Determine component structure based on type
3. Create component file:
   - Use `Write` to create `src/components/{snake_case_name}.py`
   - Generate function with html.Div or dcc component
   - Add type hints, docstrings
   - Include id-based props
4. Create test file:
   - Use `Write` to create `tests/unit/components/test_{snake_case_name}.py`
   - Generate basic test (renders, props work)
5. Apply accessibility guidelines (Skills-based)
6. Output files created

**Tools**: `Write`, `Read` (for templates)

**Skills Integration**: dash-components, accessibility-audit Skills activate

**Validation**: Both component and test files must be created

---

#### `/dash.layout [name]`

**Technical Approach**:
1. Validate name
2. Create layout file:
   - Use `Write` to create `src/layouts/{snake_case_name}.py`
   - Generate responsive grid structure:
     - Header section
     - Sidebar section (if applicable)
     - Main content area
   - Apply theming
   - Ensure accessibility (ARIA labels, semantic HTML)
3. Create test file
4. Output files created

**Tools**: `Write`

**Skills Integration**: dash-components, accessibility-audit Skills activate

**Validation**: Layout must include header and main content areas

---

#### `/dash.callback [description]`

**Technical Approach**:
1. Parse description to infer:
   - Input components
   - Output components
   - Logic required
2. Generate callback:
   - @app.callback decorator with Input/Output/State
   - Function signature with type hints
   - Business logic placeholder/implementation
   - Docstring
3. Suggest where to place callback (which module)
4. Generate callback test
5. Output callback code and test

**Tools**: `Write`, `Edit`

**Skills Integration**: dash-components Skill activates

**Validation**: Callback must have proper decorator and function signature

---

## Sub-Agent Definitions

### Sub-Agent File Format

```markdown
---
name: agent-name
specialization: Brief description
tools:
  - tool-1
  - tool-2
coordination: file-locking | queue-based | independent
context_isolation: true/false
---

# Sub-Agent: agent-name

## Specialization

Detailed description of what this agent does.

## Responsibilities

- Responsibility 1
- Responsibility 2
- Responsibility 3

## Coordination Strategy

Description of how this agent coordinates with others.

## Context Isolation

How context is managed for this agent.

## Invocation Patterns

When and how to invoke this agent.

## Examples

Example invocations.
```

---

### component-builder

**File**: `.claude/agents/component-builder.md`

**Specialization**: Autonomous UI component creation

**Tools**: `Write`, `Edit`, `Read`, `Bash` (for file locking)

**Coordination**: File locking
- Before creating/modifying component, check lock file
- Create lock: `{component-name}.lock`
- Release lock after completion

**Responsibilities**:
- Build reusable Dash components
- Write component tests
- Generate component documentation
- Apply theming and styling

**Context Isolation**: Moderate
- Shared: Project structure, component patterns, theming
- Isolated: Specific component implementation details

**Invocation Pattern**:
```
When user needs multiple components created in parallel:
Launch component-builder agent for each component
Each agent creates its component independently
File locking prevents conflicts
```

---

### data-pipeline

**File**: `.claude/agents/data-pipeline.md`

**Specialization**: Data infrastructure development

**Tools**: `Write`, `Edit`, `Read`, `Bash` (for database ops), `Grep`

**Coordination**: Queue-based
- Agents queue database operations
- Execute sequentially to avoid conflicts
- Use lock file for queue management

**Responsibilities**:
- Create data loaders
- Build transformation pipelines
- Write validators
- Optimize queries
- Set up caching

**Context Isolation**: High
- Shared: Database schemas, data contracts
- Isolated: Implementation details, query optimization

**Invocation Pattern**:
```
When building data infrastructure:
Launch data-pipeline agent
Agent creates loaders, transformers, validators
Coordinates database access via queue
```

---

### test-engineer

**File**: `.claude/agents/test-engineer.md`

**Specialization**: Comprehensive testing infrastructure

**Tools**: `Write`, `Edit`, `Read`, `Bash` (for running tests)

**Coordination**: Independent
- Test files are separate from implementation
- No conflicts expected
- Can run in parallel with other agents

**Responsibilities**:
- Write unit tests
- Create integration tests
- Build e2e test workflows
- Set up fixtures
- Configure CI/CD (later phase)

**Context Isolation**: Moderate
- Shared: Test patterns, fixtures
- Isolated: Specific test implementations

**Invocation Pattern**:
```
When comprehensive test coverage needed:
Launch test-engineer agent
Agent creates full test suite
Runs independently of other work
```

---

## Settings Configuration

### File: `.claude/settings.json`

**Structure**:
```json
{
  "version": "1.0.0",
  "project": {
    "name": "cc-dash-as-code",
    "description": "Spec-driven dashboard development with Claude Code"
  },
  "permissions": {
    "tools": {
      "allowed": [
        "Read",
        "Write",
        "Edit",
        "Bash",
        "Glob",
        "Grep",
        "Task"
      ],
      "restricted": []
    },
    "file_access": {
      "allowed_paths": [
        ".",
        "./specs",
        "./src",
        "./tests",
        "./docs",
        "./.claude"
      ],
      "denied_paths": [
        "./reference",
        "./venv",
        "./.git"
      ]
    }
  },
  "code_quality": {
    "formatter": "black",
    "linter": "ruff",
    "type_checker": "mypy",
    "test_framework": "pytest",
    "min_coverage": 80,
    "auto_format_on_save": false
  },
  "workflow": {
    "default_branch": "main",
    "feature_branch_pattern": "{number}-{feature-name}",
    "commit_message_format": "conventional-commits",
    "auto_checkpoint": false
  },
  "security": {
    "secret_scanning": true,
    "allowed_secret_patterns": [],
    "webhook_urls": []
  },
  "skills": {
    "enabled": true,
    "auto_activate": true,
    "token_budgets": {
      "level_1": 60,
      "level_2": 1000
    }
  }
}
```

**Validation**:
- JSON must be valid
- All paths in allowed_paths must exist
- Tool names must match available tools

---

## Skills Directory Placeholders

### `.claude/skills/development/`

**Purpose**: Placeholder for Development Skills (Spec 003)

**Action**: Create empty directory with README.md explaining this is populated in Spec 003

**README Content**:
```markdown
# Development Skills

This directory contains Development Skills that support building the Claude Code system.

Skills are defined in Spec 003: Agent Skills - Development.

Skills to be implemented (Spec 003):
- spec-kit-workflow
- claude-code-architecture
- research-synthesis

See specs/003-agent-skills-development/spec.md for details.
```

---

### `.claude/skills/production/`

**Purpose**: Placeholder for Production Skills (Spec 004)

**Action**: Create empty directory with README.md explaining this is populated in Spec 004

**README Content**:
```markdown
# Production Skills

This directory contains Production Skills that support dashboard developers.

Skills are defined in Spec 004: Agent Skills - Production.

Skills to be implemented (Spec 004):
- data-analysis
- plotly-viz
- dash-components
- accessibility-audit
- performance-optimizer

See specs/004-agent-skills-production/spec.md for details.
```

---

## Implementation Phases

### Phase 1: Directory Structure (1-2 hours)

**Tasks**:
1. Create `.claude/` directory
2. Create command category subdirectories
3. Create agents/ directory
4. Create skills/ directory with placeholders
5. Create `.claude/README.md` with overview

**Validation**:
- All directories exist
- README.md is present

---

### Phase 2: Spec Commands (4-6 hours)

**Tasks**:
1. Implement `/spec.create`
2. Implement `/spec.validate`
3. Implement `/spec.list`
4. Implement `/spec.show`
5. Implement `/spec.branch`
6. Test each command

**Validation**:
- All 5 commands execute successfully
- Test creating a new spec
- Test validating existing specs

---

### Phase 3: Workflow Commands (8-10 hours)

**Tasks**:
1. Implement `/workflow.observe`
2. Implement `/workflow.act`
3. Implement `/workflow.verify`
4. Implement `/workflow.loop`
5. Implement `/workflow.status`
6. Implement `/workflow.checkpoint`
7. Test EPIC cycle end-to-end

**Validation**:
- Full EPIC cycle (observe → act → verify → loop) works
- Status tracking functions correctly

---

### Phase 4: Utility Commands (4-6 hours)

**Tasks**:
1. Implement `/utils.test`
2. Implement `/utils.lint`
3. Implement `/utils.format`
4. Implement `/utils.check-deps`
5. Implement `/utils.commit`
6. Implement `/utils.diff`
7. Test all utilities

**Validation**:
- All utility commands execute
- Test with actual code files

---

### Phase 5: Dash Commands (3-4 hours)

**Tasks**:
1. Implement `/dash.component`
2. Implement `/dash.layout`
3. Implement `/dash.callback`
4. Test component generation

**Validation**:
- Generated components are valid Dash code
- Tests are created alongside components

---

### Phase 6: Sub-Agents (4-6 hours)

**Tasks**:
1. Define component-builder agent
2. Define data-pipeline agent
3. Define test-engineer agent
4. Test agent invocation
5. Test coordination strategies

**Validation**:
- Agents can be invoked
- Coordination works (file locking, queue)

---

### Phase 7: Settings & Configuration (2-3 hours)

**Tasks**:
1. Create settings.json
2. Validate JSON structure
3. Test settings are loaded by Claude Code
4. Document settings in README

**Validation**:
- settings.json is valid
- Permissions are enforced

---

### Phase 8: Integration Testing (4-6 hours)

**Tasks**:
1. Test all commands work together
2. Test EPIC workflow end-to-end
3. Test sub-agent coordination
4. Validate against Spec 002 requirements
5. Document any issues or limitations

**Validation**:
- All Spec 002 functional requirements are met
- Success criteria are achieved

---

## Testing Strategy

### Unit Testing (Command-Level)

**Approach**: Test each command in isolation

**Test Cases per Command**:
1. **Happy path**: Command executes successfully with valid inputs
2. **Invalid inputs**: Command handles errors gracefully
3. **Missing dependencies**: Command reports when required files/tools missing
4. **Output format**: Command output matches expected format

**Tools**: Manual testing initially, automated tests later if feasible

---

### Integration Testing (Workflow-Level)

**Approach**: Test command sequences

**Test Scenarios**:
1. **Full EPIC cycle**:
   - /workflow.observe → identifies task
   - /workflow.act → implements task
   - /workflow.verify → validates implementation
   - /workflow.loop → commits and continues

2. **Spec creation workflow**:
   - /spec.create → creates new spec
   - Edit spec.md manually
   - /spec.validate → validates spec
   - /spec.branch → creates git branch

3. **Component creation workflow**:
   - /dash.component → creates component
   - /utils.test → runs tests
   - /utils.format → formats code
   - /workflow.verify → full validation

**Validation**: Complete workflows must execute without errors

---

### Sub-Agent Testing

**Approach**: Test agent coordination

**Test Scenarios**:
1. **Parallel component creation**:
   - Launch 2 component-builder agents
   - Verify file locking prevents conflicts
   - Both components created successfully

2. **Data pipeline queue**:
   - Launch data-pipeline agent with multiple DB operations
   - Verify queue management works
   - Operations execute in order

3. **Independent test engineer**:
   - Launch test-engineer agent
   - Verify it runs independently
   - No conflicts with other agents

**Validation**: Agents coordinate correctly, no file conflicts

---

### Acceptance Testing (Spec 002 Requirements)

**Approach**: Validate against all FR-* and SC-* from Spec 002

**Coverage**:
- FR-001 to FR-100: All functional requirements
- SC-001 to SC-050: All success criteria

**Method**:
- Create checklist mapping each requirement to test case
- Execute tests
- Document pass/fail for each
- Address any failures

**Success Criteria**: 100% of requirements met

---

## Success Validation

### Functional Requirements (FR-*)

**Validation Method**: Manual testing with checklist

**Sample Validations**:
- FR-001: `/spec.create` creates new spec → Test by creating spec 006
- FR-008: `/workflow.observe` analyzes current state → Test on existing feature
- FR-018: `/utils.test` runs pytest → Test with sample test file
- FR-026: `/dash.component` creates component → Test component creation

**Goal**: All 100 functional requirements validated

---

### Success Criteria (SC-*)

**Validation Method**: Measurement and observation

**Sample Validations**:
- SC-001: Commands load <2s → Measure command startup time
- SC-005: Commands work together → Test EPIC workflow
- SC-015: Developers can create specs 40% faster → Observe spec creation time
- SC-030: 80% of developers use commands → Survey/observation (future)

**Goal**: Meet or exceed all success criteria targets

---

## Risks & Mitigation

### Risk 1: Command File Format Not Supported

**Mitigation**: Validate format with Claude Code documentation early

**Contingency**: Adjust format to match Claude Code requirements

---

### Risk 2: Sub-Agent Coordination Failures

**Mitigation**: Start with simple coordination (independent), add complexity gradually

**Contingency**: Document coordination requirements more explicitly

---

### Risk 3: Skills Directory Conflicts

**Mitigation**: Create clear placeholders with READMEs

**Contingency**: Coordinate with Spec 003/004 implementation

---

## Dependencies

### Internal Dependencies

- `specs/memory/constitution.md` - Required for /spec.validate
- `specs/templates/spec-template.md` - Required for /spec.create
- `specs/templates/plan-template.md` - Optional for /spec.plan (future)
- `specs/templates/tasks-template.md` - Optional for /spec.tasks (future)

### External Dependencies

- **Claude Code**: Must support custom commands via .claude/ directory
- **Git**: Required for /spec.branch, /workflow.checkpoint, /utils.commit
- **Python venv**: Required for /utils.* commands
- **Development tools**: pytest, black, ruff, mypy (already installed)

---

## Next Steps

After plan approval:

1. **Create tasks.md**: Break this plan into granular, actionable tasks
2. **Begin Phase 1**: Create directory structure
3. **Iterative implementation**: Complete each phase sequentially
4. **Continuous validation**: Test after each command/agent implementation
5. **Final integration test**: Validate all requirements met

---

**Plan Status**: Ready for tasks.md creation
**Estimated Duration**: 36-48 hours (5-7 days)
**Prerequisites**: Python environment set up ✅, All dependencies installed ✅
