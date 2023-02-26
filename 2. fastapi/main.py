from typing import Union
from fastapi import FastAPI
from fib import get_fib_num
from pydantic import BaseModel
import uvicorn

# https://fastapi.tiangolo.com/tutorial/body/
class Item(BaseModel):
	order: int
	value: Union[int, None]
	
app = FastAPI()

"""
webapp.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)
"""

@app.get('/api/fib')
def fib_get(order: int = 1) -> int:
	return get_fib_num(order)
   
@app.post('/api/fib')
def fib_post(item: Item):
	item.value = get_fib_num(item.order)
	return item

# https://stackoverflow.com/questions/67453019/uvicorn-fastapi-executable
def serve():
	"""Serve the web application."""
	uvicorn.run(app)

if __name__ == "__main__":
	serve()