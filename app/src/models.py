import uuid
from datetime import datetime
from enum import Enum


class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Task:
    def __init__(self, name, due_date, priority, description="", id=None):
        self.id = id if id else uuid.uuid4()
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.description = description

    def __str__(self):
        due_date_obj = datetime.strptime(self.due_date, "%Y-%m-%d %H:%M:%S")
        formatted_due_date = due_date_obj.strftime("%d/%m/%Y %I:%M%p")

        return (
            f"Task ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Due Date: {formatted_due_date}\n"
            f"Priority: {self.priority.name}\n"
            f"Description: {self.description}"
        )
