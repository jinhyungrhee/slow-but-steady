# Server(Client) to Server 연결

- 우리가 Client가 되어서 Server에 연결하는 방법

## Server로의 연결

- 이제까지는 우리가 client의 요청을 받는 Server의 입장에서만 살펴봤음
    - Server의 입장에서 API를 제공하는 방법
- 이제는 **우리의 Server가 Client가 되어서 또 다른 Server에 요청**하는 것을 알아볼 것임!
    - Back-end에서 Client로 다른 Server와의 연결은 필수!
- RestClient에는 여러가지 라이브러리가 존재
    - RestTemplate (Spring에서 가장 많이 사용)
    - Web Client
    - Apache Client
- RestTemplate을 통해서 Server에 연결하는 방법을 알아볼 예정
    - 서버를 두 개 띄움
        - port 8080 : Client로 사용
        - port 9090 : Server로 사용