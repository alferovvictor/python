from typing import Union
from fastapi import FastAPI
from fib import get_fib_num
from pydantic import BaseModel
import uvicorn
import threading

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
async def fib_get(order: int = 1) -> int:
	threading.active_count()
	return get_fib_num(order)
   
@app.post('/api/fib')
async def fib_post(item: Item):
	item.value = get_fib_num(item.order)
	return item

# https://fastapi.tiangolo.com/tutorial/debugging/
def serve():
	"""Serve the web application."""
	uvicorn.run(app=app, access_log=False)

if __name__ == "__main__":
	serve()