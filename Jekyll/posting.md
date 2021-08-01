### 환경설정 파일(_config.yml) 수정

- Jekyll은 설정파일로 YAML 파일 사용
    - YAML은 JSON처럼 일종의 데이터를 표현하는 방식!
- `_conig.yml` : 블로그 생성에 대한 전체 환경 세팅을 담당!

### author 수정

- Jasper2는 여러 사람이 자신의 ID로 각자 글 작성 가능
- 여려 명의 저자를 만들어서 사용 가능 (ex 회사 기술 블로그)
- `_data/author.yml` 

### tag 수정

- 글의 범주를 정해주는 기능 (카테고리화)
- 태그 별로 같은 범주의 글들을 모아서 볼 수 있음!
- `_data/tags.yml`

### 메뉴 수정

- 메뉴를 클릭했을 때 해당 태그별로 글들을 모아서 보여줌
- `_includes/navigation.html`

### 포스팅

- Jekyll Source Folder 안의 `_posts` 폴더에 우리가 작성하려는 글을 markdown 형식으로 작성
- 그후 `bundle exe jekyll serve` 명령어를 이용하여 build
    - 저장된 글들에 대한 컴파일 진행
    - 결과물이 destination 폴더에 생성

### Archive 설정

- 모든 글에 대해서 시간 순으로 정렬할 때 사용
- 시간 순서대로 태그 별로 글을 모아보고 싶을 때 사용
- `archive.md`, `author_archive.md` 생성

### post 목차 설정

