from fastapi import FastAPI
from agents import SchedulingAgent
from schema import Task
from datetime import datetime, timedelta

app = FastAPI()

agent = SchedulingAgent(
    start_time=datetime.now(),
    end_time=datetime.now() + timedelta(hours=8)
)

@app.get("/")
def read_root():
    return {"message": "Task Scheduling API is running!"}

@app.post("/tasks/")
def add_task(name: str, priority: int, duration: int):
    task = Task(name=name, priority=priority, duration=duration)
    agent.add_task(task)
    return {"message": "Task added"}

@app.post("/schedule/")
def schedule_tasks():
    agent.optimize_schedule()
    return {"schedule": agent.schedule}










