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

2. 회원가입 페이지 : 이름(닉네임), 이메일, 비밀번호를 입력하고 회원가입을 누르면, 회원가입이 완료 (DB에 저장됨), 돌아가기를 누르면 다시 첫화면으로 돌아감
![image](https://user-images.githubusercontent.com/48379869/121803928-a6b8b300-cc7e-11eb-9d53-469ec8f38598.png)

<예외처리>
만약 올바른 이메일 형식이 아니거나 비어있으면, 회원가입이 안되도록 설정
1) 정보가 비어있는 경우
![image](https://user-images.githubusercontent.com/48379869/121804480-9524da80-cc81-11eb-870f-2f6b11508e8a.png)
2) 올바른 이메일 형식이 아닌경우
![image](https://user-images.githubusercontent.com/48379869/121804515-bdacd480-cc81-11eb-99c3-bda569ea13fa.png)

3. 회원가입을 완료하면, 로그인 가능
![image](https://user-images.githubusercontent.com/48379869/121804577-006eac80-cc82-11eb-8a09-6df4f4f93d0e.png)

<예외처리>
올바르지 않은 사항을 입력하였을 때, 로그인이 안됨
![image](https://user-images.githubusercontent.com/48379869/121804602-285e1000-cc82-11eb-9e40-95fe3ca9b393.png)

4. 원하는 메뉴 선택 화면
![image](https://user-images.githubusercontent.com/48379869/121805076-7f64e480-cc84-11eb-95cb-9bd5e16cf91f.png)

