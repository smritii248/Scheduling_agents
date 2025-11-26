import heapq
from datetime import datetime, timedelta
from typing import List, Dict, Any
from schema import Task

class SchedulingAgent:
    def __init__(self, start_time: datetime, end_time: datetime):
        self.start_time = start_time
        self.end_time = end_time
        self.tasks: List[Task] = []
        self.schedule: List[Dict[str, Any]] = []

    def add_task(self, task: Task):
        heapq.heappush(self.tasks, task)

    def optimize_schedule(self):
        current_time = self.start_time
        tasks = [heapq.heappop(self.tasks) for _ in range(len(self.tasks))]
        for task in tasks:
            if current_time + task.duration <= self.end_time:
                task.scheduled_time = current_time
                self.schedule.append({
                    "name": task.name,
                    "start": current_time,
                    "end": current_time + task.duration,
                    "priority": task.priority
                })
                current_time += task.duration

        
        
        















