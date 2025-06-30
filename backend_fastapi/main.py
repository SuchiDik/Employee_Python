from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import employee

app = FastAPI(
    title="Employee CRUD API",
    description="A simple API with FastAPI, SQLite, CORS, Swagger, and Token Authentication",
    version="1.0.0"
)

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routers
app.include_router(employee.router)