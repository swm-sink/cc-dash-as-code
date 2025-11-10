# Feature Specification: Agent Skills - Production

**Feature Branch**: `004-agent-skills-production`
**Created**: 2025-11-10
**Status**: Draft
**Input**: Create 5 Production Skills (data-analysis, plotly-viz, dash-components, accessibility-audit, performance-optimizer) to support dashboard developers using the Claude Code system

## Overview

This specification defines the Production Skills required for dashboard developers to build high-quality, accessible, performant Plotly Dash applications. These Skills provide domain expertise that auto-activates when developers are implementing dashboards—analyzing data, creating visualizations, building components, ensuring accessibility, and optimizing performance.

**Production Skills** are distinct from **Development Skills** (spec 003). Production Skills support dashboard developers (end users of our system), while Development Skills support us building the system itself.

**The 5 Production Skills**:

1. **data-analysis** - Statistical analysis, exploratory data analysis (EDA), data quality checking
2. **plotly-viz** - Chart generation, accessibility compliance (WCAG 2.1 AA), theming
3. **dash-components** - Component patterns, callback architecture, layouts, state management
4. **accessibility-audit** - WCAG 2.1 Level AA compliance validation, automated checking
5. **performance-optimizer** - Bottleneck detection, optimization strategies, performance targets (<3s load, <1s callbacks)

**Progressive Disclosure**: All Skills implement three-level loading (metadata → core → references) to maintain lean context while providing deep expertise on-demand.

**Integration**: Skills auto-activate during `/workflow:*` commands and when working with data, visualizations, or Dash code.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Data Analysis Skill (Priority: P1)

As a **dashboard developer**, I want the `data-analysis` Skill to guide me through loading and analyzing data so that I can perform proper EDA, identify data quality issues, and make informed visualization decisions.

**Why this priority**: Foundational for all dashboards. Proper data analysis determines visualization choices and data quality.

**Independent Test**: Can be tested by loading a dataset and verifying the Skill provides correct analysis guidance.

**Acceptance Scenarios**:

1. **Given** I'm loading CSV data, **When** the Skill activates, **Then** it provides pandas.read_csv() patterns with common parameters (encoding, na_values, parse_dates)

2. **Given** I'm performing EDA, **When** the Skill is active, **Then** it guides through shape, dtypes, null checks, describe(), and correlations

3. **Given** I have data quality issues, **When** analyzing, **Then** the Skill helps identify missing values (MCAR/MAR/MNAR), outliers (IQR/z-score), and duplicates

4. **Given** I need to choose visualizations, **When** analyzing data types, **Then** the Skill recommends appropriate chart types based on variable types (continuous, categorical, time series)

5. **Given** I'm working with SQL data, **When** the Skill loads Level 3, **Then** it provides SQL query patterns and database connection examples

6. **Given** I need statistical testing, **When** the Skill loads Level 3 STATISTICAL_METHODS.md, **Then** it provides hypothesis testing, correlation analysis, and regression guidance

---

### User Story 2 - Plotly Visualization Skill (Priority: P1)

As a **dashboard developer**, I want the `plotly-viz` Skill to help me create accessible, well-designed visualizations so that my charts are WCAG 2.1 AA compliant and follow best practices.

**Why this priority**: Critical for dashboard quality. Poor visualizations confuse users; inaccessible charts exclude users.

**Independent Test**: Can be tested by creating charts and verifying accessibility compliance and quality.

**Acceptance Scenarios**:

1. **Given** I need to create a chart, **When** the Skill activates, **Then** it recommends appropriate chart type based on data characteristics (bar for categorical comparison, line for time series, scatter for correlation)

2. **Given** I'm using Plotly Express, **When** creating a chart, **Then** the Skill provides px.[chart_type]() pattern with common parameters (x, y, color, title, labels)

3. **Given** I need accessibility, **When** creating charts, **Then** the Skill ensures color contrast ratios meet WCAG 2.1 AA (4.5:1 for text, 3:1 for UI components)

4. **Given** I want custom styling, **When** the Skill loads Level 3 THEMING.md, **Then** it provides consistent color palettes, font sizes, and layout patterns

5. **Given** I need interactivity, **When** the Skill loads Level 3 INTERACTIVITY.md, **Then** it provides hover, click, zoom, and selection patterns

6. **Given** I create a chart, **When** verifying, **Then** the Skill reminds to add descriptive titles, axis labels, and ARIA labels for screen readers

