# Agent Skills Architecture
## Comprehensive Integration for Spec-Driven Dashboard Development

---

## Overview

Agent Skills are **model-invoked domain expertise** that automatically enhance Claude Code's capabilities without explicit user invocation. Skills form the third pillar of our architecture alongside Commands (user-invoked workflows) and Sub-Agents (task-isolated workers).

**Key Characteristics**:
- **Auto-Activation**: Skills load automatically based on context matching
- **Progressive Disclosure**: Three-level loading (metadata → core → references)
- **Dual Purpose**: Development Skills (building the system) + Production Skills (building dashboards)
- **Complementary**: Work seamlessly with Commands, Sub-Agents, and MCP servers

**Why Skills Matter**:
Without Skills, every command would need to include all domain knowledge, resulting in massive context usage and redundant information. Skills enable Claude to access deep expertise on-demand, keeping context lean while providing comprehensive guidance.

---

## 1. Skills vs Commands vs Sub-Agents

### Architectural Distinction

| Aspect | Commands | Skills | Sub-Agents |
|--------|----------|--------|------------|
| **Invocation** | User-explicit (`/workflow:act`) | Model-automatic (context-triggered) | User/model-delegated |
| **Purpose** | Workflow structure | Domain knowledge | Task execution |
| **Context** | Main agent | Shared with main agent | Isolated window |
| **Loading** | Immediate (synchronous) | Progressive (3 levels) | Full agent spawn |
| **Token Cost** | ~100-500 tokens | ~50 → 800 → variable | Separate budget |
| **When to Use** | Repeated workflows | Reusable expertise | Parallel work |
| **Example** | `/spec:specify` | `plotly-viz` | `component-builder` |

### Decision Matrix

**Use Commands when**:
- User needs to explicitly trigger a workflow
- Workflow has clear start/end points
- Sequence of steps must be followed
- Examples: Creating specs, running tests, committing code

**Use Skills when**:
- Domain expertise is reusable across many tasks
- Knowledge should activate automatically when relevant
- Progressive disclosure can save context
- Examples: Chart selection guidance, accessibility checking, statistical analysis

**Use Sub-Agents when**:
- Task is self-contained and can run independently
- Parallel execution would speed up work significantly
- Task benefits from isolated context (less noise)
- Examples: Building multiple components, comprehensive testing, data pipeline creation

### Integration Example

**Scenario**: User creates a dashboard with data visualization

```bash
# User invokes Command
/workflow:implement Create sales dashboard with date filtering

# What happens:
1. Command `/workflow:implement` executes (user-invoked)
   → Provides workflow structure (TDD, testing, validation)

2. Skills auto-activate (model-invoked):
   → `dash-components` (detecting "dashboard")
   → `plotly-viz` (detecting "visualization")
   → `data-analysis` (detecting "sales" data)

3. Sub-Agent may be launched (if complex):
   → `component-builder` for parallel UI work
   → Uses Skills within its isolated context

Result: Command provides STRUCTURE, Skills provide KNOWLEDGE, Sub-Agent provides CAPACITY
```

---

## 2. Progressive Disclosure Pattern

### The Three Levels

Progressive disclosure enables Claude to maintain a vast knowledge base without overloading context. Skills load incrementally as needed.

#### Level 1: Metadata Only (Startup)

**When Loaded**: At Claude Code initialization
**Size**: ~50 tokens per skill
**Purpose**: Enable skill discovery and matching

**Format** (YAML frontmatter in SKILL.md):
```yaml
name: data-analysis
description: Load, analyze, and generate insights from datasets including CSV, JSON, Parquet, SQL databases. Use when exploring data, performing statistical analysis, identifying trends, or creating data transformations for dashboards. Automatically invoked when user mentions data exploration, EDA, statistics, or data quality.
allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
```

**With 20 skills**: ~1000 tokens total at startup (minimal overhead)

---

#### Level 2: Core Instructions (Skill Activated)

**When Loaded**: Claude determines skill is relevant to current task
**Size**: ~800 tokens
**Purpose**: Provide essential methodology and patterns

**Format** (SKILL.md content):
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
- **CSV/JSON**: Use pandas.read_csv(), pandas.read_json()
- **SQL**: Use mcp__postgres or psycopg2
- **Parquet**: Use pandas.read_parquet()

### Exploratory Data Analysis
1. Check shape: df.shape
2. Check types: df.dtypes
3. Check nulls: df.isnull().sum()
4. Summary stats: df.describe()
5. Correlations: df.corr()

### Data Quality Checks
- Missing values (MCAR, MAR, MNAR)
- Outliers (IQR, z-score methods)
- Duplicates
- Type consistency
- Range validation

### Visualization Recommendations
[Chart selection logic based on data characteristics]
```

**Activation Triggers**:
- User mentions: "analyze", "data", "statistics", "EDA", "trends"
- Commands reading data files
- When examining datasets

---

#### Level 3: Reference Materials (On-Demand)

**When Loaded**: Skill execution requires specific deep knowledge
**Size**: Variable (can be 2000-5000+ tokens)
**Purpose**: Detailed guidance for specific scenarios

**Format** (Reference files in skill directory):
```
.claude/skills/data-analysis/
├── SKILL.md                      # Levels 1 & 2
├── STATISTICAL_METHODS.md        # ~2000 tokens
├── DATA_QUALITY.md               # ~1500 tokens
├── VISUALIZATION_GUIDE.md        # ~1800 tokens
└── scripts/
    └── analyze.py                # Loaded when executed
