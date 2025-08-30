import { useState, useEffect } from "react";
import "../../index.css";

export function Todo() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    const get_todo = async () => {
      try {
        const res = await fetch('http://localhost:3000/todo/');
        const data = await res.json();
        setTodos(data);
      } catch (err) {
        console.error(err);
      }
    }; 
    get_todo();
  }, []);

  return (
    <div>
      <h1>Todo</h1>
      <div>
        <ul>
          {todos.map((todo, index) => (
            <li key={index}>{todo.task}</li>
          ))}
        </ul>
      </div>
      <div>
        <a href="/">Home</a>
      </div>
    </div>
  );
}

export default Todo;
