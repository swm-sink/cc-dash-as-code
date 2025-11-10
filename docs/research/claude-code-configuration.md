# Research: Claude Code Configuration

**Date**: 2025-11-10
**Sources**: Claude Agent SDK repository, spec-kit, web documentation

## Key Findings

### 1. Claude Code Does NOT Use "Skills" YAML Files

**Incorrect assumption**: Agent skills defined as `.yaml` files in `.claude/skills/`

**Actual reality**: Claude Code uses three different mechanisms:
1. **Custom Commands** - Slash commands as Markdown files
2. **Hooks** - Lifecycle event handlers in settings.json
3. **Custom Tools** - Python functions (Agent SDK only)

### 2. Custom Slash Commands Structure

**Location**: `.claude/commands/`

**Format**: Markdown file with YAML frontmatter

**Example** (from Claude Agent SDK repo):
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

**Frontmatter fields**:
- `allowed-tools`: Specific tools the command can use (with argument patterns)
- `description`: Brief description shown in /help
- `argument-hint`: (optional) Hint for command arguments
- `model`: (optional) Specific model to use

**Special syntax**:
- `!`command`` - Inline command execution, results embedded in prompt

**File naming**:
- Filename becomes command name
- `commit.md` → `/commit` command
- Can use subdirectories for namespacing

### 3. settings.json Configuration

**Location**: `.claude/settings.json`

**Structure**:
```json
{
  "permissions": {
    "allow": [
      "Bash(python -m ruff check:*)",
      "Bash(python -m pytest:*)"
    ],
    "deny": [],
    "ask": []
  },
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python -m ruff format src/"
          }
        ],
        "matcher": "Edit|Write|MultiEdit"
      }
    ]
  },
  "env": {
    "CUSTOM_VAR": "value"
  },
  "model": "claude-sonnet-4",
  "statusLine": "custom status"
}
```

**Hook types**:
- `PreToolUse`: Before tool execution
- `PostToolUse`: After tool execution
- `Notification`: When Claude sends notifications
- `Stop`: When Claude finishes responding

**Hook structure**:
- `matcher`: Tool name pattern (regex-like)
- `hooks`: Array of hook definitions
  - `type`: "command" or "python"
  - `command`: Shell command to execute

### 4. Claude Agent SDK Custom Tools

**For production deployment only**

**Format**: Python functions with `@tool` decorator

**Example**:
```python
from claude_agent_sdk import tool, create_sdk_mcp_server

@tool("greet", "Greet a user", {"name": str})
async def greet_user(args):
    return {
        "content": [
            {"type": "text", "text": f"Hello, {args['name']}!"}
        ]
    }

server = create_sdk_mcp_server(
    name="my-tools",
    version="1.0.0",
    tools=[greet_user]
)
```

**Benefits**:
- In-process (no subprocess overhead)
- Type-safe
- Easier debugging
- Single Python process

### 5. MCP Servers

**Two types**:

1. **External MCP servers** (subprocess):
```json
{
  "mcpServers": {
    "postgres": {
      "command": "mcp-server-postgres",
      "args": ["--connection-string", "$POSTGRES_URL"]
    }
  }
}
```

2. **SDK MCP servers** (in-process, Agent SDK only):
```python
from claude_agent_sdk import create_sdk_mcp_server

server = create_sdk_mcp_server(
    name="calculator",
    tools=[add, subtract]
)

options = ClaudeAgentOptions(
    mcp_servers={"calculator": server}
)
```

## Implications for Our Project

### What Needs to Change

1. **Remove** `.claude/skills/` directory and all `.yaml` skill files
2. **Keep** `.claude/commands/` with properly formatted Markdown commands
3. **Update** settings.json with hooks instead of "skill" configuration
4. **Update** specification to reflect actual Claude Code architecture
5. **Clarify** difference between:
   - Development: Custom commands + hooks (Claude Code)
   - Production: Custom tools + SDK MCP servers (Agent SDK)

### What Was Correct

1. `.claude/commands/` directory structure
2. Custom slash commands concept
3. MCP integration concept
4. Agent SDK for production deployment
5. Project-specific vs. user-specific scoping

### Updated Architecture

```
Development (Claude Code):
├── Custom Slash Commands (.claude/commands/*.md)
├── Hooks (settings.json)
└── External MCP Servers (mcp_config.json)

Production (Agent SDK):
├── Custom Tools (@tool decorated functions)
├── SDK MCP Servers (in-process)
└── Hooks (via ClaudeAgentOptions)
```

## Recommendations

1. **Rename "Agent Skills" to "Custom Commands"** throughout project
2. **Remove all `.yaml` skill files**
3. **Create proper Markdown command files** with frontmatter
4. **Add settings.json** with hooks configuration
5. **Update specification** to reflect actual Claude Code capabilities
6. **Clarify dev vs. prod** separation in documentation

## Sources

1. `/reference/reference/claude-agent-sdk-python/` - Official SDK repo
2. `/reference/reference/claude-agent-sdk-python/.claude/` - Example configuration
3. `/reference/reference/spec-kit/AGENTS.md` - Agent integration guide
4. Web search: Claude Code documentation, blog posts, examples

---

**Status**: Research complete, ready to update project files
