from fastapi import APIRouter

from data_objects.product import Product

router = APIRouter()

@router.get('/products')
def get_products():
    return [Product(id=1, name='Item', price=9.99).model_dump()]
