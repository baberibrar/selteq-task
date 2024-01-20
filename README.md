# Selteq-Task Django Project

## Overview

This Django project, named "selteq_task," serves as a foundation for a custom authentication and authorization system, API development, Celery integration for asynchronous tasks, and Docker containerization.

## Project Structure

The project is organized into the following main components:

1. **Custom Authentication and Authorization:**
   - Custom middleware is implemented to secure endpoints and manage user access.

2. **API Development:**
   - **POST API Endpoint:** `{{baseurl}}/task/`
     - Retrieves the current time, date, and a short string (task name) provided by the user.
   - **GET API Endpoint:** `{{baseurl}}/tasks/`
     - Retrieves the list of created tasks for the logged-in user.

3. **Celery Integration:**
   - Utilizes Celery in conjunction with Redis to manage asynchronous task execution.

4. **Scheduled Tasks:**
   - Implements scheduled tasks using Celery that print the provided short string (task name) at the specified time when the user adds the task.

5. **Docker Containerization:**
   - Configures Docker to run the Redis service and the Django application.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Django
- Redis
- Docker

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Selteq-Task.git
   cd Selteq-Task
2. Install dependencies:
   ```bash
   pip install -r requirements.txt     
3. Run migrations:
   ```bash
   python manage.py migrate
4. Start Celery worker:
   ```bash
   celery -A selteq_task worker -l info
5. Run the Django development server:
   ```bash
   python manage.py runserver
