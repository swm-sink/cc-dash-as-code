# Specification Index

**Last Updated**: 2025-11-10
**Status**: Active Development

---

## Implementation Order

Specs are numbered sequentially (preserves git history) but implemented by priority:

| Spec | Name | Status | Priority | Implements |
|------|------|--------|----------|------------|
| **001** | Dashboard Foundation | Draft | **P2** | **Phase 5** |
| **002** | Claude Code Commands Setup | Draft | **P1** | **Phase 1** |
| **003** | Agent Skills - Development | Draft | **P1** | **Phase 2** |
| **004** | Agent Skills - Production | Draft | **P2** | **Phase 3** |
| **005** | MCP Integration | Draft | **P3** | **Phase 4** |

**⚠️ Note**: Implement in priority order (002 → 003 → 004 → 005 → 001), not numerical order.

---

## Spec Details

### 001-dashboard-foundation

**Purpose**: Establish project foundation, directory structure, and development environment

**Priority**: P2 (Implement after Claude Code setup - Phase 5)

**Note**: Originally spec 001, keeps number for git history. Implement AFTER 002-004.

**Key Features**:
- Project directory structure
- Development environment setup
- Component library structure
- Testing infrastructure
- Deployment pipeline basics

**Dependencies**:
- 002-claude-code-commands-setup (needs commands)
- 003-agent-skills-development (needs dev Skills)
- 004-agent-skills-production (provides prod Skills)

**Blocks**: None (enables dashboard work)

---

### 002-claude-code-commands-setup

**Purpose**: Configure Claude Code with custom commands, sub-agents, and hooks for spec-driven development

**Priority**: P1 (Must implement FIRST - required for all development)

**Key Features**:
- Spec-Kit commands (`/spec:*`) - Specify → Plan → Tasks workflow
- Claude Code commands (`/workflow:*`) - Research → Implement → Verify workflow
- Utility commands (`/utils:*`) - Testing, linting, formatting
- Specialized sub-agents (component-builder, data-pipeline, test-engineer)
- Hooks for automation (PostToolUse formatting, PreToolUse validation)
- Settings and permissions configuration

**Dependencies**: None (foundation)

**Blocks**: 003, 004, 001 (all development needs this setup)

**Outputs**:
- `.claude/commands/spec/*.md` - 5 commands
- `.claude/commands/workflow/*.md` - 5 commands
- `.claude/commands/utils/*.md` - 6 commands
- `.claude/agents/*.md` - 3 sub-agents
- `.claude/settings.json`
- `CLAUDE.md` - User guide

---

### 003-agent-skills-development

**Purpose**: Create Agent Skills for the development process (us building the system)

**Priority**: P1 (Implement SECOND - needed for effective development)

**Key Features**:
- `spec-kit-workflow` skill - Guides specification creation following spec-kit methodology
- `claude-code-architecture` skill - Provides expertise on Commands/Skills/Sub-Agents architecture
- `research-synthesis` skill - Analyzes reference repositories and documentation

**Dependencies**:
- 002-claude-code-commands-setup (needs `.claude/skills/` directory structure)

**Blocks**: None (can implement in parallel with 004)

**Outputs**:
- `.claude/skills/development/spec-kit-workflow/` - Complete SKILL.md + references
- `.claude/skills/development/claude-code-architecture/` - Complete SKILL.md + references
- `.claude/skills/development/research-synthesis/` - Complete SKILL.md + references

---

### 004-agent-skills-production

**Purpose**: Create Agent Skills for production use (dashboard developers building dashboards)

**Priority**: P2 (Implement THIRD - needed before dashboard work)

**Key Features**:
- `data-analysis` skill - Statistical analysis, EDA, data quality checking
- `plotly-viz` skill - Chart generation, accessibility, responsive design
- `dash-components` skill - Component patterns, callback architecture
- `accessibility-audit` skill - WCAG 2.1 AA compliance validation
- `performance-optimizer` skill - Bottleneck detection, caching strategies

**Dependencies**:
- 002-claude-code-commands-setup (needs `.claude/skills/` directory structure)

**Blocks**: 001-dashboard-foundation (needed for actual dashboard work)

**Outputs**:
- `.claude/skills/production/data-analysis/` - Complete SKILL.md + references + scripts
- `.claude/skills/production/plotly-viz/` - Complete SKILL.md + references + templates
- `.claude/skills/production/dash-components/` - Complete SKILL.md + references + examples
- `.claude/skills/production/accessibility-audit/` - Complete SKILL.md + checklist + scripts
- `.claude/skills/production/performance-optimizer/` - Complete SKILL.md + strategies

---

### 005-mcp-integration

**Purpose**: Integrate Model Context Protocol servers for data access

**Priority**: P3 (Optional - can use file-based data initially, implement FOURTH if needed)

