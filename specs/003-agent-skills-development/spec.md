# Feature Specification: Agent Skills - Development

**Feature Branch**: `003-agent-skills-development`
**Created**: 2025-11-10
**Status**: Approved
**Approved Date**: 2025-11-13
**Input**: Create 3 Development Skills (spec-kit-workflow, claude-code-architecture, research-synthesis) to support building the Claude Code dashboard development system

## Overview

This specification defines the Development Skills required to build the Claude Code setup for spec-driven dashboard development. These Skills provide domain expertise that auto-activates when we (the developers) are creating the system itself—writing specs, designing architecture, and researching best practices.

**Development Skills** are distinct from **Production Skills** (spec 004). Development Skills support the meta-level task of building the Claude Code system, while Production Skills support dashboard developers using that system.

**The 3 Development Skills**:

1. **spec-kit-workflow** - Guides specification creation following GitHub's spec-kit methodology
2. **claude-code-architecture** - Provides expertise on Commands, Skills, Sub-Agents, and Hooks
3. **research-synthesis** - Helps analyze reference implementations and extract patterns

**Progressive Disclosure**: All Skills implement three-level loading (metadata → core → references) to maintain lean context while providing deep expertise on-demand.

**Integration**: Skills auto-activate during `/spec:*` commands and when working with specs/, .claude/, or reference documentation.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Spec-Kit Workflow Skill (Priority: P1)

As a **developer building the Claude Code system**, I want the `spec-kit-workflow` Skill to guide me through creating specifications so that I follow the spec-kit methodology correctly and produce complete, high-quality specs.

**Why this priority**: This is foundational. We use spec-kit methodology for all features, and this Skill ensures consistency and completeness.

**Independent Test**: Can be tested by creating a spec and verifying the Skill provides correct templates, validation, and guidance.

**Acceptance Scenarios**:

1. **Given** I start creating a new spec, **When** I open a spec.md file, **Then** the `spec-kit-workflow` Skill activates automatically and provides the spec template structure

2. **Given** I'm writing user stories, **When** the Skill is active, **Then** it suggests the format "As a [role], I want [goal] so that [benefit]" and provides examples

3. **Given** I'm defining requirements, **When** the Skill is active, **Then** it guides me to use FR-NNN format with "System MUST" language and clear validation criteria

4. **Given** I'm writing success criteria, **When** the Skill is active, **Then** it ensures criteria are measurable with specific targets (e.g., "95%+", "<2 seconds")

5. **Given** I've drafted a spec, **When** I request validation, **Then** the Skill checks completeness against constitution and spec-kit standards

6. **Given** I need examples, **When** I reference the Skill, **Then** it loads Level 3 content with example specs from reference implementations

---

### User Story 2 - Claude Code Architecture Skill (Priority: P1)

As a **developer building the Claude Code system**, I want the `claude-code-architecture` Skill to help me make architectural decisions so that I choose the right mechanism (Command, Skill, Sub-Agent, Hook) for each use case.

**Why this priority**: Critical for correct architecture. Making the wrong choice (e.g., Command vs Skill) leads to poor user experience or inefficient context usage.

**Independent Test**: Can be tested by asking architectural questions and verifying the Skill provides correct decision guidance.

**Acceptance Scenarios**:

1. **Given** I need to decide between Command and Skill, **When** I describe the use case, **Then** the Skill provides a decision matrix and recommendation

2. **Given** I'm creating a new Command, **When** the Skill activates, **Then** it provides the Markdown + YAML frontmatter format and naming conventions (/category:action)

3. **Given** I'm creating a new Skill, **When** the Skill activates, **Then** it provides the SKILL.md structure with Level 1/2/3 organization and token budgets

4. **Given** I'm designing Sub-Agents, **When** the Skill activates, **Then** it explains coordination strategies (file locking, queue-based) and context isolation

5. **Given** I need to configure settings.json, **When** the Skill activates, **Then** it provides the structure for permissions, hooks, and workflow settings

6. **Given** I reference detailed architecture docs, **When** needed, **Then** the Skill loads Level 3 content from research files (claude-code-final-architecture.md)

