# Creating Claude Agents

Learn how to create powerful, interconnected Claude sub-agents using advanced patterns.

## Quick Start

```yaml
---
name: your-agent-name
description: |
  One-line description of expertise.
  
  Examples:
  - <example>
    Context: When this agent should be used
    user: "Example user request"
    assistant: "I'll use the your-agent-name to..."
    <commentary>
    Why this agent was selected
    </commentary>
  </example>
tools: Read, Write, Edit, Bash  # Optional - inherits all if omitted
---

You are an expert [role] specializing in [domain].

## Core Expertise
- [Specific skill 1]
- [Specific skill 2]

## Task Approach
1. [How you handle tasks]
2. [Your methodology]

## Delegation Patterns
When I encounter [type of task], I delegate to [agent-name].
```

## The XML-Style Pattern (Advanced)

Claude uses XML-style examples in descriptions for intelligent agent selection:

```yaml
description: |
  Expert Laravel backend developer specializing in APIs and security.
  
  Examples:
  - <example>
    Context: User needs to build an API
    user: "Create a REST API for products"
    assistant: "I'll use the laravel-backend-expert to build a comprehensive products API"
    <commentary>
    API development is a core Laravel backend task
    </commentary>
  </example>
  - <example>
    Context: User has completed backend and needs frontend
    user: "Now I need a UI for this API"
    assistant: "The backend is complete. Let me hand this off to the tailwind-frontend-expert"
    <commentary>
    Recognizing when to delegate to frontend specialist
    </commentary>
  </example>
```

### Why This Works

1. **Pattern Learning**: Claude learns from examples when to invoke agents
2. **Context Awareness**: Understands project stage and user intent
3. **Smart Delegation**: Knows when to hand off to other specialists
4. **Self-Documenting**: Examples serve as live documentation

## Agent Interconnection

### Basic Delegation

Add delegation patterns to your system prompt:

```markdown
## Delegation Patterns

When tasks require expertise outside my domain:
- Frontend UI needed → tailwind-frontend-expert
- Security review → security-auditor  
- Database optimization → database-architect

I will complete my portion and suggest the appropriate specialist.
```

### Advanced Orchestration

For complex workflows, use delegation examples:

```yaml
Delegations:
- <delegation>
  Trigger: Frontend implementation needed
  Handoff: "Backend API complete at /api/products. Handing off to frontend expert."
  Context: { endpoints: ["/api/products", "/api/products/{id}"], auth: "Bearer token" }
</delegation>
```

## Essential Components

### 1. Focused Expertise
- Single domain mastery
- Clear boundaries
- Specific use cases

### 2. Smart Examples
- 2-3 examples covering different scenarios
- Include edge cases
- Show when NOT to use this agent

### 3. Delegation Awareness
- Know your limits
- Identify next steps
- Pass context forward

## Testing Your Agent

1. **Invocation Test**: Does it trigger on appropriate requests?
2. **Delegation Test**: Does it hand off correctly?
3. **Quality Test**: Is the output expert-level?

## Common Patterns

### Backend → Frontend Flow
```
Laravel Expert → API Complete → Frontend Expert → UI Built → Code Auditor
```

### Full Stack Development
```
Project Orchestrator → Backend Expert + Frontend Expert → Integration → Testing
```

### Review Pipeline
```
Developer Agent → Code Complete → Security Auditor → Deployment Expert
```

## Next Steps

- See [Interconnected Agents](interconnected-agents.md) for advanced workflows
- Check [examples/](../examples/) for real agent implementations
- Use [templates/agent-template.md](../templates/agent-template.md) as starting point