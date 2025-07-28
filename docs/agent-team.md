# How Agent Coordination Works

The main Claude agent coordinates specialized sub-agents through sequential delegation. Sub-agents work in isolation and return structured findings.

## Coordination Reality

**What Actually Happens:**
- Main agent invokes tech-lead-orchestrator for routing recommendations
- Main agent creates task list with TodoWrite
- Main agent invokes specialists one by one
- Each specialist returns findings to main agent
- Main agent passes relevant context between specialists

**What Does NOT Happen:**
- Sub-agents talking to each other
- Direct collaboration between specialists
- Parallel execution by sub-agents

## The Coordination Flow

```
User Request
    ↓
Main Agent invokes tech-lead-orchestrator
    ↓
Tech-lead returns agent routing map
    ↓
Main Agent creates TodoWrite task list
    ↓
Main Agent invokes specialists sequentially
    ↓
Each specialist returns structured findings
    ↓
Main Agent coordinates handoffs
```

## Real Example: Building Authentication

**User**: "Add authentication to my app"

**Step 1: Get Routing**
```
Main Agent: "I'll use tech-lead-orchestrator to analyze this request"
→ Tech-lead returns: Use django-backend-expert, django-api-developer
```

**Step 2: Create Tasks**
```
Main Agent creates TodoWrite:
1. Use django-backend-expert for auth models
2. Use django-api-developer for auth endpoints
3. Use code-reviewer for security audit
```

**Step 3: Sequential Execution**
```
Main Agent → django-backend-expert
Returns: "Created User model, auth middleware. Next specialist needs: Model specifications for API design"

Main Agent → django-api-developer (with context from backend expert)
Returns: "Created login/register endpoints. Next specialist needs: Auth implementation for security review"

Main Agent → code-reviewer (with full context)
Returns: "Security audit complete. Recommendations implemented."
```

## Structured Returns

Each specialist returns findings in this format:

```markdown
## Task Completed: [Task Name]
- What was accomplished
- Key decisions made
- Files created/modified

## Handoff Information
- What next specialist needs to know
- Context from this implementation
- Specific requirements or constraints

## Next Steps
- Recommended next specialist
- What should be done next
```

## Context Passing

The main agent extracts and passes relevant information:

```
Backend Expert returns → Main Agent filters relevant API context → API Developer receives

NOT:
Backend Expert → API Developer (direct communication - impossible)
```

## Routing Intelligence

Tech-lead-orchestrator provides routing based on:

1. **Project Analysis**: Framework detection, existing patterns
2. **Agent Availability**: Which specialists exist for this stack
3. **Task Requirements**: What expertise is needed
4. **Execution Order**: Dependencies and logical sequence

Example routing response:
```
## Agent Routing Map
Task 1: Database Design
- PRIMARY AGENT: django-orm-expert
- REASON: Django detected, needs Django-specific patterns

Task 2: API Implementation  
- PRIMARY AGENT: django-api-developer
- REASON: DRF patterns required

## Available Agents
- django-orm-expert
- django-api-developer
- code-reviewer

## CRITICAL: Use ONLY these agents
```

## Why This Architecture?

**Technical Limitations:**
- Sub-agents cannot invoke other sub-agents in Claude Code
- Each invocation is isolated
- No shared memory between specialists

**Benefits:**
- Clear coordination responsibility (main agent)
- Structured information flow
- Predictable execution order
- No coordination conflicts

## Main Agent's Job

The main agent acts as project manager:

1. **Route requests** through tech-lead-orchestrator
2. **Create task lists** with TodoWrite
3. **Invoke specialists** in correct order
4. **Pass context** between invocations
5. **Coordinate deliverables** into final solution

## What Users See

```
User: "Build user management system"

Main Agent: "I'll coordinate the specialists for this feature:
1. ✓ Using tech-lead for routing analysis
2. ✓ Using django-backend-expert for models  
3. ✓ Using django-api-developer for endpoints
4. ✓ Using code-reviewer for security audit

[Each step shows specialist's work and handoff to next]"
```

The end result feels like team collaboration, but it's actually main agent coordination with structured handoffs.