# 제가 만든 일기 웹페이지를 로컬에서 보시려면?

우선, cmd 창을 열어, `git clone https://github.com/i-zro/my_diary` 명령어를 사용하여, 원하는 경로에 저장해준 후, 아래 과정을 따라갑니다.

### 1. 몽고 DB를 윈도우 설치 페이지에서 설치하기
✅ [link](https://www.mongodb.com/try/download/community)

### 2. 몽고 DB의 bin폴더 설치 경로를 시스템 환경 변수 편집에서 추가

### 3. 가상환경 만들어주기
`python -m virtualenv <가상환경 이름>`

### 4. 가상환경 실행
`<가상환경 이름>/Scripts/activate`

### 5. requirements.txt 설치해주기
`pip install -r requirements.txt`

### 6. cmd에서 아래와 같이 명령어 입력
`mongod --dbpath <db폴더 경로>`

(db 설치를 원하는 로컬 경로에 폴더를 만들어, 해당 경로를 잡아줍니다.)

# 사용자 메뉴얼
1. 첫 페이지 : 로그인 / 회원가입 시작 페이지
![image](https://user-images.githubusercontent.com/48379869/121802940-019bdb80-cc7a-11eb-933a-9141aa90200b.png)

2. 회원가입 페이지