```

**Example Reference File** (STATISTICAL_METHODS.md):
```markdown
# Statistical Methods Reference

## Descriptive Statistics
[Detailed explanations of mean, median, mode, std dev, variance...]

## Inferential Statistics
[Hypothesis testing, confidence intervals, p-values...]

## Correlation Analysis
[Pearson, Spearman, Kendall correlations...]

## Regression Analysis
[Linear, logistic, polynomial regression...]

## Time Series Analysis
[Trend, seasonality, ARIMA models...]
```

**Level 3 files load**:
- Only when needed (Claude requests specific knowledge)
- Via Read tool calls
- As context permits

---

### Progressive Disclosure Benefits

**Comparison: Skills vs MCP**

| Approach | Startup Cost | Runtime Access | Scalability |
|----------|--------------|----------------|-------------|
| **MCP** (Load all upfront) | 50,000+ tokens | Immediate | Limited (~10 servers) |
| **Skills** (Progressive) | 1,000 tokens | 2-3 tool calls | High (100+ skills) |

**Example**:
- 20 Skills at startup: 1,000 tokens
- 5 Skills activate in session: +4,000 tokens (5 × 800)
- 2 Skills need Level 3: +3,500 tokens
- **Total**: 8,500 tokens

vs.

- 5 MCP servers loaded: 50,000 tokens
- All tools available immediately
- **Total**: 50,000 tokens

**Trade-off**: Skills use 3-4x more tool calls but 6x less context

---

## 3. Development Skills

These Skills support **us** (developers) in building the Claude Code dashboard development system.

### 3.1 spec-kit-workflow

**Metadata** (Level 1):
```yaml
name: spec-kit-workflow
description: Guide for creating specifications following GitHub's spec-kit approach. Use when creating or validating feature specifications, planning technical implementations, or breaking down work into tasks. Covers Constitution → Specify → Plan → Tasks workflow. Automatically invoked when working with spec.md, plan.md, or tasks.md files.
allowed-tools: [Read, Write, Edit, Bash(git:*)]
```

**Purpose**: Provide methodology for spec-driven development following Spec-Kit standard

**Activation Triggers**:
- User runs `/spec:*` commands
- Reading/writing spec.md, plan.md, tasks.md files
- Mentions "specification", "requirements", "user stories"

**Directory Structure**:
```
.claude/skills/spec-kit-workflow/
├── SKILL.md                      # Levels 1 & 2
├── SPEC_TEMPLATE.md              # Complete spec template
├── PLAN_TEMPLATE.md              # Technical plan template
├── TASKS_TEMPLATE.md             # Task breakdown template
├── CONSTITUTION_GUIDE.md         # Alignment checking
├── examples/
│   ├── example-spec.md           # Reference specification
│   ├── example-plan.md           # Reference plan
│   └── example-tasks.md          # Reference tasks
└── validation/
    └── checklist.md              # Spec validation checklist
```

**SKILL.md Outline** (Level 2):
```markdown
# Spec-Kit Workflow Skill

## Overview
Spec-driven development methodology from GitHub's spec-kit

## The Four Phases

### 1. Constitution
- Project principles and guidelines
- Located in specs/memory/constitution.md
- Defines quality standards, tech stack, patterns

### 2. Specify (spec.md)
- User stories with acceptance scenarios
- Functional requirements (FR-NNN)
- Success criteria (SC-NNN)
- Edge cases
- NO implementation details
- NO time estimates

### 3. Plan (plan.md)
- Technical approach
- Architecture decisions
- Component breakdown
- Technology choices
- Testing strategy

### 4. Tasks (tasks.md)
- Actionable task list
- Dependencies resolved
- Success criteria per task
- Files to create/modify listed
- Becomes frozen after approval

## Spec Template Structure
[Details on required sections...]

## Validation Checklist
[Completeness checks...]

## Common Patterns
[Examples of well-written specs...]
```

**Example Activation**:
```
User: /spec:specify Create authentication system

1. Command `/spec:specify` runs
2. `spec-kit-workflow` Skill activates (detecting spec creation)
3. Level 2 loads: Template structure and guidelines
4. User writes spec with Skill guidance
5. Level 3 loads on-demand: examples/example-spec.md for reference
6. Skill ensures all required sections present
```

---

### 3.2 claude-code-architecture

**Metadata** (Level 1):
```yaml
name: claude-code-architecture
description: Expert knowledge of Claude Code's architecture including Commands, Sub-Agents, Skills, and Hooks. Use when designing .claude/ directory structure, choosing between extension mechanisms, troubleshooting configuration, or understanding Claude Code best practices. Automatically invoked when working with .claude/ directory.
allowed-tools: [Read, Write, Edit, Glob]
```

**Purpose**: Provide deep expertise on Claude Code architecture and extension mechanisms

**Activation Triggers**:
- Working with `.claude/` directory
- Creating commands, sub-agents, or skills
- Mentions "claude code", "commands", "sub-agents"
- Configuration troubleshooting

**Directory Structure**:
```
.claude/skills/claude-code-architecture/
├── SKILL.md                      # Levels 1 & 2
├── COMMANDS_GUIDE.md             # Command creation patterns
├── SUBAGENTS_GUIDE.md            # Sub-agent patterns
├── SKILLS_GUIDE.md               # Skills creation (meta!)
├── HOOKS_GUIDE.md                # Hook configuration
├── DECISION_MATRIX.md            # Choose mechanism
├── reference/
│   ├── claude-code-final-architecture.md  # From research
│   └── complete-architecture-quick-reference.md
└── examples/
    ├── example-command.md
    ├── example-subagent.md
    └── example-skill/
