from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

# Import your schema
from app.schemas.ticket import TicketResponse, TicketStatus, TicketPriority

router = APIRouter()

# Example mock data (Replace this with actual data from your database later)
tickets = [
    TicketResponse(
        id=1,
        title="Issue with login",
        description="I can't log in with my credentials",
        status=TicketStatus.OPEN,
        priority=TicketPriority.HIGH,
        owner_id=123,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
    TicketResponse(
        id=2,
        title="Password reset issue",
        description="I forgot my password and can't reset it",
        status=TicketStatus.IN_PROGRESS,
        priority=TicketPriority.MEDIUM,
        owner_id=124,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ),
]

# Define the route
@router.get("/tickets", response_model=List[TicketResponse])
async def get_tickets() -> List[TicketResponse]:
    # Return the list of tickets
    return tickets


@router.get("/tickets/{ticket_id}", response_model=TicketResponse)
async def get_ticket(ticket_id: int) -> TicketResponse:
    # Find the ticket by ID (Replace this with actual database query)
    for ticket in tickets:
        if ticket.id == ticket_id:
            return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")