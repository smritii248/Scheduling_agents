from datetime import datetime, timedelta
from typing import Optional

class Task:
    def __init__(self, name: str, priority: int, duration_minutes: int, deadline: Optional[datetime] = None):
        self.name = name
        self.priority = priority
        self.duration = timedelta(minutes=duration_minutes)
        self.deadline = deadline
        self.scheduled_time = None

    def __lt__(self, other):
        return self.priority < other.priority





