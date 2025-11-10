# Additional Clarifications
## Q6-Q10: Skills and Hybrid Workflow

These clarifications supplement Q1-Q5 in the main spec with detailed explanations of Agent Skills and the hybrid workflow architecture.

---

## Q6: What's the difference between Skills and Commands?

**A**: Skills and Commands serve fundamentally different purposes and are complementary, not competing.

### Commands (User-Invoked)

**Invocation**: User explicitly types command (e.g., `/workflow:implement`)

**Purpose**: Provide workflow structure and sequence

**Example**:
```bash
User: /workflow:implement Create sales dashboard

Command does:
1. Sets up TDD workflow (tests first)
2. Structures implementation process
3. Enforces quality gates (testing, linting)
4. Manages git operations
```

**Characteristic**: Synchronous, predictable, user-controlled

---

### Skills (Model-Invoked)

**Invocation**: Claude automatically activates based on context

**Purpose**: Provide domain expertise and methodology

**Example**:
```bash
# Same task, but showing Skills

User: /workflow:implement Create sales dashboard

Skills auto-activate:
- dash-components (detecting "dashboard")
- plotly-viz (will create charts)
- accessibility-audit (ensure WCAG compliance)

Skills provide:
- Component structure patterns
- Chart selection guidance
- Accessibility requirements
```

**Characteristic**: Asynchronous, context-driven, automatic

---

### Integration Example

**Complete workflow showing both**:

```
User: /workflow:implement Task 5 - Create bar chart component

1. COMMAND `/workflow:implement` provides STRUCTURE:
   ✓ Read task from tasks.md
   ✓ Create test file first (TDD)
   ✓ Create implementation file
   ✓ Run verification
   ✓ Commit if successful

2. SKILLS provide EXPERTISE (auto-activated):
   ✓ plotly-viz: "For bar chart, use plotly.express.bar()..."
   ✓ plotly-viz: "Ensure WCAG 2.1 AA: contrast ratio 4.5:1..."
   ✓ dash-components: "Structure component with dcc.Graph()..."
   ✓ accessibility-audit: "Add aria-label: 'Bar chart showing...'"

3. RESULT: Command completes with Skill-enhanced quality
   ✓ Test file created: test_sales_chart.py
   ✓ Implementation: sales_chart.py (accessible, optimized)
   ✓ Tests pass, coverage 85%
   ✓ WCAG compliant
```

**Key Insight**: Command says "WHAT to do" (implement task), Skills say "HOW to do it well" (with accessibility, best practices, optimization).

---

### Decision Guide

**Use Commands when you want to**:
- Trigger a specific workflow
- Follow a defined sequence
- Have explicit control

**Use Skills when you want to**:
- Provide reusable knowledge
- Activate based on context
- Scale expertise across many tasks

**In our setup**: We use BOTH together for maximum effectiveness.

---

## Q7: What's the difference between Skills and Sub-Agents?

**A**: Skills and Sub-Agents have different architectural patterns and use cases.

### Comparison Table

| Aspect | Skills | Sub-Agents |
|--------|--------|------------|
| **Context** | Shared with main agent | Isolated context window |
| **Invocation** | Automatic (context-based) | Manual/delegated |
| **Purpose** | Domain knowledge | Task execution |
| **Parallelism** | No (sequential) | Yes (true parallel work) |
| **Tool Calls** | 3-4x more (progressive) | Fewer (dedicated context) |
| **Best For** | Reusable expertise | Self-contained work |
| **Example** | `plotly-viz` | `component-builder` |

---

### Skills: Shared Context, Progressive Knowledge

**Pattern**:
```
Main Agent Context (200K tokens)
├── User conversation
├── Task information
├── Skill: spec-kit-workflow (Level 2 loaded: +800 tokens)
├── Skill: plotly-viz (Level 2 loaded: +800 tokens)
└── Skill: accessibility-audit (activated when needed)
```

**Characteristics**:
- Skills share context with main agent
- Progressive disclosure (load incrementally)
- More tool calls (reading skill files)
- Knowledge benefits all subsequent tasks

**Use When**:
- Expertise is reusable across tasks
- Context sharing important
- Sequential work preferred

---

### Sub-Agents: Isolated Context, Parallel Execution

**Pattern**:
```
Main Agent Context
└── Delegates task

    Sub-Agent: component-builder (Isolated 200K context)
    ├── Task: "Create 3 dashboard components"
    ├── Skills available in Sub-Agent context too!
    │   ├── dash-components
    │   └── plotly-viz
    └── Works independently

    Main Agent continues other work in parallel
```

