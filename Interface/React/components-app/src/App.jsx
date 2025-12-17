import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Button from './components/Button'
import Counter from './components/Counter'
import Student from './components/Student'
import Box from './components/Box'
import CardList from './components/CardList'
import Card from './components/Card'
import Title from './components/Title'
import UserCard from './components/UserCard'
import Product from './components/Product'

function App() {
  const totalCount = 3;

  return (
    <>
    {/* props 전달하기
    HTML 속성을 지정하듯이 원하는 데이터를 key-value 쌍으로 전달한다.*/}
      <Button text="확인" />
      <Button/>
      {/* jsx에서 중괄호에 숫자를 넣으면 정수로 전달된다 */}
      <Counter count={totalCount}/>
      <Student name = {"kim"} age = {20} isStudent={true}/>
      <Box style ={{
        width : "600px",
        border : "1px solid #ccc",
        backgroundColor : "pink"}}/>
       <CardList/>
       <Card>
        <h1>공지사항</h1>
        <p>오늘은 휴강입니다.</p>
       </Card>
        <Title text ={"물건 팝니다."}/>
        <UserCard name="정연" age={20}/>
        <Product name ="키보드" price={120000}/>
        <Product name ="마우스" price={38000}/>
        <Product name ="모니터" price={1300000}/>
    </>
  )
}

export default App;
