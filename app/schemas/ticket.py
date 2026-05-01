from datetime import datetime
from enum import StrEnum

from fastapi import HTTPException
from pydantic import BaseModel, Field, model_validator


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
        examples= ["high"],
    )


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus
    priority: TicketPriority
    owner_id: int
    created_at: datetime
    updated_at: datetime


class TicketUpdate(BaseModel):
    title: str | None= Field(
        default=None,
        min_length=3,
        max_length=100,
        description= "The title of the ticket, must be between 3 and 100 characters.",
        examples= ["Issue with login"],
    )
    description: str | None = Field(
        default=None,
        min_length=10,
        max_length=1000,
        description= "A detailed description of the issue, must be between 10 and 1000 characters.",
        examples= ["I am unable to log in to my account using my credentials."],
    )
    status: TicketStatus | None = Field(
        default=None,
        description= "The current status of the ticket.",
        examples= ["in progress"],
    )
    priority: TicketPriority | None = Field(
        default=None,
        description= "The priority level of the ticket.",
        examples= ["high"],
    )

    @model_validator(mode="after") # this runs after all the above checks, we use this in ticket update to make sure that at least one field is provided for update otherwise returns self
    def validate_at_least_one_field(self):
        if (
            self.title is None
            and self.description is None
            and self.status is None
            and self.priority is None
        ):
            raise HTTPException(status_code=400, detail="At least one field must be provided for update.")
        return self
    
class TicketListResponse(BaseModel):
    tickets: list[TicketResponse]
    total: int
    page: int
    limit: int
    