**Key Features**:
- MCP server configuration in `.claude/mcp_config.json`
- PostgreSQL MCP server for database access
- Filesystem MCP server for CSV/JSON/Parquet files
- REST API MCP server for external integrations
- Search MCP server for documentation

**Dependencies**:
- 002-claude-code-commands-setup (needs `.claude/` directory)
- 004-agent-skills-production (Skills use MCP for data access)

**Blocks**: None (optional enhancement)

**Outputs**:
- `.claude/mcp_config.json` - Complete MCP configuration
- `docs/MCP_SETUP.md` - Setup and usage guide


---

## Dependency Graph

```
[002-claude-code-commands-setup] (P1, Phase 1)
              ↓
    ┌─────────┴─────────┐
    ↓                   ↓
[003-agent-skills-dev] [004-agent-skills-prod] (P1/P2, Phase 2/3)
    (parallel)          ↓
                   [005-mcp-integration] (P3, Phase 4)
                        ↓
              [001-dashboard-foundation] (P2, Phase 5)
```

**Implementation Order**: 002 → 003 → 004 → 005 (optional) → 001

**Critical Path**: 002 → 003 → 004 → 001 (minimum for dashboard development)

**Optional**: 005 (MCP) can be added anytime after 004

---

## Implementation Phases

### Phase 1: Core Commands Setup (Week 1-2)

**Implement**: 002-claude-code-commands-setup

**Deliverables**:
- `/spec:*` commands working
- `/workflow:*` commands working
- `/utils:*` commands working
- Sub-agents defined
- Hooks configured

**Success Criteria**:
- Can create specs using `/spec:specify`
- Can generate tasks using `/spec:tasks`
- Can execute tasks using `/workflow:*`
- All commands pass validation

---

### Phase 2: Development Skills (Week 3)

**Implement**: 003-agent-skills-development

**Deliverables**:
- `spec-kit-workflow` skill complete
- `claude-code-architecture` skill complete
- `research-synthesis` skill complete

**Success Criteria**:
- Skills auto-invoke during planning
- Progressive disclosure works (3-level loading)
- Context usage optimized (<5% overhead per skill)

---

### Phase 3: Production Skills (Week 4-5)

**Implement**: 004-agent-skills-production

**Deliverables**:
- `data-analysis` skill complete
- `plotly-viz` skill complete
- `dash-components` skill complete
- `accessibility-audit` skill complete
- `performance-optimizer` skill complete

**Success Criteria**:
- Skills auto-invoke during execution
- Each skill has complete reference documentation
- Skills integrate with commands seamlessly

---

### Phase 4: MCP Integration (Optional, Week 6)

**Implement**: 005-mcp-integration

**Deliverables**:
- MCP configuration complete
- PostgreSQL server configured
- Filesystem server configured
- Integration with Skills tested

**Success Criteria**:
- Skills can access data through MCP
- Database queries work
- File operations work

---

### Phase 5: Dashboard Foundation (Week 7)

**Implement**: 001-dashboard-foundation

**Deliverables**:
- Complete directory structure
- Development environment working
- Component library scaffolded
- Testing infrastructure operational

**Success Criteria**:
- Can create new dashboard project
- All dependencies install correctly
- Tests run successfully

---

## Status Tracking

### Completed

- [x] Specs reorganization (moved to `specs/` directory)
- [x] Research on Agent Skills integration
- [x] Workflow architecture defined
- [x] Spec index created

### In Progress

- [ ] Spec 002 revision (integrate workflow architecture, Agent Skills)
- [ ] Spec 003 creation (development skills)
- [ ] Spec 004 creation (production skills)
- [ ] Spec 005 creation (MCP integration)
- [ ] Spec 001 revision (update dependencies, mark as Phase 5)

### Pending

- [ ] Implementation of Phase 1
- [ ] Implementation of Phase 2
- [ ] Implementation of Phase 3
- [ ] Implementation of Phase 4 (optional)
- [ ] Implementation of Phase 5

---

## Quick Reference

### Find a Spec

- **Commands & Sub-Agents**: 002-claude-code-commands-setup
- **Development Skills**: 003-agent-skills-development
- **Production Skills**: 004-agent-skills-production
- **MCP Setup**: 005-mcp-integration
- **Project Structure**: 001-dashboard-foundation

### Implementation Order

1. ✅ First: Commands (002)
2. ✅ Second: Dev Skills (003)
3. ✅ Third: Prod Skills (004)
4. ⚠️ Optional: MCP (005)
5. ✅ Fifth: Dashboard Foundation (001)

### Dependencies

- **001**: Requires 002, 003, 004 (implement last)
- **002**: None (start here)
- **003**: Requires 002
- **004**: Requires 002
- **005**: Requires 002, 004 (optional)

---

**Next Action**: Revise spec 002 to integrate hybrid workflow architecture, then create specs 003-005, then update spec 001.

**Version**: 1.0.0
