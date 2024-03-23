from fastapi import APIRouter, Request, status, HTTPException
from schemas.todo import ResponseGetTodoSchema, ResponseListTodoSchema, ResponsePostTodoSchema, ResponseUpdateTodoSchema, ResponseDeleteTodoSchema
from schemas.todo import RequestUpdateTodoSchema, RequestPostTodoSchema


router = APIRouter()

# Get
@router.get("/{todo_id}", status_code=status.HTTP_200_OK, response_model=ResponseGetTodoSchema)
def get_todo(todo_id: str):
    return {"id": "1", "text": "Fazer compras"}

@router.get("/", status_code=status.HTTP_200_OK, response_model=ResponseListTodoSchema)
def list_todo() -> ResponseListTodoSchema:
    return {[{"id": "1", "text": "Fazer compras"}, {"id": "2", "text": "Limpar casa"}]}

# Post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResponsePostTodoSchema)
def post_todo(request: Request, payload: RequestPostTodoSchema):
    return {"response": {"id": "1", "text": payload.text}}

# Update
@router.put("/{todo_id}", status_code=status.HTTP_200_OK, response_model=ResponseUpdateTodoSchema)
def put_todo(todo_id: str, request: Request, payload: RequestUpdateTodoSchema):
    return {"id": todo_id, "text": payload.text}

# Delete
@router.delete("/{todo_id}", status_code=status.HTTP_200_OK, response_model=ResponseDeleteTodoSchema)
def delete_todo(todo_id: str):
    return {"message": "EXCLUIDO!"}