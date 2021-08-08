## Geolocation

- navigator
    - user의 위치(geolocation)를 알려주는 함수
    - `navigator.geolocation.getCurrentPosition()`
        - argument1 : 모든 게 잘 됐을 때 실행될 함수
        - argument2 : 에러가 발생했을 때 실행될 함수
    ```js
    function onGeoOk(position) {
        const lat = position.coords.latitude; 
        const lng = position.coords.longitude;
        console.log("you live in", lat, lng);
    }
    function onGeoError() {
        alert("Can't find you. No weather for you.");
    }

    navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
    ```

## Weather API

- API
    - 다른 서버와 이야기할 수 있는 방법
    - open weather map server에 요청해서 정보를 얻어올 것임
    - current weather data - By geographic coordinates 이용해 url에 좌표를 보냄
        - 회원가입 몇 시간 후에 API key가 activate되므로 조금 기다려야 함!
    - `fetch()`를 사용해서 URL을 부름!
        - 실제로 URL에 갈 필요 없이 JavaScript가 대신 URL 부르는 것
            - 개발자도구 - Network탭에서 내가 요청한 정보(URL) 확인할 수 있음!
        - `fetch()`는 당장 뭔가 일어나지 않고 시간이 좀 걸린 뒤에 일어나는 **promise**임!
            - 서버의 응답이 5분 걸린다면 우리는 그 시간을 기다려야 함
            - `.then()` 사용
                - URL을 fetch하고 그 다음으로(`then()`) response의 JSON을 얻어야 함!
                - JSON을 추출했으면 그 다음으로(`then()`) data를 얻어야 함!
            ```js
            fetch(url).then(response => response.json()).then(data => {
                console.log(data.name, data.weather[0].main);
            });
            ```
