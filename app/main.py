import uvicorn
from fastapi import FastAPI

from app.api import router_api_v1

app = FastAPI(
    title="GKP Info",
    version="1.0"
)

app.include_router(router_api_v1)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
        port=7777
    )