---

### User Story 3 - Research Synthesis Skill (Priority: P2)

As a **developer building the Claude Code system**, I want the `research-synthesis` Skill to help me analyze reference implementations and documentation so that I can extract best practices and create implementation guidance.

**Why this priority**: Important for quality but not blocking. We can manually research, but the Skill makes it more systematic and thorough.

**Independent Test**: Can be tested by providing reference code/docs and verifying the Skill extracts patterns correctly.

**Acceptance Scenarios**:

1. **Given** I have cloned a reference repository, **When** I ask to analyze it, **Then** the Skill guides a systematic analysis process (discovery, analysis, synthesis)

2. **Given** I'm examining code patterns, **When** the Skill is active, **Then** it suggests using Glob to find file patterns and Grep to search for specific implementations

3. **Given** I've found relevant code, **When** analyzing, **Then** the Skill helps identify architectural patterns, best practices, and common pitfalls

4. **Given** I'm synthesizing findings, **When** creating documentation, **Then** the Skill provides templates for research reports and implementation guides

5. **Given** I need detailed analysis techniques, **When** the Skill loads Level 3, **Then** it provides ANALYSIS_METHODS.md and PATTERN_EXTRACTION.md references

6. **Given** I'm documenting findings, **When** creating examples, **Then** the Skill guides creating clear, reusable example code with explanations

---

### Edge Cases

- **What happens when** I'm working on a spec but the `spec-kit-workflow` Skill doesn't activate?
  - System should detect .md files in specs/ directory and activate based on file path or content keywords like "## User Scenarios"

- **What happens when** I ask an architectural question but the `claude-code-architecture` Skill provides outdated information?
  - Skill content must be version-controlled and updated when Claude Code evolves; Level 3 references should include version notes

- **What happens when** the `research-synthesis` Skill suggests analysis methods that don't apply to the reference material?
  - Skill should provide multiple analysis approaches and let user select appropriate method based on material type

- **What happens when** multiple Development Skills activate simultaneously (e.g., researching architecture patterns)?
  - Skills should complement each other without conflicts; research-synthesis guides process, claude-code-architecture provides domain knowledge

- **What happens when** Skills exceed token budgets (Level 1: 50, Level 2: 800)?
  - CI/CD validation should catch this during development; Skills must be refactored to meet budgets

- **What happens when** a Skill's Level 3 references are too large for context?
  - Use progressive loading within Level 3 (load one reference file at a time); provide summaries in Level 2

---

## Requirements *(mandatory)*

### Functional Requirements

#### Spec-Kit Workflow Skill (FR-001 to FR-015)

- **FR-001**: System MUST provide `spec-kit-workflow` Skill with metadata describing spec-driven development guidance
- **FR-002**: Skill MUST activate when working with spec.md, plan.md, or tasks.md files in specs/ directory
- **FR-003**: Skill MUST activate when keywords match: "specification", "requirements", "user stories", "success criteria"
- **FR-004**: Level 1 (metadata) MUST be 40-60 tokens describing spec-kit methodology
- **FR-005**: Level 2 (core) MUST be 600-1000 tokens covering Constitution → Specify → Plan → Tasks workflow
- **FR-006**: Level 2 MUST include spec template structure, requirement formats (FR-NNN), success criteria patterns
- **FR-007**: Level 3 (references) MUST include SPEC_TEMPLATE.md, PLAN_TEMPLATE.md, TASKS_TEMPLATE.md
- **FR-008**: Level 3 MUST include CONSTITUTION_GUIDE.md for alignment checking
- **FR-009**: Level 3 MUST include examples/ directory with reference specs, plans, and tasks
- **FR-010**: Skill MUST provide validation guidance for checking spec completeness
- **FR-011**: Skill MUST enforce "no time estimates" rule from constitution
- **FR-012**: Skill MUST guide writing measurable success criteria with specific targets
- **FR-013**: Skill MUST suggest user story format: "As a [role], I want [goal] so that [benefit]"
- **FR-014**: Skill MUST guide requirement writing with "System MUST" language and clear validation
- **FR-015**: Skill directory structure MUST be: `.claude/skills/development/spec-kit-workflow/`

