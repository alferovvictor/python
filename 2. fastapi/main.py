from typing import Union
from fastapi import FastAPI
from fib import get_fib_num
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/body/
class Item(BaseModel):
    order: int
    value: Union[int, None]
    
app = FastAPI()

@app.get('/api/fib')
def fib_get(order: int = 1) -> int:
	return get_fib_num(order)
   
@app.post('/api/fib')
def fib_post(item: Item):
	item.value = get_fib_num(item.order)
	return item
