import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI, responses

sys.path.append(str(Path(__file__).parent.parent))

from src.api.incident import router as incident_router



app = FastAPI(description="<h1>Api Incident Service</h1>")


@app.get("/", include_in_schema=False)
async def root():
    return responses.RedirectResponse(url="/docs")


app.include_router(incident_router)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
