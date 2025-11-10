# Complete Claude Code Architecture - Quick Reference

**For**: Spec-driven Plotly Dash Development
**Date**: 2025-11-10

---

## The Four Extension Mechanisms

| Mechanism | Type | Invocation | Purpose | Example |
|-----------|------|------------|---------|---------|
| **Commands** | Workflow | User types `/command` | Repeatable workflows | `/workflow.act` |
| **Skills** | Knowledge | Auto (model-decided) | Domain expertise | `plotly-viz` skill |
| **Sub-Agents** | Worker | Manual or auto | Parallel task execution | `component-builder` |
| **Hooks** | Automation | Event-triggered | Automatic actions | PostToolUse formatting |

---

## Two-Process Model

### Process 1: Development (Meta - We Build the System)

```
┌─────────────────────────────────────────────────────────────┐
│  DEVELOPMENT PROCESS (Building Claude Code Setup)           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Skills (Auto-loaded when relevant):                        │
│  • spec-kit-workflow      → Spec creation guidance          │
│  • claude-code-setup      → Config architecture decisions   │
│  • research-synthesis     → Analyzing reference repos       │
│                                                              │
│  Commands (User executes):                                  │
│  • /spec.create          → Create new specifications        │
│  • /spec.validate        → Check spec completeness          │
│  • /workflow.observe     → Analyze what needs building      │
│  • /workflow.act         → Build commands/agents/skills     │
│  • /workflow.verify      → Test our setup                   │
│                                                              │
│  Sub-Agents (Parallel work):                                │
│  • research-agent        → Analyze cloned repos             │
│  • documentation-agent   → Generate docs                    │
│  • validation-agent      → Check consistency                │
│                                                              │
│  Output: Working Claude Code setup for dashboard dev        │
└─────────────────────────────────────────────────────────────┘
```

### Process 2: Production (User Builds Dashboards)

```
┌─────────────────────────────────────────────────────────────┐
│  PRODUCTION PROCESS (Using Our Setup to Build Dashboards)   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Skills (Auto-loaded when relevant):                        │
│  • data-analysis         → Statistical analysis, EDA        │
│  • plotly-viz            → Chart generation                 │
│  • dash-components       → Component patterns               │
│  • accessibility-audit   → WCAG compliance                  │
│  • performance-optimizer → Speed optimization               │
│                                                              │
│  Commands (User executes):                                  │
│  • /spec.create          → Create dashboard spec            │
│  • /workflow.observe     → Analyze requirements             │
│  • /workflow.act         → Build dashboard features         │
│  • /workflow.verify      → Test dashboard                   │
│  • /dash.component       → Generate Dash components         │
│                                                              │
│  Sub-Agents (Parallel work):                                │
│  • component-builder     → Create UI components             │
│  • data-pipeline         → Build ETL pipelines              │
│  • test-engineer         → Write comprehensive tests        │
│                                                              │
│  Output: Production-ready Plotly Dash dashboard             │
└─────────────────────────────────────────────────────────────┘
```

---

## Skills Integration with EPIC Workflow

### Observe Phase → Skills Auto-Load for Analysis

```
User: /workflow.observe

Claude's Internal Process:
1. Read specification file
   ↓
   ✓ spec-kit-workflow skill activates
   ↓
   Provides context on spec structure

2. Examine existing codebase
   ↓
   ✓ dash-patterns skill activates (if Dash code exists)
   ✓ data-analysis skill activates (if data files found)
   ↓
   Provides patterns and conventions

3. Identify next task
   ↓
   Returns task recommendation based on spec + skills knowledge
```

### Act Phase → Skills Auto-Load for Implementation

```
User: /workflow.act Create sales dashboard with bar chart

Claude's Internal Process:
1. Write tests first (TDD)
   ↓
   ✓ testing-patterns skill activates
   ↓
   Provides TDD guidance

2. Create dashboard layout
   ↓
   ✓ dash-components skill activates
   ↓
   Provides component structure patterns

3. Generate bar chart
   ↓
   ✓ plotly-viz skill activates
   ↓
   Provides chart creation code

4. Ensure accessibility
   ↓
   ✓ accessibility-audit skill activates
   ↓
   Checks WCAG compliance

Output: Complete dashboard with tests
```

### Verify Phase → Skills Auto-Load for Validation

```
User: /workflow.verify

Claude's Internal Process:
1. Run tests
   ↓
   ✓ testing-patterns skill (coverage analysis)

2. Check accessibility
   ↓
   ✓ accessibility-audit skill (WCAG validation)

3. Performance check
   ↓
   ✓ performance-optimizer skill (bottleneck analysis)

Output: Verification report
```

