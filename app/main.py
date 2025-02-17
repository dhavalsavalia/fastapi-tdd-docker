import logging

from fastapi import FastAPI

from app.api import ping
from app.db import init_db


def create_application() -> FastAPI:
    application = FastAPI(
        lifespan=init_db
    )

    application.include_router(ping.router)

    return application


app = create_application()