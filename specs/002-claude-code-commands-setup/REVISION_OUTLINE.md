# Spec 002 Revision Outline
## Integrating Hybrid Workflow Architecture & Agent Skills

**Date**: 2025-11-10
**Purpose**: Plan comprehensive revision to integrate Agent Skills in extreme depth

---

## Structure Overview

### 1. Header & Metadata
- Feature Branch (unchanged)
- Status: Draft - Awaiting Review
- Input: Add "hybrid workflow" and "Agent Skills"

### 2. Overview ✨ MAJOR REVISION
**Current**: EPIC methodology, command categories
**Revised**:
- Introduce two-process model (Spec-Kit planning vs Claude Code execution)
- Explain handoff mechanism via tasks.md
- Introduce Skills as third pillar (Commands, Sub-Agents, Skills)
- Reference WORKFLOW.md for detailed architecture

**Key Principles** (updated):
- Spec-First (unchanged)
- Hybrid Workflow: Spec-Kit (planning) + Claude Code (execution)
- Agent Skills: Auto-invoked domain expertise
- Namespaced Commands: /spec:*, /workflow:*, /utils:*
- Progressive Disclosure: Skills load in 3 levels

### 3. NEW SECTION: Agent Skills Architecture ✨ EXTREMELY DETAILED
**Size**: ~3000-4000 tokens (this is the main addition)

#### 3.1 Skills vs Commands vs Sub-Agents
- Definition matrix
- When to use each
- How they complement each other

#### 3.2 Progressive Disclosure Pattern
- Three-level loading explained in detail
- Token budgets per level
- Example with actual file content

#### 3.3 Development Skills (For Building This System)
For each skill:
- Name, description (50 tokens)
- Purpose and when it activates
- Directory structure
- SKILL.md outline
- Reference files
- Example activation scenario

Skills:
1. **spec-kit-workflow** - Spec-driven development methodology
2. **claude-code-architecture** - Commands/Agents/Skills/Hooks expertise
3. **research-synthesis** - Reference documentation analysis

#### 3.4 Production Skills (For Dashboard Developers)
For each skill:
- Name, description (50 tokens)
- Purpose and when it activates
- Directory structure
- SKILL.md outline
- Reference files
- Example activation scenario

Skills:
1. **data-analysis** - Statistical analysis, EDA, data quality
2. **plotly-viz** - Chart generation, accessibility, theming
3. **dash-components** - Component patterns, callbacks, layouts
4. **accessibility-audit** - WCAG 2.1 AA compliance checking
5. **performance-optimizer** - Bottleneck detection, optimization

#### 3.5 Skills Integration with Commands
- Show how /workflow:* commands benefit from Skills
- Complete workflow example with Skills auto-activating
- Token usage comparison (with vs without progressive disclosure)

#### 3.6 Skills vs MCP: Complementary Relationship
- MCP provides WHAT (data access)
- Skills provide HOW (methodology)
- Commands provide WHEN (workflow)
- Example showing all three working together

### 4. User Scenarios & Testing - UPDATE EXISTING
**Changes**:
- Update User Story 2: "EPIC" → "Workflow" (Spec-Kit + Claude Code)
- Add Skills mentions in acceptance scenarios
- Show Skills auto-activating during commands

User Stories (updated):
1. Specification Workflow Commands (/spec:*) - Add Skills activation
2. Hybrid Workflow Commands (/workflow:*) - Rename from "EPIC", add Skills
3. Utility Commands (/utils:*) - Minor updates
4. Dash-Specific Commands - Combine into /workflow:* context
5. Specialized Sub-Agents - Show distinction from Skills
6. Command Discovery - Unchanged

### 5. Requirements - MAJOR ADDITIONS
**Add new sections**:

#### FR-061 to FR-090: Agent Skills Requirements (30 new requirements)

**Skills Architecture** (FR-061 to FR-070):
- FR-061: System MUST support Skills with progressive disclosure
- FR-062: Skills MUST use three-level loading (metadata → core → references)
- FR-063: Skills MUST auto-activate based on context matching
- FR-064: Skills MUST be organized by process (development/ vs production/)
- FR-065: Each Skill MUST have SKILL.md with metadata YAML
- FR-066: Skills MUST define allowed-tools in YAML frontmatter
- FR-067: System MUST load Level 1 (metadata) at startup (~50 tokens/skill)
- FR-068: System MUST load Level 2 (core) when Skill activates (~800 tokens)
- FR-069: System MUST load Level 3 (references) on-demand (variable size)
- FR-070: Skills MUST NOT conflict with Commands or Sub-Agents

