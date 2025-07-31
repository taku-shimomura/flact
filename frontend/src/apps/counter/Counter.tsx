import { useState } from "react";

import "../../index.css";

export function Counter() {
  const [count, setCount] = useState<number>(0);

  return (
    <>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>Click</button>
    </>
  );
}

export default Counter;
