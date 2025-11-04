# filename: main.py
from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi

# --- Routers setup ---
router_v1 = APIRouter(prefix="/v1", tags=["Players"])

@router_v1.get("/players/{player_name}", summary="Get player profile")
def get_player(player_name: str):
    return {"player_name": player_name, "level": 10, "coins": 250}

@router_v1.get("/leaderboard", summary="Get leaderboard")
def get_leaderboard():
    return {"top_players": ["WillyPhan", "Sakamoto", "AlanWalker"]}


# --- Main app ---
app = FastAPI(
    title="Game API",
    description="An API for player profiles and leaderboards.",
    version="1.0.0",
    contact={
        "name": "Support Team",
        "url": "https://example.com/support",
        "email": "support@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(router_v1)


# --- Customizing OpenAPI schema ---
def custom_openapi():
    """
    This function overrides FastAPI's default OpenAPI schema generator.
    You can modify the schema before it's served or exported.
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Add custom logo or metadata
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }

    # Add custom field
    openapi_schema["info"]["x-game-meta"] = {
        "developer": "Willy Phan",
        "genre": "RPG",
    }

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# Override default schema generator
app.openapi = custom_openapi


# --- Optional route to export OpenAPI schema ---
@app.get("/openapi.json", include_in_schema=False)
def export_openapi_schema():
    """Export the custom OpenAPI schema as JSON."""
    return app.openapi()
