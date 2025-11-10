# Specs Directory Structure

**Date**: 2025-11-10
**Status**: Reorganized from .specify/ to specs/

---

## Overview

All specification-related files are now consolidated in the `specs/` directory in the project root. This replaces the previous `.specify/` hidden directory approach.

---

## Directory Layout

```
specs/
├── README.md                          # Spec workflow guide
├── STRUCTURE.md                       # This file - directory overview
├── memory/
│   └── constitution.md                # Project principles and guidelines
├── templates/
│   ├── spec-template.md              # Feature specification template
│   ├── plan-template.md              # Implementation plan template
│   ├── tasks-template.md             # Task breakdown template
│   ├── checklist-template.md         # Review checklist template
│   └── agent-file-template.md        # Sub-agent definition template
├── research/
│   ├── agent-skills-integration-analysis.md    # Skills integration study
│   ├── claude-code-final-architecture.md       # Architecture guide
│   ├── complete-architecture-quick-reference.md # Quick reference
│   └── spec-revision-notes.md                  # Revision history
├── 001-dashboard-foundation/
│   └── spec.md                       # Foundation specification
└── 002-claude-code-commands-setup/
    └── spec.md                       # Claude Code setup specification
```

---

## Subdirectories

### `memory/`
**Purpose**: Persistent project knowledge

**Contents**:
- `constitution.md` - 10 core principles for development
  - Spec-first approach
  - Code quality standards (80% coverage)
  - Dashboard standards (WCAG 2.1 AA)
  - Testing requirements
  - Documentation standards

### `templates/`
**Purpose**: Reusable templates for specifications and planning

**Contents**:
- **spec-template.md** - Feature specification template following spec-kit methodology
- **plan-template.md** - Technical implementation plan template
- **tasks-template.md** - Task breakdown template with dependency tracking
- **checklist-template.md** - Review and acceptance checklist
- **agent-file-template.md** - Claude Code sub-agent definition template

### `research/`
**Purpose**: Research documents and architectural analysis

**Contents**:
- **agent-skills-integration-analysis.md** (29KB)
  - 20 web searches + chain-of-verification
  - Skills vs Commands vs Sub-Agents analysis
  - Two-process model (development vs production)
  - Progressive disclosure pattern
  - Complete architectural guide

- **claude-code-final-architecture.md** (12KB)
  - Commands, Sub-Agents, Skills architecture
  - MCP integration
  - Hooks and settings
  - Decision matrices

- **complete-architecture-quick-reference.md** (19KB)
  - Visual guides
  - Decision matrices
  - Example workflows
  - Skills directory structure

- **spec-revision-notes.md** (10KB)
  - History of spec revisions
  - What changed and why
  - Implementation status

### Specification Directories

Each specification gets its own directory:

**Format**: `NNN-feature-name/`

**Required**: `spec.md`

**Optional**:
- `plan.md` - Technical implementation plan
- `tasks.md` - Task breakdown
- `research.md` - Feature-specific research notes

---

## Specification Numbering

Specifications follow a structured numbering scheme:

| Range | Purpose |
|-------|---------|
| **001-099** | Foundation and infrastructure |
| **100-199** | Core dashboard features |
| **200-299** | Data integration and pipelines |
| **300-399** | Advanced features and optimization |
| **400-499** | Deployment and production |
| **500+** | Experimental and future features |

---

## Current Specifications

### 001-dashboard-foundation
**Status**: Draft
**Priority**: P1

Establishes project foundation:
- Directory structure
- Development environment
- Component library
- Testing infrastructure
- Deployment pipeline

### 002-claude-code-commands-setup
**Status**: Draft - Awaiting Review
**Priority**: P1

Claude Code configuration:
- Commands in 4 categories (spec/, workflow/, utils/, dash/)
- EPIC methodology (observe → act → verify → loop)
- Sub-agents (component-builder, data-pipeline, test-engineer)
- Agent Skills integration
- Hooks and automation

---

## Workflow

### Creating a New Specification

1. **Determine next feature number** based on category
2. **Create directory**: `specs/NNN-feature-name/`
3. **Copy template**: `cp specs/templates/spec-template.md specs/NNN-feature-name/spec.md`
4. **Fill in all sections**:
   - Overview
   - User Scenarios & Testing
   - Requirements (FR-NNN)
   - Success Criteria (SC-NNN)
   - Key Entities
   - Edge Cases
   - Clarifications
   - Dependencies
   - Implementation Phases
   - Review Checklist
5. **Request review**

### Using Commands (Once Implemented)

```bash
/spec.create "Feature description"
```

Auto-generates:
- Feature number
- Spec directory
- Populated template
- Git branch

---

## Integration with Claude Code

When spec 002 is implemented, Claude Code commands will:

1. **Read from specs/** - All commands reference `specs/` directory
2. **Create in specs/** - New specs created in `specs/NNN-feature-name/`
3. **Validate against constitution** - Uses `specs/memory/constitution.md`
4. **Use templates** - References `specs/templates/`
5. **Store research** - Feature research goes in `specs/research/`

---

## Migration Notes

### What Changed

**Before** (`.specify/` approach):
```
.specify/
├── memory/constitution.md
├── specs/
├── templates/
└── scripts/
```

**After** (`specs/` approach):
```
specs/
├── memory/
├── templates/
├── research/
└── NNN-feature-name/
```

### Benefits

1. **Discoverability**: `specs/` is more obvious than hidden `.specify/`
2. **Consolidation**: All spec-related files in one place
3. **Co-location**: Research documents alongside specs
4. **Standard naming**: Follows common conventions (specs/ not .specify/)
5. **Simplicity**: Flatter structure, easier to navigate

### Breaking Changes

- Old path `.specify/specs/` → New path `specs/`
- Commands need updating to reference `specs/`
- Documentation references need updating

---

## References

- **README**: See `specs/README.md` for detailed workflow
- **Constitution**: See `specs/memory/constitution.md` for principles
- **Templates**: See `specs/templates/` for all templates
- **Research**: See `specs/research/` for architectural analysis

---

**Last Updated**: 2025-11-10
**Maintained By**: Project Team
