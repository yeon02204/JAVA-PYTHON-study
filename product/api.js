

// 서버의 주소와 포트를 명시한다
export const BASE_URL="http://localhost:8080";

// 범용 api fetch 함수 응답상태를 확인하고, json 데이터를 파싱하여 반환
export async function apiFetch(endpoint,options = {}){
    const url = BASE_URL + endpoint;

    try {
        // fetch() 요청을 한다
        const response = await fetch(url,options);

        // 응답 본문을 JSON으로 파싱한다
        const result = await response.json();

        // response.ok -> 통신이 성공하면 true를 반환, 4xx, 5xx 에러를 반환하며 false를 반환
        // http 상태코드가  200이 아니면 에러로 처리
        // errorMassage에는 서버에서 보낸 에러 문구를 넣어주면된다
        // throw new Error(errorMassage);

        if (!response.ok) {
            // responseDTO의 error 팔드에 담긴 메세지를 꺼낸다
            const errorMassage = result.error;
            // 통신이 잘 되지 않으면 예외를 발생시킨다
            throw new Error(errorMassage);
        } 

        // 성공시 응답 DTO의 데이터 필드를 반환
        return result.data;
        
    }catch(error){
        console.log("API 호출중 오류발생 :"+ error.message);
        throw error; // 함수를 호출한 쪽에서 예외를 처리
    }
}

