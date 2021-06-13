# 제가 만든 일기 웹페이지를 로컬에서 보시려면?

### 1. 몽고 DB 윈도우 설치 페이지에서 설치하기
✅ [link](https://www.mongodb.com/try/download/community)

### 2. 몽고 DB bin파일 설치 경로 환경 변수 추가

### 3. 터미널에서 가상환경 만들어서 pip freeze로 추출한 requirements.txt 설치해주기
`pip install -r requirements.txt`

### 4. cmd에서 아래와 같이 명령어 입력
`mongod --dbpath <db폴더 경로>`
