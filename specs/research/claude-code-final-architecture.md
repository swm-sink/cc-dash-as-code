# Claude Code Architecture - Complete Research Findings

**Date**: 2025-11-10
**Status**: FINAL - Comprehensive research complete
**Sources**: Claude Agent SDK, Anthropic Cookbook, Spec-Kit, Web Documentation

## Executive Summary

Claude Code has THREE distinct extension mechanisms, all using Markdown:

1. **Custom Commands** (`.claude/commands/*.md`) - Slash commands
2. **Sub-Agents** (`.claude/agents/*.md`) - Isolated specialist agents
3. **Skills** (custom skills with `SKILL.md`) - Domain expertise packages

Additionally, there's a `settings.json` for permissions and hooks.

---

## 1. Custom Commands (Slash Commands)

### Location
- Project-specific: `.claude/commands/*.md`
- User-specific: `~/.claude/commands/*.md`

### Format
Markdown file with YAML frontmatter:

```markdown
---
allowed-tools: Read, Write, Bash(git:*)
description: Brief description shown in /help
argument-hint: <optional argument hint>
model: claude-sonnet-4  # optional
---

# Command Instructions

Your detailed instructions for Claude...

## Context

- Current directory: !`pwd`
- Git status: !`git status`

## Task

$ARGUMENTS contains user input...
```

### Key Features
- **`$ARGUMENTS`**: User input after command
- **`!`command``**: Inline command execution, results embedded in prompt
- **`allowed-tools`**: Restricts which tools command can use
- File name becomes command name (e.g., `commit.md` → `/commit`)

### Example (from Claude Agent SDK):
```markdown
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context
- Current git status: !`git status`
- Current git diff: !`git diff HEAD`

## Your task
Based on the above changes, create a single git commit.
```

---

## 2. Sub-Agents

### Location
- Project-specific: `.claude/agents/*.md`
- User-specific: `~/.claude/agents/*.md`

### Format
Markdown file with YAML frontmatter:

```markdown
---
name: agent-name
description: What this agent specializes in
tools:  # optional, restricts tools
  - Read
  - Write
  - Bash
---

# System Prompt for Sub-Agent

You are a specialized agent for [domain]...

## Your Responsibilities

1. Task 1
2. Task 2

## Guidelines

- Guideline 1
- Guideline 2
```

### Key Features
- **Isolated Context**: Each sub-agent has independent conversation context
- **Specialized**: Designed for specific types of tasks
- **Auto-Discovery**: Claude Code automatically discovers and can invoke them
- **Manual or Auto Invocation**: Can be triggered explicitly or Claude chooses best agent
- **Programmatic (SDK)**: Can also be defined in code via `agents` parameter

### Use Cases
- **component-builder**: Autonomous UI component creation
- **test-engineer**: Writing comprehensive tests
- **code-reviewer**: Performing code reviews
- **documentation**: Generating docs
- **data-pipeline**: Building data infrastructure

### Example Structure:
```markdown
---
name: test-engineer
description: Write comprehensive test suites for Python code
tools:
  - Read
  - Write
  - Bash(python -m pytest:*)
---

# Test Engineer Agent

You are a specialized testing agent focused on writing high-quality tests.

## Your Mission

Write comprehensive test suites that achieve:
- 80%+ code coverage
- Unit, integration, and e2e tests
- Clear, descriptive test names
- Proper fixtures and mocking

## Approach

1. Read the implementation code
2. Identify test scenarios
3. Write pytest tests
4. Run tests and verify coverage
```

---

## 3. Skills

### Location
Custom skills directory (e.g., `custom_skills/my-skill/`)

### Structure
```
my-skill/
├── SKILL.md         # Required: Instructions for Claude
├── REFERENCE.md     # Optional: Additional reference material
├── scripts/         # Optional: Python/JS helper code
│   └── processor.py
└── resources/       # Optional: Templates, data files
    └── template.xlsx
```

