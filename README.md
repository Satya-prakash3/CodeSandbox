# CodeSandbox

A secure, scalable backend system for executing untrusted user code in isolated environments using containerization and strict resource controls.

---

## Overview

CodeSandbox is designed to safely execute arbitrary code submitted by users without compromising the host system. It leverages Docker-based isolation, asynchronous job processing, and enforced runtime constraints to prevent malicious behavior such as infinite loops, resource exhaustion, and unauthorized system access.

This project demonstrates strong backend engineering capabilities, including secure system design, distributed processing, and infrastructure-level problem solving.

---

## Key Features

### Secure Execution

- Isolated execution using Docker containers
- No direct access to host system resources
- Optional network isolation
- Configurable read-only file system

### Execution Engine

- Supports dynamic code execution
- Handles standard input, output, and error streams
- Enforces execution time limits
- Extensible for multiple programming languages

### Resource Management

- CPU usage limits
- Memory constraints
- Execution timeouts
- Process limits to prevent abuse

### Asynchronous Processing

- Job queue implemented using Celery and Redis
- Non-blocking API design
- Retry mechanism for failed executions

### Logging and Monitoring

- Execution logs (stdout and stderr)
- Execution time tracking
- Job status lifecycle (Pending, Running, Success, Failed, Timeout)

### Abuse Prevention

- Rate limiting for API usage
- Optional user-level quotas

---

## System Architecture

Client → Django API → Redis Queue → Celery Worker → Docker Container → Result Storage

### Components

- Django and Django REST Framework: API layer
- Redis: Message broker for job queue
- Celery: Asynchronous task processing
- Docker: Secure execution environment
- PostgreSQL: Persistent data storage

---

## Execution Flow

1. User submits code via API
2. API validates input and creates a job entry
3. Job is pushed to Redis queue
4. Celery worker retrieves the job
5. Worker initializes a Docker container
6. Code is executed with defined constraints
7. Output and execution metadata are captured
8. Results are stored and made available via API

---

## Security Considerations

CodeSandbox is built to mitigate common risks associated with executing untrusted code:

- Infinite loops: Controlled via execution timeouts
- Memory exhaustion: Restricted using container memory limits
- File system access: Prevented through container isolation
- Network abuse: Optional disabling of network access
- Process spawning attacks: Limited using process constraints
- Privilege escalation: Containers run with restricted permissions

---

## Technology Stack

- Backend: Django, Django REST Framework
- Frontend: Next JS
- Task Queue: Celery
- Message Broker: Redis
- Database: PostgreSQL
- Containerization: Docker

## Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Docker
- Redis
- PostgreSQL
- node and npm

### Setup Steps

1. Clone the repository
   git clone https://github.com/Satya-prakash3/CodeSandbox.git
   cd CodeSandbox

## Testing

Run tests using:

pytest

Testing includes:

- Unit tests for execution logic
- API integration tests
- Security-focused test scenarios

---

## Future Enhancements

- Support for multiple programming languages
- Real-time execution updates using WebSockets
- Distributed worker architecture
- Execution result caching
- Static code analysis before execution
- Monitoring dashboard

---

## License

This project is licensed under the apache2 License.

---

## Author

Satyaprakash Sethy
Contact: satyaprakashsethy905@gmail.com

---

## Summary

CodeSandbox is a backend-focused system that demonstrates secure execution of untrusted code, asynchronous processing, and infrastructure-level design. It is intended to reflect real-world engineering challenges and solutions in building safe and scalable execution environments.
