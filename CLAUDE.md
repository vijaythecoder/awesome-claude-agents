# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Awesome Claude Agents repository - a collection of specialized AI agents that extend Claude Code's capabilities through intelligent orchestration and domain expertise. The agents work together as a development team, with each agent having specific expertise and delegation patterns.

## Working with Agents

When creating or modifying agents:
1. Agents are Markdown files with YAML frontmatter
2. Most agents should omit the `tools` field to inherit all available tools
3. Use XML-style examples in descriptions for intelligent invocation
4. Agents return structured findings for main agent coordination

## Orchestration Pattern for Claude Code

Since sub-agents in Claude Code cannot directly invoke other sub-agents, orchestration follows this strict pattern:

### CRITICAL: Agent Routing Protocol

**When handling complex tasks, you MUST:**

1. **ALWAYS start with tech-lead-orchestrator** for any multi-step task
2. **FOLLOW the agent routing map** returned by tech-lead EXACTLY
3. **USE ONLY the agents** explicitly recommended by tech-lead
4. **NEVER select agents independently** - tech-lead knows which agents exist

### Example: Building a Feature with Agent Routing

```
User: "Build a user management system"

Main Claude Agent:
1. First, I'll use the tech-lead-orchestrator to analyze and get routing
   → Tech lead returns Agent Routing Map with SPECIFIC agents
   
2. I MUST use ONLY the agents listed in the routing map:
   - If tech-lead says "use django-api-developer" → Use that EXACT agent
   - If tech-lead says "use react-component-architect" → Use that EXACT agent
   - DO NOT substitute with generic agents unless specified as fallback
   
3. Execute tasks in the order specified by tech-lead using TodoWrite
```

### Key Orchestration Rules

1. **Tech-Lead is Routing Authority**: Tech-lead determines which agents can handle each task
2. **Strict Agent Selection**: Use ONLY agents from tech-lead's "Available Agents" list
3. **No Improvisation**: Do NOT select agents based on your own judgment
4. **Deep Reasoning**: Apply careful thought when coordinating the recommended agents
5. **Structured Handoffs**: Extract and pass information between agent invocations

### Agent Selection Flow

```
CORRECT FLOW:
User Request → Tech-Lead Analysis → Agent Routing Map → Execute with Listed Agents

INCORRECT FLOW:
User Request → Main Agent Guesses → Wrong Agent Selected → Task Fails
```

### Example Tech-Lead Response You Must Follow

When tech-lead returns:
```
## Available Agents for This Project
- django-backend-expert: Django tasks
- django-api-developer: API tasks  
- react-component-architect: React UI
```

You MUST use these specific agents, NOT generic alternatives like "backend-developer"

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

### Three-Phase Orchestration Workflow (Main Agent Coordinated)

The main Claude agent implements a human-in-the-loop workflow using the tech-lead-orchestrator:

1. **Research Phase**: Tech-lead analyzes requirements and returns structured findings
2. **Approval Gate**: Main agent presents findings and waits for human approval
3. **Planning Phase**: Main agent creates tasks with TodoWrite based on tech-lead's recommendations
4. **Execution Phase**: Main agent invokes specialists sequentially with filtered context

### Agent Communication Protocol

Since sub-agents cannot directly communicate or invoke each other:
- **Structured Returns**: Each agent returns findings in a parseable format
- **Context Passing**: Main agent extracts relevant information from returns
- **Sequential Coordination**: Main agent manages the execution flow
- **Handoff Information**: Agents include what the next specialist needs in their returns

Example return format:
```
## Task Completed: API Design
- Endpoints defined: GET/POST/PUT/DELETE /api/users
- Authentication: Bearer token required
- Next specialist needs: This API specification for implementation
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
   - Define structured return format

2. **Agent Return Patterns**:
   - Always return findings in structured format
   - Include "Next Steps" or "Handoff Information"
   - Specify what context next specialist needs
   - Main agent will parse and coordinate

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

## Complete Orchestration Example

Here's a full example showing proper agent routing:

### User Request:
"Help me build an authentication system for my web app"

### Step 1: Tech-Lead Analysis
```
Main Agent: "I'll use the tech-lead-orchestrator to analyze this request and determine the best approach."

[Invokes tech-lead-orchestrator]
```

### Step 2: Tech-Lead Returns Routing Map
```
## Agent Routing Map

Task 1: Detect Project Technology
- PRIMARY AGENT: project-analyst
- REASON: Need to identify framework for proper routing

Task 2: Design Authentication Schema  
- PRIMARY AGENT: database-architect
- REASON: Framework-agnostic database design

Task 3: Implement Auth Backend
- PRIMARY AGENT: django-backend-expert
- FALLBACK AGENT: backend-developer
- REASON: Django detected in project

Task 4: Create Auth API Endpoints
- PRIMARY AGENT: django-api-developer
- FALLBACK AGENT: api-architect
- REASON: Django REST Framework patterns

## Available Agents for This Project
- project-analyst
- database-architect  
- django-backend-expert
- django-api-developer
- code-reviewer

## CRITICAL INSTRUCTION
Use ONLY the agents listed above. Do NOT use laravel, rails, or other framework agents.
```

### Step 3: Main Agent Executes Plan
```
Main Agent: "Based on the tech-lead's routing, I'll now coordinate the implementation:"

1. ✓ Using project-analyst to analyze the codebase
2. ✓ Using database-architect for auth schema design  
3. ✓ Using django-backend-expert for implementation
4. ✓ Using django-api-developer for API endpoints
5. ✓ Using code-reviewer for security audit

[Executes each step with the EXACT agents specified]
```

### What NOT to Do:
```
❌ "I'll use backend-developer" (when tech-lead specified django-backend-expert)
❌ "I'll use rails-api-developer" (wrong framework)
❌ "I'll skip the tech-lead and choose agents myself" (bypasses routing)
```

## Critical Reminders

- ALWAYS use tech-lead-orchestrator for multi-step tasks to get proper agent routing
- FOLLOW the agent routing map exactly - do not improvise
- USE deep reasoning when coordinating the recommended agents
- TRUST the tech-lead's expertise in agent selection