### Format of SKILL.md
```markdown
---
name: skill-name
description: What expertise this skill provides
---

# Skill Title

Detailed instructions for Claude on how to use this skill...

## When to Use

This skill should be used when...

## Standards

- Standard 1
- Standard 2

## Examples

Example usage...

## Scripts

- `script.py`: What it does
```

### Key Features
- **Domain Expertise**: Provides specialized knowledge and instructions
- **Progressive Disclosure**: Claude loads skills only when needed
- **Built-in Skills**: `xlsx` (Excel), `pptx` (PowerPoint), `pdf` (PDF), `docx` (Word)
- **Custom Skills**: Create your own for specific workflows
- **Beta Feature**: Requires specific API headers in production

### Example (from Anthropic Cookbook):
```markdown
---
name: applying-brand-guidelines
description: Apply consistent corporate branding to documents
---

# Corporate Brand Guidelines Skill

## Brand Identity

### Company: Acme Corporation
**Tagline**: "Innovation Through Excellence"

## Visual Standards

### Color Palette
- **Primary**: #0066CC (Acme Blue)
- **Secondary**: #003366 (Acme Navy)

### Typography
- **H1**: 32pt, Bold, Acme Blue
- **Body**: 11pt, Regular, Acme Navy

## Application Instructions

When creating any document:
1. Start with brand colors and fonts
2. Apply appropriate template structure
3. Include logo on first page
```

---

## 4. settings.json

### Location
`.claude/settings.json`

### Format
```json
{
  "permissions": {
    "allow": [
      "Read(*)",
      "Bash(python -m pytest:*)",
      "Bash(git:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)"
    ],
    "ask": []
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python -m ruff format {file_path}"
          }
        ]
      }
    ],
    "PreToolUse": [...],
    "Notification": [...],
    "Stop": [...]
  },
  "env": {
    "CUSTOM_VAR": "value"
  },
  "model": "claude-sonnet-4",
  "statusLine": "Custom status text"
}
```

### Hook Types
- **PreToolUse**: Before tool execution
- **PostToolUse**: After tool execution
- **Notification**: When Claude sends notifications
- **Stop**: When Claude finishes responding

### Hook Structure
- `matcher`: Tool name pattern (regex-like)
- `type`: "command" or "python"
- `command`: Shell command to execute

---

## Comparison Table

| Feature | Location | Format | Purpose | Scope |
|---------|----------|--------|---------|-------|
| **Commands** | `.claude/commands/*.md` | MD + YAML frontmatter | Slash commands for workflows | Conversation-level |
| **Sub-Agents** | `.claude/agents/*.md` | MD + YAML frontmatter | Isolated specialist agents | Task-level (new context) |
| **Skills** | `custom_skills/*/SKILL.md` | MD + YAML frontmatter | Domain expertise packages | Knowledge-level |
| **Hooks** | `.claude/settings.json` | JSON | Lifecycle event handlers | Tool-level |

---

## Development vs. Production

### Claude Code (Development)
```
.claude/
├── commands/          # Slash commands
│   └── *.md
├── agents/            # Sub-agents
│   └── *.md
└── settings.json      # Permissions & hooks
```

### Agent SDK (Production)
```python
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    tool,
    create_sdk_mcp_server
)

# Programmatic sub-agents
subagent = {
    "name": "test-engineer",
    "system_prompt": "You are a testing specialist...",
    "allowed_tools": ["Read", "Write", "Bash"]
}

# Custom tools (replaces need for some commands)
@tool("greet", "Greet a user", {"name": str})
async def greet(args):
    return {"content": [{"type": "text", "text": f"Hello {args['name']}!"}]}

server = create_sdk_mcp_server(
    name="tools",
    tools=[greet]
)

# Skills via API (beta)
options = ClaudeAgentOptions(
    agents=[subagent],
    mcp_servers={"tools": server},
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    }
)
```

---

## Our Project Should Have