**Characteristics**:
- Sub-Agents have separate context windows
- Can work in true parallel
- Less context noise (focused on task)
- Complete task then return results

**Use When**:
- Task is self-contained
- Parallel execution helps
- Context isolation beneficial

---

### Working Together

**Scenario**: Build dashboard with 5 components + data pipeline

**Option 1: Main Agent + Skills** (Sequential)
```
Main Agent:
1. Create component 1 (plotly-viz & dash-components Skills help)
2. Create component 2 (same Skills help)
3. Create component 3 (same Skills help)
4. Create data pipeline (data-analysis Skill helps)
5. Create component 4 (Skills help)
6. Create component 5 (Skills help)

Time: ~90 minutes (sequential)
```

**Option 2: Main Agent + Sub-Agents + Skills** (Parallel)
```
Main Agent:
1. Launch component-builder Sub-Agent: "Create components 1-5"
   → Sub-Agent uses dash-components and plotly-viz Skills
2. Launch data-pipeline Sub-Agent: "Create data loaders"
   → Sub-Agent uses data-analysis Skill
3. While Sub-Agents work, prepare integration

Sub-Agents complete independently, then integrate

Time: ~35 minutes (parallel)
```

**Best Approach**: Use Sub-Agents for parallel work, and Skills enhance BOTH main agent AND Sub-Agents.

---

### Example: Skills Working in Sub-Agent

```python
# Sub-Agent: component-builder

# Task: Create sales chart component

# Skills activate WITHIN Sub-Agent context:
# - plotly-viz (chart creation)
# - dash-components (component structure)
# - accessibility-audit (WCAG compliance)

# Result: Sub-Agent creates high-quality component using Skills
```

**Key Insight**: Skills are available everywhere (main agent and Sub-Agents). Sub-Agents provide parallel capacity, Skills provide expertise.

---

## Q8: How does progressive disclosure actually work?

**A**: Progressive disclosure is a three-level loading pattern that keeps context lean while providing deep expertise.

### The Three Levels Explained

---

#### Level 1: Metadata Only (~50 tokens)

**When Loaded**: At Claude Code startup (before any user interaction)

**Content**: YAML frontmatter from SKILL.md
```yaml
---
name: data-analysis
description: Load, analyze, and generate insights from datasets including CSV, JSON, Parquet, SQL databases. Use when exploring data, performing statistical analysis, identifying trends, or creating data transformations for dashboards. Automatically invoked when user mentions data exploration, EDA, statistics, or data quality.
allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
---
```

**Token Count**: ~50 tokens (name ~2, description ~40, allowed-tools ~8)

**Purpose**:
- Help Claude discover which skills exist
- Match skill descriptions to current context
- Decide which skills to activate

**With 20 Skills**: 20 × 50 = 1,000 tokens at startup (minimal overhead)

---

#### Level 2: Core Instructions (~800 tokens)

**When Loaded**: Claude determines skill is relevant to current task

**Content**: Main SKILL.md content (after frontmatter)
```markdown
# Data Analysis Skill

## Quick Start
1. Load data using pandas or SQL
2. Perform exploratory data analysis (EDA)
3. Generate statistical summaries
4. Identify data quality issues
5. Suggest appropriate visualizations

## Core Workflow

### Loading Data
[Pandas patterns, SQL connection patterns...]

### Exploratory Data Analysis
[EDA process: shape, types, nulls, describe, correlations...]

### Data Quality Checks
[Missing values, outliers, duplicates, consistency...]

### Visualization Recommendations
[Chart selection based on data types...]

## Common Patterns
[Typical workflows...]
```

**Token Count**: ~800 tokens (500-1000 acceptable range)

**Purpose**:
- Provide essential methodology
- Cover 80% of common use cases
- Enable Claude to work effectively

**Loading Trigger**:
```
User: Analyze sales data

→ "Analyze" and "data" keywords match data-analysis description
→ Claude loads data-analysis Level 2
→ +800 tokens added to context
→ Claude now has EDA methodology available
```

---

#### Level 3: Reference Materials (Variable size)

**When Loaded**: Claude needs specific deep knowledge

**Content**: Separate reference files in skill directory
```
data-analysis/
├── SKILL.md                    # Levels 1 & 2
├── STATISTICAL_METHODS.md      # ~2000 tokens (Level 3)
├── DATA_QUALITY.md             # ~1500 tokens (Level 3)
├── VISUALIZATION_GUIDE.md      # ~1800 tokens (Level 3)
└── scripts/
    └── analyze.py              # Loaded when executed (Level 3)
```

