@router.get("/ticket")
async def get_ticket():
    return {"message": "This is the ticket endpoint"}

