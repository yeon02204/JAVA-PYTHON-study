const Jsx = () => {

    // HTML 테그를 직접 변수에 담을 수 있다
    const element = <h1> Hello, word!</h1>

    // js 값은 중괄호로 넣을 수 있다
    const name = "kim";
    const age = 20;

    const boxStyle = {
        backgroundColor : 'red',
        color :'black', 
        fontSize: '20px'
    }

    // jsx에서 자주 사용하는 패턴
    // 1. 조건부 렌더링 (삼항연산자)
    // jsx안에서 if문을 직접 쓸 수는 없고 , 보통 삼항연산자를 사용한다.

    const isLogin = true;

    // 2. 조건부 렌더링(AND 연산자 &&)
    // 조건이 true면 렌더링을 한다

    const hasMessage = false;

    // 3. 리스트의 렌더링(map() 메서드)
    // 배열을 ul 목록으로 바꿀때 map() 메서드를 사용한다
    const fruits =["사과","바나나","배"];

    return (
    // 반드시 하나의 부모 요소로 감싸야 한다
    // 불필요한 div를쓰고 싶지 않다면 Fragment를 사용한다
    // <> </>
        <>
            {element}
            <h2> 이름 : {name}</h2>
            <h2> 나이  : {age}</h2>
            <h2> 내년 나이  : {age + 1}</h2>
            <div className="container">박스</div>
            {/* css문자열이 아니라 js 객체 형태로 써야한다
            속성들은 fontSize, backgroundColor 처럼 카멜 표현식으로 써야한다 */}
            <div style={{color :'red', fontSize: '20px'}}>스타일 박스</div>
            <div style={boxStyle}>스타일 박스2</div>
            {/* 테그는 반드시 닫는다 */}
            <input />
            <br></br>
            <img src ="logo.png" alt = "logo" />
            {isLogin ? <h1>환영합니다!</h1> : <h1>로그인 해주세요.</h1>}
            <div>{hasMessage && <p>새 메세지가 있습니다</p>}</div>
            <u1>
                {fruits.map((item,index) => (
                    // 이때 리스트의 속성으로 key를 쓰는것이 좋다
                    // 리엑트가 각 li를 구분하는 용도로 쓴다.
                    <li key={index}>{item}</li>
                ))}
            </u1>
            
        </>
     );
}

export default Jsx;