---

## Progressive Disclosure in Action

### Example: `data-analysis` Skill

**Level 1: Startup (50 tokens)**
```yaml
name: data-analysis
description: Load, analyze, and generate insights from datasets...
```
*Loaded for ALL sessions - helps Claude decide when to use*

**Level 2: Activated (800 tokens)**
```markdown
# Data Analysis Skill

## Quick Start
1. Load data using pandas or SQL
2. Perform exploratory data analysis
3. Generate statistical summaries
...
```
*Loaded only when Claude detects data analysis context*

**Level 3: As Needed (3000+ tokens)**
```
STATISTICAL_METHODS.md    → When doing statistics
DATA_QUALITY.md           → When checking data quality
scripts/analyze.py        → When running analysis
```
*Loaded only when specific sub-task requires it*

**Total Context Impact**:
- Without Skill: 0 tokens (no guidance, Claude guesses)
- Skill at startup: 50 tokens (discovery enabled)
- Skill activated: 850 tokens (methodology loaded)
- Full Skill: 3850 tokens (only if needed)

**Compare to MCP** (loading everything upfront):
- GitHub MCP alone: 50,000+ tokens
- 3 MCP servers: 150,000+ tokens
- Context window 200k: 75% consumed before any work!

**Skills approach**: Start with 50 tokens × 20 skills = 1,000 tokens total

---

## Decision Matrix

### When to Use Each Extension Mechanism

#### Use **Commands** when:
- ✅ User needs to initiate specific workflow
- ✅ Workflow has clear steps to follow
- ✅ Action should be explicit and traceable
- **Example**: `/spec.create`, `/workflow.verify`

#### Use **Skills** when:
- ✅ Knowledge is reusable across many tasks
- ✅ Expertise should activate automatically
- ✅ Context needs to stay efficient
- **Example**: `plotly-viz`, `data-analysis`

#### Use **Sub-Agents** when:
- ✅ Task is large and self-contained
- ✅ Parallel execution would help
- ✅ Context isolation is beneficial
- **Example**: `component-builder` building 5 components

#### Use **Hooks** when:
- ✅ Action should happen automatically on event
- ✅ No user intervention needed
- ✅ Deterministic behavior desired
- **Example**: Auto-format on file write

---

## Complete Example: User Creates Dashboard

```
┌────────────────────────────────────────────────────────┐
│ User Request: Build sales analytics dashboard         │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│ Step 1: Create Specification                           │
├────────────────────────────────────────────────────────┤
│ User: /spec.create "Sales analytics dashboard"        │
│                                                        │
│ Command execution:                                     │
│  → /spec.create (user-invoked)                        │
│  → spec-kit-workflow skill (auto-invoked)             │
│                                                        │
│ Result: .specify/specs/003-sales-dashboard/spec.md    │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│ Step 2: Observe Requirements                           │
├────────────────────────────────────────────────────────┤
│ User: /workflow.observe                                │
│                                                        │
│ Command execution:                                     │
│  → /workflow.observe (user-invoked)                   │
│  → spec-kit-workflow skill (reads spec)               │
│  → dash-patterns skill (examines code)                │
│                                                        │
│ Result: "Need to create: data loader, bar chart,      │
│          filter component"                             │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│ Step 3: Implement Features                             │
├────────────────────────────────────────────────────────┤
│ User: /workflow.act Create data loader and bar chart  │
│                                                        │
│ Command execution:                                     │
│  → /workflow.act (user-invoked)                       │
│                                                        │
│ For data loader:                                       │
│  → data-analysis skill (auto-invoked)                 │
│     ↳ Provides: pandas patterns, error handling       │
│  → testing-patterns skill (TDD guidance)              │
│                                                        │
│ For bar chart:                                         │
│  → plotly-viz skill (auto-invoked)                    │
│     ↳ Provides: Plotly Express code, customization    │
│  → accessibility-audit skill (WCAG check)             │
│                                                        │
│ Hooks trigger:                                         │
│  → PostToolUse: Black formatting                      │
│  → PostToolUse: Ruff linting                          │
│                                                        │
│ Result: src/data/loaders.py                           │
│         src/components/sales_chart.py                 │
│         tests/unit/test_loaders.py                    │
│         tests/unit/test_sales_chart.py                │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│ Step 4: Verify Implementation                          │
├────────────────────────────────────────────────────────┤
│ User: /workflow.verify                                 │
│                                                        │
│ Command execution:                                     │
│  → /workflow.verify (user-invoked)                    │
│  → testing-patterns skill (coverage analysis)         │
│  → accessibility-audit skill (WCAG validation)        │
│  → performance-optimizer skill (speed check)          │
│                                                        │
│ Tests run:                                             │
│  ✓ pytest --cov (85% coverage)                        │
│  ✓ mypy (type check passed)                           │
│  ✓ ruff (linting passed)                              │
│  ✓ WCAG AA (accessibility passed)                     │
│                                                        │
│ Hooks trigger:                                         │
│  → PostToolUse: Update coverage badge                 │
│                                                        │
│ Result: All checks passed ✓                           │
└────────────────────────────────────────────────────────┘
                          ↓
┌────────────────────────────────────────────────────────┐
│ Step 5: Loop - Next Task                               │
├────────────────────────────────────────────────────────┤
│ User: /workflow.loop                                   │
│                                                        │
│ Command execution:                                     │
│  → /workflow.loop (user-invoked)                      │
│  → spec-kit-workflow skill (check requirements)       │
│  → git-workflow skill (create checkpoint)             │
│                                                        │
│ Git operations:                                        │
│  ✓ git add src/ tests/                                │
│  ✓ git commit -m "Add data loader and sales chart"   │
│                                                        │
│ Next task presented:                                   │
│  "Add date filter component to dashboard"             │
│                                                        │
│ Result: Progress checkpointed, ready for next task    │
└────────────────────────────────────────────────────────┘
```