```

**SKILL.md Outline** (Level 2):
```markdown
# Claude Code Architecture Skill

## Quick Reference

### When to Use What

**Commands** (/category:action):
- User-invoked workflows
- Explicit structure and sequence
- Examples: /spec:specify, /workflow:implement

**Skills** (auto-activate):
- Domain knowledge
- Progressive disclosure
- Examples: data-analysis, plotly-viz

**Sub-Agents** (task-isolated):
- Parallel execution
- Self-contained work
- Examples: component-builder, test-engineer

**Hooks** (event-triggered):
- Automatic actions
- Tool call events
- Examples: PostToolUse formatting

## Command Creation

### Format (.md with YAML frontmatter)
```yaml
---
description: Short description for help
allowed-tools: [Read, Write, Edit]
argument-hint: [required-arg] [optional-arg]
---

# Prompt content here
```

### Naming Convention
- Use namespacing: /category:action
- Categories: spec, workflow, utils
- Lowercase, hyphens for multi-word

## Sub-Agent Creation
[Patterns for sub-agents...]

## Skills Creation
[Meta: How to create Skills...]

## Settings Configuration
[settings.json structure...]
```

**Example Activation**:
```
User: Should I create a Command or Skill for data analysis?

1. Claude detects "Command or Skill" decision question
2. `claude-code-architecture` Skill activates
3. Level 2 loads: Decision matrix
4. Skill provides: "Use Skill (reusable knowledge, auto-activates)"
5. If user proceeds, Level 3 loads: SKILLS_GUIDE.md
6. Complete guidance for creating data-analysis Skill
```

---

### 3.3 research-synthesis

**Metadata** (Level 1):
```yaml
name: research-synthesis
description: Analyze reference implementations, documentation, and codebases to extract best practices and patterns. Use when researching new technologies, analyzing cloned repositories, synthesizing documentation, or creating implementation guidance. Automatically invoked when examining reference code or documentation.
allowed-tools: [Read, Grep, Glob, WebFetch]
```

**Purpose**: Extract patterns and best practices from reference materials

**Activation Triggers**:
- Researching technologies or frameworks
- Analyzing reference repositories
- Reading documentation
- Creating implementation guides

**Directory Structure**:
```
.claude/skills/research-synthesis/
├── SKILL.md                      # Levels 1 & 2
├── ANALYSIS_METHODS.md           # Research techniques
├── PATTERN_EXTRACTION.md         # Identifying patterns
├── DOCUMENTATION_GUIDE.md        # Creating docs from research
└── templates/
    ├── research-report.md
    └── implementation-guide.md
```

**SKILL.md Outline** (Level 2):
```markdown
# Research Synthesis Skill

## Research Process

### 1. Discovery Phase
- Identify relevant sources
- Clone reference repositories
- Gather documentation

### 2. Analysis Phase
- Code pattern extraction
- API design analysis
- Architecture understanding
- Best practices identification

### 3. Synthesis Phase
- Pattern documentation
- Implementation recommendations
- Example creation
- Integration guidance

## Analysis Techniques

### Code Analysis
- Structure examination (Glob for patterns)
- Implementation search (Grep for specific code)
- Dependency analysis
- Design pattern identification

### Documentation Analysis
- API surface documentation
- Configuration patterns
- Usage examples extraction
- Common pitfalls identification

## Output Formats
- Research reports
- Implementation guides
- Pattern libraries
- Example collections
```

**Example Activation**:
```
User: Research how Plotly Dash handles callbacks

1. User request triggers research task
2. `research-synthesis` Skill activates
3. Level 2 loads: Research process and techniques
4. Skill guides: Use Grep to find callback patterns
5. Skill guides: Extract common patterns
6. Level 3 loads: PATTERN_EXTRACTION.md for detailed methods
7. Creates implementation guide from findings
```

---

## 4. Production Skills

These Skills support **dashboard developers** (end users) building dashboards with our system.

### 4.1 data-analysis

**Metadata** (Level 1):
```yaml
name: data-analysis
description: Load, analyze, and generate insights from datasets including CSV, JSON, Parquet, SQL databases. Use when exploring data, performing statistical analysis, identifying trends, or creating data transformations for dashboards. Automatically invoked when user mentions data exploration, EDA, statistics, or data quality.
allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
```

**Purpose**: Provide statistical analysis and data exploration expertise

**Activation Triggers**:
- Loading or analyzing datasets
- Mentions "data", "analyze", "statistics", "EDA", "trends"
- Working with CSV, JSON, Parquet, SQL files
- Data quality checking

**Directory Structure**:
```
.claude/skills/data-analysis/
├── SKILL.md                      # Levels 1 & 2
├── STATISTICAL_METHODS.md        # ~2000 tokens
├── DATA_QUALITY.md               # ~1500 tokens
├── VISUALIZATION_GUIDE.md        # ~1800 tokens
├── scripts/
│   ├── analyze.py                # Basic analysis script
│   ├── quality_check.py          # Data quality validation
│   └── transform.py              # Common transformations
└── examples/
    ├── eda-example.py            # Complete EDA workflow
    └── sample-analysis.ipynb     # Jupyter notebook example