---

### User Story 3 - Dash Components Skill (Priority: P1)

As a **dashboard developer**, I want the `dash-components` Skill to guide me in building reusable Dash components and callbacks so that my dashboards are maintainable and follow best practices.

**Why this priority**: Core to Dash development. Proper component structure and callback design determine code quality and maintainability.

**Independent Test**: Can be tested by creating components and callbacks, verifying they follow patterns.

**Acceptance Scenarios**:

1. **Given** I'm creating a component, **When** the Skill activates, **Then** it provides component function pattern with html.Div structure, id-based props, and className for styling

2. **Given** I'm creating callbacks, **When** writing callback functions, **Then** the Skill provides @app.callback decorator pattern with Input, Output, State imports and proper signatures

3. **Given** I need state management, **When** the Skill loads Level 3 STATE_MANAGEMENT.md, **Then** it provides dcc.Store patterns for sharing state across callbacks

4. **Given** I'm building layouts, **When** creating dashboard structure, **Then** the Skill provides responsive grid patterns with header, sidebar, and main content areas

5. **Given** I need callback optimization, **When** the Skill loads Level 3 CALLBACK_ARCHITECTURE.md, **Then** it provides prevent_initial_call usage, callback chaining patterns, and performance tips

6. **Given** I create a component, **When** verifying, **Then** the Skill reminds to add type hints, docstrings, and unit tests

---

### User Story 4 - Accessibility Audit Skill (Priority: P2)

As a **dashboard developer**, I want the `accessibility-audit` Skill to automatically check WCAG 2.1 AA compliance so that my dashboards are accessible to all users including those with disabilities.

**Why this priority**: Important for compliance and inclusivity, but not blocking basic functionality. Can be added after initial implementation.

**Independent Test**: Can be tested by running audit on dashboards and verifying violation detection.

**Acceptance Scenarios**:

1. **Given** I run `/workflow:verify`, **When** the Skill activates, **Then** it automatically checks color contrast ratios for all text and UI components

2. **Given** I have accessibility issues, **When** the audit runs, **Then** the Skill reports specific violations with element locations and remediation suggestions

3. **Given** I use interactive elements, **When** checking keyboard navigation, **Then** the Skill verifies all elements are reachable via keyboard and have visible focus indicators

4. **Given** I have charts without alt text, **When** auditing, **Then** the Skill flags missing ARIA labels and descriptive text for screen readers

5. **Given** I need detailed WCAG guidance, **When** the Skill loads Level 3 WCAG_CHECKLIST.md, **Then** it provides complete Level AA criteria with examples

6. **Given** I fix violations, **When** re-running audit, **Then** the Skill confirms fixes and shows compliance status

---

### User Story 5 - Performance Optimizer Skill (Priority: P2)

As a **dashboard developer**, I want the `performance-optimizer` Skill to identify and fix performance issues so that my dashboards load quickly (<3s) and respond fast (<1s callbacks).

**Why this priority**: Important for user experience but not blocking initial development. Performance can be optimized after basic functionality works.

**Independent Test**: Can be tested by profiling slow dashboards and verifying optimization suggestions.

**Acceptance Scenarios**:

1. **Given** my dashboard is slow, **When** the Skill activates, **Then** it identifies common bottlenecks (slow callbacks, large data loading, inefficient rendering)

2. **Given** I have slow callbacks, **When** analyzing, **Then** the Skill suggests caching strategies using @cache.memoize or dcc.Store

3. **Given** I'm loading large datasets, **When** the Skill provides guidance, **Then** it recommends pagination, lazy loading, or data downsampling

4. **Given** I have complex charts, **When** optimizing rendering, **Then** the Skill suggests using scattergl for >10K points or simplifying chart types

5. **Given** I need profiling, **When** the Skill loads Level 3 PROFILING.md, **Then** it provides callback timing methods, cProfile usage, and browser DevTools guidance

6. **Given** I implement optimizations, **When** measuring, **Then** the Skill helps verify performance targets are met (<3s load, <1s callbacks)

---

### Edge Cases

- **What happens when** `data-analysis` Skill activates but I'm not working with data?
  - Skill should only activate when context clearly indicates data work (file extensions .csv/.json/.parquet, pandas imports, data-related keywords)

