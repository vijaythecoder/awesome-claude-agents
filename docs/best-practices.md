# Best Practices for Claude Agents

Essential guidelines for creating effective, interconnected agents.

## Core Principles

### 1. Single Responsibility
Each agent should master ONE domain.

✅ `tailwind-frontend-expert` - Just Tailwind CSS  
❌ `full-stack-developer` - Too broad

### 2. XML-Style Examples
Use Claude's pattern for smart invocation:

```yaml
description: |
  Expert API developer for any technology stack.
  
  Examples:
  - <example>
    Context: User needs an API
    user: "Create a REST API"  
    assistant: "I'll use the api-architect to design the endpoints"
    <commentary>
    API design is this agent's specialty
    </commentary>
  </example>
```

### 3. Delegation Awareness
Agents should know their limits:

```markdown
## Delegation Patterns
When I need:
- Frontend work → tailwind-frontend-expert
- Security review → security-auditor
- Database optimization → database-architect
```

## Writing Effective Descriptions

### Include Multiple Examples
Cover different scenarios:
1. Common use case
2. Edge case  
3. Delegation scenario

### Add Commentary
Explain WHY the agent was chosen - this trains the pattern matching.

### Specify Delegations
Show how agents work together:

```yaml
Delegations:
- <delegation>
  Trigger: Frontend needed
  Target: frontend-expert
  Handoff: "API ready at /api/users"
</delegation>
```

## System Prompt Best Practices

### Clear Structure
```markdown
# Expert Title

You are [role] with [experience].

## Core Expertise
- Specific skills

## Task Approach  
1. How you work

## Delegation Patterns
When to hand off
```

### Concrete Examples
Show, don't just tell:

```php
// Good: Specific example in any language
// JavaScript/Express
app.get('/api/users', async (req, res) => {
  const users = await User.findAll({ 
    include: ['roles'],
    limit: 20 
  });
  res.json(users);
});

// Bad: Vague description
"Follow best practices"
```

## Interconnection Strategies

### 1. Context Passing
Pass rich information:

```json
{
  "from": "backend-developer",
  "to": "frontend-developer",
  "context": {
    "endpoints": ["/api/users"],
    "auth": "Bearer token"
  }
}
```

### 2. Clear Handoff Points
Define when to delegate:
- Task complete → next phase
- Outside expertise → specialist
- Review needed → auditor

### 3. Orchestration
Use orchestrator agents for complex workflows:
- Break down requirements
- Coordinate specialists
- Track progress

## Testing Your Agents

### 1. Invocation Testing
```bash
# Should trigger
"Build a responsive navbar"

# Should NOT trigger  
"Create a Python script"
```

### 2. Delegation Testing
Verify handoffs work correctly.

### 3. Integration Testing
Test complete workflows end-to-end.

## Common Mistakes

### 1. Over-Engineering
Keep agents focused and simple.

### 2. Missing Examples
Examples are crucial for pattern matching.

### 3. No Delegation Info
Isolated agents limit capability.

### 4. Too Many Tools
Only request necessary tools:

```yaml
# Good: Specific tools
tools: Read, Write, Edit, Bash

# Bad: Everything
tools: # Inherits all (usually too much)
```

## Optimization Tips

### 1. Use Orchestrators
For complex multi-step tasks.

### 2. Parallel Execution
Some agents can work simultaneously.

### 3. Context Preservation  
Pass information forward efficiently.

### 4. Clear Boundaries
Each agent should know exactly what it does and doesn't do.

## Summary

The best agents are:
- **Focused** - One domain, deep expertise
- **Connected** - Know when to delegate
- **Smart** - Use XML examples for intelligent invocation
- **Clear** - Well-documented with examples

Build agents that work together like a real development team!