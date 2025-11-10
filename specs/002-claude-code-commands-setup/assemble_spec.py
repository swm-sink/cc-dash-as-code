#!/usr/bin/env python3
"""
Assemble the complete revised spec 002 from component files.
"""

def read_file(filepath):
    """Read file and return contents."""
    with open(filepath, 'r') as f:
        return f.read()

def extract_section(content, start_marker, end_marker=None):
    """Extract a section from content between markers."""
    lines = content.split('\n')
    extracting = False
    result = []

    for line in lines:
        if start_marker in line:
            extracting = True
            continue
        if end_marker and end_marker in line:
            break
        if extracting:
            result.append(line)

    return '\n'.join(result)

def main():
    print("Assembling revised spec 002...")

    # Read all component files
    overview = read_file('OVERVIEW_REVISED.md')
    skills_arch = read_file('AGENT_SKILLS_SECTION.md')
    skills_req = read_file('SKILLS_REQUIREMENTS.md')
    skills_sc = read_file('SKILLS_SUCCESS_CRITERIA.md')
    skills_clarif = read_file('SKILLS_CLARIFICATIONS.md')
    impl_phases = read_file('IMPLEMENTATION_PHASES_REVISED.md')
    current_spec = read_file('spec.md')

    # Build the complete spec
    spec_parts = []

    # 1. Header (from current spec) - lines 1-7
    header_lines = current_spec.split('\n')[:7]
    spec_parts.append('\n'.join(header_lines))
    spec_parts.append('')

    # 2. Overview (revised)
    # Remove the "# Overview Section (Revised)" header
    overview_content = '\n'.join(overview.split('\n')[2:])
    spec_parts.append(overview_content)
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 3. Agent Skills Architecture (new major section)
    spec_parts.append(skills_arch)
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 4. User Scenarios & Testing (from current spec, lines ~19 to ~178)
    # We'll keep this mostly as-is, just note that Skills are mentioned in scenarios
    user_scenarios_start = current_spec.find('## User Scenarios & Testing')
    requirements_start = current_spec.find('## Requirements *(mandatory)*')
    user_scenarios = current_spec[user_scenarios_start:requirements_start]
    spec_parts.append(user_scenarios.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 5. Requirements - KEEP FR-001 to FR-060, ADD FR-061 to FR-090
    # Extract original requirements section up to Key Entities
    key_entities_start = current_spec.find('### Key Entities')
    requirements = current_spec[requirements_start:key_entities_start]
    spec_parts.append(requirements.strip())
    spec_parts.append('')

    # Add Skills requirements
    # Remove the "# Skills Functional Requirements" header
    skills_req_content = '\n'.join(skills_req.split('\n')[4:])
    spec_parts.append(skills_req_content.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 6. Key Entities (from current spec, update with Skills entity)
    success_criteria_start = current_spec.find('## Success Criteria *(mandatory)*')
    key_entities = current_spec[key_entities_start:success_criteria_start]

    # Add Agent Skill entity
    key_entities += '''

- **Agent Skill**: Domain knowledge provider with progressive disclosure
  - Attributes: name, description, directory structure, loading levels (1-3), allowed-tools, token budgets
  - Relationships: Auto-activates during Commands, complements MCP, distinct from Sub-Agents, benefits both planning and execution

- **Skill Level**: Progressive disclosure tier
  - Attributes: level number (1-3), token budget, content type (metadata/core/references)
  - Relationships: Belongs to Skill, loads sequentially based on need
'''

    spec_parts.append(key_entities.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 7. Success Criteria - KEEP SC-001 to SC-030, ADD SC-031 to SC-045
    non_func_start = current_spec.find('## Non-Functional Requirements')
    success_criteria = current_spec[success_criteria_start:non_func_start]
    spec_parts.append(success_criteria.strip())
    spec_parts.append('')

    # Add Skills success criteria
    skills_sc_content = '\n'.join(skills_sc.split('\n')[4:])
    spec_parts.append(skills_sc_content.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 8-10. Non-Functional Requirements, Technology Stack, Out of Scope (unchanged)
    out_of_scope_start = current_spec.find('## Out of Scope')
    clarifications_start = current_spec.find('## Clarifications')

    non_func_section = current_spec[non_func_start:clarifications_start]
    spec_parts.append(non_func_section.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 11. Clarifications - KEEP Q1-Q5, ADD Q6-Q10
    dependencies_start = current_spec.find('## Dependencies')
    clarifications = current_spec[clarifications_start:dependencies_start]
    spec_parts.append(clarifications.strip())
    spec_parts.append('')

    # Add Skills clarifications
    skills_clarif_content = '\n'.join(skills_clarif.split('\n')[4:])
    spec_parts.append(skills_clarif_content.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 12. Dependencies (update)
    impl_phases_start = current_spec.find('## Implementation Phases')
    dependencies = current_spec[dependencies_start:impl_phases_start]

    # Add new dependencies
    dependencies += '''

### Research Dependencies
- specs/research/agent-skills-integration-analysis.md (29KB)
- specs/research/claude-code-final-architecture.md (12KB)
- specs/research/complete-architecture-quick-reference.md (19KB)
- specs/research/spec-revision-notes.md

### Architecture Dependencies
- specs/WORKFLOW.md - Two-process workflow architecture
- specs/INDEX.md - Spec numbering and implementation order

### Template Dependencies
- specs/templates/spec-template.md
- specs/templates/plan-template.md
- specs/templates/tasks-template.md
'''

    spec_parts.append(dependencies.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 13. Implementation Phases (completely replaced)
    impl_content = '\n'.join(impl_phases.split('\n')[2:])
    spec_parts.append(impl_content.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 14. Review & Acceptance Checklist (update)
    review_start = current_spec.find('## Review & Acceptance Checklist')
    review_end = current_spec.find('**Next Steps**:')
    review = current_spec[review_start:review_end]

    # Add Skills-specific checks
    review += '''

### Skills Integration
- [ ] Agent Skills architecture is comprehensive and clear
- [ ] Progressive disclosure pattern is explained in extreme detail
- [ ] All 8 Skills have complete directory structures defined
- [ ] Development Skills (3) and Production Skills (5) are distinguished
- [ ] Skills integration with Commands is well-documented
- [ ] Skills vs MCP relationship is clarified
- [ ] Token budgets are specified for all loading levels
- [ ] Activation triggers are documented for each Skill
- [ ] Skills functional requirements (FR-061 to FR-090) are complete
- [ ] Skills success criteria (SC-031 to SC-045) are measurable

### Hybrid Workflow Architecture
- [ ] Two-process model (Spec-Kit + Claude Code) is clearly explained
- [ ] Handoff mechanism via tasks.md is documented
- [ ] Agentic correction loops (max 3 attempts) are specified
- [ ] Escalation thresholds and governance are defined
- [ ] Workflow architecture references specs/WORKFLOW.md
- [ ] Namespaced commands (/spec:*, /workflow:*, /utils:*) are used consistently

'''

    spec_parts.append(review.strip())
    spec_parts.append('')
    spec_parts.append('---')
    spec_parts.append('')

    # 15. Next Steps (update)
    next_steps = '''**Next Steps**:
1. **Review this specification** - Validate hybrid workflow, Agent Skills integration, and all requirements
2. **Approve specification** - Mark as "approved" when ready to proceed (user review required)
3. **Create implementation branch** - Branch: `002-claude-code-commands-setup`
4. **Begin Phase 1** - Core architecture setup (directory structure, settings.json)
5. **Iterate through 8 phases** - Complete all phases with continuous testing and validation
6. **Deploy to team** - Team members access via git pull

---

**Status**: Draft - Awaiting Review (Requires user approval before implementation)

**Major Revisions**:
- Added complete Agent Skills architecture (~4000 tokens of detailed documentation)
- Integrated hybrid workflow (Spec-Kit planning + Claude Code execution)
- Added 30 Skills functional requirements (FR-061 to FR-090)
- Added 15 Skills success criteria (SC-031 to SC-045)
- Added 5 clarifications for Skills and workflow (Q6-Q10)
- Revised implementation to 8 phases including Skills development
- Updated command naming to namespaced format (/spec:*, /workflow:*, /utils:*)

**Key Changes from Previous Version**:
- REMOVED: "EPIC" methodology term (replaced with "hybrid workflow")
- REMOVED: `/dash.*` separate command category (integrated into `/workflow:*`)
- ADDED: Complete Agent Skills system (8 skills with progressive disclosure)
- ADDED: Two-process model with clear handoff mechanism
- ADDED: Agentic correction loops with 3-attempt limit

**Review Focus Areas**:
1. Is the Agent Skills architecture clear and comprehensive enough?
2. Are all 8 Skills properly defined with directory structures?
3. Is the hybrid workflow architecture well-explained?
4. Are the 30 new functional requirements complete and testable?
5. Are the 15 new success criteria measurable?
6. Is the 8-phase implementation plan realistic and well-ordered?

---

**Version**: 2.0.0 (Major revision with Agent Skills integration)
**Last Updated**: 2025-11-10
**Specification File**: specs/002-claude-code-commands-setup/spec.md
'''

    spec_parts.append(next_steps)

    # Assemble final spec
    final_spec = '\n'.join(spec_parts)

    # Write to new file
    with open('spec-revised.md', 'w') as f:
        f.write(final_spec)

    # Count words and estimate tokens
    word_count = len(final_spec.split())
    token_estimate = int(word_count / 0.75)

    print(f"✓ Revised spec created: spec-revised.md")
    print(f"  Word count: {word_count:,}")
    print(f"  Estimated tokens: {token_estimate:,}")
    print(f"  Increase from original: ~{token_estimate - 6500:,} tokens")
    print()
    print("Next step: Review spec-revised.md, then replace spec.md")

if __name__ == '__main__':
    main()
