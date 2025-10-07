from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project_name.api.v1 import api_router

# Initialize FastAPI app
app = FastAPI(
    title="project_name",
    version="0.1.0",
    description="A FastAPI application.",
    summary="This is a minimal example API to serve as a template for IIDS applications using FastAPI as a backend",
    terms_of_service="https://example.com/terms/",
    contact={"name": "your_name", "email": "your-email@uidaho.edu"},
    license_info={
        "name": "GNU General Public License v3.0",
        "identifier": "GNU GPL-3.0-or-later",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
    servers=[
        {
            "url": "https://project-name.insight.uidaho.edu",
            "description": "Production server",
        },
        {
            "url": "https://project-name.k8s-dev.hpc.uidaho.edu",
            "description": "Development server",
        },
    ],
)

# Example CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
