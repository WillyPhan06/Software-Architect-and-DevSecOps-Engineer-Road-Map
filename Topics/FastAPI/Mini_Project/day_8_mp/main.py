from fastapi import FastAPI
from end_points.users import router as users_router
from end_points.products import router as products_router

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)