```

**SKILL.md Outline** (Level 2):
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
```python
# CSV/JSON
import pandas as pd
df = pd.read_csv('data.csv')

# SQL (via MCP)
# Use mcp__postgres tool

# Parquet
df = pd.read_parquet('data.parquet')
```

### Exploratory Data Analysis
```python
# Shape and structure
print(df.shape)
print(df.dtypes)
print(df.info())

# Missing values
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# Correlations
print(df.corr())
```

### Data Quality Checks
- Missing values (MCAR, MAR, MNAR)
- Outliers (IQR method, z-score)
- Duplicates
- Type consistency
- Range validation

### Visualization Recommendations

**Continuous variable**: histogram, box plot, violin plot
**Categorical variable**: bar chart, pie chart
**Continuous vs Continuous**: scatter plot, line chart
**Categorical vs Continuous**: box plot, violin plot
**Time series**: line chart, area chart
**Distributions**: histogram, density plot

## Common Patterns
[Typical analysis workflows...]

## Integration with Plotly
[How to pass insights to plotly-viz Skill...]
```

**Example Activation**:
```
User: /workflow:implement Analyze sales data and create dashboard

1. Command `/workflow:implement` runs
2. `data-analysis` Skill activates (detecting "analyze sales data")
3. Level 2 loads: EDA workflow and quality checks
4. Skill guides through data loading and analysis
5. User requests specific statistical test
6. Level 3 loads: STATISTICAL_METHODS.md
7. Skill provides detailed guidance on hypothesis testing
8. Analysis complete, passes insights to plotly-viz Skill
```

---

### 4.2 plotly-viz

**Metadata** (Level 1):
```yaml
name: plotly-viz
description: Generate appropriate Plotly visualizations based on data characteristics. Use when creating charts, graphs, or interactive visualizations. Automatically invoked when user requests dashboards, charts, plots, or data visualization. Ensures accessibility (WCAG 2.1 AA) and responsive design.
allowed-tools: [Read, Write, Edit]
```

**Purpose**: Provide chart creation expertise with accessibility compliance

**Activation Triggers**:
- Creating visualizations or charts
- Mentions "chart", "graph", "plot", "visualization", "dashboard"
- Working with Plotly or Dash code
- Accessibility checking for visualizations

**Directory Structure**:
```
.claude/skills/plotly-viz/
├── SKILL.md                      # Levels 1 & 2
├── CHART_TYPES.md                # ~2500 tokens - All chart types
├── ACCESSIBILITY.md              # ~1800 tokens - WCAG compliance
├── THEMING.md                    # ~1200 tokens - Consistent styling
├── INTERACTIVITY.md              # ~1500 tokens - Hover, click, zoom
├── templates/
│   ├── bar_chart.py
│   ├── line_chart.py
│   ├── scatter_plot.py
│   ├── heatmap.py
│   ├── pie_chart.py
│   └── [other chart templates]
└── examples/
    ├── accessible-dashboard.py   # WCAG 2.1 AA compliant example
    └── interactive-charts.py     # Interactivity examples
```

**SKILL.md Outline** (Level 2):
```markdown
# Plotly Visualization Skill

## Chart Selection Guide

### Based on Data Type

**One continuous variable**:
- Histogram (distribution)
- Box plot (distribution with outliers)
- Violin plot (distribution with density)

**One categorical variable**:
- Bar chart (counts or aggregates)
- Pie chart (proportions, max 5-7 categories)

**Continuous vs Continuous**:
- Scatter plot (relationship)
- Line chart (time series or ordered)
- Bubble chart (3 variables)

**Categorical vs Continuous**:
- Bar chart (comparison)
- Box plot (distribution comparison)
- Violin plot (detailed distribution)

**Multivariate**:
- Heatmap (correlation matrix)
- Scatter matrix (pairwise relationships)
- Parallel coordinates (high-dimensional)

### Chart Creation Pattern

```python
import plotly.express as px

# Basic pattern
fig = px.[chart_type](
    data_frame=df,
    x='column_x',
    y='column_y',
    color='category_column',  # Optional grouping
    title='Chart Title',
    labels={'column_x': 'Display Name'}
)

# Apply accessibility
fig.update_layout(
    font=dict(size=14),  # Readable font size
    plot_bgcolor='white',  # High contrast
)

# Add ARIA labels (handled by dash-components Skill)
```

## Accessibility Requirements (WCAG 2.1 AA)

### Color Contrast
- Text: 4.5:1 ratio minimum
- Large text: 3:1 ratio minimum
- Use colorblind-friendly palettes

### Non-Color Information
- Don't rely on color alone
- Use patterns, labels, markers

### Keyboard Navigation
- All interactive elements accessible via keyboard
- Focus indicators visible

### Screen Reader Support
- Descriptive titles and labels
- ARIA labels for complex charts
- Alt text for chart images

## Plotly Express vs Graph Objects

**Use Plotly Express when**:
- Quick, simple charts
- Standard chart types
- Minimal customization

**Use Graph Objects when**:
- Complex, custom layouts
- Fine-grained control
- Multiple subplot types

## Common Patterns
[Chart creation examples...]
```

