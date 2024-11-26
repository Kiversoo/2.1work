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

@app.post("/update")
def update_order(dto : Annotation[UpdateOrderDTO, Form()]):
    for o in repo:
        if o.number == dto.number:
            if dto.status != o.status and dto.status != "":
                o.status = dto.status
            if dto.description != "":
                o.description = dto.description
            if dto.master != "":
                o.master = dto.master
            return o 
    return "не найдено"