**Token Count**: Variable per file (1000-5000+ tokens)

**Purpose**:
- Provide deep expertise for specific scenarios
- Detailed reference documentation
- Complex examples and templates

**Loading Trigger**:
```
Claude (internal): User needs hypothesis testing guidance

→ Claude uses Read tool: data-analysis/STATISTICAL_METHODS.md
→ +2000 tokens added to context
→ Now has detailed statistical methods available
→ Provides comprehensive guidance to user
```

**Important**: Level 3 files load **only when Claude explicitly reads them**, not automatically.

---

### Token Usage Comparison

**Scenario**: Session working with data, creating charts, checking accessibility

**Without Progressive Disclosure** (Load everything upfront):
```
At startup:
- All 8 Skills, full content loaded
- data-analysis: +3000 tokens
- plotly-viz: +3500 tokens
- dash-components: +3200 tokens
- accessibility-audit: +4000 tokens
- (and 4 more...)
Total: ~25,000 tokens before any work

During session:
- All knowledge immediately available
- No additional loading needed

Total session: 25,000 tokens (high context pressure)
```

**With Progressive Disclosure** (Our approach):
```
At startup:
- All 8 Skills, Level 1 only
- 8 × 50 = 400 tokens

During session:
- data-analysis activates (Level 2): +800 tokens
- plotly-viz activates (Level 2): +800 tokens
- accessibility-audit activates (Level 2): +800 tokens
- One Level 3 reference needed: +2000 tokens

Total session: 400 + 2400 + 2000 = 4,800 tokens

Savings: 25,000 - 4,800 = 20,200 tokens (81% reduction)
```

**Benefits**:
1. Can support 100+ skills (5,000 tokens at startup vs. impossible with full loading)
2. Context stays lean (more room for code, conversation)
3. Still get deep expertise when needed
4. Scales to large knowledge bases

**Trade-off**:
- More tool calls (Claude reads skill files)
- Slight latency for Level 2/3 loading (~1-2 seconds)
- Worth it for the context efficiency

---

### How Claude Decides What to Load

**Level 1 → Level 2 Decision**:
```
1. User input or file context contains keywords
2. Claude checks Level 1 descriptions (all loaded)
3. Finds matching keywords (e.g., "analyze data" matches data-analysis)
4. Activates skill: Reads SKILL.md content
5. Level 2 now available for this skill
```

**Level 2 → Level 3 Decision**:
```
1. Claude is using Level 2 knowledge
2. Encounters scenario needing deeper expertise
3. Claude explicitly uses Read tool on reference file
4. Level 3 content loaded
5. Provides detailed guidance
```

**Important**: All loading decisions are made by Claude based on context, not by user commands.

---

## Q9: What Skills should I create for my use case?

**A**: Skills depend on whether you're building the system (development) or using it (production).

### Development Skills (Building the System)

If you're setting up Claude Code for a new domain, create these types of skills:

#### 1. Methodology Skill

**Purpose**: Guide the development approach

**Example**: `spec-kit-workflow`
- Specification writing methodology
- Planning and task breakdown
- Quality gates and validation

**When to Create**: You have a defined development methodology to encode

---

#### 2. Architecture Skill

**Purpose**: Decisions about system structure

**Example**: `claude-code-architecture`
- When to use Commands vs Skills vs Sub-Agents
- Directory structure patterns
- Configuration best practices

**When to Create**: You're building something with architectural choices

---

#### 3. Domain Research Skill

**Purpose**: Analyze reference materials

**Example**: `research-synthesis`
- Extract patterns from reference repos
- Analyze documentation
- Create implementation guides

**When to Create**: You frequently reference existing implementations

---

### Production Skills (Using the System)

If you're building dashboards (or whatever your domain is), create these types:

#### 1. Data Processing Skill

**Purpose**: How to work with data

**Example**: `data-analysis`
- Data loading patterns
- Analysis methodology
- Quality checking

**When to Create**: Domain involves data processing

---

#### 2. Visualization Skill

**Purpose**: How to create visualizations

**Example**: `plotly-viz`
- Chart type selection
- Accessibility compliance
- Best practices

**When to Create**: Domain involves visual output

---

#### 3. Component/Framework Skill

**Purpose**: Framework-specific patterns

**Example**: `dash-components`
- Component structure
- Framework-specific patterns (callbacks, layouts)
- State management

**When to Create**: You use a specific framework extensively

---