**Example Activation**:
```
User: /workflow:implement Create bar chart showing sales by region

1. Command `/workflow:implement` runs
2. `plotly-viz` Skill activates (detecting "bar chart")
3. Level 2 loads: Chart selection and creation patterns
4. Skill provides: Bar chart template with accessibility
5. User wants custom styling
6. Level 3 loads: THEMING.md and CHART_TYPES.md
7. Complete bar chart created with WCAG 2.1 AA compliance
```

---

### 4.3 dash-components

**Metadata** (Level 1):
```yaml
name: dash-components
description: Create reusable Plotly Dash components following best practices. Use when building dashboard layouts, interactive controls, or custom components. Automatically invoked when user mentions components, callbacks, layouts, or Dash-specific features.
allowed-tools: [Read, Write, Edit]
```

**Purpose**: Provide Dash component architecture and callback patterns

**Activation Triggers**:
- Creating Dash components or layouts
- Mentions "component", "callback", "layout", "dash"
- Working with Dash application code
- Interactive dashboard features

**Directory Structure**:
```
.claude/skills/dash-components/
├── SKILL.md                      # Levels 1 & 2
├── COMPONENT_PATTERNS.md         # ~2000 tokens
├── CALLBACK_ARCHITECTURE.md      # ~2200 tokens
├── LAYOUT_GUIDE.md               # ~1500 tokens
├── STATE_MANAGEMENT.md           # ~1800 tokens
├── templates/
│   ├── basic_component.py
│   ├── filter_component.py
│   ├── table_component.py
│   └── chart_component.py
└── examples/
    ├── complete_dashboard.py
    └── callback_patterns.py
```

**SKILL.md Outline** (Level 2):
```markdown
# Dash Components Skill

## Component Creation Pattern

```python
import dash
from dash import html, dcc, Input, Output, State

def create_filter_component(id_prefix='filter'):
    """Reusable filter component with date range and dropdown"""
    return html.Div([
        html.Label('Date Range:'),
        dcc.DatePickerRange(
            id=f'{id_prefix}-date-range',
            start_date='2024-01-01',
            end_date='2024-12-31'
        ),

        html.Label('Category:'),
        dcc.Dropdown(
            id=f'{id_prefix}-category',
            options=[{'label': c, 'value': c} for c in categories],
            multi=True
        )
    ], className='filter-component')
```

## Callback Architecture

### Basic Callback
```python
@app.callback(
    Output('output-id', 'children'),
    Input('input-id', 'value')
)
def update_output(input_value):
    return f'You selected: {input_value}'
```

### Multiple Inputs/Outputs
```python
@app.callback(
    [Output('chart', 'figure'),
     Output('table', 'data')],
    [Input('filter-date', 'start_date'),
     Input('filter-date', 'end_date'),
     Input('filter-category', 'value')]
)
def update_dashboard(start_date, end_date, categories):
    filtered_df = filter_data(df, start_date, end_date, categories)

    fig = create_chart(filtered_df)
    table_data = filtered_df.to_dict('records')

    return fig, table_data
```

### State Management
```python
@app.callback(
    Output('data-store', 'data'),
    Input('load-button', 'n_clicks'),
    State('data-store', 'data'),
    prevent_initial_call=True
)
def load_data(n_clicks, stored_data):
    # Load and cache data
    return new_data
```

## Layout Patterns

### Responsive Grid
```python
app.layout = html.Div([
    # Header
    html.Div([
        html.H1('Dashboard Title'),
    ], className='header'),

    # Filters (left sidebar)
    html.Div([
        create_filter_component(),
    ], className='sidebar'),

    # Main content
    html.Div([
        dcc.Graph(id='main-chart'),
        dcc.Graph(id='secondary-chart'),
    ], className='main-content'),
], className='dashboard-container')
```

## Best Practices

### Component Design
- Keep components pure (no side effects)
- Use type hints
- Document props clearly
- Write unit tests

### Callback Optimization
- Use prevent_initial_call when appropriate
- Minimize callback chain length
- Cache expensive computations
- Use dcc.Store for shared state

### Performance
- Lazy loading for large datasets
- Pagination for tables
- Downsampling for time series
- Virtual scrolling for long lists

## Common Patterns
[Examples of common dashboard layouts...]
```

**Example Activation**:
```
User: /workflow:implement Add date range filter to dashboard

1. Command `/workflow:implement` runs
2. `dash-components` Skill activates (detecting "filter" and "dashboard")
3. Level 2 loads: Component patterns and callback architecture
4. Skill provides: Filter component template
5. User needs state management between callbacks
6. Level 3 loads: STATE_MANAGEMENT.md
7. Complete filter component with callbacks created
```

---

### 4.4 accessibility-audit

**Metadata** (Level 1):
```yaml
name: accessibility-audit
description: Validate WCAG 2.1 AA compliance for dashboards. Use when checking color contrast, keyboard navigation, screen reader compatibility, or accessibility standards. Automatically invoked when user mentions accessibility, WCAG, a11y, or inclusivity.
allowed-tools: [Read, Bash]
```

**Purpose**: Ensure WCAG 2.1 Level AA compliance for all dashboards

