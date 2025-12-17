import { useState } from "react";

export default function CounterBugExample(){
    const [count, setCount] = useState(0);

    return(
        <div>
            <h1>count : {count}</h1>
            <button onClick={()=>{
                // setCount(count + 1);
                // setCount(count + 1);
                // prev에는 직전의 state값이 들어있다
                setCount((prev) => prev +1);
                setCount((prev) => prev +1);
                
            }}>
                +2 증가
            </button>
        </div>
    )
}