from fastapi import FastAPI
from pydantic import BaseModel

from calculate.calculator import perform_calculation

class User_Input(BaseModel):
    operation: str
    number1: float
    number2: float

app = FastAPI()

@app.post("/calculate")
def operate(input: User_Input):
    result = perform_calculation(input.operation, input.number1, input.number2)
    return result

