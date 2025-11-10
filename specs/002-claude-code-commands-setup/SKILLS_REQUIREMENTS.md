# Skills Functional Requirements
## FR-061 to FR-090

These requirements supplement the core functional requirements (FR-001 to FR-060) with Agent Skills specifications.

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