---

#### Claude Code Architecture Skill (FR-016 to FR-030)

- **FR-016**: System MUST provide `claude-code-architecture` Skill with metadata describing architectural expertise
- **FR-017**: Skill MUST activate when working with .claude/ directory or discussing architectural decisions
- **FR-018**: Skill MUST activate when keywords match: "command", "skill", "sub-agent", "hook", "architecture"
- **FR-019**: Level 1 (metadata) MUST be 40-60 tokens describing Commands/Skills/Sub-Agents/Hooks expertise
- **FR-020**: Level 2 (core) MUST be 600-1000 tokens covering decision matrix for choosing mechanisms
- **FR-021**: Level 2 MUST include Command format (Markdown + YAML), Skill format (SKILL.md + levels), Sub-Agent format
- **FR-022**: Level 2 MUST explain when to use each mechanism with clear criteria
- **FR-023**: Level 3 (references) MUST include COMMANDS_GUIDE.md, SUBAGENTS_GUIDE.md, SKILLS_GUIDE.md, HOOKS_GUIDE.md
- **FR-024**: Level 3 MUST include DECISION_MATRIX.md with detailed comparison table
- **FR-025**: Level 3 MUST include reference/ directory with claude-code-final-architecture.md and complete-architecture-quick-reference.md
- **FR-026**: Level 3 MUST include examples/ directory with example command, sub-agent, and skill
- **FR-027**: Skill MUST provide settings.json structure and configuration guidance
- **FR-028**: Skill MUST explain progressive disclosure pattern for Skills (50 → 800 → variable tokens)
- **FR-029**: Skill MUST explain coordination strategies for Sub-Agents (file locking, queue-based)
- **FR-030**: Skill directory structure MUST be: `.claude/skills/development/claude-code-architecture/`

---

#### Research Synthesis Skill (FR-031 to FR-042)

- **FR-031**: System MUST provide `research-synthesis` Skill with metadata describing analysis and synthesis capabilities
- **FR-032**: Skill MUST activate when analyzing reference repositories, documentation, or research tasks
- **FR-033**: Skill MUST activate when keywords match: "research", "analyze", "reference", "patterns", "best practices"
- **FR-034**: Level 1 (metadata) MUST be 40-60 tokens describing research and analysis methodology
- **FR-035**: Level 2 (core) MUST be 600-1000 tokens covering research process (discovery → analysis → synthesis)
- **FR-036**: Level 2 MUST include guidance on using Glob for finding files and Grep for searching code
- **FR-037**: Level 2 MUST include pattern extraction techniques and architecture analysis methods
- **FR-038**: Level 3 (references) MUST include ANALYSIS_METHODS.md with detailed research techniques
- **FR-039**: Level 3 MUST include PATTERN_EXTRACTION.md with code pattern identification methods
- **FR-040**: Level 3 MUST include DOCUMENTATION_GUIDE.md for creating research reports and guides
- **FR-041**: Level 3 MUST include templates/ directory with research-report.md and implementation-guide.md templates
- **FR-042**: Skill directory structure MUST be: `.claude/skills/development/research-synthesis/`

---

#### General Skills Requirements (FR-043 to FR-055)

- **FR-043**: All Development Skills MUST implement three-level progressive disclosure (metadata → core → references)
- **FR-044**: All Skills MUST have SKILL.md as primary file with YAML frontmatter and Markdown content
- **FR-045**: All Skills MUST declare allowed-tools in YAML frontmatter (e.g., [Read, Write, Edit, Bash])
- **FR-046**: All Skills MUST reside in `.claude/skills/development/` directory
- **FR-047**: Skills MUST NOT activate during production dashboard development (only when building the system)
- **FR-048**: Skills MUST auto-activate based on description keyword matching (no explicit user invocation)
- **FR-049**: Skills MUST be version-controlled in git (no .gitignore exclusions)
- **FR-050**: Skills MUST include activation trigger documentation in SKILL.md
- **FR-051**: Skills MUST include example activation scenarios in SKILL.md or examples/
- **FR-052**: Skills content MUST align with constitution principles (spec-first, quality standards)
- **FR-053**: Skills MUST NOT conflict with each other (complementary, not competing)
- **FR-054**: Skills MUST work correctly when multiple activate simultaneously
- **FR-055**: Skills updates MUST NOT break existing workflows (backward compatibility)

