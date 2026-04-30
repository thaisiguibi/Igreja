from fastapi import FastAPI, Request
from routers import posts
from routers import users
from core.db import init_db
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import newsletter
from fastapi.middleware.cors import CORSMiddleware
import traceback

app = FastAPI()
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(newsletter.router)

init_db()

@app.get("/")
def home():
    return {
        "message": "API Igreja online 🚀",
        "docs": "/docs"


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
            status_code=exc.status_code,
            content={
                "data": None,
                "message": exc.detail
                }
            )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
            status_code=422,
            content={
                "data": None,
                "message": "Erro de validação",
                "error": exc.errors()
                }
            )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
            status_code=500,
            content={
                "data": None,
                "message": "Erro interno de servidor"
                }
            )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    print(traceback.format_exc())  # 👈 loga erro real

    return JSONResponse(
            status_code=500,
            content={
                "data": None,
                "message": "Erro interno de servidor"
                }
            )
