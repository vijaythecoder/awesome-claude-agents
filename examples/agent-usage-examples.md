# Agent Usage Examples

This guide demonstrates how to effectively use specialized agents for various development tasks. These examples show real-world scenarios and the expected agent responses.

## Table of Contents

1. [Tech Lead Orchestration](#tech-lead-orchestration)
2. [Code Archaeology](#code-archaeology)
3. [Code Review Process](#code-review-process)
4. [Performance Optimization](#performance-optimization)
5. [Frontend Development](#frontend-development)
6. [Full-Stack Features](#full-stack-features)
7. [Security Auditing](#security-auditing)
8. [Agent Collaboration](#agent-collaboration)

## Tech Lead Orchestration

### Example 1: Building a New Feature

**User Request:**
```
Build a user authentication system with email verification
```

**Expected Flow:**
```
Tech Lead Orchestrator activates and:
1. Analyzes requirements
2. Delegates to API Architect for endpoint design
3. Delegates to Database Optimizer for schema
4. Coordinates Backend Developer for implementation
5. Engages Frontend Developer for UI
6. Calls Security Guardian for audit
7. Ensures Test Engineer validates everything
```

**Result:** Complete authentication system with:
- RESTful API endpoints
- Secure password handling
- Email verification flow
- Frontend forms
- Comprehensive tests

### Example 2: Complex Integration

**User Request:**
```
Integrate Stripe payment processing into our e-commerce platform
```

**Expected Flow:**
```
Tech Lead Orchestrator:
├─→ Payment Integration Expert: Stripe setup
├─→ Backend Developer: API implementation
├─→ Frontend Developer: Checkout UI
├─→ Security Guardian: PCI compliance
└─→ Test Engineer: Integration tests
```

## Code Archaeology

### Example 3: Understanding Legacy Code

**User Request:**
```
I inherited this codebase. Help me understand its architecture
```

**Code Archaeologist Response:**
```
## Codebase Analysis Report

### Architecture Overview
- **Type**: Microservices architecture
- **Services**: 5 independent services
- **Languages**: Python (60%), Go (30%), JavaScript (10%)
- **Database**: PostgreSQL primary, Redis caching

### Key Components
1. **Auth Service** (Python/FastAPI)
   - JWT-based authentication
   - User management
   - Role-based access control

2. **Product Service** (Go)
   - High-performance catalog API
   - Elasticsearch integration
   - Real-time inventory

3. **Order Service** (Python/Django)
   - Order processing workflow
   - Payment integration
   - Email notifications

### Data Flow
[Provides detailed sequence diagrams]

### Technical Debt
- Inconsistent error handling
- Missing API documentation
- Outdated dependencies in auth service
```

### Example 4: Finding Patterns

**User Request:**
```
Find all API endpoints and their authentication methods
```

**Code Archaeologist Analysis:**
```
## API Endpoint Analysis

### Public Endpoints (No Auth)
- GET /api/products
- GET /api/products/{id}
- POST /api/auth/register
- POST /api/auth/login

### Protected Endpoints (JWT Required)
- GET /api/users/profile
- PUT /api/users/profile
- POST /api/orders
- GET /api/orders/history

### Admin Endpoints (Role: admin)
- GET /api/admin/users
- PUT /api/admin/products
- DELETE /api/admin/orders/{id}

### Authentication Patterns
1. JWT in Authorization header
2. 1-hour token expiry
3. Refresh token mechanism
4. Role-based middleware
```

## Code Review Process

### Example 5: Post-Implementation Review

**User Request:**
```
Review the changes I just made to the payment processing
```

**Code Reviewer Analysis:**
```
## Code Review Report

### Changes Reviewed
- Files modified: 8
- Lines added: 342
- Lines removed: 89

### Critical Issues (Must Fix)
1. **Security**: API key exposed in config.js:42
   ```javascript
   // NEVER commit this!
   const STRIPE_KEY = "sk_live_abc123..."; 
   ```
   **Fix**: Use environment variables

2. **Error Handling**: Unhandled promise rejection
   ```javascript
   // Missing catch block
   processPayment(amount).then(result => {...})
   ```

### Warnings (Should Fix)
1. No input validation on amount parameter
2. Missing transaction rollback on failure
3. Logging sensitive customer data

### Suggestions
1. Add idempotency keys for payment retry
2. Implement rate limiting
3. Add monitoring for failed payments

### Positive Findings
✓ Good separation of concerns
✓ Clear function naming
✓ Proper async/await usage
```

## Performance Optimization

### Example 6: Slow Application

**User Request:**
```
Our dashboard takes 15 seconds to load. Fix it!
```

**Performance Optimizer Process:**
```
## Performance Analysis

### Bottlenecks Identified
1. **Database Queries** (12s)
   - N+1 query problem in user listings
   - Missing indexes on frequently queried columns
   - No query result caching

2. **Frontend Bundle** (2s)
   - 8MB JavaScript bundle
   - No code splitting
   - Loading unused libraries

3. **API Calls** (1s)
   - Sequential instead of parallel
   - No response caching

### Optimizations Applied
1. **Database**
   ```sql
   -- Added composite index
   CREATE INDEX idx_users_active_created 
   ON users(active, created_at);
   
   -- Implemented eager loading
   User.with(:orders, :profile).where(active: true)
   ```

2. **Frontend**
   - Implemented code splitting
   - Lazy loaded components
   - Removed moment.js (saved 500KB)

3. **API**
   - Parallelized data fetching
   - Added Redis caching
   - Implemented pagination

### Results
- Load time: 15s → 1.2s (92% improvement)
- First paint: 8s → 0.8s
- Time to interactive: 12s → 2s
```

## Frontend Development

### Example 7: Building UI Components

**User Request:**
```
Create a responsive data table with sorting and filtering
```

**Frontend Expert Implementation:**
```javascript
// Technology-agnostic approach
// Works with React, Vue, Angular, or vanilla JS

class DataTable {
  constructor(config) {
    this.data = config.data;
    this.columns = config.columns;
    this.container = config.container;
    this.state = {
      sortColumn: null,
      sortDirection: 'asc',
      filterText: '',
      currentPage: 1,
      itemsPerPage: 10
    };
  }

  // Sorting logic
  sort(column) {
    if (this.state.sortColumn === column) {
      this.state.sortDirection = 
        this.state.sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      this.state.sortColumn = column;
      this.state.sortDirection = 'asc';
    }
    this.render();
  }

  // Filtering logic
  filter(text) {
    this.state.filterText = text;
    this.state.currentPage = 1;
    this.render();
  }

  // Responsive design with CSS
  getStyles() {
    return `
      .data-table { overflow-x: auto; }
      .data-table table { width: 100%; }
      @media (max-width: 768px) {
        .data-table td { display: block; }
      }
    `;
  }
}
```

## Full-Stack Features

### Example 8: Real-Time Chat System

**User Request:**
```
Build a real-time chat system with typing indicators
```

**Agent Collaboration:**
```
Tech Lead Orchestrator coordinates:

1. Backend Developer creates:
   - WebSocket server (any language)
   - Message persistence
   - User presence tracking

2. Frontend Developer builds:
   - Chat UI components
   - WebSocket client
   - Typing indicators

3. Database Optimizer designs:
   - Message schema
   - Efficient query patterns
   - Archival strategy

4. DevOps Engineer handles:
   - WebSocket scaling
   - Load balancing
   - Redis pub/sub
```

## Security Auditing

### Example 9: Security Review

**User Request:**
```
Audit our application for security vulnerabilities
```

**Security Guardian Report:**
```
## Security Audit Report

### Critical Vulnerabilities
1. **SQL Injection** - user search endpoint
2. **XSS** - unescaped user content
3. **CSRF** - missing tokens on state-changing operations

### High Priority Issues
1. Weak password policy
2. No rate limiting on login
3. Sensitive data in logs
4. Missing HTTPS redirect

### Recommendations
1. Implement prepared statements
2. Add Content Security Policy
3. Enable 2FA
4. Regular dependency updates
5. Security headers configuration

### Positive Findings
✓ Passwords properly hashed (bcrypt)
✓ JWT implementation secure
✓ Input validation on most endpoints
```

## Agent Collaboration

### Example 10: Complex Workflow

**User Request:**
```
Our mobile app crashes when offline. Make it work offline with data sync
```

**Multi-Agent Solution:**
```
1. Debugger Detective:
   - Identifies crash: network timeout exception
   - Finds: no offline handling

2. Mobile Developer:
   - Implements offline storage
   - Adds network state detection
   - Creates sync queue

3. Backend Developer:
   - Creates sync API endpoints
   - Implements conflict resolution
   - Adds versioning

4. Test Engineer:
   - Tests offline scenarios
   - Validates sync integrity
   - Ensures no data loss

Result: Fully offline-capable app with automatic sync
```

## Best Practices for Agent Usage

### 1. Clear Requests
```
// Good
"Build a REST API for user management with authentication"

// Too vague
"Make an API"
```

### 2. Provide Context
```
// Good
"Optimize this React app's bundle size - currently 5MB"

// Missing context
"Make it smaller"
```

### 3. Trust Agent Delegation
Let the Tech Lead Orchestrator coordinate specialists rather than calling each agent manually.

### 4. Iterative Refinement
```
1. "Build a search feature"
2. "Add filters to the search"
3. "Make search results real-time"
```

### 5. Leverage Expertise
Each agent has deep knowledge in their domain - use them for both implementation and consultation.

## Advanced Patterns

### Chain of Responsibility
```
User Request → Tech Lead → Specialists → Integration → Review → Deploy
```

### Parallel Processing
Multiple agents can work simultaneously:
- Frontend Dev builds UI
- Backend Dev creates API
- DevOps sets up infrastructure

### Feedback Loops
```
Code → Review → Fix → Re-review → Approve
```

The agent system is designed to mirror real development teams, providing expertise exactly when needed while maintaining context and ensuring quality throughout the development process.