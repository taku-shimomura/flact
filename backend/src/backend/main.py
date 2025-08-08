from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Todo(BaseModel):
    task: str
    done: bool = False


todo_list: List[Optional[Todo]] = []
app = FastAPI()


@app.get("/api/todos")
async def todos() -> List[Optional[Todo]]:
    return todo_list


@app.post("/api/todos")
async def create_todo(todo: Todo) -> List[Optional[Todo]]:
    todo_list.append(todo)
    return todo_list