**Development Skills** (FR-071 to FR-075):
- FR-071: System MUST provide spec-kit-workflow Skill
- FR-072: System MUST provide claude-code-architecture Skill
- FR-073: System MUST provide research-synthesis Skill
- FR-074: Development Skills MUST activate during planning commands
- FR-075: Development Skills MUST include reference documentation

**Production Skills** (FR-076 to FR-085):
- FR-076: System MUST provide data-analysis Skill
- FR-077: System MUST provide plotly-viz Skill
- FR-078: System MUST provide dash-components Skill
- FR-079: System MUST provide accessibility-audit Skill
- FR-080: System MUST provide performance-optimizer Skill
- FR-081: Production Skills MUST activate during workflow commands
- FR-082: plotly-viz Skill MUST ensure WCAG 2.1 AA compliance
- FR-083: data-analysis Skill MUST support CSV, JSON, Parquet, SQL
- FR-084: accessibility-audit Skill MUST check color contrast, keyboard nav, ARIA
- FR-085: performance-optimizer Skill MUST target <3s load, <1s callbacks

**Skills Integration** (FR-086 to FR-090):
- FR-086: Skills MUST enhance Commands without replacing them
- FR-087: Skills MUST be discoverable via description matching
- FR-088: Skills MUST work with MCP servers (complementary)
- FR-089: Skills MUST include example activation scenarios
- FR-090: Skills MUST be version-controlled in .claude/skills/

#### Update Command Requirements (FR-001 to FR-060)
- Change command naming: /spec.* → /spec:*
- Change workflow naming: /workflow.* → /workflow:*
- Change utils naming: /utils.* → /utils:*
- Remove /dash.* as separate category (integrate into /workflow:*)
- Reference WORKFLOW.md for two-process model

### 6. Key Entities - ADD NEW ENTITIES
**Add**:
- **Agent Skill**: Domain knowledge with progressive disclosure
  - Attributes: name, description, directory structure, loading levels, allowed-tools
  - Relationships: Auto-activates during Commands, complements MCP, distinct from Sub-Agents

- **Skill Level**: Progressive disclosure tier
  - Attributes: level number (1-3), token budget, content type
  - Relationships: Belongs to Skill, loads sequentially

### 7. Success Criteria - ADD SKILLS METRICS
**Add** (SC-031 to SC-045):

**Skills Effectiveness**:
- SC-031: Skills activate correctly 95%+ of the time based on context
- SC-032: Progressive disclosure reduces context usage by 60%+ vs loading all
- SC-033: Development Skills reduce spec creation time by 40%+
- SC-034: Production Skills improve code quality (accessibility, performance)
- SC-035: Skill activation latency: <2 seconds for Level 2 load

**Skills Adoption**:
- SC-036: Dashboard developers use Skills without explicit invocation 90%+ of time
- SC-037: Skills documentation clarity: 4.5/5.0 rating
- SC-038: Skill-enhanced commands produce better output 80%+ of time

**Skills Maintenance**:
- SC-039: Skills remain under token budgets (50/800/variable per level)
- SC-040: Skills update without breaking existing workflows
- SC-041: Skill conflicts occur <1% of activations

**Integration Metrics**:
- SC-042: Commands + Skills complete tasks 30% faster than Commands alone
- SC-043: MCP + Skills integration works seamlessly 100% of time
- SC-044: Sub-Agents benefit from Skills when applicable
- SC-045: Zero Skills loaded when not needed (efficient discovery)

### 8. Clarifications - ADD MAJOR CLARIFICATIONS
**Add**:

#### Q6: What's the difference between Skills and Commands?
- Commands: User-invoked workflows (/workflow:act)
- Skills: Model-invoked knowledge (auto-loads when relevant)
- Integration example showing both working together

#### Q7: What's the difference between Skills and Sub-Agents?
- Skills: Shared context, progressive disclosure, domain knowledge
- Sub-Agents: Isolated context, parallel execution, task completion
- Decision matrix for choosing

