from fastapi import FastAPI
from tortoise import Tortoise, fields
from tortoise.models import Model
from contextlib import asynccontextmanager

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["tortoise_main"]}

    )
    await Tortoise.generate_schemas()
    yield
    # Shutdown logic
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

@app.post("/async-users/")
async def create_user(username: str, email: str):
    user = await User.create(username=username, email=email)
    return user

@app.get("/async-users/")
async def get_users():
    return await User.all()