- **What happens when** `plotly-viz` Skill suggests a chart type that doesn't fit my use case?
  - Skill provides recommendations, not requirements; developer can override; Level 2 should show multiple chart options

- **What happens when** `accessibility-audit` Skill reports false positives?
  - Skill should have clear remediation guidance; developer can document exceptions; false positive rate target <5%

- **What happens when** `performance-optimizer` Skill suggests optimizations that break functionality?
  - Skill should emphasize testing after optimization; provide safe, proven patterns first; warn about trade-offs

- **What happens when** multiple Production Skills activate simultaneously (e.g., creating accessible chart)?
  - Skills should complement each other: plotly-viz creates chart, accessibility-audit validates it, performance-optimizer ensures it renders quickly

- **What happens when** Skills exceed token budgets?
  - Progressive disclosure prevents this: Level 1 (50 tokens) always loaded, Level 2 (800 tokens) on activation, Level 3 (variable) only when explicitly needed

---

## Requirements *(mandatory)*

### Functional Requirements

#### Data Analysis Skill (FR-001 to FR-018)

- **FR-001**: System MUST provide `data-analysis` Skill with metadata describing data processing and analysis capabilities
- **FR-002**: Skill MUST activate when loading data files (.csv, .json, .parquet) or working with pandas/SQL
- **FR-003**: Skill MUST activate when keywords match: "data", "analyze", "EDA", "statistics", "dataframe", "quality"
- **FR-004**: Level 1 (metadata) MUST be 40-60 tokens describing data analysis, EDA, and quality checking
- **FR-005**: Level 2 (core) MUST be 600-1000 tokens covering data loading, EDA process, quality checks, and visualization recommendations
- **FR-006**: Level 2 MUST include patterns for CSV/JSON/Parquet (pandas) and SQL (MCP or psycopg2)
- **FR-007**: Level 2 MUST include EDA workflow: shape, dtypes, nulls, describe(), correlations
- **FR-008**: Level 2 MUST include data quality checks: missing values, outliers, duplicates, type consistency
- **FR-009**: Level 2 MUST recommend chart types based on data characteristics
- **FR-010**: Level 3 MUST include STATISTICAL_METHODS.md (~2000 tokens) with hypothesis testing, regression, time series
- **FR-011**: Level 3 MUST include DATA_QUALITY.md (~1500 tokens) with MCAR/MAR/MNAR, IQR/z-score methods
- **FR-012**: Level 3 MUST include VISUALIZATION_GUIDE.md (~1800 tokens) with chart selection decision tree
- **FR-013**: Level 3 MUST include scripts/ directory with analyze.py, quality_check.py, transform.py
- **FR-014**: Level 3 MUST include examples/ directory with eda-example.py
- **FR-015**: Skill MUST declare allowed-tools: [Read, Bash, mcp__postgres, mcp__filesystem]
- **FR-016**: Skill MUST support multiple data formats: CSV, JSON, Parquet, SQL databases
- **FR-017**: Skill MUST integrate with plotly-viz Skill (pass analysis insights to visualization)
- **FR-018**: Skill directory structure MUST be: `.claude/skills/production/data-analysis/`

---

#### Plotly Visualization Skill (FR-019 to FR-038)

- **FR-019**: System MUST provide `plotly-viz` Skill with metadata describing visualization and accessibility capabilities
- **FR-020**: Skill MUST activate when creating charts or mentions: "chart", "graph", "plot", "visualization", "figure"
- **FR-021**: Skill MUST activate when working with Plotly or Dash visualization code
- **FR-022**: Level 1 (metadata) MUST be 40-60 tokens describing chart generation and WCAG 2.1 AA compliance
- **FR-023**: Level 2 (core) MUST be 600-1000 tokens covering chart selection, creation patterns, and accessibility basics
- **FR-024**: Level 2 MUST include chart selection guide based on data types (continuous, categorical, time series, multivariate)
- **FR-025**: Level 2 MUST include Plotly Express patterns for common charts (bar, line, scatter, pie, histogram)
- **FR-026**: Level 2 MUST enforce WCAG 2.1 AA: color contrast (4.5:1 text, 3:1 UI), non-color encoding, keyboard nav
- **FR-027**: Level 3 MUST include CHART_TYPES.md (~2500 tokens) with detailed guidance for all chart types
- **FR-028**: Level 3 MUST include ACCESSIBILITY.md (~1800 tokens) with WCAG compliance patterns
- **FR-029**: Level 3 MUST include THEMING.md (~1200 tokens) with color palettes, fonts, consistent styling
- **FR-030**: Level 3 MUST include INTERACTIVITY.md (~1500 tokens) with hover, click, zoom, selection patterns
- **FR-031**: Level 3 MUST include templates/ directory with chart template files (bar_chart.py, line_chart.py, etc.)
- **FR-032**: Level 3 MUST include examples/ directory with accessible-dashboard.py example
- **FR-033**: Skill MUST declare allowed-tools: [Read, Write, Edit]
- **FR-034**: Skill MUST ensure all generated charts meet WCAG 2.1 Level AA compliance
- **FR-035**: Skill MUST support both Plotly Express (simple) and Graph Objects (advanced)
- **FR-036**: Skill MUST provide colorblind-friendly palette recommendations
- **FR-037**: Skill MUST integrate with accessibility-audit Skill for validation
- **FR-038**: Skill directory structure MUST be: `.claude/skills/production/plotly-viz/`

