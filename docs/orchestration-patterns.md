# Orchestration Patterns - Claude Code Agent Coordination

This guide documents how to orchestrate multiple sub-agents in Claude Code, where sub-agents cannot directly invoke each other.

## 🎯 Core Orchestration Philosophy

The main Claude agent coordinates complex tasks through three distinct phases, using the tech-lead-orchestrator for analysis:

1. **Research Phase** - Tech-lead analyzes and returns structured findings
2. **Planning Phase** - Main agent creates tasks based on recommendations
3. **Execution Phase** - Main agent invokes specialists sequentially

## 📊 Three-Phase Workflow

### Phase 1: Research & Analysis

The main Claude agent uses the tech-lead-orchestrator to analyze requirements:

```
Main Agent: "I'll use the tech-lead-orchestrator to analyze this payment system request"
→ Invokes tech-lead-orchestrator
→ Tech lead returns structured analysis with task breakdown
```

The tech-lead-orchestrator examines:
- Project structure and technology stack
- Technical requirements and constraints  
- Security and compliance needs
- Required components and integrations

**Example Tech-Lead Response:**

```
## Project Analysis
- Technology Stack: Django 4.2 with PostgreSQL
- Key Requirements: Payment processing with Stripe
- Constraints: PCI compliance required

## Task Breakdown
1. Payment Model Design - database-architect
2. Stripe Integration - django-backend-expert  
3. Payment API - django-api-developer
4. Payment UI - react-frontend-developer

## Implementation Strategy
- Phase 1: Design database schema
- Phase 2: Backend implementation
- Phase 3: Frontend and testing
```

### Phase 2: Planning & Task Creation

The main agent creates tasks using TodoWrite based on the tech-lead's recommendations:

```javascript
// Main agent creates tasks from tech-lead analysis
todos = [
  { content: "Design payment database schema", 
    specialist: "database-architect",
    priority: "high" },
  { content: "Implement Stripe integration",
    specialist: "django-backend-expert", 
    priority: "high",
    depends_on: "schema" },
  { content: "Create payment API endpoints",
    specialist: "django-api-developer",
    priority: "high", 
    depends_on: "stripe" },
  { content: "Build payment UI components",
    specialist: "react-frontend-developer",
    priority: "medium",
    depends_on: "api_design" }
]
```

**Dependency Management by Main Agent:**

The main agent tracks dependencies and ensures proper execution order:
- Sequential tasks wait for dependencies
- Parallel tasks can be started together
- Results from one agent inform the next invocation

### Phase 3: Execution & Coordination

The main agent executes the plan by invoking specialists sequentially:

```python
# Main agent execution flow
1. Mark task as in_progress in TodoWrite
2. Invoke specialist with filtered context
3. Receive structured response
4. Extract relevant information for next specialist
5. Mark task as completed
6. Move to next task based on dependencies
```

**Example Execution:**
```
Main Agent: "Starting with database design task"
→ Invokes database-architect with payment requirements
← Receives: Schema design with tables and relationships

Main Agent: "Now implementing Stripe integration" 
→ Invokes django-backend-expert with schema + Stripe requirements
← Receives: Implementation details and API methods

Main Agent: "Creating API endpoints"
→ Invokes django-api-developer with implementation details
← Receives: Endpoint specifications and authentication approach
```

## 🔄 Context Filtering Patterns

### Information Scoping by Main Agent

The main agent filters information when invoking each specialist:

**When invoking Backend Developer:**
```
Context provided:
- API requirements from tech-lead analysis
- Database schema from database-architect
- Authentication requirements
- Business logic rules

Context filtered out:
- UI mockups
- CSS framework details  
- Frontend routing plans
```

**When invoking Frontend Developer:**
```
Context provided:
- API endpoints from backend developer
- Response formats and data structures
- Authentication flow (simplified)
- UI requirements from tech-lead

Context filtered out:
- Database implementation details
- Server configuration
- Backend algorithms
```

### Context Passing Examples

**Main Agent to Backend Developer:**
```
"Based on the tech-lead's analysis, you need to implement a user API with these specifications:
- CRUD operations for users
- JWT authentication
- Role-based access control
The database schema is: [schema details]"
```

