import { useState } from "react";

import "../../index.css";

export function Sample() {
  const [count, setCount] = useState<number>(0);

  const countUp = (e: Event) => {
    e.preventDefault();
    setCount(count + 1);
  }

  return (
    <>
      <p>{count}</p>
      <button onClick={countUp}>Up</button>
    </>
  );
}

export default Sample;
