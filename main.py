import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv(override=True)

if __name__ == "__main__":
    from app.api.api import router
    app = FastAPI(
        title="metadata_ms",
        description="Retrieves the metadata from the contract",
        version="0.1.0"
    )
    app.include_router(router)

    uvicorn.run(app, host="0.0.0.0", port=8000)
    