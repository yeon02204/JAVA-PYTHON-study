// 매개변수 이름은 그냥 변수명이라서 아무 이름이나 써도 된다
// 다만 관례상 props를 많이 쓴다
// const props = {props : "확인"};
const Button = (props) =>{
    return(
        <button>
            {props.text ? props.text : "기본버튼"}
        </button>
    )
}


export default Button;