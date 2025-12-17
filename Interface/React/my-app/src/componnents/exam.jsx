const Exam = () =>{
    // name을 변수에 이름을 하나 넣고
    // 안녕하세요 xxx 님 출력하기
    const name = "신정연";

    // age 변수에 나이를 하나 넣고 
    // 성인입니다 또는 미성년자 입니다 출력하기

    const age = 25;
    const isAdult = true; 

    const code = ["HTML","CSS","JS","REACT"];

    const isDarkMode = true;

    const users = [{id:1, name:"Kim"},{id : 2, name:"Lee"}];


    return(
        <>
        <h1> 안녕하세요, {name}님</h1>
        {age > 19 ? <p>성인입니다</p> : <p>미성년자 입니다</p> }
            <u1>
                {code.map((item,index) => (
                    <li key={index}>{item}</li>
                ))}
            </u1>
        {isDarkMode? <div style={backgroundColor = balck}>검정</div> : <div style={backgroundColor = white}>흰색</div>}        
        <ul>
        {users.map((user) => (
                    <li key={user.id}>{user.name}</li>
                ))}
                </ul>
        </>
    );
}

export default Exam;