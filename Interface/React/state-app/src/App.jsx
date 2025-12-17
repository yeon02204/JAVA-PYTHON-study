import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import BadCounter from './components/BadCounter'
import CounterFunctional from './components/CounterFunctional'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <BadCounter></BadCounter>
      <CounterFunctional/>
    </>
  )
}

export default App