---

### Key Entities

- **Development Skill**: Domain expertise for building the Claude Code system
  - Attributes: name, description, activation triggers, directory structure, token budgets per level
  - Relationships: Auto-activates during system development, complements `/spec:*` commands, distinct from Production Skills (spec 004)

- **Skill Level Content**: Progressive disclosure tier content
  - Attributes: level (1/2/3), token budget, file location, content type (metadata/core/references)
  - Relationships: Belongs to Development Skill, loads sequentially based on need

- **Reference Material**: Level 3 detailed documentation
  - Attributes: filename, token count, topic, format (MD/py/examples)
  - Relationships: Part of Skill Level 3, loaded on-demand via Read tool

- **Activation Trigger**: Keyword or condition that causes Skill to activate
  - Attributes: trigger type (keyword/file-path/context), pattern, priority
  - Relationships: Defined in Skill metadata, matched by Claude during operation

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

#### Spec-Kit Workflow Skill Effectiveness

- **SC-001**: Skill activates correctly 95%+ of the time when working with spec files
- **SC-002**: Specs created with Skill assistance are complete (all required sections present) 98%+ of the time
- **SC-003**: Spec validation catches incomplete sections 100% of the time
- **SC-004**: Developers can create specs 40%+ faster with Skill than without
- **SC-005**: Spec quality score (constitution alignment) averages 4.5/5.0 or higher
- **SC-006**: Zero specs violate "no time estimates" rule when Skill is active

---

#### Claude Code Architecture Skill Effectiveness

- **SC-007**: Skill provides correct architectural recommendations 95%+ of the time
- **SC-008**: Developers make correct Command vs Skill vs Sub-Agent decisions 90%+ of the time with Skill guidance
- **SC-009**: Commands created with Skill follow correct format (YAML + Markdown) 100% of the time
- **SC-010**: Skills created with Skill meet token budgets (Level 1: 50, Level 2: 800) 95%+ of the time
- **SC-011**: Settings.json configurations created with Skill are valid JSON 100% of the time
- **SC-012**: Architectural decisions documented with Skill reference level 3 content 80%+ of the time

---

#### Research Synthesis Skill Effectiveness

- **SC-013**: Skill helps identify relevant code patterns 85%+ of the time
- **SC-014**: Research reports created with Skill are comprehensive and well-structured 90%+ of the time
- **SC-015**: Pattern extraction using Skill finds 30%+ more patterns than manual review
- **SC-016**: Implementation guides created with Skill are clear and actionable (4.0/5.0+ rating)
- **SC-017**: Skill reduces research time by 25%+ compared to unguided research

---

#### Overall Development Skills Performance

- **SC-018**: All 3 Development Skills stay within token budgets (Level 1: 50, Level 2: 800) 95%+ of the time
- **SC-019**: Skills activate automatically (no explicit invocation) 90%+ of the time
- **SC-020**: Multiple Skills work together without conflicts 100% of the time
- **SC-021**: Skills context usage is 70%+ less than loading all content upfront
- **SC-022**: Developers rate Skills clarity and usefulness 4.5/5.0 or higher
- **SC-023**: Skills are updated and maintained with zero breakage to existing workflows
- **SC-024**: Level 3 content loads on-demand (not preloaded) 100% of the time
- **SC-025**: Skills documentation is clear enough that new developers can use them without training

---

## Non-Functional Requirements

### Performance
- Skill activation latency: <2 seconds (from context match to Level 2 loaded)
- Level 3 file loading: <1 second per reference file
- No noticeable delay when Skills auto-activate during normal workflow

