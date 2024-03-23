from pydantic import BaseModel
from typing import List


class TodoSchema(BaseModel):
    id: str
    text: str

# Get
class ResponseGetTodoSchema(BaseModel):
    response: TodoSchema

class ResponseListTodoSchema(BaseModel):
    todos: List[TodoSchema]

# Post 
class RequestPostTodoSchema(BaseModel):
    text: str

class ResponsePostTodoSchema(BaseModel):
    response: TodoSchema

# Update
class RequestUpdateTodoSchema(BaseModel):
    text: str

class ResponseUpdateTodoSchema(BaseModel):
    response: TodoSchema

# Delete
class ResponseDeleteTodoSchema(BaseModel):
    message: str