- Jasper2가 제공하는 기능X
- CSS와 html 생성하여 post에 끼워넣는 식
- 목차를 구성하는 HTML파일(python-table-of-contents.html) 생성
- `_includes`폴더에 저장, 관리
- CSS minified : 공백이나 쓸데없는 부분을 삭제하여 용량을 줄이는 것 (`Gulp`사용)
    - Node.js 설치 - NPM(Node Package Manager) 이용해 Gulp 모듈 설치
    - node.js 11버전 사용(상위 버전 사용 시 컴파일 에러 발생) : `node-v11.15.0-x64.msi`  
    (https://nodejs.org/download/release/v11.15.0/)
    - node.js를 다운받았으면 환경변수에 대한 내용이 한번 바뀌었기 때문에 IDE가 다시 읽어들여야 함 => IDE 재부팅

    - package.json 업데이트 하고 `npm install`명령어 입력하면 필요한 서브모듈 다운

        - node virtual machine이용해 다운해야 제대로 적용됨! (nvm list available - nvm install 11.15.0 )

    - `gulp css`하여 minified된 css파일 생성함
        - asset/css/custom.css 가 minified 되어 asset/built/custom.css가 추가됨

    - css 적용하기
        - `_layout/default.html` :  모든 post의 기반이 되는 파일. 이 안에 우리가 작성한 post의 내용이 덧붙여져서 화면에 보여지는 것!
        - 'styles n scripts' 부분에 link 태그를 이용해서 custom.css적용


### GitHub Page에 올리기

- github에 `닉네임.github.io` 레포지토리 생성
- **git을 이용하여 컴파일 결과인 `C:/[GitHubPage]/`안의 내용을 레포지토리에 push함**(간단!)
    - git 설치 후 `git config --global user.name "이름"`, `git config --global user.email "이메일주소"` 해주기
    - `bundle exec jekyll serve` 명령어를 입력하면 컴파일이 되고 결과물이 `C:/[GitHubPage]/`에 생성됨. 이것이 우리의 최종 블로그 파일들임!
    - 새 창에 `C:/[GitHubPage]/`를 열고 local git repository를 생성함 
        - VCS - (import into Version Control) - create git repository 
        - 로컬 깃 저장소가 만들어지고 파일 색깔이 변함(git이 파일들을 추적중이라는 뜻)
    - commit repository (파일들 로컬 저장소에 저장하기)
        - 파일 오른쪽 클릭 - GIT - Commit Directory
        - Unversioned Files 전체 체크 - Commit Message 작성 - commit 버튼 클릭 (우리가 작성한 내용이 로컬 레포지토리 안에 저장됨)
    - push하기 (원격 저장소에 저장하기)
        - git - manage Remotes에 원격 저장소 URL입력
        - 파일 오른쪽 클릭 - push

### 폰트 변경하기

- jasper2는 한글에 대한 가독성(readability)가 떨어짐
- 로컬 폰트가 아닌 `웹폰트` 사용 : 구글 폰트 - '나눔고딕 폰트'
1. 이 웹폰트 링크를 `_layout/default.html`에 포함시켜줌 (사이트 전체적으로 적용)
    - custom.css 아래 부분에 추가
2. css 파일을 수정해서 특정 class에 대해 font-family에 나눔고딕 폰트 추가함
    - Jasper2의 일반적인 포스트는 모두 `assets/css/screen.css`안에 있는 `.post-full-content`의 영향을 받음
    - `font-family: Georgia, 'Nanum Gothic', serif;`

3. Font Awesome 적용하기
    - 아이콘을 폰트처럼 편하게 사용할 수 있게 함
    - 아이콘의 색상이나 크기 변경하는 것도 가능
    - Font Awesome은 GPL 라이선스임
    - `_layout/default.html`에 CDN링크 추가만 하면 됨!
        - custom.css 안에 font awesome에 대한 설정들이 이미 들어가 있음


4. css가 변경되었으니 `gulp`를 이용하여 minified 시킴
    - `gulp css` 명령어

### 코드 예쁘게 표현하기
1. rouge 사용
    - `_config.yml`에 highlighter: rouge 설정은 했지만 다운로드 필요
    - `gem install rouge`
    - `rougify` 명령을 이용하면 원하는 스타일의 css 파일 생성 가능!
        - rougify help style : 어떤 스타일을 사용할 수 있는지 확인
        - rougify style {원하는 테마 명} > assets/css/syntax.css : 해당 테마를 이용하여 css파일 생성(>)
    - 생성된 css 파일을 `_layout/default.html`에 코드 추가
        - 우리가 만드는 모든 스타일은 여기에 추가되어야 사용이 가능함
    - gulp css 사용해 minified
        - 여기서 에러 발생해서 일단 skip (GitHub Gist 시도해보기)

2. GitHub Gist 사용

### search 기능 추가하기

- Jekyll이나 Jasper에서 제공하지 않기 때문에 직접 구현해서 갖다 붙혀야 함!

1. `Google Custom Search` 사용
    - 장점 : 쉽고 편하게 검색 기능을 블로그에 갖다 붙힐 수 있음
    - 단점 : 구글 광고가 뜸, style을 조절하기 쉽지 않다(예쁘지 않음)

2. `lunr.js` 사용
    - 클라이언트 사이드에서 텍스트 서치하는 자바스크립트 엔진
    - subscribe 화면을 수정해서 search기능 구현
    1. `_include/site-nav.html`에서 Subscribe를 Search로 변경
        - 글 내용이 아닌 사이트 구조 자체가 변경되면 다시 컴파일 필요!
    2. `_layouts/default.html`을 열어서 검색 화면으로 수정
    3. `_includes/subscribe-form.html`을 열어서 수정
    4. search로 검색한 결과를 보여주는 `search.html`페이지 생성
        - `C:/blogmaker/search.html`
    5. `lunr.js`파일(다운 필요)과 해당 검색을 동작하게 하는 `search.js`파일(작성 필요)을 `assets/js`안에 넣어줌

### 내 post가 다른사람에게 검색되도록 하는 방법

- `Google Search Console` 활용
- 내 GitHub Page의 domain을 등록시키고 `sitemap.xml`을 생성해 Google Search Console에 제출함
- `sitemap.xml`을 등록하면 Google 검색 크롤러가 주기적으로 페이지를 크롤링하여 indexing함!
- 네이버(웹마스터도구), 다음에서도 유사한 방식으로 적용 
1. 루트 디렉토리 밑에 robots.txt 파일 생성
2. 루트 디렉토리 밑에 sitemap.xml 파일 생성
3. `google search console tools` 검색 - 시작하기
    - html 태그 이용해서 내 사이트임을 인증함
4. sitemaps 들어가서 `sitemap.xml`입력해서 등록함
    - 이때 깃헙 레포지토리에 sitemap.xml파일 올라가 있어야함
    - 구글 크롤러봇이 아무리 빠르더라도 이용자가 매우 많기 때문에 적용되는데 시간이 걸림

### GitHub Gist

- 블로그 내에서 단위 코드 조각(code snippet)을 관리하는 것
- code snippet 관리
    1. 완성되지 않은 sample코드를 보여줄 때에는 `rouge-syntax highlighter`이용
    2. 완성된 코드를 공유할 목적으로 블로그에 올리는 경우 `GitHub Gist`사용
        - 완성된 코드들은 블로그 내에 여기저기 반복적으로 사용될 가능성이 있기 때문에 만약 코드가 변경되면 이곳 저곳에 흩어져 있는 많은 코드들을 일일이 변경하기 어려움
        - 프로그램 코드 조각들을 한 곳에 모아놓고 블로그에 삽입해서 편리하게 사용
        - 단위 코드 조각을 관리하고 공유하도록 도와주는 서비스

1. GitHub에 접속해서 프로필 사진 옆에 `+`클릭하여 new gist로 들어감 
2. 파일명('_config.yml')과 완료된 코드 작성한 뒤 `create public gist`클릭(공유할 목적이므로)
3. gist를 블로그에 사용하기 위해 gem설치
    - `gem install jekyll-gist`
4. gist를 사용할 수 있도록 기존 파일('_config.yml')수정
    - `plugins: [jekyll-paginate, jekyll-feed, jekyll-gist]`
5. 코드 스니펫(조각)을 블로그 내에 코드 단위로 포함시키기
    - GitHub Gist의 Embed에서 script태그 copy해옴
    - 그 중에서 github 닉네임부터 .js 앞의 내용만을 추출해서 문법에 맞게 사용
        -  ex) `{% gist jinhyungrhee/6b0284730b0b900e3da250ec20e721cc %}


### Travis CI 활용(빌드, 배포 자동화)

- CI(Continous Integration)란?
    - 배포와 빌드를 자동화시켜주는 툴
    - Java의 Jenkins 같은 것

- Travis CI
    - GitHub와 편한 연동
    - public repository에 대해서는 무료

- 과정
    1. GitHub에 2개의 Repository 준비
        - 배포용 repository (`C:/[GitHubPage]/`) -> 이미 존재
        - 원본 자체(Jekyll 소스폴더)가 올라갈 repository (`C:/blogmaker`) -> 생성 필요
            - public으로 생성
            - README.md 파일 생성X
    2. 새로 생성한 repository에 Jekyll 소스폴더를 commit/push함
    3. Jekyll 소스 폴더에 Git Submodule 생성
        - `git submodule add https://github.com/jinhyungrhee/jinhyungrhee.github.io.git output`
        - 내부적으로 git clone이 실행되며 레포지토리가 복제됨
        - `C:/blogmaker` 아래에 `ouput` 폴더 생성
            - jekyll 소스폴더를 컴파일한 결과물이 이 안으로 들어감
        - 주의! : 이 폴더명(`output`)은 `_config.yml`에 있는 destination 속성의 값과 이름이 동일해야 함!!
            - `destination: ../[GitHubPage]/`에서 `destination: ./output/`으로 변경!
    4. submodule을 생성했다면 `git submodule update` 명령어 입력
    5. Travis 사이트에 접속해 repository 연결 활성화
        - `https://travis-ci.org` => public repository 위한 사이트 (무료)
        - `https://travis-ci.com` => private repository 위한 사이트 (유료)
        - github 계정으로 로그인
        - `+` 누른 뒤 `sync account` 클릭해서 두 레포지토리 모두 체크(활성화)
            - 두 레포지토리가 마스터 브랜치에 사용할 수 있는 형태로 잡힘
        - 우리가 blogMaker 폴더의 내용을 원격 저장소에 올리면 Travis CI가 그것을 가져다가 컴파일함
        - 그 컴파일 된 결과물을 배포 레포지토리에 밀어넣어줌
    6. token 생성
        - Travis CI에서 다른 레포로 push하기 위해서는 token 필요
        - GitHub에 접속 - Settings - Developer settings - Personal access Tokens 들어가서 `Generate New Token` 클릭
        - description 작성 - Select scopes : repo 선택 - generate token
        - token이 생성되면 잘 저장해둠
            - 주의! : token값을 직접 Travis CI 설정파일(`.travis.yml`)에 직접 노출시키면 안됨! => 암호화해서 사용
    7. travis gem 설치
        - `gem install travis`
    8. 암호화 진행
        - 반드시 먼저 로그인이 되어 있어야 함
        - 위에서 생성한 token 사용
        - `travis login --pro`
        - `travis encrypt GITHUB_TOKEN=<token> -r <repo-name>`
            1. token
            2. 깃헙 아이디/깃헙 레포 이름(jinhyungrhee/GitHubPageMaker)
        - 터미널에 암호화 코드가 출력되면 일단 메모장에 저장
    9. 루트 디렉토리 밑에 travis.yml 파일 생성 및 작성
        - 루비 버전 업데이트
        - env - global - secure : 저장해뒀던 시크릿코드 작성
    10. Rakefile 생성 및 작성
    11. 커밋 & 푸시

- 현재는 Travis CI 무료 서비스가 대폭 축소됨.
    - 무료 크레딧 1회 제공 (연장 불가)

