# Production Skills

This directory contains Production Skills that support dashboard developers using the Claude Code system.

Skills are defined in **Spec 004: Agent Skills - Production**.

## Skills to be Implemented

These skills will be created when implementing Spec 004:

1. **data-analysis**
   - Purpose: Statistical analysis, exploratory data analysis (EDA), data quality checking
   - Activation: When loading .csv/.json/.parquet files, using pandas/SQL
   - Provides: EDA workflows, quality checks, visualization recommendations

2. **plotly-viz**
   - Purpose: Chart generation with WCAG 2.1 AA compliance
   - Activation: When creating charts, mentions "visualization", "plot", "chart"
   - Provides: Chart selection guide, accessible color palettes, Plotly patterns

3. **dash-components**
   - Purpose: Component patterns, callback architecture, layouts, state management
   - Activation: When creating Dash components, writing callbacks
   - Provides: Component patterns, callback best practices, state management

4. **accessibility-audit**
   - Purpose: WCAG 2.1 Level AA compliance validation
   - Activation: When running `/workflow.verify`, mentions "accessibility"
   - Provides: WCAG checklist, color contrast checking, keyboard nav testing

5. **performance-optimizer**
   - Purpose: Bottleneck detection and optimization (targets: <3s load, <1s callbacks)
   - Activation: When performance issues detected, mentions "slow", "optimize"
   - Provides: Bottleneck identification, caching strategies, profiling methods

## Implementation Status

**Current**: Placeholder directory (Phase 1 - Spec 002)
**Next**: Skills will be implemented in Phase 3 (Spec 004)

See `specs/004-agent-skills-production/spec.md` for complete details.
