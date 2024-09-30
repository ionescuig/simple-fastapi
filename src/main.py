from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse


app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    """Redirect to the /docs page."""
    return RedirectResponse(url="/docs", status_code=status.HTTP_303_SEE_OTHER)


app.router.prefix = "/api"


@app.get("/test")
async def test():
    """Test endpoint."""
    return {"message": "Hello World!"}
