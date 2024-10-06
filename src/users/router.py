from fastapi import APIRouter, HTTPException, status
from uuid import UUID
router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users():
    """Get all users."""
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{uuid}")
async def get_user(uuid: UUID):
    """Get all users."""
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    # return [{"username": "Rick"}, {"username": "Morty"}]
