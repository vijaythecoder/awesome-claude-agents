# Creating Claude Agents - Complete Guide

This guide will walk you through creating high-quality Claude sub-agents that enhance productivity and provide specialized expertise.

## Table of Contents

1. [Understanding Claude Agents](#understanding-claude-agents)
2. [Planning Your Agent](#planning-your-agent)
3. [Writing Effective System Prompts](#writing-effective-system-prompts)
4. [Tool Selection](#tool-selection)
5. [Testing Your Agent](#testing-your-agent)
6. [Common Pitfalls](#common-pitfalls)
7. [Advanced Techniques](#advanced-techniques)

## Understanding Claude Agents

Claude sub-agents are specialized AI assistants that can be invoked to handle specific types of tasks. They provide:

- **Focused Expertise**: Deep knowledge in a specific domain
- **Separate Context**: Their own context window, preserving the main conversation
- **Custom Tools**: Access to only the tools they need
- **Automatic Invocation**: Can be triggered based on task descriptions

### When to Create an Agent

Create an agent when:
- You have expertise in a specific domain that requires specialized knowledge
- Tasks in this domain have consistent patterns or workflows
- The domain has specific best practices or methodologies
- You want to encapsulate complex logic or decision-making

## Planning Your Agent

### 1. Define the Scope

Start by clearly defining:
- **Primary Purpose**: What specific problems does this agent solve?
- **Target Users**: Who will benefit from this agent?
- **Key Capabilities**: What are the 3-5 main things it should excel at?
- **Boundaries**: What is explicitly outside the agent's scope?

### 2. Research the Domain

- Identify common tasks and challenges
- Document best practices and standards
- List common tools and technologies
- Understand typical workflows

### 3. Design the Personality

Your agent should have:
- **Expertise Level**: Senior, expert, specialist
- **Communication Style**: Technical, friendly, formal
- **Proactiveness**: How much should it anticipate needs?
- **Teaching Approach**: How should it explain concepts?

## Writing Effective System Prompts

### Structure Template

```markdown
# [Role] - [Specialization]

You are [description of expertise and background].

## Core Expertise
[Detailed breakdown of knowledge areas]

## Working Principles
[Numbered list of guiding principles]

## Task Approach
[Step-by-step methodology]

## Best Practices
[Domain-specific best practices]

## Common Patterns
[Code examples or standard approaches]

## Quality Standards
[What constitutes good work]
```

### Key Elements

#### 1. Clear Identity
```markdown
You are an expert DevOps engineer specializing in Kubernetes orchestration, 
with 10+ years of experience in cloud-native architectures and CI/CD pipelines.
```

#### 2. Specific Knowledge Areas
```markdown
## Core Expertise
### Container Orchestration
- Kubernetes cluster design and management
- Pod scheduling and resource optimization
- Service mesh implementation (Istio, Linkerd)
- Multi-cluster federation

### Cloud Platforms
- AWS EKS optimization
- GCP GKE best practices
- Azure AKS deployment patterns
- Multi-cloud strategies
```

#### 3. Concrete Methodologies
```markdown
## Task Approach
When deploying a new application to Kubernetes:
1. Analyze application requirements (stateful vs stateless, resource needs)
2. Design the deployment architecture (pods, services, ingress)
3. Create manifests following security best practices
4. Implement monitoring and logging
5. Set up autoscaling and resource limits
6. Document the deployment process
```

#### 4. Examples and Patterns
```markdown
## Common Patterns
### Blue-Green Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-blue
  labels:
    version: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
      version: blue
  template:
    # ... pod spec
```
```

### Writing Tips

1. **Be Specific**: Avoid vague statements like "you are good at coding"
2. **Show Expertise**: Include technical terminology and industry standards
3. **Provide Structure**: Use clear sections and formatting
4. **Include Examples**: Show concrete implementations
5. **Set Standards**: Define what quality looks like

## Tool Selection

### Choosing the Right Tools

Only request tools that are essential for your agent's tasks:

```yaml
# Minimal tool set for a CSS specialist
tools: Read, Write, Edit, Grep, WebFetch

# Comprehensive set for a DevOps engineer
tools: Read, Write, Edit, Bash, Grep, Glob, WebFetch
```

### Tool Guidelines

| Tool | Use When |
|------|----------|
| Read | Analyzing existing code/files |
| Write | Creating new files |
| Edit/MultiEdit | Modifying existing files |
| Bash | Running commands, testing |
| Grep | Searching codebases |
| Glob | Finding files by pattern |
| WebFetch | Researching documentation |

### MCP Tools

If you omit the `tools` field, your agent inherits all tools including MCP servers:

```yaml
# Inherits all tools including MCP
---
name: database-architect
description: Database design and optimization expert
---
```

## Testing Your Agent

### 1. Create Test Scenarios

Write diverse test cases:

```markdown
## Test Cases for Tailwind Agent

1. **Basic Component**: "Create a responsive card component"
2. **Complex Layout**: "Build a dashboard with sidebar navigation"
3. **Animation**: "Add smooth transitions to a dropdown menu"
4. **Dark Mode**: "Implement dark mode for an existing component"
5. **Performance**: "Optimize a page with too many Tailwind classes"
```

### 2. Test Auto-Invocation

```bash
# Should trigger your agent automatically
claude "Create a responsive navigation with Tailwind CSS"

# Should NOT trigger your agent
claude "Create a Python API endpoint"
```

### 3. Test Explicit Invocation

```bash
claude "Use the tailwind-frontend-expert to review this component"
```

### 4. Validate Output Quality

Check that your agent:
- Provides accurate, working solutions
- Follows stated best practices
- Uses appropriate tools efficiently
- Maintains consistent quality

## Common Pitfalls

### 1. Too Broad Scope
❌ **Bad**: "You are a frontend developer"
✅ **Good**: "You are a React component architect specializing in accessible, performant UI"

### 2. Weak Descriptions
❌ **Bad**: `description: Helps with CSS`
✅ **Good**: `description: Expert in Tailwind CSS, responsive design, and utility-first styling. Use proactively for any CSS or styling tasks.`

### 3. Requesting All Tools
❌ **Bad**: Requesting all tools when you only need Read and Edit
✅ **Good**: Precisely selecting only necessary tools

### 4. No Concrete Examples
❌ **Bad**: "Follow best practices"
✅ **Good**: Providing specific code examples and patterns

### 5. Forgetting Proactiveness
❌ **Bad**: Only responding when explicitly asked
✅ **Good**: Including "use proactively" in description and anticipating needs

## Advanced Techniques

### 1. Dynamic Behavior

```markdown
## Adaptive Approach
Based on project size:
- **Small projects (<10 components)**: Inline all styles
- **Medium projects (10-50 components)**: Extract common patterns
- **Large projects (50+ components)**: Implement design system
```

### 2. Error Recovery

```markdown
## Error Handling
When encountering issues:
1. Diagnose root cause (check logs, inspect code)
2. Communicate clearly what went wrong
3. Propose 2-3 solution options
4. Implement chosen solution
5. Add preventive measures
```

### 3. Learning from Context

```markdown
## Context Awareness
I analyze the existing codebase to:
- Match existing code style
- Use established patterns
- Respect project conventions
- Integrate with current tooling
```

### 4. Proactive Assistance

```markdown
When I see [specific pattern], I proactively:
- Suggest improvements
- Warn about potential issues
- Offer optimization opportunities
- Recommend best practices
```

## Example: Creating a Database Agent

Let's walk through creating a database optimization agent:

### 1. Plan
- **Purpose**: Optimize database queries and schema design
- **Users**: Backend developers, DBAs
- **Capabilities**: Query optimization, indexing, schema design
- **Tools**: Read, Write, Bash, Grep

### 2. Write the Agent

```yaml
---
name: database-optimizer
description: Database performance expert specializing in query optimization, indexing strategies, and schema design. Use proactively when working with databases, SQL queries, or performance issues.
tools: Read, Write, Edit, Bash, Grep
---

# Database Optimization Expert

You are a senior database architect with expertise in relational and NoSQL databases, 
specializing in performance optimization and scalable schema design.

## Core Expertise

### Query Optimization
- Execution plan analysis
- Index strategy development
- Query rewriting techniques
- Partitioning strategies

### Schema Design
- Normalization vs denormalization decisions
- Data type optimization
- Constraint design
- Relationship modeling

### Performance Tuning
- Database configuration optimization
- Connection pooling strategies
- Caching implementation
- Monitoring and metrics

## Task Approach

When optimizing database performance:
1. Analyze current query patterns and execution plans
2. Identify bottlenecks using EXPLAIN/profiling tools
3. Design targeted indexes based on query patterns
4. Implement query rewrites for better performance
5. Monitor impact and iterate

## Best Practices

### Indexing Strategy
```sql
-- Composite index for common query pattern
CREATE INDEX idx_orders_customer_date 
ON orders(customer_id, order_date DESC)
WHERE status = 'active';

-- Covering index to avoid table lookups
CREATE INDEX idx_products_category_price 
ON products(category_id, price) 
INCLUDE (name, description);
```

### Query Patterns
```sql
-- Efficient pagination
SELECT * FROM users
WHERE id > :last_id
ORDER BY id
LIMIT 100;

-- Avoid N+1 queries
SELECT u.*, 
       COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

## Quality Standards
- Query response time < 100ms for OLTP
- Index usage ratio > 90%
- No full table scans in production
- Proper connection pooling configured
- Monitoring alerts for slow queries
```

### 3. Test Thoroughly
- Create test database scenarios
- Verify optimization recommendations
- Check tool usage efficiency
- Validate auto-invocation

## Final Checklist

Before submitting your agent:

- [ ] Clear, specific name following conventions
- [ ] Comprehensive description with keywords
- [ ] Well-structured system prompt
- [ ] Appropriate tool selection
- [ ] Concrete examples and patterns
- [ ] Tested with various scenarios
- [ ] Documentation and examples created
- [ ] No typos or formatting issues

Remember: Quality over quantity. One excellent agent is worth more than ten mediocre ones.

---

Need help? Check our [examples](../examples/) or ask in [discussions](https://github.com/yourusername/awesome-claude-agents/discussions).