### Usability
- Skill activation is transparent (developers don't need to think about it)
- Skill content is clear, concise, and actionable
- Examples are realistic and directly applicable
- Error messages (if any) are helpful and specific

### Reliability
- Skills activate consistently based on triggers 95%+ of the time
- Skills provide correct, up-to-date information 98%+ of the time
- Skills gracefully handle edge cases (unclear context, missing files)
- Skills don't activate inappropriately (false positive rate <5%)

### Maintainability
- Skill content is version-controlled in git
- Skills are easy to update (Markdown files, no complex build process)
- Token budgets are enforced via automated checks (CI/CD)
- Skills are modular (one Skill per domain, minimal coupling)

### Compatibility
- Skills work in Claude Code environment (primary)
- Skills can be deployed via Claude Agent SDK (future)
- Skills integrate seamlessly with Commands and Sub-Agents
- Skills complement MCP servers (don't conflict)

---

## Technology Stack

### Required
- **Claude Code**: Development environment with Skills support
- **Markdown**: SKILL.md file format
- **YAML**: Frontmatter for metadata
- **Git**: Version control for Skill content

### Skills Implementation
- SKILL.md files in `.claude/skills/development/`
- Progressive disclosure pattern (three levels)
- Auto-activation via description matching
- Reference files in Markdown and Python formats

---

## Out of Scope

The following are explicitly **not** included in this specification:

- Production Skills (those are in spec 004: Agent Skills - Production)
- MCP server integration (that's in spec 005: MCP Integration)
- Command implementations (those are in spec 002: Claude Code Commands Setup)
- Sub-Agent implementations (those are in spec 002: Claude Code Commands Setup)
- Actual Claude Code configuration (that's implementation, not Skills content)
- Skills for non-development contexts (e.g., skills for dashboard users)

---

## Clarifications

### Q1: How are Development Skills different from Production Skills?

**A**: Development Skills support **us** building the Claude Code system. Production Skills support **dashboard developers** using that system.

**Development Skills activate when**:
- Creating specs (spec-kit-workflow)
- Designing architecture (claude-code-architecture)
- Researching references (research-synthesis)

**Production Skills activate when** (spec 004):
- Analyzing data (data-analysis)
- Creating charts (plotly-viz)
- Building components (dash-components)

**Example**:
- **Development**: Creating spec 003 → spec-kit-workflow Skill activates
- **Production**: Implementing a dashboard → plotly-viz Skill activates

---

### Q2: Why do we need separate specs for Development Skills vs Production Skills?

**A**: Different business requirements and different implementation details.

**Development Skills**:
- Focus: Supporting system creation
- Users: Us (developers building Claude Code setup)
- Content: Spec-kit, architecture, research methods
- Spec: This one (003)

**Production Skills**:
- Focus: Supporting dashboard development
- Users: Dashboard developers (end users of our system)
- Content: Data analysis, visualization, Dash patterns
- Spec: 004

Separation keeps each spec focused and manageable.

---

### Q3: What if a Skill's Level 2 content exceeds 800 tokens?

**A**: Refactor to move detailed content to Level 3.

**Level 2 should contain**:
- Essential workflow (Quick Start)
- Core patterns (80% of use cases)
- Brief examples

**Level 3 should contain**:
- Detailed methodologies
- Complete reference guides
- Extensive examples
- Edge cases and advanced topics

**If Level 2 is too large**: Split content, move details to new Level 3 files, update Level 2 to reference them.

---

### Q4: How do these Skills integrate with `/spec:*` commands?

**A**: Skills auto-activate during command execution, enhancing the command with domain expertise.

**Example with `/spec:specify` command**:
```
User: /spec:specify Create sales dashboard

1. Command /spec:specify runs:
   - Creates specs/NNN-sales-dashboard/spec.md
   - Prompts for user stories, requirements

2. spec-kit-workflow Skill activates (auto):
   - Detects spec.md file creation
   - Provides spec template
   - Guides requirement writing
   - Suggests success criteria format

3. Result: Complete spec following spec-kit methodology
```

Command provides STRUCTURE (create file, prompt for sections).
Skill provides EXPERTISE (templates, formats, best practices).

---

### Q5: Can these Skills be used outside of building this specific project?

**A**: Yes, they're reusable for any spec-driven development.

**spec-kit-workflow**: Useful for any project using spec-kit methodology
**claude-code-architecture**: Useful for any Claude Code project
**research-synthesis**: Useful for any project requiring reference analysis

**Customization**: Content can be updated for specific domains, but the structure is general-purpose.

**Portability**: Skills are Markdown files in git, easy to copy to other projects.

---

## Dependencies

### Prerequisites
- Spec 002 (Claude Code Commands Setup) approved
- `.claude/skills/development/` directory exists
- Understanding of progressive disclosure pattern
- Familiarity with spec-kit methodology

### Internal Dependencies
- specs/memory/constitution.md (alignment checking)
- specs/templates/ (spec, plan, tasks templates)
- specs/research/agent-skills-integration-analysis.md (Skills architecture understanding)
- specs/WORKFLOW.md (hybrid workflow architecture)

### External Dependencies
- Claude Code with Skills support
- Git for version control
- Markdown and YAML tooling

---

## Implementation Phases

**Note**: This spec defines WHAT the Development Skills must accomplish. The HOW (implementation details, file contents, token optimization) goes in plan.md.

### Phase 1: spec-kit-workflow Skill
- Create directory structure
- Write SKILL.md (Levels 1 & 2)
- Create Level 3 reference files (templates, examples, guide)
- Test activation and content quality

### Phase 2: claude-code-architecture Skill
- Create directory structure
- Write SKILL.md (Levels 1 & 2)
- Create Level 3 reference files (guides, decision matrix, examples)
- Test architectural decision guidance

### Phase 3: research-synthesis Skill
- Create directory structure
- Write SKILL.md (Levels 1 & 2)
- Create Level 3 reference files (methods, templates)
- Test research workflow support

### Phase 4: Integration & Validation
- Test all 3 Skills activating appropriately
- Verify token budgets met
- Test with `/spec:*` commands
- Validate against success criteria

---

## Review & Acceptance Checklist

### Completeness
- [ ] All 3 Development Skills have clear user stories
- [ ] All 55 functional requirements defined (FR-001 to FR-055)
- [ ] All 25 success criteria are measurable (SC-001 to SC-025)
- [ ] Edge cases documented with resolution strategies
- [ ] Key entities identified with attributes and relationships
- [ ] Clarifications address potential ambiguities

### Clarity
- [ ] Development Skills vs Production Skills distinction is clear
- [ ] Progressive disclosure pattern is well-explained
- [ ] Activation triggers are documented for each Skill
- [ ] Token budgets are specified (Level 1: 50, Level 2: 800, Level 3: variable)
- [ ] Integration with Commands is explained

### Testability
- [ ] Each user story has concrete acceptance scenarios
- [ ] Success criteria can be measured objectively
- [ ] Activation scenarios are testable
- [ ] Token budgets can be validated programmatically

### Alignment with Constitution
- [ ] Spec-first approach maintained (implementation details in plan.md)
- [ ] No time estimates included
- [ ] Quality standards specified (95%+ accuracy, 4.5/5.0 ratings)
- [ ] All requirements use "System MUST" language

### Feasibility
- [ ] Skills can be implemented with Claude Code
- [ ] Token budgets are realistic for content needed
- [ ] Progressive disclosure pattern is well-understood
- [ ] Dependencies are available (spec 002 approved)

### Dependencies
- [ ] Spec 002 approved (prerequisite)
- [ ] Directory structure from spec 002 available
- [ ] No blocking external dependencies

---

**Next Steps**:
1. **Review this specification** - Validate requirements, success criteria, and scope
2. **Approve specification** - Mark as "approved" when ready
3. **Create plan.md** - Define technical approach and content structure
4. **Create tasks.md** - Break down into actionable implementation tasks
5. **Implement** - Following 4-phase plan (one Skill at a time)

---

**Status**: Draft
**Dependencies**: Spec 002 (approved)
**Blocks**: Spec 002 implementation (Phase 3), Spec 004
**Version**: 1.0.0
**Last Updated**: 2025-11-10
