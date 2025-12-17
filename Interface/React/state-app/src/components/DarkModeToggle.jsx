import { useState } from 'react'

export default function DarkModeToggle(){
    const [isDark, setDark] = useState(false)

    
    return(
        <div
      style={{
        padding: 16,
        backgroundColor: isDark ? "#111" : "#fff",
        color: isDark ? "#fff" : "#111",
        minHeight: 200,
        border:'1px',
      }}>
      <h2>확장 1) 다크모드</h2>
      <p>현재 모드: {isDark ? "Dark" : "Light"}</p>
        <button onClick={()=>{setIsDark(!isDark)}}>{isDark ? "화이트 전환" : "블랙 전환"}</button>
        </div>
    )
}