# Task Scheduling API


A FastAPI-based REST API for scheduling tasks with priority-based optimization.

# Features
- Add tasks with name, priority, and duration
- Optimize task schedule based on priority
- 8-hour scheduling window
- RESTful API endpoints

# Installation 
1. Clone the repository
2. Install dependencies:
   
pip install fastapi uvicorn

# API Endpoints

# GET /
Health check endpoint that confirms the API is running.

# POST /tasks/
Add a new task to be scheduled.

Parameters:

name (string): Task name
priority (integer): Task priority (higher number = higher priority)
duration (integer): Task duration in minutes







 