---

#### Dash Components Skill (FR-039 to FR-056)

- **FR-039**: System MUST provide `dash-components` Skill with metadata describing component patterns and callbacks
- **FR-040**: Skill MUST activate when creating Dash components or mentions: "component", "callback", "layout", "dash"
- **FR-041**: Skill MUST activate when working with Dash application code
- **FR-042**: Level 1 (metadata) MUST be 40-60 tokens describing component creation, callbacks, and layouts
- **FR-043**: Level 2 (core) MUST be 600-1000 tokens covering component patterns, callback basics, and layout structures
- **FR-044**: Level 2 MUST include component creation pattern with html.Div, dcc components, and id management
- **FR-045**: Level 2 MUST include callback architecture with @app.callback, Input/Output/State, and function signatures
- **FR-046**: Level 2 MUST include layout patterns: responsive grid, header/sidebar/main structure
- **FR-047**: Level 3 MUST include COMPONENT_PATTERNS.md (~2000 tokens) with reusable component examples
- **FR-048**: Level 3 MUST include CALLBACK_ARCHITECTURE.md (~2200 tokens) with advanced callback patterns
- **FR-049**: Level 3 MUST include LAYOUT_GUIDE.md (~1500 tokens) with responsive design patterns
- **FR-050**: Level 3 MUST include STATE_MANAGEMENT.md (~1800 tokens) with dcc.Store and state sharing patterns
- **FR-051**: Level 3 MUST include templates/ directory with component templates (basic_component.py, filter_component.py, etc.)
- **FR-052**: Level 3 MUST include examples/ directory with complete_dashboard.py example
- **FR-053**: Skill MUST declare allowed-tools: [Read, Write, Edit]
- **FR-054**: Skill MUST provide callback optimization guidance (prevent_initial_call, caching, chaining)
- **FR-055**: Skill MUST encourage type hints, docstrings, and unit tests for all components
- **FR-056**: Skill directory structure MUST be: `.claude/skills/production/dash-components/`

---

#### Accessibility Audit Skill (FR-057 to FR-072)

- **FR-057**: System MUST provide `accessibility-audit` Skill with metadata describing WCAG validation capabilities
- **FR-058**: Skill MUST activate during `/workflow:verify` phase automatically
- **FR-059**: Skill MUST activate when mentions: "accessibility", "WCAG", "a11y", "screen reader", "keyboard navigation"
- **FR-060**: Level 1 (metadata) MUST be 40-60 tokens describing WCAG 2.1 Level AA compliance checking
- **FR-061**: Level 2 (core) MUST be 600-1000 tokens covering WCAG requirements, audit process, and common issues
- **FR-062**: Level 2 MUST include WCAG 2.1 Level AA requirements across 4 principles: Perceivable, Operable, Understandable, Robust
- **FR-063**: Level 2 MUST include audit process: automated checks → manual checks → report generation
- **FR-064**: Level 2 MUST include common issues and fixes (color contrast, missing ARIA, keyboard traps, missing alt text)
- **FR-065**: Level 3 MUST include WCAG_CHECKLIST.md (~2500 tokens) with complete Level AA criteria
- **FR-066**: Level 3 MUST include COLOR_CONTRAST.md (~1200 tokens) with calculation methods and tools
- **FR-067**: Level 3 MUST include KEYBOARD_NAV.md (~1500 tokens) with navigation testing patterns
- **FR-068**: Level 3 MUST include SCREEN_READERS.md (~1800 tokens) with ARIA best practices
- **FR-069**: Level 3 MUST include scripts/ directory with check_contrast.py, check_aria.py, generate_report.py
- **FR-070**: Level 3 MUST include examples/ directory with accessible_patterns.py
- **FR-071**: Skill MUST declare allowed-tools: [Read, Bash]
- **FR-072**: Skill directory structure MUST be: `.claude/skills/production/accessibility-audit/`