#### Q8: How does progressive disclosure work?
- Detailed three-level explanation
- Token budget breakdown
- Trade-offs vs MCP upfront loading

#### Q9: What Skills should I create for my use case?
- Development Skills for building system
- Production Skills for dashboard development
- Optional Skills for specific needs

#### Q10: How do Skills work with the hybrid workflow?
- Spec-Kit planning phase: Development Skills
- Claude Code execution phase: Production Skills
- Handoff at tasks.md
- Skills enhance both processes

### 9. Dependencies - UPDATE
**Add**:
- Research documents in specs/research/
- WORKFLOW.md for two-process architecture
- Agent Skills research and analysis

### 10. Implementation Phases - MAJOR REVISION
**Revise to**:

#### Phase 1: Core Architecture Setup (Week 1)
- .claude/ directory structure
- settings.json configuration
- Command namespacing (/spec:*, /workflow:*, /utils:*)
- Documentation framework

#### Phase 2: Specification Commands (Week 2)
- Implement /spec:* commands
- Create spec-kit-workflow Skill (development)
- Test spec creation workflow

#### Phase 3: Development Skills (Week 3)
- Implement claude-code-architecture Skill
- Implement research-synthesis Skill
- Test Skills integration with /spec:* commands
- Validate progressive disclosure

#### Phase 4: Workflow Commands (Week 4)
- Implement /workflow:* commands (research, implement, verify, next)
- Integrate with hybrid workflow architecture
- Test with sample feature

#### Phase 5: Production Skills - Core (Week 5)
- Implement data-analysis Skill
- Implement plotly-viz Skill
- Implement dash-components Skill
- Test Skills auto-activation during /workflow:implement

#### Phase 6: Production Skills - Extended (Week 6)
- Implement accessibility-audit Skill
- Implement performance-optimizer Skill
- Test WCAG compliance automation
- Performance optimization validation

#### Phase 7: Utility Commands & Sub-Agents (Week 7)
- Implement /utils:* commands
- Implement Sub-Agents (component-builder, data-pipeline, test-engineer)
- Test parallel execution with Skills
- Coordination validation

#### Phase 8: Integration & Documentation (Week 8)
- End-to-end testing with real dashboard feature
- Documentation and examples
- CLAUDE.md creation (project instructions)
- User acceptance testing

### 11. Review & Acceptance Checklist - UPDATE
**Add checks for**:
- [ ] Agent Skills architecture is comprehensive and clear
- [ ] Progressive disclosure is explained in extreme detail
- [ ] Development Skills and Production Skills are distinguished
- [ ] Skills integration with Commands is well-documented
- [ ] Skills vs MCP relationship is clarified
- [ ] All Skills have directory structure and SKILL.md outline
- [ ] Hybrid workflow architecture is integrated throughout
- [ ] Namespaced commands are used consistently

---

## Revision Approach

### Step 1: Complete new "Agent Skills Architecture" section
This is the major addition, ~3000-4000 tokens of extremely detailed content.

### Step 2: Update Overview
Introduce two-process model, Skills as third pillar.

### Step 3: Revise User Stories
Add Skills mentions, update EPIC → hybrid workflow.

### Step 4: Add Skills Requirements (FR-061 to FR-090)
30 new functional requirements covering Skills architecture.

### Step 5: Add Skills Success Criteria (SC-031 to SC-045)
15 new measurable outcomes for Skills.

### Step 6: Add Clarifications
Q6-Q10 covering Skills, progressive disclosure, hybrid workflow.

### Step 7: Revise Implementation Phases
8 phases including Skills development.

### Step 8: Update Review Checklist
Add Skills-specific validation items.

---

## Token Budget Estimate

**Current spec**: ~6500 tokens
**Revised spec**: ~15,000-18,000 tokens

**Major additions**:
- Agent Skills Architecture section: +4000 tokens
- Skills Requirements: +1500 tokens
- Skills Success Criteria: +800 tokens
- Skills Clarifications: +1200 tokens
- Updated User Stories: +1000 tokens
- Revised Implementation Phases: +500 tokens

**Total increase**: ~9000 tokens (140% larger)

This is justified by user's request for "extremely in depth" Skills documentation.

---

## Next Steps

1. Write the complete "Agent Skills Architecture" section
2. Revise the spec 002 file section by section
3. Validate all cross-references
4. Request user review

**Status**: Ready to begin revision
