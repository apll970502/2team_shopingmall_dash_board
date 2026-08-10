# 2team_shopingmall_dash_board
# 개인별 작업 기록

팀원 전원이 본인 섹션을 직접 작성합니다.

---

## 형준 (hyungjune)

### 담당 기능

통합, 테스트, 문서화 (3인 팀 담당자 C)

### 담당 Issue와 PR

| 구분 | 번호 | 내용 |
|---|---|---|
| Issue | # | 프로젝트 구조 및 문서화 |
| PR | #18 | 통합·문서 작업 |
| 리뷰 | # | 팀원 PR 리뷰 참여 |

### 수행 절차

1. 팀 GitHub 저장소를 생성하고 팀원을 Collaborator로 등록했습니다.
2. 공통 폴더 구조(`data/`, `notebooks/`, `src/`, `docs/`, `presentation/`)를 준비했습니다.
3. `.gitignore` 와 `requirements.txt` 초안을 작성했습니다.
4. 개인 브랜치에서 작업하고 Pull Request로 병합했습니다.
5. 팀원의 PR을 실행해 확인하고 리뷰를 남겼습니다.
6. develop → main 병합(PR #21) 후 main 브랜치에서 통합 테스트를 진행했습니다.
7. `C:\temp` 에 새로 clone하여 실행 재현 테스트를 진행했습니다.
8. README와 통합 테스트 결과, 발표 자료를 작성했습니다.

### AI 활용 내용

`.gitignore` 표준 설정, PowerShell에서의 Git 명령 실행 문제, 새 환경 실행 재현 절차에 대해 질문했습니다. 제안받은 내용은 그대로 사용하지 않고 프로젝트 구조에 맞게 수정한 뒤 직접 실행해 확인했습니다. 자세한 내용은 `docs/ai_usage.md` 에 있습니다.

### 검증한 코드 단위

| 단위 | 목적 | 예상 결과 | 실제 결과 | 검증 방법 |
|---|---|---|---|---|
| 1. `.gitignore` 적용 | 가상환경·캐시가 저장소에 올라가지 않도록 함 | `git status` 에 `.venv`, `__pycache__` 가 나타나지 않음 | 제외 대상이 추적되지 않음을 확인 | `git status` 출력 확인, `git ls-files` 로 추적 파일 목록 대조 |
| 2. `requirements.txt` 설치 | 빈 환경에서 필요한 패키지가 모두 설치되는지 확인 | 설치 후 `import pandas, streamlit` 성공 | 설치 성공, 앱 실행됨 | 새 가상환경에서 설치 후 `python -c "import pandas, streamlit"` 실행 |
| 3. 새 폴더 clone 실행 | 개발 환경에 의존하지 않고 실행되는지 확인 | `C:\temp` 에서 clone 후 앱이 개발 폴더와 동일하게 실행됨 | 실행 성공. 단, 개발 폴더에는 없던 Streamlit 버전 경고가 출력됨 | `C:\temp` 에 clone → 새 `.venv` 생성 → 설치 → `streamlit run app.py` |

### 발생한 문제

1. PowerShell에서 여러 줄로 붙여넣은 Git 명령이 실행되지 않았습니다.
2. develop 브랜치가 main보다 뒤처진 상태로 남아 있었습니다.
3. 새 환경에서 실행했을 때 개발 폴더에는 없던 Streamlit 경고(`use_container_width` 제거 예정)가 출력되었습니다.
4. `git switch develop` 입력 중 오타로 `witch develop` 이라는 불필요한 파일이 생성되었습니다.

### 해결 방법

1. 명령을 한 줄씩 실행하고, 성공한 순서를 문서에 기록해 이후 같은 절차로 재현할 수 있게 했습니다.
2. main을 develop에 병합해 두 브랜치를 동일한 상태로 정리했습니다.
3. `requirements.txt` 에 버전이 고정되어 있지 않아 새 환경에 더 최신 버전이 설치된 것이 원인임을 확인했습니다.
4. 커밋 전 `git status` 로 발견해 파일을 삭제했습니다. 불필요한 파일이 저장소에 올라가지 않도록 커밋 전 확인 절차의 필요성을 확인했습니다.

### 본인이 이해한 내용

- 브랜치는 나누는 것보다 합치는 순서가 중요합니다. 늦게 병합할수록 공용 파일에서 충돌이 커집니다.
- `import` 오류는 문법 문제가 아니라 폴더 구조와 실행 위치의 문제였습니다. 구조를 먼저 확정해야 하는 이유입니다.
- `requirements.txt` 는 단순한 목록이 아니라, 다른 사람이 같은 환경을 만들 수 있게 하는 기준입니다.
- 개발 폴더에서 앱이 실행되는 것과, 새 환경에서 실행되는 것은 별개의 검증 항목입니다.
- 에러가 없다는 것이 정상이라는 뜻은 아닙니다. 경고도 이후 버전에서 실행 실패로 이어질 수 있습니다.

### 아직 이해되지 않는 내용

- `rebase` 와 `merge` 를 언제 어느 쪽으로 선택해야 하는지 기준을 아직 감으로 판단하고 있습니다.
- 가상환경이 패키지를 어떻게 격리하는지, 버전을 고정해야 하는 원리까지는 정확히 이해하지 못했습니다.
- Streamlit이 화면을 다시 그리는 시점과 캐시가 동작하는 조건을 정확히 예측하지 못합니다.
---
## 이름: 박진

## GitHub ID: jeanpark0115@naver.com	

## 담당 기능: streamlit 화면 및 시각화

## 담당 Issue와 PR

## 수행 절차: 요구사항 분석 후 AI에게 해야 할 순서를 대입 후 단위 별로 기능 구현 후 검증

## AI 활용 내용: 질문 활용 Streamlit이 무엇인지, 어떤 용도로 사용하는지
Streamlit 대시보드를 개발할 때 어떤 순서로 진행해야 하는지
차트 및 UI 요소의 색상을 변경하는 방법
데이터 시각화를 구현하는 방법

## 검증한 코드 단위

| 단위 | 목적 | 예상 결과 | 실제 결과 | 검증 방법 |

|---|---|---|---|---|

| 1 |  |  |  |  |

| 2 |  |  |  |  |

| 3 |  |  |  |  |





cd /home/claude/project && python3 << 'EOF'
from streamlit.testing.v1 import AppTest
import pandas as pd, json, shutil, os

results = {}

# 1. 첫 화면 정상 실행
at = AppTest.from_file("app.py")
at.run(timeout=30)
results["01_first_run"] = {
    "no_exception": len(at.exception) == 0,
    "title_text": at.title[0].value if at.title else None,
}

# 2. 지표(메트릭) 존재 여부 - 8개 있어야 함
metric_labels = [m.label for m in at.metric]
results["02_metrics"] = {"count": len(metric_labels), "labels": metric_labels}

# 3. 카테고리 필터 선택 -> 지표 변화 확인
before_total_orders = [m.value for m in at.metric if m.label == "전체 주문 수"][0]
cat_multiselect = at.sidebar.multiselect[0]  # 상품 카테고리
options = cat_multiselect.options
pick_cat = options[0]
cat_multiselect.select(pick_cat).run(timeout=30)
after_total_orders = [m.value for m in at.metric if m.label == "전체 주문 수"][0]
results["03_category_filter"] = {
    "picked": pick_cat,
    "before_total_orders": before_total_orders,
    "after_total_orders": after_total_orders,
    "changed": before_total_orders != after_total_orders,
}
cat_multiselect.unselect(pick_cat).run(timeout=30)  # 초기화

# 4. 주문 상태 필터 선택 -> 지표 변화 확인
status_multiselect = at.sidebar.multiselect[1]  # 주문 상태
status_options = status_multiselect.options
pick_status = status_options[0]
before_delivered = [m.value for m in at.metric if m.label == "배송완료 주문 수"][0]
status_multiselect.select(pick_status).run(timeout=30)
after_orders_count = [m.value for m in at.metric if m.label == "전체 주문 수"][0]
results["04_status_filter"] = {
    "picked": pick_status,
    "after_total_orders_with_status_filter": after_orders_count,
}
status_multiselect.unselect(pick_status).run(timeout=30)

# 5. 표 출력 여부
results["05_dataframe"] = {"dataframe_count": len(at.dataframe), "rows_estimate": "확인은 실제 df shape로"}

# 6. 차트 존재 개수 (VegaLiteChart 프로토 탐색)
def find_vega_charts(node):
    out = []
    for c in getattr(node, "children", {}).values():
        proto = getattr(c, "proto", None)
        if proto is not None and proto.__class__.__name__ == "VegaLiteChart":
            out.append(proto)
        out.extend(find_vega_charts(c))
    return out

charts = find_vega_charts(at._tree[0])
results["06_charts"] = {"chart_count": len(charts)}

print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
EOF
출력

{
  "01_first_run": {
    "no_exception": true,
    "title_text": ":bar_chart: 이커머스 데이터 대시보드"
  },
  "02_metrics": {
    "count": 8,
    "labels": [
      "전체 고객 수",
      "전체 상품 수",
      "전체 주문 수",
      "총 주문 수량",
      "총 주문 금액",
      "평균 주문 금액",
      "배송완료 주문 수",
      "취소/환불 주문 수"
    ]
  },
  "03_category_filter": {
    "picked": "가전",
    "before_total_orders": "200 건",
    "after_total_orders": "40 건",
    "changed": true
  },
  "04_status_filter": {
    "picked": "배송완료",
    "after_total_orders_with_status_filter": "105 건"
  },
  "05_dataframe": {
    "dataframe_count": 1,
    "rows_estimate": "확인은 실제 df shape로"
  },
  "06_charts": {
    "chart_count": 5
  }
}









## 발생한 문제
1. 막대 차트 색상 변경 문제
원인 st.bar_char/st.line_chart는 데이터가 pandas.Series일 때 color 파라미터를 제대로 못받는 경우가 있슴.



## 해결 방법
공식 문서에서 color는 리스트로 넘기라고 되어있다 ["#4C78A8"] 로 변경 원래 코드는 문자열 하나만 넘기고 있었음.

## 본인이 이해한 내용

## 아직 이해되지 않는 내용
---
## 전예진

## wjs0951467-wq

## 담당 기능
- 데이터 점검 (Data Check)
- 데이터 분석 (Analysis)
- 분석 함수 (analysis.py) 구현

## 담당 Issue와 PR
- 담당 A: 데이터 점검 및 분석 기능 구현
- 데이터 분석 Notebook 수정 및 정리
- analysis.py 분석 함수 확인 및 정리

## 수행 절차
1. CSV 파일 4개를 불러왔다.
2. 데이터의 크기(shape)와 구조(info)를 확인하였다.
3. 결측치와 중복 여부를 확인하였다.
4. 날짜 데이터를 datetime 형식으로 변환하였다.
5. 주문 금액(total_amount)을 계산하였다.
6. 데이터를 하나의 DataFrame으로 병합하였다.
7. 카테고리별 매출을 분석하였다.
8. 월별 매출을 분석하였다.
9. 총매출, 주문 건수, 평균 주문 금액(AOV) 등 핵심 지표를 계산하였다.

## AI 활용 내용
- 데이터 병합(merge) 코드 작성 및 수정
- 카테고리별 및 월별 매출 분석 코드 작성
- 핵심 지표(KPI) 계산 코드 작성
- Notebook 코드 검토 및 수정
- 코드 검증 방법 및 결과 확인

## 검증한 코드 단위

| 단위 | 목적 | 예상 결과 | 실제 결과 | 검증 방법 |
|---|---|---|---|---|
| 1 | 기본키 중복 및 결측치 확인 | ID 중복과 결측치가 없어야 한다. | 중복 없음, 결측치 0개로 확인되었다. | `duplicated().any()`, `isnull().sum()` 확인 |
| 2 | 데이터 병합(merge) 검증 | 주문, 상품, 고객 데이터가 하나의 DataFrame으로 정상 병합된다. | 정상적으로 병합되었다. | `df.shape`, `df.head()` 출력 확인 |
| 3 | 핵심 지표(KPI) 계산 검증 | 총매출, 주문 건수, 평균 주문 금액(AOV)이 정상 계산된다. | 정상적으로 계산되었다. | 계산 결과 출력값 확인 |

## 발생한 문제

- `info()` 함수를 `print()`와 함께 사용하여 `None`이 함께 출력되는 문제가 발생하였다.
- 처음에는 데이터의 전체적인 상태 확인에 집중하여 결측치 확인이 부족하였다.
- Pandas의 `merge()`, `groupby()` 등의 사용 방법이 익숙하지 않았다.

## 해결 방법

- `print(info())` 대신 `info()`만 호출하도록 수정하였다.
- `isnull().sum()`을 추가하여 결측치를 확인하도록 수정하였다.
- AI의 도움을 받아 `merge()`와 `groupby()`의 사용 방법을 확인하고 직접 실행하여 결과를 검증하였다.

## 본인이 이해한 내용

- CSV 파일을 불러와 데이터를 확인하는 기본적인 방법을 알게 되었다.
- 여러 데이터를 ID를 기준으로 `merge()`를 사용하여 하나로 합칠 수 있다는 것을 알게 되었다.
- 데이터를 분석하기 전에 결측치와 중복 데이터를 확인하는 것이 중요하다는 것을 알게 되었다.
- 데이터를 이용해 매출과 주문 건수 같은 기본적인 분석 결과를 만들 수 있다는 것을 알게 되었다.
- 코드가 실행되는 것뿐만 아니라 결과가 예상한 것과 맞는지 확인하는 과정도 중요하다는 것을 배웠다.

## 아직 이해되지 않는 내용

- 전체적인 내용을 충분히 이해한 상태에서 과제를 진행하기보다는 AI의 도움을 받아 과제를 수행한 부분이 많아, 전체적인 데이터 분석 과정과 일부 Pandas 코드의 동작 원리는 아직 완전히 이해하지 못했다.