---

#### Performance Optimizer Skill (FR-073 to FR-088)

- **FR-073**: System MUST provide `performance-optimizer` Skill with metadata describing optimization capabilities
- **FR-074**: Skill MUST activate when performance issues detected or mentions: "slow", "performance", "optimize", "lag"
- **FR-075**: Skill MUST activate during `/workflow:verify` if performance targets not met
- **FR-076**: Level 1 (metadata) MUST be 40-60 tokens describing bottleneck detection and optimization with targets (<3s load, <1s callbacks)
- **FR-077**: Level 2 (core) MUST be 600-1000 tokens covering common bottlenecks and optimization strategies
- **FR-078**: Level 2 MUST identify 4 bottleneck categories: slow callbacks, large data loading, inefficient rendering, callback chains
- **FR-079**: Level 2 MUST provide optimization strategies: caching, lazy loading, downsampling, callback combining
- **FR-080**: Level 3 MUST include BOTTLENECK_PATTERNS.md (~2000 tokens) with detailed bottleneck identification
- **FR-081**: Level 3 MUST include OPTIMIZATION_STRATEGIES.md (~2200 tokens) with specific optimization techniques
- **FR-082**: Level 3 MUST include CACHING_GUIDE.md (~1500 tokens) with Flask-Caching and dcc.Store patterns
- **FR-083**: Level 3 MUST include PROFILING.md (~1200 tokens) with callback timing, cProfile, browser DevTools
- **FR-084**: Level 3 MUST include scripts/ directory with profile_callbacks.py, analyze_bundle.py, benchmark.py
- **FR-085**: Level 3 MUST include examples/ directory with optimized_dashboard.py
- **FR-086**: Skill MUST declare allowed-tools: [Read, Edit, Bash]
- **FR-087**: Skill MUST target performance goals: <3s initial load, <1s callback response, <5s time to interactive
- **FR-088**: Skill directory structure MUST be: `.claude/skills/production/performance-optimizer/`

---

#### General Production Skills Requirements (FR-089 to FR-100)

- **FR-089**: All Production Skills MUST implement three-level progressive disclosure (metadata → core → references)
- **FR-090**: All Skills MUST have SKILL.md as primary file with YAML frontmatter and Markdown content
- **FR-091**: All Skills MUST declare allowed-tools in YAML frontmatter
- **FR-092**: All Skills MUST reside in `.claude/skills/production/` directory
- **FR-093**: Skills MUST NOT activate during meta-level system development (only during dashboard development)
- **FR-094**: Skills MUST auto-activate based on description keyword matching (no explicit user invocation)
- **FR-095**: Skills MUST be version-controlled in git (no .gitignore exclusions)
- **FR-096**: Skills MUST include activation trigger documentation in SKILL.md
- **FR-097**: Skills MUST NOT conflict with each other (complementary, not competing)
- **FR-098**: Skills MUST work correctly when multiple activate simultaneously
- **FR-099**: Skills updates MUST NOT break existing workflows (backward compatibility)
- **FR-100**: All Skills MUST integrate with MCP servers where appropriate (data-analysis with mcp__postgres)

---

### Key Entities

- **Production Skill**: Domain expertise for dashboard development
  - Attributes: name, description, activation triggers, directory structure, token budgets per level, allowed-tools
  - Relationships: Auto-activates during dashboard implementation, complements `/workflow:*` commands, distinct from Development Skills (spec 003)

- **Skill Level Content**: Progressive disclosure tier content
  - Attributes: level (1/2/3), token budget, file location, content type (metadata/core/references)
  - Relationships: Belongs to Production Skill, loads sequentially based on need

- **Reference Material**: Level 3 detailed documentation
  - Attributes: filename, token count, topic, format (MD/py/examples)
  - Relationships: Part of Skill Level 3, loaded on-demand via Read tool

