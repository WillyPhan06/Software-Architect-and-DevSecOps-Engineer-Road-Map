from fastapi import Depends, FastAPI
from sqlalchemy import Column, Integer, String
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from db_engine import AsyncSessionLocal, Base, engine
from typing import List
from pydantic import BaseModel, EmailStr
import asyncio
import time

class UserCreate(BaseModel):
    username: str
    email: EmailStr


# ------------------------
# ORM Model
# ------------------------
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

# ------------------------
# Dependency: get async DB session
# ------------------------
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# ------------------------
# Lifespan for startup/shutdown
# ------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield  # Application runs here
    # Shutdown code could go here if needed

# ------------------------
# FastAPI app
# ------------------------
app = FastAPI(lifespan=lifespan)

# ------------------------
# Routes
# ------------------------
@app.post("/async-users/")
async def create_user(username: str, email: str, db: AsyncSession = Depends(get_db)):
    user = User(username=username, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@app.get("/async-users/")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()

@app.post("/async-users-batch/")
async def create_multiple_users(
    users: List[UserCreate],  # Use Pydantic model
    db: AsyncSession = Depends(get_db)
):
    start = time.time()
    created_users = []
    async with db.begin():  # Transaction block
        for u in users:
            user = User(username=u.username, email=u.email)
            db.add(user)
            created_users.append(user)
    await db.commit()
    
    # Refresh to get database-generated IDs
    await asyncio.gather(*(db.refresh(user) for user in created_users))
    duration = time.time() - start
    print(f"Created {len(users)} users in {duration:.2f} seconds")
    
    return {"message": f"{len(users)} users created", "users": [u.__dict__ for u in created_users]}

@app.post("/sync-users-batch/")
async def create_multiple_users(
    users: List[UserCreate],  # Use Pydantic model
    db: AsyncSession = Depends(get_db)
):
    start = time.time()
    created_users = []
    async with db.begin():  # Transaction block
        for u in users:
            user = User(username=u.username, email=u.email)
            db.add(user)
            created_users.append(user)
    await db.commit()
    
    # Refresh to get database-generated IDs
    for user in created_users:
        await db.refresh(user)
    duration = time.time() - start
    print(f"Created {len(users)} users in {duration:.2f} seconds")
    
    return {"message": f"{len(users)} users created", "users": [u.__dict__ for u in created_users]}

