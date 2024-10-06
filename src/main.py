from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

from settings.database import init_db
from users import router as users

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Initialize the database."""
    await init_db()


@app.get("/", include_in_schema=False)
async def root():
    """Redirect to the /docs page."""
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)


app.router.prefix = "/api"

app.include_router(users.router)
