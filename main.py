from fastapi import FastAPI, Request
from routers import posts
from routers import users
from core.db import init_db
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)

init_db()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.detail,
                "status": exc.status_code
                }
            )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
            status_code=422,
            content={
                "error": "Invalid data",
                "details": exc.errors()
                }
            )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
            status_code=500,
            content={
                "error": "Internal server error"
                }
            )   
