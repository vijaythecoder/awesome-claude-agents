# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Awesome Claude Agents repository - a collection of specialized AI agents that extend Claude Code's capabilities through intelligent orchestration and domain expertise. The agents work together as a development team, with each agent having specific expertise and delegation patterns.

## Working with Agents

When creating or modifying agents:
1. Agents are Markdown files with YAML frontmatter
2. Most agents should omit the `tools` field to inherit all available tools
3. Use XML-style examples in descriptions for intelligent invocation
4. Include delegation patterns for agent interconnection

## High-Level Architecture

### Agent Organization
The project follows a hierarchical structure:

1. **Orchestrators** (`agents/orchestrators/`)
   - `tech-lead-orchestrator`: Coordinates complex projects through three-phase workflow (Research → Planning → Execution)
   - `project-analyst`: Detects technology stack and enables intelligent routing
   - `team-configurator`: Creates agent routing rules in CLAUDE.md files

2. **Core Agents** (`agents/core/`)
   - Cross-cutting concerns like code archaeology, reviews, performance, and documentation
   - These agents support all technology stacks

3. **Universal Agents** (`agents/universal/`)
   - Framework-agnostic specialists (API, backend, frontend, Tailwind)
   - Fallback when no framework-specific agent exists

4. **Specialized Agents** (`agents/specialized/`)
   - Framework-specific experts organized by technology
   - Subdirectories: laravel/, django/, rails/, react/, vue/

### Three-Phase Orchestration Workflow

The tech-lead-orchestrator implements a human-in-the-loop workflow:

1. **Research Phase**: Parallel information gathering from specialists
2. **Approval Gate**: Present findings and wait for human approval
3. **Planning Phase**: Create tasks with TodoWrite, identify dependencies
4. **Execution Phase**: Coordinate specialists with filtered context

### Agent Communication Protocol

Agents communicate through:
- **Delegations**: Defined in agent descriptions with trigger conditions
- **Context Filtering**: Each agent receives only relevant information
- **Direct Communication**: Agents coordinate during execution

Example delegation pattern:
```yaml
Delegations:
- <delegation>
  Trigger: Frontend needed
  Target: frontend-developer
  Handoff: "API ready at /api/users with JWT auth"
</delegation>
```

### Intelligent Routing

The system automatically routes tasks based on:
1. Project context (detected by project-analyst)
2. Framework-specific routing when applicable
3. Universal fallback for unknown stacks
4. Task requirements and agent expertise

## Key Concepts

### Agent Definition Format
```yaml
---
name: agent-name
description: |
  Expertise description with XML examples
  Examples:
  - <example>
    Context: When to use
    user: "Request"
    assistant: "I'll use agent-name"
    <commentary>Why selected</commentary>
  </example>
# tools: omit for all tools, specify for restrictions
---

# Agent Name
System prompt content...
```

### Ambiguity Detection
- Project-analyst flags uncertainties in analysis
- Tech-lead presents research findings for approval before execution
- Agents should identify assumptions needing clarification

### Tool Inheritance
- Omitting `tools` field = inherit all tools (recommended)
- Specify tools only for security restrictions
- Includes WebFetch, MCP tools when available

## Development Guidelines

1. **Creating New Agents**:
   - Use templates/agent-template.md as starting point
   - Focus on single domain expertise
   - Include 2-3 XML examples
   - Define delegation patterns

2. **Agent Interconnection**:
   - Agents should know their limits
   - Define clear handoff points
   - Pass relevant context forward
   - Use structured communication

3. **Testing Agents**:
   - Test invocation patterns
   - Verify delegation works correctly
   - Ensure quality of output

## Important Files and Patterns

- `docs/orchestration-patterns.md`: Detailed three-phase workflow documentation
- `docs/creating-agents.md`: Guide for creating new agents
- `docs/best-practices.md`: Agent development best practices
- `examples/`: Real-world usage examples
- All agents support human-in-the-loop through the tech-lead's approval gate