- **Performance Target**: Measurable performance goal
  - Attributes: metric name (load time, callback time), target value (<3s, <1s), measurement method
  - Relationships: Defined by performance-optimizer Skill, validated during `/workflow:verify`

- **Accessibility Criterion**: WCAG 2.1 Level AA requirement
  - Attributes: criterion ID (e.g., 1.4.3), description, success criteria, level (A/AA)
  - Relationships: Checked by accessibility-audit Skill, enforced by plotly-viz Skill

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

#### Data Analysis Skill Effectiveness

- **SC-001**: Skill activates correctly 95%+ of the time when working with data
- **SC-002**: Data quality issues identified by Skill match manual review 90%+ of the time
- **SC-003**: Chart type recommendations are appropriate for data 85%+ of the time
- **SC-004**: Developers complete EDA 30%+ faster with Skill than without
- **SC-005**: Data analysis code quality (proper null handling, type checking) improves 40%+

---

#### Plotly Visualization Skill Effectiveness

- **SC-006**: Skill generates WCAG 2.1 AA compliant charts 95%+ of the time
- **SC-007**: Chart type selections match best practices 90%+ of the time
- **SC-008**: Color contrast violations detected and prevented 98%+ of the time
- **SC-009**: Developers create charts 35%+ faster with Skill than without
- **SC-010**: Chart quality rating (clarity, accessibility, design) improves from 3.2/5.0 to 4.5/5.0

---

#### Dash Components Skill Effectiveness

- **SC-011**: Components created with Skill follow best practices 95%+ of the time
- **SC-012**: Callbacks created with Skill are properly structured 90%+ of the time
- **SC-013**: Components include type hints and docstrings 85%+ of the time
- **SC-014**: Callback optimization patterns reduce render time 30%+ on average
- **SC-015**: Component reusability rate increases 50%+ with Skill guidance

---

#### Accessibility Audit Skill Effectiveness

- **SC-016**: Skill detects 95%+ of WCAG 2.1 AA violations
- **SC-017**: False positive rate for accessibility checks <5%
- **SC-018**: Dashboards achieve WCAG 2.1 AA compliance 90%+ of the time with Skill
- **SC-019**: Accessibility issues fixed on first attempt 80%+ of the time with Skill guidance
- **SC-020**: Time to achieve compliance reduced 50%+ with automated checking

---

#### Performance Optimizer Skill Effectiveness

- **SC-021**: Skill identifies performance bottlenecks correctly 90%+ of the time
- **SC-022**: Optimization suggestions improve performance measurably 85%+ of the time
- **SC-023**: Dashboards meet <3s load time target 80%+ of the time with Skill optimizations
- **SC-024**: Callbacks meet <1s response time target 85%+ of the time with Skill guidance
- **SC-025**: Overall dashboard performance score improves 45%+ with Skill

---

#### Overall Production Skills Performance

- **SC-026**: All 5 Production Skills stay within token budgets (Level 1: 50, Level 2: 800) 95%+ of the time
- **SC-027**: Skills activate automatically (no explicit invocation) 90%+ of the time
- **SC-028**: Multiple Skills work together without conflicts 100% of the time
- **SC-029**: Skills context usage is 70%+ less than loading all content upfront
- **SC-030**: Dashboard developers rate Skills usefulness 4.5/5.0 or higher
- **SC-031**: Development velocity (tasks completed per week) increases 35%+ with Skills
- **SC-032**: Code quality (coverage, linting, accessibility) improves 40%+ with Skills
- **SC-033**: Production bug rate decreases 30%+ (Skills catch issues earlier)
- **SC-034**: Developer onboarding time reduced 40%+ (Skills provide guidance)
- **SC-035**: Skills are used in 95%+ of dashboard implementations

---

## Non-Functional Requirements

### Performance
- Skill activation latency: <2 seconds
- Level 3 file loading: <1 second per reference
- Automated checks (accessibility, performance) complete in <10 seconds
- No noticeable workflow slowdown from Skills

### Usability
- Skills activate transparently without user intervention
- Skill guidance is actionable and specific (not generic)
- Examples are realistic and directly applicable to dashboard development
- Error detection includes clear remediation steps

### Reliability
- Skills provide correct, current information 98%+ of the time
- Skills activate consistently based on triggers 95%+ of the time
- Skills handle edge cases gracefully (missing data, unusual patterns)
- False positive rate for automated checks <5%

