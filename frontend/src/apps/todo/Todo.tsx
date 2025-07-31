import { useState } from "react";

export function Todo() {
  const [task, setTask] = useState("");
  const [todo, setTodo] = useState([]);

  return (
    <>
      <h1>ToDo</h1>

      <div>
        <input
          type="text"
          id="task"
          onChange={e => setTask(e.target.value)}
        />

        <button
          onClick={() => setTodo(prevTodo => [...prevTodo, task])}
        >
          登録
        </button>
      </div>

      <div>
        { todo.map((t, id) => <p key={id}>{t}</p>) }
      </div>
    </>
  )
}

export default Todo;