---

## Key Insights

### 1. Skills Are Invisible to Users
Users never explicitly invoke Skills - they just type commands and Skills activate automatically.

### 2. Skills Enhance Commands
Commands provide structure, Skills provide expertise:
- Command: "What to do" (`/workflow.act`)
- Skill: "How to do it well" (`plotly-viz` provides chart code)

### 3. Progressive Disclosure Scales
- 20 Skills = 1,000 tokens at startup
- vs. 3 MCP servers = 150,000 tokens
- Can have 100+ Skills without context issues

### 4. Both Processes Need Skills
- Development process: `spec-kit-workflow`, `claude-code-setup`
- Production process: `data-analysis`, `plotly-viz`, `dash-components`

### 5. Skills + Commands + Sub-Agents + Hooks = Complete System
- **Commands**: User-initiated workflows
- **Skills**: Auto-loaded knowledge
- **Sub-Agents**: Parallel task workers
- **Hooks**: Automatic event responses

---

## Skills We Need to Create

### Development Skills (Priority 1)
```
.claude/skills/
├── spec-kit-workflow/       ← Guide spec creation
│   ├── SKILL.md
│   ├── SPEC_TEMPLATE.md
│   └── PLAN_TEMPLATE.md
│
├── claude-code-setup/       ← Config decisions
│   ├── SKILL.md
│   ├── DECISION_MATRIX.md
│   └── ARCHITECTURE.md
│
└── research-synthesis/      ← Analyze repos
    ├── SKILL.md
    └── METHODS.md
```

### Production Skills (Priority 2)
```
.claude/skills/
├── data-analysis/           ← Data processing
│   ├── SKILL.md
│   ├── STATISTICAL_METHODS.md
│   └── scripts/analyze.py
│
├── plotly-viz/              ← Visualization
│   ├── SKILL.md
│   ├── CHART_TYPES.md
│   └── templates/
│
├── dash-components/         ← Components
│   ├── SKILL.md
│   ├── PATTERNS.md
│   └── examples/
│
├── accessibility-audit/     ← WCAG checks
│   ├── SKILL.md
│   └── CHECKLIST.md
│
└── performance-optimizer/   ← Speed
    ├── SKILL.md
    └── STRATEGIES.md
```

---

## Next Steps for Spec Revision

1. **Add Skills Section** to spec 002
   - Explain Skills vs Commands vs Sub-Agents
   - Show progressive disclosure
   - List Skills for both processes

2. **Update Command Descriptions**
   - Show Skills integration
   - Provide concrete examples

3. **Add Skills to Success Criteria**
   - Skill activation rates
   - Context efficiency metrics
   - Progressive disclosure effectiveness

4. **Create Skills Implementation Plan**
   - Phase 1: Development Skills
   - Phase 2: Core Production Skills
   - Phase 3: Extended Production Skills

---

**Status**: Analysis complete, ready for spec revision
**Date**: 2025-11-10
**Verification Method**: 20 web searches + chain-of-verification