### .claude/ Directory Structure
```
.claude/
├── commands/                    # Slash commands for workflow
│   ├── dashboard.spec.md       # Create specifications
│   ├── dashboard.plan.md       # Create plans
│   ├── dashboard.tasks.md      # Generate tasks
│   ├── dashboard.implement.md  # Execute implementation
│   ├── dashboard.test.md       # Run tests
│   ├── dashboard.review.md     # Code review
│   └── dashboard.deploy.md     # Deploy to Agent SDK
├── agents/                      # Sub-agents for specialized work
│   ├── component-builder.md    # Build UI components
│   ├── data-pipeline.md        # Data infrastructure
│   ├── test-engineer.md        # Testing specialist
│   └── documentation.md        # Doc generation
└── settings.json               # Permissions and hooks
```

### Custom Skills (Optional)
```
skills/
├── dashboard-analysis/
│   ├── SKILL.md                # Data analysis expertise
│   └── scripts/
│       └── analyze.py
├── plotly-viz/
│   ├── SKILL.md                # Visualization expertise
│   └── resources/
│       └── chart_templates/
└── accessibility-audit/
    └── SKILL.md                # WCAG compliance expertise
```

---

## What We Got Wrong Initially

1. ❌ **"Agent skills"Human: continueas YAML files** - There's no such thing. Skills are:
   - Built-in (xlsx, pptx, pdf, docx) via API
   - Custom skills are directories with SKILL.md files
   - Not `.yaml` files in `.claude/skills/`

2. ❌ **Mixed up Commands, Sub-Agents, and Skills** - They serve different purposes:
   - Commands: User-invoked workflows (slash commands)
   - Sub-Agents: Isolated specialists for specific task types
   - Skills: Domain expertise and knowledge packages

3. ❌ **agent_config.yaml** - No such file in Claude Code
   - Configuration goes in `settings.json`
   - Not a YAML file

4. ✅ **What we got right**:
   - Custom commands in `.claude/commands/`
   - MCP integration concept
   - Agent SDK for production
   - General project structure

---

## Recommended Actions

### 1. Delete Incorrect Files
```bash
rm .claude/agent_config.yaml
rm -rf .claude/skills/  # These were wrong
```

### 2. Keep and Update
```bash
.claude/commands/   # Update format with proper frontmatter
.claude/settings.json  # Keep and enhance
.claude/mcp_config.json  # Keep for MCP servers
```

### 3. Add New
```bash
.claude/agents/     # Create sub-agent definitions
```

### 4. Optional: Skills
```bash
skills/             # If we want custom domain expertise
```

---

## Implementation Priority

### Phase 1: Core Structure (High Priority)
1. ✅ Custom Commands (`.claude/commands/*.md`)
2. ✅ settings.json with permissions and hooks
3. ✅ MCP configuration

### Phase 2: Specialization (Medium Priority)
1. Sub-Agents (`.claude/agents/*.md`)
2. More custom commands
3. Enhanced hooks

### Phase 3: Domain Expertise (Low Priority)
1. Custom Skills directories
2. Skill-specific scripts and resources
3. Integration with Claude.ai/desktop app

---

## References

### Official Documentation
- Claude Code Slash Commands: https://docs.claude.com/en/docs/claude-code/slash-commands
- Sub-agents: https://docs.claude.com/en/docs/claude-code/sub-agents
- Agent SDK Sub-agents: https://docs.claude.com/en/docs/agent-sdk/subagents
- Skills Overview: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- Hooks Reference: https://docs.claude.com/en/docs/claude-code/hooks

### Repositories Examined
- `/reference/reference/claude-agent-sdk-python/` - Official SDK with examples
- `/reference/reference/anthropic-cookbook/skills/` - Skills implementation
- `/reference/reference/spec-kit/AGENTS.md` - Agent integration guide

### Blog Posts & Articles
- "Claude Creates Files" - Anthropic announcement
- "Equipping agents for the real world with Skills" - Engineering blog
- Various community examples on GitHub

---

**Conclusion**: Claude Code uses three distinct Markdown-based extension mechanisms (Commands, Sub-Agents, Skills), each serving a specific purpose. Our project should be restructured to reflect this actual architecture, not the incorrect "agent skills YAML" approach we initially implemented.