**Activation Triggers**:
- Checking accessibility compliance
- Mentions "accessibility", "WCAG", "a11y", "screen reader", "keyboard navigation"
- Running accessibility audits
- During `/workflow:verify` phase

**Directory Structure**:
```
.claude/skills/accessibility-audit/
├── SKILL.md                      # Levels 1 & 2
├── WCAG_CHECKLIST.md             # ~2500 tokens - Complete checklist
├── COLOR_CONTRAST.md             # ~1200 tokens
├── KEYBOARD_NAV.md               # ~1500 tokens
├── SCREEN_READERS.md             # ~1800 tokens
├── scripts/
│   ├── check_contrast.py         # Color contrast checker
│   ├── check_aria.py             # ARIA validation
│   └── generate_report.py        # Audit report generator
└── examples/
    └── accessible_patterns.py    # Accessible component examples
```

**SKILL.md Outline** (Level 2):
```markdown
# Accessibility Audit Skill

## WCAG 2.1 Level AA Requirements

### 1. Perceivable

**Color Contrast**:
- Normal text: 4.5:1 minimum
- Large text (18pt+ or 14pt+ bold): 3:1 minimum
- UI components: 3:1 minimum

**Non-Text Content**:
- Alt text for images
- Text alternatives for charts
- Captions for multimedia

**Adaptable**:
- Content order logical
- Responsive design
- No information lost in any presentation

### 2. Operable

**Keyboard Accessible**:
- All functionality available via keyboard
- No keyboard trap
- Visible focus indicator

**Navigation**:
- Skip navigation links
- Clear page titles
- Logical heading structure (H1 → H2 → H3)

**Timing**:
- No time limits (or adjustable)
- Pause/stop animations
- Auto-update control

### 3. Understandable

**Readable**:
- Language specified
- Clear labels and instructions
- Error identification

**Predictable**:
- Consistent navigation
- Consistent identification
- No unexpected context changes

### 4. Robust

**Compatible**:
- Valid HTML
- ARIA labels where needed
- Name, role, value for UI components

## Audit Process

### Step 1: Automated Checks
```bash
# Run axe-core accessibility tests
npm run test:a11y

# Check color contrast
python scripts/check_contrast.py

# Validate ARIA
python scripts/check_aria.py
```

### Step 2: Manual Checks
- Keyboard navigation testing
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Zoom to 200% (ensure no content loss)

### Step 3: Generate Report
```bash
python scripts/generate_report.py
```

## Common Issues and Fixes

### Low Color Contrast
❌ Problem: Light gray text on white background
✅ Solution: Use #606060 or darker on white

### Missing ARIA Labels
❌ Problem: Icon button with no text
✅ Solution: Add aria-label
```python
html.Button('🔍', id='search-btn', **{'aria-label': 'Search'})
```

### Keyboard Trap
❌ Problem: Modal dialog can't be closed with keyboard
✅ Solution: Add Escape key handler

### Missing Alt Text
❌ Problem: Chart image with no description
✅ Solution: Add descriptive alt text
```python
dcc.Graph(figure=fig, config={'alt': 'Bar chart showing sales by region'})
```

## Integration with dash-components

When `dash-components` Skill creates components, `accessibility-audit` Skill provides:
- ARIA label recommendations
- Color contrast validation
- Keyboard navigation patterns
- Screen reader text suggestions

## Tools

### Python Libraries
- `colorspacious` - Color contrast calculation
- `beautifulsoup4` - HTML parsing for ARIA validation

### Browser Tools
- Chrome DevTools Lighthouse
- axe DevTools browser extension

### Screen Readers
- NVDA (Windows, free)
- JAWS (Windows, commercial)
- VoiceOver (macOS, built-in)
```

**Example Activation**:
```
User: /workflow:verify (after implementing dashboard)

1. Command `/workflow:verify` runs
2. `accessibility-audit` Skill activates (auto-check during verification)
3. Level 2 loads: WCAG checklist and audit process
4. Skill runs automated checks
5. Issue found: Low color contrast on button
6. Level 3 loads: COLOR_CONTRAST.md for detailed guidance
7. Skill suggests fix: Change button color from #AAAAAA to #606060
8. Verification passes after fix
```

---

### 4.5 performance-optimizer

**Metadata** (Level 1):
```yaml
name: performance-optimizer
description: Identify and fix performance issues in Plotly Dash dashboards. Use when optimizing callback speed, data loading efficiency, or rendering performance. Automatically invoked when user mentions performance, optimization, speed, or when dashboards are slow. Targets: <3s initial load, <1s callback response.
allowed-tools: [Read, Edit, Bash]
```

**Purpose**: Optimize dashboard performance for production readiness

**Activation Triggers**:
- Performance optimization requests
- Mentions "slow", "performance", "optimize", "speed", "lag"
- Dashboard load time issues
- During `/workflow:verify` if performance targets missed

**Directory Structure**:
```
.claude/skills/performance-optimizer/
├── SKILL.md                      # Levels 1 & 2
├── BOTTLENECK_PATTERNS.md        # ~2000 tokens
├── OPTIMIZATION_STRATEGIES.md    # ~2200 tokens
├── CACHING_GUIDE.md              # ~1500 tokens
├── PROFILING.md                  # ~1200 tokens
├── scripts/
│   ├── profile_callbacks.py      # Callback timing
│   ├── analyze_bundle.py         # Bundle size analysis
│   └── benchmark.py              # Performance benchmarks
└── examples/
    └── optimized_dashboard.py    # Optimized patterns
```