#### 4. Quality Assurance Skill

**Purpose**: Automated quality checking

**Example**: `accessibility-audit`
- Compliance checking (WCAG, etc.)
- Automated validation
- Common issue detection

**When to Create**: You have specific quality standards to enforce

---

#### 5. Performance Skill

**Purpose**: Optimization guidance

**Example**: `performance-optimizer`
- Bottleneck patterns
- Optimization strategies
- Performance targets

**When to Create**: Performance is critical in your domain

---

### Creating Custom Skills

**Template**:
```
my-custom-skill/
├── SKILL.md                      # Required
│   └── YAML frontmatter + core content
├── REFERENCE_GUIDE.md            # Optional (Level 3)
├── EXAMPLES.md                   # Optional (Level 3)
├── scripts/                      # Optional (Level 3)
└── templates/                    # Optional (Level 3)
```

**SKILL.md Template**:
```markdown
---
name: my-custom-skill
description: Clear description with keywords that trigger activation. Mention use cases, when to use, what problem it solves. Keep to 40-60 tokens.
allowed-tools: [Read, Write, Edit, Bash]
---

# My Custom Skill

## Quick Start
[3-5 step workflow]

## Core Patterns
[Essential knowledge for 80% of use cases]

## Common Scenarios
[Examples of when this skill helps]

## Integration
[How this skill works with others]
```

**Best Practices**:
1. **Clear Description**: Include keywords that match when skill should activate
2. **Focused Scope**: One skill = one domain of expertise
3. **Progressive Disclosure**: Keep SKILL.md under 1000 tokens, detailed stuff in Level 3
4. **Examples**: Show activation scenarios
5. **Integration**: Document how skill works with Commands, other Skills

---

### Our Dashboard Development Skills

**Development Phase** (3 skills):
- `spec-kit-workflow` - How to write specs
- `claude-code-architecture` - How to structure .claude/
- `research-synthesis` - How to analyze references

**Production Phase** (5 skills):
- `data-analysis` - How to process data
- `plotly-viz` - How to create charts
- `dash-components` - How to build components
- `accessibility-audit` - How to ensure WCAG compliance
- `performance-optimizer` - How to optimize performance

**Total**: 8 skills covering full lifecycle

---

## Q10: How do Skills work with the hybrid workflow?

**A**: Skills enhance BOTH processes in the hybrid workflow architecture.

### Recap: Two-Process Model

**Process 1: Spec-Kit** (Planning)
- Constitution → Specify → Plan → Tasks → [Approval] → tasks.md

**Process 2: Claude Code** (Execution)
- For each task: Research → Implement → Verify → Next

**Handoff**: tasks.md file (frozen after approval)

See `specs/WORKFLOW.md` for complete documentation.

---

### Skills in Process 1: Spec-Kit Planning

**Commands**: `/spec:*`

**Skills Active**:
- `spec-kit-workflow` (development)
- `claude-code-architecture` (development)
- `research-synthesis` (development)

**Example Flow**:

```bash
# Step 1: Create Specification
User: /spec:specify Create sales analytics dashboard

Command /spec:specify:
- Creates specs/NNN-sales-dashboard/spec.md
- Prompts for user stories, requirements, success criteria

Skill spec-kit-workflow activates:
- Provides spec template structure
- Suggests requirement categories (FR-NNN format)
- Validates completeness against constitution
- Examples of well-written user stories

Result: Complete spec.md following spec-kit methodology

---

# Step 2: Create Implementation Plan
User: /spec:plan

Command /spec:plan:
- Creates specs/NNN-sales-dashboard/plan.md
- Prompts for technical approach, architecture

Skills activate:
- spec-kit-workflow: Plan template and structure
- claude-code-architecture: Decides if Custom components or standard
- plotly-viz: Recommends chart types based on requirements
- data-analysis: Suggests data pipeline approach

Result: Comprehensive plan.md with justified decisions

---

# Step 3: Generate Task Breakdown
User: /spec:tasks

Command /spec:tasks:
- Creates specs/NNN-sales-dashboard/tasks.md
- Breaks plan into actionable tasks

Skill spec-kit-workflow activates:
- Task breakdown methodology
- Dependency analysis
- Success criteria per task
- File structure planning

Result: Actionable tasks.md with clear dependencies

---

# Step 4: Review & Approve
User: /spec:review

Command /spec:review:
- Runs approval checklist
- Validates completeness

Skill spec-kit-workflow activates:
- Constitutional alignment check
- Completeness validation
- Quality standards check

Result: Spec approved, tasks.md frozen

[HANDOFF TO PROCESS 2]
```

