# 팀 작업 계획

| 팀원 | 역할 | 담당 파일 | 코드 검증 단위 | 완료 기준 |
|---|---|---|---|---|
| 전예진 | 데이터 점검·분석 | 01_data_check.ipynb, 02_analysis.ipynb, data_loader.py, analysis.py | 4파일 로드, PK/FK 검사, 3테이블 병합 | 데이터 구조·품질 설명 가능 |
| 박진 | 앱·시각화 | app.py, charts.py | 지표 표시, 필터 연동, 빈 데이터 처리 | 필터 연동 앱 정상 실행 |
| 안형준 | 통합·문서 | README.md, requirements.txt, docs/ | gitignore 적용, 새 폴더 clone 재현, 통합 테스트 | 새 환경에서 실행 성공 |

## 담당 Issue

| 팀원 | Issue |
|---|---|
| 전예진 | #7 [DATA] |
| 박진 | #8 [APP] |
| 안형준 | #6 [DOCS] |

## 브랜치 전략

- 통합 브랜치: develop (개인 브랜치는 develop으로 PR)
- 배포 브랜치: main (마감 전 develop 내용을 main에 반영)
- 개인 브랜치는 최신 develop에서 생성
- develop, main 직접 push 금지

## Merge 짝

- 전예진 PR → 박진이 리뷰·merge
- 박진 PR → 안형준이 리뷰·merge
- 안형준 PR → 전예진이 리뷰·merge

## 파일 소유 규칙

- 담당 파일 밖은 직접 수정하지 않고 담당자에게 요청
- 노트북은 담당자 1명만 편집 (공동 편집 시 충돌 해결 불가)
- requirements.txt 패키지 추가는 안형준에게 요청