**Backend Developer Response (structured):**
```
## Task Completed: User API Implementation
- Endpoints created: GET/POST/PUT/DELETE /api/users
- Authentication: JWT with 1-hour expiry
- Roles: admin, user, guest
- Next specialist needs: Endpoint URLs and auth header format
```

**Main Agent to Frontend Developer:**
```
"The backend team has completed the API. Here's what you need:
- Endpoints: [list from backend response]
- Auth: Bearer token in Authorization header
- Please build the user management UI"
```

## 🚀 Parallel Execution Patterns

### Identifying Parallelism

Tasks can run in parallel when they:
- Have no shared dependencies
- Work in different domains (backend vs frontend)
- Implement independent features
- Involve research or planning activities

**Parallel Execution Timeline:**

**Time 1 (Parallel execution):**
- API Design by api-architect
- Database Schema by database-expert
- UI Wireframes by frontend-designer

**Time 2 (Sequential - waits for Time 1):**
- API Implementation by backend-developer (needs completed API design)

**Time 3 (Parallel again):**
- Frontend Build by frontend-developer (uses implemented API)
- API Tests by test-engineer (tests the implemented API)

### TodoWrite for Task Management

The Tech Lead creates tasks with clear descriptions and priorities:

1. "Design authentication flow" - Assigned to security-architect (high priority)
2. "Plan user interface mockups" - Assigned to ui-designer (medium priority)
3. "Implement authentication API" - Assigned to backend-developer (high priority)

The Tech Lead notes that tasks 1 and 2 can run simultaneously since they're independent, while task 3 must wait for task 1 to complete.

## 💬 Agent Communication via Main Coordinator

### Indirect Communication Protocol

Since agents cannot communicate directly, all coordination flows through the main agent:

**Communication Flow:**

1. **Agent A completes task** → Returns findings with handoff notes
2. **Main agent extracts info** → Identifies what Agent B needs  
3. **Main agent invokes Agent B** → Provides filtered context
4. **Agent B works** → Returns results with next steps

### Return Format for Communication

Agents include handoff information in their responses:

```markdown
## Task Completed: [Task Name]
[Task results and details]

## Handoff Information
- What was accomplished: [summary]
- What the next specialist needs: [specific details]
- Any warnings or considerations: [if applicable]
- Suggested next agent: [recommendation]
```

### Communication Examples

**Scenario: Building User Dashboard**

**Backend Developer Returns:**
```
## Task Completed: User API Implementation
- Endpoint: GET /api/users/:id
- Response includes nested 'stats' object
- Structure: {user: {...}, stats: {total_orders: 42, last_login: '2024-01-15'}}

## Handoff Information  
- Frontend needs: Endpoint URL and response structure above
- Consider: Stats object may be large, implement pagination
- Suggested next: frontend-developer for UI implementation
```

**Main Agent to Frontend Developer:**
```
"The backend has completed the user API. It's available at GET /api/users/:id and returns user data with a nested stats object containing metrics. Please implement the dashboard UI with this structure in mind."
```

**Frontend Developer Returns:**
```
## Task Completed: Dashboard UI Started
- Basic UI implemented
- Issue discovered: Need pagination for user lists

## Handoff Information
- Backend needs: Add pagination support (?page=1&limit=20)
- This is blocking the user list view
- Suggested next: django-backend-expert to add pagination
```

## 📋 Common Orchestration Scenarios

### Scenario 1: Full Feature Development

**Request: "Add shopping cart to e-commerce site"**

**Phase 1 - Research:**
The Tech Lead coordinates parallel research:
- E-commerce specialist researches cart implementation patterns
- Payment expert evaluates integration options
- UI/UX designer reviews best practices for cart flows
- Performance expert considers scalability needs

**Phase 2 - Planning:**
Based on research, the Tech Lead creates tasks:
1. Design cart database schema
2. Design cart API endpoints
3. Implement cart backend logic (waits for 1 & 2)
4. Build frontend cart components (waits for 2)
5. Integrate payment processing (waits for 3)
6. Test complete cart flow (waits for 4 & 5)

**Phase 3 - Execution:**
- Group A: Tasks 1 & 2 run in parallel
- Group B: Tasks 3 & 4 run in parallel after Group A
- Group C: Task 5 runs after task 3 completes
- Group D: Task 6 runs after everything else

