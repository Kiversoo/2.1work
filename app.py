import datetime
from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form

class Order(BaseModel):
   number : int
   startDate: datetime.date
   device : str
   problemType : str
   description : str 
   client : str
   status : str 

repo = [
   Order(
      number : 1,
      startDate : "2000-12-01",
      device : "123",
      problemType : "123",
      description : "123",
      client : "123",
      status : "в ожидании",
      master : Optional[str] = "не назначен"

   )
]

class UpdateOrderDTO(BaseModel):
      number: int
      status: Optional[str] = ""
      description: Optional[str] = ""
      master: Optional[str] = ""
    


app = FastAPI()
 
@app.get("/orders")
def get_orders():
   return repo

@app.post("/orders")
def create_order(dto : Annotated[Order, Form()]):
   repo.append(dto)
