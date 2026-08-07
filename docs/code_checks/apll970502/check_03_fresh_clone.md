# 코드 단위 검증 기록

## 작성자
- 이름: 안형준
- GitHub ID: apll970502
- 담당 기능: 통합·테스트·문서

## 1. 검증 단위
- 기능명: 새 환경에서 clone 후 실행 재현
- 관련 Issue: #6
- 관련 파일: README.md, requirements.txt

## 2. AI 요청 내용
GitHub 저장소를 완전히 새 폴더에 clone해서 requirements.txt만으로
앱이 실행되는지 확인하려 합니다. 확인 절차와 각 단계에서
실패할 수 있는 조건만 알려주세요.

## 3. 실행 전 예상
- 입력: 저장소 URL과 빈 폴더(C:\temp)
- 예상 결과: README 절차대로 실행하면 앱이 정상 실행됨
- 오류 가능 조건:
  1. A와 B가 사용한 패키지가 requirements.txt에 없을 수 있다
  2. 코드에 개발자 PC의 절대 경로가 남아 있을 수 있다
  3. data/raw/의 CSV가 저장소에 올라가지 않았을 수 있다
- 기존 환경에는 이미 패키지가 깔려 있어서 문제가 안 보였을 가능성이 있다고 예상

## 4. 실행 코드
cd C:\temp
git clone https://github.com/apll970502/2team_shopingmall_dash_board.git
cd 2team_shopingmall_dash_board
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py

## 5. 실제 결과
- clone: 성공
- 가상환경 생성 및 패키지 설치: 성공
- 앱 실행: 성공
- 예상과 다른 점: 없음. requirements.txt만으로 실행됨

## 6. 정상 조건 검증
기존 개발 폴더(C:\dev)가 아니라 완전히 다른 폴더(C:\temp)에서
새 가상환경을 만들어 실행했다. 따라서 기존 환경에 남아 있던
패키지에 의존하지 않고 requirements.txt만으로 실행됨을 확인한 것이다.

## 7. 예외 조건 검증
- README에 적힌 명령만 사용하고 추가 설치는 하지 않음
- data/raw/의 CSV 4개가 저장소에 포함되어 있는지 GitHub에서 직접 확인
- Activate.ps1 실행 시 권한 오류 발생 가능성을 확인하고
  README에 Set-ExecutionPolicy 안내를 포함시킴

## 8. AI 코드에서 수정한 목적
- 확인 경로를 우리 저장소 URL과 실제 폴더 구조에 맞춰 수정
- README에 있는 Set-ExecutionPolicy 안내가 실제로 필요한지 함께 확인

## 9. 내 말로 설명
내 컴퓨터에서 앱이 돌아가는 걸 보고 다됐다 생각했는데 
그게 아닐수도있고 실제로 아니라는사실이 신기했다

내 컴퓨터에는 그동안 이것저것 설치한 게 쌓여 있어서, 
requirements.txt에 안 적힌 패키지도 이미 깔려 있을 수 있다.  


clone이라는 게 신기했다. 명령어 한 줄 치면 GitHub에 있는 
폴더 구조와 파일이 그대로 내 컴퓨터에 만들어진다. 
파일을 하나씩 다운로드하는 게 아니라 프로젝트 전체가 
통째로 복사되는 느낌이었다

그리고 CSV 파일이 저장소에 실제로 올라가 있는지도 확인했다 
.gitignore에 걸려서 안 올라갔으면 다른 사람이 받았을 때 
데이터가 없어서 앱이 안 돌아갈 텐데, GitHub에서 직접 
data/raw 폴더를 열어보니 4개가 다 있었다

## 10. 아직 이해되지 않는 부분
clone이 GitHub에 있는 파일들을 내 컴퓨터로 그대로 가져오는 
과정이 아직 신기하고, 정확히 어떤 방식으로 동작하는지 
이해되지 않는다 파일만 복사되는 게 아니라 지금까지의 커밋 
기록까지 함께 온다는 점도 더 알아보고 싶다

VS Code에서 코드를 고치고 git push를 치면 GitHub 웹사이트의 
내용이 바뀌는 것도 마찬가지다. 내 폴더와 인터넷에 있는 
저장소가 어떻게 연결되어 있는지, 그 연결을 Git이 어디에 
기억하고 있는지 궁금하다.
