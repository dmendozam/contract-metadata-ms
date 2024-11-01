from datetime import datetime, timezone

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from app.core.metadata import process_metadata
from app.db import settings
from app.schemas.schemas import Metadata


router = APIRouter(
    prefix="/api/v1",
    tags=["api"]
)


@router.get("")
async def root():
    return {"message": "Server is Working"}


@router.get("/health")
async def health():
    return JSONResponse({"status": "ok"})


@router.post("/metadata")
async def metadata(metadata: Metadata):
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
    try:
        request_date = datetime.now(tz=timezone.utc).isoformat()
        # TODO How can we get the ip and host from the client
        client_info = {
            "host": "Null",
            "port": 0,
            "user_agent": "Null"
        }

        insert_res = process_metadata(request_date, client_info, metadata)
        resp = {"message": insert_res}
        status_code = 200
    except Exception as e:
        resp = {"error": "There was an error processing the metadata",
                "metadata": metadata.__dict__}
        status_code = 500
    return JSONResponse(resp, status_code=status_code)