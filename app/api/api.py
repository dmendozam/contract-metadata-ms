from datetime import datetime, timezone

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.schemas.schemas import Metadata


router = APIRouter(
    prefix="/api/v1",
    tags=["api"]
)


@router.get("/")
async def root():
    return {"message": "Server is Working"}


@router.get("/health")
async def health():
    return JSONResponse({"status": "ok"})


@router.post("/metadata")
async def metadata(metadata: Metadata, request: Request):
    """
    Retrieves the metadata from the contract and writes
    it to the database.

    Args:
        Metadata (Metadata): metadata from the contract
        request (Request): request information 
            from the client
        
    Returns:
        JSONResponse: response from the server
    """
    request_date = datetime.now(tz=timezone.utc).isoformat()
    client_info = {
        "host": request.client.host,
        "port": request.client.port,
        "user_agent": request.headers.get("User-Agent")
    }
    print(f"{request_date}")
    return JSONResponse(client_info)
