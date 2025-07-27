# Orchestration Patterns - Advanced Agent Coordination

This guide documents the three-phase orchestration workflow and patterns for efficient agent coordination.

## 🎯 Core Orchestration Philosophy

The Tech Lead Orchestrator manages complex tasks through three distinct phases:

1. **Research Phase** - Parallel information gathering
2. **Planning Phase** - Task creation with dependencies
3. **Execution Phase** - Coordinated implementation with context filtering

## 📊 Three-Phase Workflow

### Phase 1: Research & Analysis

During research, the Tech Lead coordinates multiple specialists who work in parallel:

- The project-analyst examines the codebase structure and technology stack
- Domain experts research specific requirements for their areas
- Security specialists identify potential concerns early
- Performance experts consider optimization needs from the start

All findings are aggregated to inform the planning phase.

**Example Research Delegation:**

When a user requests "Build a payment system", the Tech Lead delegates research tasks in parallel:
- To payment-expert: "What payment providers work best with our technology stack?"
- To security-guardian: "What PCI compliance requirements must we meet?"
- To database-optimizer: "How should we securely store payment data?"
- To frontend-developer: "What UI components are needed for payment flows?"

### Phase 2: Planning & Task Creation

Based on research, the Tech Lead creates a detailed execution plan using TodoWrite. Each task includes:
- A specific, actionable description
- The assigned specialist agent
- Priority level (high, medium, or low)
- Current status (pending, in_progress, or completed)

**Dependency Management:**

The Tech Lead identifies which tasks can run in parallel and which have dependencies:

**Group A (Can run simultaneously):**
- Database schema design
- API endpoint planning  
- UI mockup creation

**Group B (Depends on Group A):**
- API implementation (requires completed schema)
- Frontend development (requires API endpoint design)

**Group C (Final phase):**
- Integration testing
- Documentation
- Security review

### Phase 3: Execution & Coordination

During execution, the Tech Lead ensures smooth coordination:

1. Tasks are assigned according to the TodoWrite plan
2. Each agent receives only the context relevant to their task
3. Parallel tasks execute simultaneously for efficiency
4. Agents communicate directly with each other when coordination is needed
5. Results are aggregated and presented as a cohesive solution

## 🔄 Context Filtering Patterns

### Information Scoping

Each agent receives only the information relevant to their task:

**Backend Developer receives:**
- API requirements and specifications
- Database schema details
- Business logic rules
- Authentication method to implement

**Backend Developer doesn't receive:**
- CSS framework choices
- UI component details
- Frontend state management decisions

**Frontend Developer receives:**
- API endpoint URLs and methods
- Response formats and data structures
- Authentication flow details
- UI requirements and mockups

**Frontend Developer doesn't receive:**
- Database query implementations
- Server configuration details
- Backend algorithm specifics

### Context Passing Examples

**From Tech Lead to Backend Developer:**
"Your task is to implement the user API. You need to create CRUD operations with JWT authentication and role-based access control. Focus on the backend logic - the frontend team will handle the UI separately."

**From Backend to Frontend Developer:**
"The API is ready. User endpoints are available at POST /api/users and GET /api/users/:id. Authentication uses Bearer tokens in the Authorization header. Here are the response formats you'll receive..."

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

## 💬 Inter-Agent Communication

### Direct Communication Protocol

Agents communicate during execution for coordination:

**Types of Communication:**

1. **Information Sharing**
   - Backend to Frontend: "Just a heads up - all API endpoints now use the /api/v2 prefix"
   
2. **Request for Change**
   - Frontend to Backend: "I need CORS enabled for localhost:3000 to test the integration"
   
3. **Warning/Alert**
   - Security to Backend: "Make sure you're not logging any sensitive user data in the new endpoints"
   
4. **Confirmation**
   - Database to Backend: "I've created the indexes - your queries should run much faster now"

### Communication Examples

**Scenario: Building User Dashboard**

Backend developer to Frontend developer:
"The user API at GET /api/users/:id now includes a nested 'stats' object with user metrics. The response structure is {user: {...}, stats: {total_orders: 42, last_login: '2024-01-15'}}."

Frontend developer to Backend developer:
"I need pagination for the user list. Can you support query parameters like ?page=1&limit=20? We want to load 20 users per page."

Database optimizer to Backend developer:
"I've created a compound index 'idx_users_created_status' on the users table. This will significantly improve your getUsersSorted() query performance."

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
- Always start with project-analyst for context
- Run domain research in parallel
- Gather all information before planning

### 2. Planning Phase
- Break down into atomic, specific tasks
- Clearly mark dependencies
- Identify parallelism opportunities
- Assign specific agents to each task

### 3. Execution Phase
- Filter context to relevant information only
- Enable direct agent communication
- Monitor progress via TodoWrite
- Aggregate results for coherent output

### 4. Communication
- Keep messages concise and specific
- Include only necessary context
- Use structured format for clarity
- Document decisions for future reference

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

---

By following these orchestration patterns, the Tech Lead can efficiently coordinate complex projects while maximizing parallel execution and maintaining clear communication channels between specialists.