### Maintainability
- Skill content version-controlled in git
- Skills easy to update (Markdown files, Python scripts)
- Token budgets enforced via CI/CD
- Skills modular with minimal coupling

### Compatibility
- Skills work in Claude Code (primary environment)
- Skills deployable via Claude Agent SDK (future)
- Skills integrate with MCP servers (mcp__postgres, mcp__filesystem)
- Skills compatible with Plotly Dash 2.14+ and Python 3.11+

---

## Technology Stack

### Required
- **Claude Code**: Development environment with Skills support
- **Python 3.11+**: Runtime for dashboard development
- **Plotly Dash 2.14+**: Dashboard framework
- **Pandas**: Data analysis library
- **Markdown/YAML**: Skill file formats

### Skills Implementation
- SKILL.md files in `.claude/skills/production/`
- Progressive disclosure (three levels)
- Auto-activation via keyword matching
- Reference files: Markdown, Python scripts, templates, examples

### Integration
- MCP servers: mcp__postgres, mcp__filesystem
- Claude Code commands: `/workflow:*`
- Development tools: pytest, Black, Ruff, mypy

---

## Out of Scope

The following are explicitly **not** included in this specification:

- Development Skills (those are in spec 003: Agent Skills - Development)
- MCP server configuration (that's in spec 005: MCP Integration)
- Command implementations (those are in spec 002: Claude Code Commands Setup)
- Sub-Agent implementations (those are in spec 002: Claude Code Commands Setup)
- Actual dashboard implementations (those use the Skills)
- Skills for non-Dash frameworks (Flask, Streamlit, etc.)
- Advanced statistical methods beyond common use cases
- Custom visualization libraries beyond Plotly

---

## Clarifications

### Q1: How are Production Skills different from Development Skills?

**A**: Production Skills support **dashboard developers** using our system. Development Skills support **us** building the system.

**Production Skills activate when**:
- Analyzing data (data-analysis)
- Creating visualizations (plotly-viz)
- Building components (dash-components)
- Checking accessibility (accessibility-audit)
- Optimizing performance (performance-optimizer)

**Development Skills activate when** (spec 003):
- Writing specs (spec-kit-workflow)
- Designing architecture (claude-code-architecture)
- Researching patterns (research-synthesis)

**Context**: Different users, different phases of project lifecycle.

---

### Q2: Why 5 Production Skills but only 3 Development Skills?

**A**: Production (dashboard development) is more complex and domain-specific than Development (building the system).

**Production complexity**:
- Data: Multiple formats, quality issues, transformations
- Visualization: Many chart types, accessibility requirements
- Components: Dash-specific patterns, callback architecture
- Quality: Accessibility standards, performance targets

**Development focus**:
- Methodology: One standard approach (spec-kit)
- Architecture: One target (Claude Code)
- Research: General analysis methods

5 Production Skills provide coverage across dashboard development workflow.

---

### Q3: How do Production Skills ensure WCAG 2.1 AA compliance?

**A**: Two-layer approach: Prevention (plotly-viz) + Validation (accessibility-audit).

**Prevention Layer** (plotly-viz Skill):
- Enforces color contrast ratios during chart creation
- Provides accessible color palettes
- Reminds to add ARIA labels and descriptions
- Suggests non-color encoding (patterns, labels)

**Validation Layer** (accessibility-audit Skill):
- Automated checking during `/workflow:verify`
- Detects violations: contrast, keyboard nav, ARIA, semantic HTML
- Provides remediation guidance
- Generates compliance reports

**Together**: Prevent issues at creation time, catch any that slip through with validation.

---

### Q4: What if performance optimization breaks functionality?

**A**: Skills emphasize testing and provide safe, proven patterns first.

**Safety measures**:
1. **Test after optimization**: Skill reminds to run full test suite
2. **Proven patterns first**: Caching, lazy loading (low-risk)
3. **Advanced patterns later**: With warnings and trade-offs explained
4. **Performance targets are goals**: Not mandatory; some dashboards may exceed if functionality requires

**Skill guidance**: "Always verify functionality after optimization. If tests fail, roll back and try alternative approach."

---

### Q5: How do Skills handle conflicting recommendations?

**A**: Skills are designed to complement, not conflict. When multiple activate, they work together.

**Example: Creating accessible chart**:
```
data-analysis: "Bar chart appropriate for categorical comparison"
plotly-viz: "Use px.bar() with accessible colors (contrast 4.5:1)"
accessibility-audit: "Verify ARIA labels present"
performance-optimizer: "If >10K bars, consider aggregation"
```

Each Skill provides expertise in its domain. No conflicts because:
- Clear domain boundaries (data vs visualization vs accessibility vs performance)
- Complementary guidance (build on each other)
- Same goal (high-quality dashboard)

**If rare conflict**: User decides; Skills suggest, not mandate.

---

## Dependencies

### Prerequisites
- Spec 002 (Claude Code Commands Setup) approved
- Spec 003 (Agent Skills - Development) completed (Development Skills must exist first)
- `.claude/skills/production/` directory exists
- Understanding of progressive disclosure pattern
- Plotly Dash 2.14+ installed

### Internal Dependencies
- specs/memory/constitution.md (quality standards)
- specs/WORKFLOW.md (hybrid workflow architecture)
- specs/002-claude-code-commands-setup/spec.md (Commands and architecture)
- `/workflow:*` commands for integration

### External Dependencies
- Claude Code with Skills support
- Python 3.11+ runtime
- Plotly Dash 2.14+ framework
- Pandas, NumPy for data analysis
- Git for version control

---

## Implementation Phases

**Note**: This spec defines WHAT the Production Skills must accomplish. The HOW (implementation details, file contents, token optimization) goes in plan.md.

### Phase 1: Core Data & Visualization Skills
- data-analysis Skill (most foundational)
- plotly-viz Skill (works with data-analysis)
- Test integration between Skills

### Phase 2: Component Skill
- dash-components Skill (builds on plotly-viz)
- Test with real dashboard component creation

### Phase 3: Quality Skills
- accessibility-audit Skill (validates plotly-viz output)
- performance-optimizer Skill (optimizes all code)
- Test integration with `/workflow:verify`

### Phase 4: Integration & Validation
- Test all 5 Skills together
- Verify token budgets
- End-to-end dashboard creation
- Validate against success criteria

---

## Review & Acceptance Checklist

### Completeness
- [ ] All 5 Production Skills have clear user stories
- [ ] All 100 functional requirements defined (FR-001 to FR-100)
- [ ] All 35 success criteria are measurable (SC-001 to SC-035)
- [ ] Edge cases documented with resolution strategies
- [ ] Key entities identified with attributes and relationships
- [ ] Clarifications address potential ambiguities

### Clarity
- [ ] Production Skills vs Development Skills distinction is clear
- [ ] Progressive disclosure pattern is well-explained for all Skills
- [ ] Activation triggers documented for each Skill
- [ ] Token budgets specified (Level 1: 50, Level 2: 800, Level 3: variable)
- [ ] Integration with Commands and MCP is explained
- [ ] WCAG 2.1 AA compliance approach is clear
- [ ] Performance targets are specific (<3s load, <1s callbacks)

### Testability
- [ ] Each user story has concrete acceptance scenarios
- [ ] Success criteria can be measured objectively
- [ ] Activation scenarios are testable
- [ ] Token budgets can be validated programmatically
- [ ] Accessibility compliance can be verified
- [ ] Performance targets can be measured

### Alignment with Constitution
- [ ] Spec-first approach maintained
- [ ] No time estimates included
- [ ] Quality standards specified (95%+ accuracy, 4.5/5.0 ratings)
- [ ] All requirements use "System MUST" language
- [ ] Accessibility and performance emphasized

### Feasibility
- [ ] Skills can be implemented with Claude Code
- [ ] Token budgets are realistic
- [ ] Progressive disclosure pattern proven (spec 003)
- [ ] Dependencies available (spec 002 approved, spec 003 complete)
- [ ] WCAG checking is automatable
- [ ] Performance profiling is practical

---

**Next Steps**:
1. **Review this specification** - Validate requirements, success criteria, scope
2. **Approve specification** - Mark as "approved" when ready
3. **Create plan.md** - Define technical approach and content structure for each Skill
4. **Create tasks.md** - Break down into actionable implementation tasks
5. **Implement** - Following 4-phase plan (data/viz → components → quality → integration)

---

**Status**: Draft
**Dependencies**: Spec 002 (approved), Spec 003 (to be completed)
**Blocks**: Spec 002 implementation (Phases 5-6)
**Version**: 1.0.0
**Last Updated**: 2025-11-10
