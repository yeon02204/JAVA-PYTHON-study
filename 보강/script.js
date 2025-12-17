const inputs = document.querySelectorAll('.check');
const joinBtn = document.querySelector('#join');

/*
 포커스(focus)
비어 있으면 일단 빨간색 켜고 안내문구 붙여

입력(input)
글자가 들어오면 -> 정상색 + 문구 삭제
글자를 지우면 -> 다시 빨간색 + 문구 생성

회원가입 버튼(click)
입력칸들을 순회
하나라도 빈칸 → 빨강 처리 + 경고창
모두 값 있음 → 성공 알림
 */
inputs.forEach(input => {

    // 포커스: 값이 비어있을 때 에러 표시
    input.addEventListener('blur', () => {
        if (!input.value.trim()) {
            showError(input);
        }
    });

    // 입력 중: 값 있으면 정상, 없으면 에러 표시
    input.addEventListener('input', () => {
        if (input.value.trim()) {
            clearError(input);   // 값 입력됨 -> 정상 처리
        } else {
            showError(input);    // 값 없음 -> 에러 표시
        }
    });
});



// -------- 회원가입 버튼 --------
joinBtn.addEventListener('click', () => {
    let isEmpty = false; // 값 없는게 기본

    inputs.forEach(input => {
        // input.value.trim() : 앞뒤 공백 제거한 실제 입력값
        // !input.value.trim() : 값이 비어있으면 true (에러 조건)
        if (!input.value.trim()) {  // 값이 비어있다면 (실패 조건)
            isEmpty = true;         // 전체 검사에서 '빈칸 있음'으로 표시
            showError(input);       // 이 입력칸에 빨간 테두리 + 안내문구 표시 
        } else {                    // 값이 있다면 (정상 조건)
            clearError(input);      // 빨간 테두리 + 문구 제거 (정상 처리)
        }
    });
    
    /*
    에러 먼저 확인하기” 패턴
    조건이 이상하면 -> 바로 처리하고 끝내라
    정상 흐름은 else쪽 혹은 아래쪽에

    이유 : 에러 체크는 짧고 여러 개 나오고, 정상 흐름은 길고 중요하기 때문
    <이 구조가 유지보수에 훨씬 유리>

    공백/빈문자열 체크는 대부분 “없으면 -> !value”로 봄
    if (!value) → 빈칸일 때
    else → 값 있을 때
    */

    if (isEmpty) {
        alert("필수 입력값을 모두 입력하세요."); // 값 없으면
    } else {
        alert("회원가입 성공!"); // 값 다 들어있으면
    }
});

// -------- 기능 함수들 --------

function showError(input) {      // 빨간 테두리 + 안내문구 생성
    input.style.border = '1px solid red';     // 테두리 빨간색으로 변경
    removeMessage(input);                     // 기존 메시지 제거

    const msg = document.createElement('p');  // <p> 태그 생성
    msg.classList.add('msg');                 // msg 클래스 추가
    msg.style.color = 'red';                  // 글자색 빨강
    msg.textContent = getMessage(input);      // 라벨 기반 안내문구 생성

    input.parentNode.appendChild(msg);        // input이 속한 박스 아래 추가
};

function clearError(input) {     // 에러 표시 제거
    input.style.border = '1px solid #ccc';    // 기본 테두리로 복구
    removeMessage(input);                     // 안내문구 제거
};

function removeMessage(input) {  // 기존 안내문구 1개만 제거
    const old = input.parentNode.querySelector('.msg');
    if (old) old.remove();       // 있으면 삭제
};

function getMessage(input) {     // 라벨 + 안내문구 생성
    const wrapper = input.closest('.boxid, .box'); // input이 포함된 상위 박스
    const label = wrapper.querySelector('label')?.textContent.trim() || "";
    return `${label}를 입력하세요`;   // 예: "아이디를 입력하세요"
};