**SKILL.md Outline** (Level 2):
```markdown
# Performance Optimizer Skill

## Performance Targets

**Initial Load**: <3 seconds
**Callback Response**: <1 second
**Time to Interactive**: <5 seconds
**Bundle Size**: <500 KB (excluding data)

## Common Bottlenecks

### 1. Slow Callbacks
**Symptom**: Dashboard freezes when interacting
**Causes**:
- Expensive computations in callbacks
- Large dataframe operations
- Repeated database queries
- No caching

**Solutions**:
- Cache expensive computations
- Use dcc.Store for shared state
- Precompute aggregations
- Use background callbacks for long tasks

### 2. Large Data Loading
**Symptom**: Slow initial load
**Causes**:
- Loading entire dataset at once
- No pagination
- Uncompressed data transfer

**Solutions**:
- Implement pagination
- Use lazy loading
- Compress data (Parquet better than CSV)
- Load summary data first, details on-demand

### 3. Inefficient Rendering
**Symptom**: Charts take long to render
**Causes**:
- Too many data points
- Complex chart types
- No downsampling

**Solutions**:
- Downsample time series data
- Use scattergl instead of scatter for >10K points
- Simplify chart types
- Use virtual scrolling for tables

### 4. Callback Chains
**Symptom**: Multiple sequential updates
**Causes**:
- Callbacks triggering other callbacks
- Unnecessary intermediate states

**Solutions**:
- Combine related callbacks
- Use pattern-matching callbacks
- Reduce callback chain length

## Optimization Strategies

### Caching

```python
from functools import lru_cache
from flask_caching import Cache

# Setup cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

# Cache expensive function
@cache.memoize(timeout=300)
def load_and_process_data(start_date, end_date):
    df = load_data(start_date, end_date)
    return process_data(df)
```

### Lazy Loading

```python
# Load summary first
@app.callback(
    Output('summary', 'children'),
    Input('load-trigger', 'n_clicks')
)
def load_summary(n_clicks):
    summary_df = load_summary_data()  # Fast
    return create_summary_table(summary_df)

# Load details on-demand
@app.callback(
    Output('details', 'children'),
    Input('row-click', 'data')
)
def load_details(row_data):
    details_df = load_details_data(row_data['id'])
    return create_details_view(details_df)
```

### Downsampling

```python
def downsample_timeseries(df, max_points=5000):
    if len(df) <= max_points:
        return df

    # Use LTTB (Largest Triangle Three Buckets) algorithm
    # Or simple nth point selection
    step = len(df) // max_points
    return df.iloc[::step]
```

### Background Callbacks

```python
from dash.long_callback import DiskcacheLongCallbackManager

@app.long_callback(
    Output('result', 'children'),
    Input('compute-button', 'n_clicks'),
    running=[
        (Output('compute-button', 'disabled'), True, False),
    ],
    manager=long_callback_manager
)
def long_computation(n_clicks):
    # This runs in background, doesn't block UI
    result = expensive_computation()
    return result
```

## Profiling

### Measure Callback Time
```python
import time

@app.callback(...)
def my_callback(...):
    start = time.time()
    result = process()
    duration = time.time() - start
    print(f'Callback took {duration:.2f}s')
    return result
```

### Use Dash Dev Tools
```python
app.run_server(debug=True, dev_tools_ui=True)
# Enable "Callback Graph" to visualize callback chains
```

### Profile with cProfile
```bash
python -m cProfile -o profile.stats app.py
# Analyze with snakeviz
snakeviz profile.stats
```

## Performance Checklist

- [ ] Initial load <3 seconds
- [ ] Callbacks respond <1 second
- [ ] No unnecessary callback triggers
- [ ] Large datasets paginated or downsampled
- [ ] Expensive computations cached
- [ ] Bundle size optimized (<500 KB)
- [ ] Charts use efficient types (scattergl for large data)
- [ ] Images optimized and lazy-loaded
- [ ] No console errors or warnings
- [ ] Memory usage stable (no leaks)
```

**Example Activation**:
```
User: Dashboard is slow when filtering large dataset

1. User reports performance issue
2. `performance-optimizer` Skill activates (detecting "slow")
3. Level 2 loads: Bottleneck patterns and optimization strategies
4. Skill analyzes: Callback processes 1M rows on each filter change
5. Skill suggests: Add caching + downsampling
6. Level 3 loads: CACHING_GUIDE.md and OPTIMIZATION_STRATEGIES.md
7. Implementation: Add flask_caching + downsample to 10K points
8. Result: Callback time reduced from 8s to 0.5s
```

---

## 5. Skills Integration with Commands

### How Skills Enhance Commands

Commands provide **workflow structure**, Skills provide **domain expertise**. They work together seamlessly.

**Example: Complete Dashboard Creation**

