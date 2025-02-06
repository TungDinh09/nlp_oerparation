from fastapi import FastAPI
from nlp_perpararion.routes.text_route import text_route
from nlp_perpararion.routes.frontend_route import frontend_route
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import re

def create_app():
    app = FastAPI(docs_url="/docs",
            description='''
            Base frame with FastAPI micro framework + MySql
            ''')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
    app.mount("/nlp_perparation_fe", StaticFiles(directory="nlp_perparation_fe"), name="nlp_perparation_fe")

    app.include_router(text_route)
    app.include_router(frontend_route)
    return app
app = create_app()
