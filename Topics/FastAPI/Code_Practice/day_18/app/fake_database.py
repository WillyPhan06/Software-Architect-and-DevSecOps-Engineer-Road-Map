from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.main import app, get_db
from app.models import User
from app.database import Base

# In-memory test database
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine_test = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = async_sessionmaker(bind=engine_test, expire_on_commit=False)

# Dependency override
async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

# Apply override before tests
app.dependency_overrides[get_db] = override_get_db

# Create tables for testing
async def init_test_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
