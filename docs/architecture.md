# Architecture - Technical Implementation

## System Reality

Sub-agents cannot invoke other sub-agents. Main Claude agent coordinates everything through sequential delegation.

## Agent Hierarchy

```
agents/
├── orchestrators/     # Analysis and routing only
├── core/             # Cross-cutting utilities  
├── universal/        # Framework-agnostic fallbacks
└── specialized/      # Framework-specific experts
```

## Orchestration Flow

### 1. Tech-Lead Analysis
Main agent invokes `tech-lead-orchestrator` for complex tasks:

```
Input: User request
Output: Agent routing map with specific agents to use
```

### 2. Agent Routing Protocol
Tech-lead returns structured routing:

```markdown
## Agent Routing Map
Task 1: Database Design
- PRIMARY AGENT: django-orm-expert
- REASON: Django detected

## Available Agents
- project-analyst
- django-orm-expert  
- django-api-developer
```

### 3. Sequential Execution
Main agent uses ONLY agents from routing map:

```
Main Agent:
1. Invokes django-orm-expert → Gets structured findings
2. Extracts context from return
3. Invokes django-api-developer with filtered context
4. Coordinates until completion
```

## Communication Pattern

**No Direct Agent Communication**
- Agent A cannot call Agent B
- All coordination through main Claude agent
- Agents return structured findings for parsing

**Example Agent Return:**
```markdown
## Task Completed: Database Schema
- Models created: User, Product, Order
- Relationships defined
- Next specialist needs: These model definitions for API
```

## Project Detection

`project-analyst` examines files:
- `composer.json` → Laravel routing
- `requirements.txt` → Django routing  
- `package.json` → React/Vue routing
- Returns technology context for routing decisions

## Agent Selection Logic

### Framework-Specific Routing
```
Laravel Project:
- API tasks → laravel-eloquent-expert
- Backend → laravel-backend-expert

Django Project:  
- API tasks → django-api-developer
- ORM → django-orm-expert
```

### Fallback Chain
```
No Django specialist available → django-backend-expert → backend-developer
```

## Tool Access

**Orchestrators:**
- Read, Grep, TodoWrite for analysis

**Specialists:**  
- Read, Write, Edit, Bash for implementation

**Core Agents:**
- Read, Grep, Glob for analysis tasks

## Actual Workflow Example

### User: "Build user authentication"

**Step 1:** Main agent invokes tech-lead-orchestrator
```
Returns: Use project-analyst → django-backend-expert → code-reviewer
```

**Step 2:** Main agent executes sequentially
```
1. project-analyst → "Django 4.x detected"
2. django-backend-expert → "Auth models created"  
3. code-reviewer → "Security audit complete"
```

**Step 3:** Main agent coordinates handoffs
```
Passes Django context from analyst to backend expert
Passes implementation details to reviewer
```

## Key Constraints

- **No Agent-to-Agent Calls**: Everything routes through main agent
- **Sequential Only**: No parallel agent execution
- **Structured Returns**: Agents must return parseable findings
- **Strict Routing**: Use only tech-lead recommended agents

## Extension Pattern

**Adding New Agent:**
1. Create agent markdown file
2. Add to tech-lead's routing logic  
3. Define structured return format
4. Test through main agent coordination

## Performance Notes

- Context passed between agents via main agent memory
- Project analysis cached per session
- Agent selection optimized by routing map
- No persistent agent state between invocations