### Scenario 2: Performance Optimization

**Request: "Site is slow, fix performance"**

**Phase 1 - Research (All parallel):**
- Performance expert profiles backend bottlenecks
- Database specialist analyzes slow queries
- Frontend developer checks bundle sizes
- DevOps reviews infrastructure capacity

**Phase 2 - Planning:**
Priority tasks identified:
1. Add missing database indexes (quick win)
2. Implement Redis caching layer
3. Optimize and compress images
4. Add code splitting for JavaScript

**Phase 3 - Execution:**
Immediate actions (parallel):
- Database optimization
- Image compression

Secondary actions:
- Caching implementation
- Frontend bundle optimization

## 🎯 Best Practices

### 1. Research Phase
- Use tech-lead-orchestrator for comprehensive analysis
- Request structured findings with clear task breakdown
- Ensure tech-lead includes specialist recommendations

### 2. Planning Phase  
- Create TodoWrite tasks based on tech-lead recommendations
- Track dependencies between tasks
- Mark tasks with assigned specialists
- Plan sequential execution order

### 3. Execution Phase
- Invoke one specialist at a time
- Extract handoff information from responses
- Pass filtered context to next specialist
- Update TodoWrite status after each task

### 4. Agent Returns
- Agents must return structured findings
- Include "Handoff Information" section
- Specify what next specialist needs
- Suggest next agent when appropriate

## 🔧 Advanced Patterns

### Dynamic Re-planning

When agents discover unexpected complexity during execution:

1. The agent reports the issue to the Tech Lead
2. Tech Lead updates the task list in TodoWrite
3. New tasks are added or existing ones modified
4. Execution continues with the updated plan

For example, if the backend developer discovers the need for a caching layer that wasn't initially planned, they inform the Tech Lead who then adds a new task for cache implementation.

### Cross-Domain Coordination

For features that span multiple domains, the Tech Lead ensures smooth coordination:

**API-First Development Pattern:**
1. API design is completed first, setting the contract
2. Backend implements according to the API specification
3. Frontend builds against the same API specification
4. Both teams work from the same design, reducing integration issues

### Feedback Loops

The orchestration includes continuous improvement cycles:

1. **Execute** - Agents implement their assigned tasks
2. **Review** - Code reviewer or security expert reviews the work
3. **Refine** - Original agents apply feedback and improvements
4. **Approve** - Tech Lead ensures all requirements are met

This iterative approach ensures high-quality outcomes while maintaining momentum.

## 📊 Metrics for Success

Effective orchestration shows:
- Reduced total execution time via parallelism
- Fewer context switches between agents
- Clear task dependencies and flow
- Minimal information overhead
- Successful inter-agent coordination

## 📊 Main Agent Orchestration Example

Here's a complete example of the main agent orchestrating a feature:

```python
# User: "Build a user authentication system"

# Step 1: Analyze with tech-lead
tech_lead_response = invoke_agent("tech-lead-orchestrator", 
    "Analyze requirements for building a user authentication system")

# Step 2: Create tasks from analysis
tasks = [
    {"id": "1", "content": "Design auth database schema", 
     "agent": "database-architect", "status": "pending"},
    {"id": "2", "content": "Implement auth backend", 
     "agent": "django-backend-expert", "status": "pending"},
    {"id": "3", "content": "Create auth API", 
     "agent": "django-api-developer", "status": "pending"},
    {"id": "4", "content": "Build login UI", 
     "agent": "react-frontend-developer", "status": "pending"}
]

# Step 3: Execute tasks sequentially
for task in tasks:
    # Update task status
    task["status"] = "in_progress"
    update_todo(task)
    
    # Invoke specialist with context
    if task["id"] == "1":
        response = invoke_agent(task["agent"], 
            "Design schema for user authentication with roles")
    elif task["id"] == "2":
        response = invoke_agent(task["agent"],
            f"Implement auth using this schema: {schema_from_task_1}")
    # ... continue for other tasks
    
    # Extract handoff information
    handoff_info = extract_handoff(response)
    
    # Mark complete
    task["status"] = "completed"
    update_todo(task)
```

---

By following these orchestration patterns, the main Claude agent can efficiently coordinate complex projects using specialized sub-agents, despite the limitation that sub-agents cannot invoke each other directly.