from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.models import User
from app.database import Base, get_db, engine

# Lifespan context
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup: create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown: (optional cleanup if needed)
    # e.g., await engine.dispose()

app = FastAPI(lifespan=lifespan)

# Endpoints
@app.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@app.post("/users/")
async def create_user(user: dict, db: AsyncSession = Depends(get_db)):
    new_user = User(username=user["username"], email=user["email"])
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
