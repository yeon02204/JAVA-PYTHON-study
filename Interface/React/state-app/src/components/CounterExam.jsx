import { useState } from 'react'

export default function CounterExam(){
    const [count, setCount] = useState(0)
    return(
        <>
        <h1>{count}</h1>
        <button onClick={()=>{
            setCount((prev) => prev +1);
        }}>+1</button>

        <button onClick={()=>{
            setCount((prev) => prev -1);
        }}>-1</button>

        <button onClick={()=>{
            setCount(0);
        }}>Reset</button>
        </>
    )
}