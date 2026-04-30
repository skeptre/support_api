from pydantic import BaseModel, Field
from datetime import datetime
from enum import StrEnum

class TicketStatus(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class TicketPriority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class TicketCreate(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=100,
        description= "The title of the ticket, must be between 3 and 100 characters.",
        examples= ["Issue with login"],
    )
    description: str = Field(
        min_length=10,
        max_length=1000,
        description= "A detailed description of the issue, must be between 10 and 1000 characters.",
        examples= ["I am unable to log in to my account using my credentials."],
    )
    priority: TicketPriority = Field(
        default=TicketPriority.MEDIUM,
        description= "The priority level of the ticket.",
        examples= [TicketPriority.HIGH],
    )