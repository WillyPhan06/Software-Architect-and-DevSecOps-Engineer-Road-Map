from fastapi import APIRouter

from data_objects.user import User

router = APIRouter()

@router.get('/users')
def get_users():
    return [User(id=1, name='Willy').model_dump()]
