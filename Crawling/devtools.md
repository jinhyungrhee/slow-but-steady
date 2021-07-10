## 크롤링 vs 스크랩핑

- 크롤링:  
  크롤러 봇이 사이트 하나하나를 방문하면서 무작위로 또는 정해진 규칙에 따라 데이터를 수집하는 것.  
  데이터의 양을 우선으로 하면서 일정한 시간 간격으로 데이터 수집. (규칙적임)  
  ex) 구글 검색 엔진의 경우, 구글 크롤러들이 방대한 양의 데이터를 수집했기 때문에 수많은 검색 결과가 나오는 것!

- 스크래핑:  
  브라우저의 타겟이 되는 데이터가 명확한 경우.

## HTML 태그

- HTML은 tag로 구성되어 있고 tag들의 규칙에 따라 우리가 작성한 코드들이 브라우저를 통해 사용자들에게 보여짐
- HTML tag에 대해서 잘 알면 데이터를 가져오기 수월함!

## 크롬 개발자도구

- Elements Tab - CSS Selector

  - 원하는 데이터의 위치 python으로 가져오기 위한 것!

  1. 원하는 데이터를 화살표로 click
  2. 해당 태그에서 마우스 오른쪽 click - Copy selector누르고 메모장에 복사/붙여넣기  
     또는 해당 태그에서 마우스 오른쪽 click - Copy XPATH누르고 메모장에 복사/붙여넣기

  ```
  #news > div.news_prime.news_tab1 > div > ul > li:nth-child(1) > a : css selector(copy selector)
  /div/div/ul/li[1]/a : xpath selector(copy XPATH)
  ```

- Network Tab = Http 처리 과정

  - 일련의 서버에서 response(수신)되는 전처리 과정을 전부 확인할 수 있음
