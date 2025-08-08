from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Todo(BaseModel):
    task: str
    done: bool = False


todo_list: List[Optional[Todo]] = []
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/todos")
async def todos() -> List[Optional[Todo]]:
    return todo_list


@app.post("/api/todos")
async def create_todo(todo: Todo) -> List[Optional[Todo]]:
    todo_list.append(todo)
    return todo_list