```bash
# Step 1: Create Specification
User: /spec:specify Build sales analytics dashboard

Skills activated:
- spec-kit-workflow (development): Provides spec template and guidance

Output: Well-structured spec.md following spec-kit methodology

---

# Step 2: Create Plan
User: /spec:plan

Skills activated:
- claude-code-architecture (development): Architecture patterns
- plotly-viz (production): Visualization recommendations
- data-analysis (production): Data pipeline suggestions

Output: Comprehensive plan.md with architecture, tech stack, components

---

# Step 3: Generate Tasks
User: /spec:tasks

Skills activated:
- spec-kit-workflow (development): Task breakdown methodology

Output: Actionable tasks.md with dependencies and success criteria

---

# Step 4: Implement First Task
User: /workflow:implement Task 1 - Create data loader

Skills activated:
- data-analysis (production): Data loading patterns
- research-synthesis (development): Extract patterns from existing code

Output:
- src/data/sales_loader.py (implementation)
- tests/unit/test_sales_loader.py (TDD tests)

---

# Step 5: Implement Second Task
User: /workflow:implement Task 2 - Create bar chart component

Skills activated:
- plotly-viz (production): Chart creation patterns
- dash-components (production): Component structure
- accessibility-audit (production): WCAG compliance

Output:
- src/components/sales_chart.py (accessible chart)
- tests/unit/test_sales_chart.py (tests)

---

# Step 6: Verify Implementation
User: /workflow:verify

Skills activated:
- accessibility-audit (production): Auto-check WCAG compliance
- performance-optimizer (production): Check performance targets

Output:
- All tests pass ✓
- Coverage: 87% ✓
- WCAG 2.1 AA compliant ✓
- Load time: 2.1s ✓
```

### Token Usage Comparison

**Without Progressive Disclosure** (all knowledge upfront):
```
At startup: Load all Skills fully = 80,000 tokens
During session: Immediate access
Total: 80,000 tokens
```

**With Progressive Disclosure** (Skills approach):
```
At startup: 20 Skills × 50 tokens = 1,000 tokens
Task 1: data-analysis Level 2 = +800 tokens
Task 2: plotly-viz L2 + dash-components L2 = +1,600 tokens
Task 6: accessibility-audit L2 + Level 3 = +3,000 tokens
Total: 6,400 tokens (92% reduction)
```

**Benefit**: 12x more efficient context usage while maintaining comprehensive expertise

---

## 6. Skills vs MCP: Complementary Relationship

Skills and MCP (Model Context Protocol) are **complementary**, not competing.

### What MCP Provides

**MCP** = External data and tool access

**Examples**:
- `mcp__postgres` - Database queries
- `mcp__filesystem` - File operations
- `mcp__github` - Repository operations
- `mcp__fetch` - HTTP requests

**Characteristic**: All tools loaded upfront at startup (~50,000 tokens for 5 servers)

**Use When**: Need to ACCESS external systems (databases, APIs, files)

---

### What Skills Provide

**Skills** = Domain knowledge and methodology

**Examples**:
- `data-analysis` - How to analyze data
- `plotly-viz` - How to create visualizations
- `spec-kit-workflow` - How to write specifications

**Characteristic**: Progressive disclosure (50 → 800 → variable tokens)

**Use When**: Need EXPERTISE on how to do something well

---

### Working Together

**Scenario**: Build dashboard with database-driven charts

```
1. User: /workflow:implement Create sales dashboard with PostgreSQL data

2. MCP provides the WHAT (data access):
   → mcp__postgres connects to database
   → Executes SQL queries
   → Returns data to Claude

3. Skills provide the HOW (methodology):
   → data-analysis: How to analyze the query results
   → plotly-viz: How to choose appropriate chart types
   → dash-components: How to structure the dashboard

4. Command provides the WHEN (workflow):
   → /workflow:implement orchestrates the work
   → TDD structure (tests first)
   → Validation and verification

Result: Database data → Analyzed → Visualized → Dashboard component
```

**Anthropic's Guidance**:
> "MCP is the universal connector, providing the what—the access to tools and data. Skills are the procedural knowledge, providing the how—the instructions and methodology."

### When to Use Each

| Need | Use | Example |
|------|-----|---------|
| Access database | MCP | mcp__postgres |
| Know how to write queries | Skill | data-analysis |
| Access files | MCP | mcp__filesystem |
| Know what to analyze | Skill | data-analysis |
| Access GitHub | MCP | mcp__github |
| Know git workflows | Skill | git-workflow |
| Call APIs | MCP | mcp__fetch |
| Know API patterns | Skill | api-integration |

**Key Insight**: MCP + Skills together provide complete solution - access AND expertise.

---

## Summary

**Agent Skills are the expertise layer** in our architecture:

1. **Commands** = User-invoked workflows (structure)
2. **Skills** = Model-invoked knowledge (expertise)
3. **Sub-Agents** = Task-isolated workers (capacity)
4. **MCP** = External data access (connectivity)

**Progressive Disclosure** enables massive knowledge bases (100+ Skills) without context bloat.

**Two Skill Sets**:
- **Development Skills**: For building this system (spec-kit-workflow, claude-code-architecture, research-synthesis)
- **Production Skills**: For dashboard developers (data-analysis, plotly-viz, dash-components, accessibility-audit, performance-optimizer)

**Integration**: Skills automatically enhance Commands at every phase of the hybrid workflow (Spec-Kit planning + Claude Code execution).

**Next**: See Functional Requirements (FR-061 to FR-090) for detailed Skills specifications.

---

**Token Count**: ~4200 tokens (as requested: extremely detailed)
