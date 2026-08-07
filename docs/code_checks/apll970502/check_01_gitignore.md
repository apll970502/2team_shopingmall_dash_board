# 코드 단위 검증 기록

## 작성자
- 이름: 안형준
- GitHub ID: apll970502
- 담당 기능: 통합·테스트·문서

## 1. 검증 단위
- 기능명: .gitignore 적용 확인
- 관련 Issue: #6
- 관련 파일: .gitignore

## 2. AI 요청 내용
Windows 프로젝트 루트에 .venv 가상환경을 만들었습니다.
.gitignore에 .venv/ 를 넣었을 때 git status에서 제외되는지
확인하는 방법만 알려주세요.
.gitignore가 작동하지 않는 조건도 알려주세요.

## 3. 실행 전 예상
- 입력: 프로젝트 루트에 생성한 .venv 폴더
- 예상 결과: .venv 안에 수백 개 파일이 생기지만 git status에 나타나지 않음
- 오류 가능 조건: .gitignore 작성 전에 이미 커밋했다면 계속 추적됨

## 4. 실행 코드
python -m venv .venv
git status

## 5. 실제 결과
- 출력값: git status에 data/, docs/, presentation/, src/ 만 표시
- .venv/ 는 나타나지 않음
- 예상과 다른 점: 없음. 예상과 일치

## 6. 정상 조건 검증
.venv 폴더에 수백 개 파일이 실제로 존재하는데도
git status 목록에 나타나지 않음을 확인했다.

## 7. 예외 조건 검증
- .env 파일을 임시 생성 후 git status → 무시됨
- data/processed/ 에 임시 csv 생성 → 무시되고 .gitkeep만 추적됨
- src/__pycache__/ 생성 확인 → 무시됨

## 8. AI 코드에서 수정한 부분
- 검증 대상을 .venv 하나가 아니라 .env, data/processed/, __pycache__ 까지 확장
- 우리 저장소의 실제 .gitignore 항목에 맞춰 확인 대상 조정

## 9. 내 말로 설명
처음에는 .gitignore가 "이 파일들은 GitHub에 올리지 마"라고 
적어두면 알아서 다 걸러주는 파일이라고 생각했다.

그런데 확인해보니 조건이 있었다. Git이 아직 모르는 파일만 
막을 수 있고, 한 번이라도 커밋해서 Git이 기억하고 있는 파일은 
나중에 .gitignore에 적어도 계속 따라온다.

그래서 순서가 중요했다. 만약 가상환경(.venv)을 먼저 만들고 
그 상태로 커밋했다면, 수백 개 파일이 이미 올라간 뒤라서 
.gitignore를 써도 늦었을 것이다. 
내가 프로젝트 구조를 만들 때 .gitignore를 가장 먼저 
올린 게 결과적으로 맞는 순서였다.

git status를 쳤을 때 .venv가 안 보이는 걸 확인하고 나서야 
"안 올라간다"는 걸 믿을 수 있었다. 파일을 만들었다고 
자동으로 되는 게 아니라, 직접 확인해봐야 아는 부분이었다.
## 10. 아직 이해되지 않는 부분
이미 추적 중인 파일을 무시 목록으로 옮기는 방법(git rm --cached)의 정확한 동작