**Key Point**: Development Skills guide the planning process, ensuring high-quality specs.

---

### Skills in Process 2: Claude Code Execution

**Commands**: `/workflow:*`

**Skills Active**:
- `data-analysis` (production)
- `plotly-viz` (production)
- `dash-components` (production)
- `accessibility-audit` (production)
- `performance-optimizer` (production)

**Example Flow**:

```bash
# Task 1: Create data loader
User: /workflow:implement Task 1

Command /workflow:implement:
- Reads Task 1 from tasks.md
- Sets up TDD workflow
- Creates test and implementation files

Skills activate:
- data-analysis: Data loading patterns (CSV, SQL)
- research-synthesis: Examines existing loaders in codebase

Result:
- tests/unit/test_sales_loader.py
- src/data/sales_loader.py

---

# Verify Task 1
User: /workflow:verify

Command /workflow:verify:
- Runs pytest
- Runs linting (ruff, black, mypy)
- Checks coverage

Skills activate:
- data-analysis: Validates data handling patterns

Result: Tests pass, 87% coverage ✓

---

# Task 2: Create bar chart component
User: /workflow:implement Task 2

Command /workflow:implement:
- Reads Task 2 from tasks.md
- TDD workflow

Skills activate:
- plotly-viz: Chart creation, accessibility
- dash-components: Component structure, callbacks
- data-analysis: Data transformation for visualization

Result:
- tests/unit/test_sales_chart.py
- src/components/sales_chart.py (accessible, WCAG compliant)

---

# Verify Task 2
User: /workflow:verify

Command /workflow:verify:
- Runs pytest
- Runs linting
- Accessibility check

Skills activate:
- accessibility-audit: WCAG 2.1 AA compliance check
- performance-optimizer: Rendering performance check

Result:
- Tests pass ✓
- Coverage: 84% ✓
- WCAG compliant ✓
- Render time: 0.3s ✓

---

# Continue through all tasks...
User: /workflow:next

[Process repeats for remaining tasks]
```

**Key Point**: Production Skills provide domain expertise during implementation, ensuring quality.

---

### Skills Across Both Processes

**Same Infrastructure, Different Content**:

| Process | Commands | Development Skills | Production Skills |
|---------|----------|-------------------|-------------------|
| **Spec-Kit** | `/spec:*` | ✓ Active | ○ Referenced in planning |
| **Claude Code** | `/workflow:*` | ○ Not needed | ✓ Active |

**Example of Cross-Process Benefit**:

```
Planning (Spec-Kit):
- plotly-viz Skill consulted for chart recommendations in plan.md
- Level 1 + 2 loaded to suggest chart types
- Recommendations documented in plan

Execution (Claude Code):
- Same plotly-viz Skill activates during implementation
- Level 2 already understood from planning
- Provides consistent guidance

Result: Planning and execution use same expertise source
```

---

### Handoff Point: tasks.md

**After Approval**:
- tasks.md is frozen (no scope changes)
- Minor edits allowed (typos, clarifications)
- Skills continue to enhance execution

**During Execution**:
- Skills provide "how" for each task's "what"
- Commands structure the workflow
- Agentic corrections within task scope (max 3 verify attempts)

**Feedback Loop** (rare):
- If task technically impossible → Escalate
- Return to Spec-Kit process
- Update spec, regenerate tasks
- Skills help with revision

---

### Summary: Skills' Role in Hybrid Workflow

**In Planning**:
- Development Skills guide spec creation
- Production Skills inform technical decisions
- Result: High-quality, implementable plans

**In Execution**:
- Production Skills provide domain expertise
- Development Skills dormant (not needed)
- Result: High-quality, accessible, performant code

**Throughout**:
- Progressive disclosure keeps context lean
- Auto-activation means seamless integration
- Same Skills benefit multiple phases

**The Benefit**: Comprehensive expertise available exactly when and where needed, across both processes.

---

## Summary of Q6-Q10

**Q6**: Skills vs Commands - Complementary (knowledge vs structure)
**Q7**: Skills vs Sub-Agents - Different patterns (shared vs isolated context)
**Q8**: Progressive disclosure - Three-level loading for efficiency
**Q9**: What Skills to create - Development + Production based on domain
**Q10**: Skills in hybrid workflow - Enhance both planning and execution

**Together**: Complete understanding of how Agent Skills integrate into spec-driven dashboard development.

**Next**: Implementation Phases detail the 8-week plan to build this system, including all Skills.
