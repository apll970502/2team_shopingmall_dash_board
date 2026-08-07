# 팀 작업 계획

## 프로젝트
온라인 쇼핑몰 데이터 마케팅 인사이트 대시보드 (2팀)

## 역할과 담당 파일

| 팀원 | GitHub ID | 역할 | 담당 파일 | 코드 검증 단위 | 완료 기준 |
|---|---|---|---|---|---|
| 전예진 | (ID) | 데이터 점검·분석 | notebooks/01_data_check.ipynb, notebooks/02_analysis.ipynb, src/data_loader.py, src/analysis.py | 4파일 일괄 로드, PK/FK 검사, 3테이블 병합 | 데이터 구조·품질 설명 가능, 재사용 가능한 분석 함수 제공 |
| 박진 | (ID) | Streamlit 앱·시각화 | app.py, src/charts.py | 지표 표시, 필터 연동, 빈 데이터 처리 | streamlit run app.py 정상 실행, 필터 연동 동작 |
| 안형준 | apll970502 | 통합·테스트·문서 | README.md, requirements.txt, .gitignore, docs/, presentation/ | .gitignore 적용, 새 폴더 clone 재현, 통합 테스트 | 새 환경에서 README만 보고 실행 성공 |

## 담당 Issue

| 팀원 | Issue |
|---|---|
| 전예진 | #7 [DATA] |
| 박진 | #8 [APP] |
| 안형준 | #6 [DOCS] |

## 파일 단독 소유 규칙 (충돌 방지)

- README.md, requirements.txt, .gitignore → 안형준만 수정. 패키지 추가는 요청으로 전달
- notebooks/*.ipynb → 노트북 1개당 담당자 1명. 공동 편집 금지 (JSON 구조라 충돌 해결 불가)
- app.py, src/charts.py → 박진만 수정
- src/data_loader.py, src/analysis.py → 전예진만 수정
- docs/data_dictionary.md → 뼈대는 안형준, 컬럼 설명 내용은 전예진
- 담당 밖 파일은 직접 수정하지 않고 담당자에게 요청

## Merge 짝 순환

- 전예진 PR → 박진이 리뷰·merge
- 박진 PR → 안형준이 리뷰·merge
- 안형준 PR → 전예진이 리뷰·merge

리뷰는 최소 1개의 구체적 수정 요청을 포함한다. 승인만 하는 리뷰는 인정하지 않는다.

## 공통 규칙

- 브랜치는 반드시 최신 main에서 생성 (git switch main && git pull origin main)
- 브랜치명은 작업 내용 기준 (feature/data-analysis, feature/streamlit-app, docs/setup)
- main 직접 push 금지
- 커밋 접두어: feat / fix / docs / refactor / chore / test
- 1인당 의미 있는 커밋 2회 이상 (코드와 검증 기록을 분리 커밋)
- 1인당 검증 기록 3개 이상, 각 기록에 예외 조건 검증 포함
- "실행 전 예상"은 코드 실행 전에 작성

## AI 활용 원칙

전체 코드 일괄 요청 금지. 기능 단위로 나누어 요청한다.

프롬프트 4원칙
1. 실제 컬럼명을 명시한다
2. 기능 하나만 요청한다
3. 각 줄의 역할 설명을 요구한다
4. 빈 데이터가 발생할 수 있는 조건을 미리 확인한다

## 진행 상황 추적

| 팀원 | Issue | Branch | Commit | PR | 리뷰한 PR | Merge한 PR | 검증기록 |
|---|---|---|---|---|---|---|---|
| 전예진 | #7 |  |  |  |  |  | 0/3 |
| 박진 | #8 |  |  |  |  |  | 0/3 |
| 안형준 | #6 |  |  |  |  |  | 0/3 |
