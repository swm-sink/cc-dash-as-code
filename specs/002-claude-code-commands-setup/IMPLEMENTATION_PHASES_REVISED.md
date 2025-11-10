# Implementation Phases (Revised)
## 8-Phase Plan with Agent Skills Integration

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
