# 코드 단위 검증 기록

## 작성자
- 이름: 박진
- GitHub ID: jeanpark0115@naver.com
- 담당 기능: Streamlit 및 시각화

## 1. 검증 단위
- 기능명: 빈 DataFrame 처리 검증
- 관련 Issue: #
- 관련 파일: app.py, src/data_loader.py (is_data_empty)

## 2. AI 요청 내용
"앱 구조 ... 7. 빈 데이터 처리" 요구사항에 따라, 원본 CSV가 비어있거나
필터 결과가 0건인 경우 앱이 에러로 죽지 않고 안내 문구를 보여주도록 요청함.

## 3. 실행 전 예상
- 입력 데이터: (1) 4개 CSV가 모두 빈 DataFrame인 경우, (2) 정상 데이터인데 필터 조합 결과가 0건인 경우
- 예상 결과: (1)은 st.error 후 즉시 중단, (2)는 st.warning 후 중단. 둘 다 Traceback 없이 종료되어야 한다.
- 예상 행/열 수: 두 경우 모두 최종 화면에 표/차트/지표가 렌더링되지 않아야 한다.
- 오류 가능 조건: order_amount 계산(quantity * unit_price)에서 order_items가 비어있으면 merge 단계에서 KeyError가 날 수 있다.

## 4. 실행 코드
```python
import pandas as pd
from src.data_loader import is_data_empty
from src import analysis

empty_data = {"customers": pd.DataFrame(), "products": pd.DataFrame(),
              "orders": pd.DataFrame(), "order_items": pd.DataFrame()}
print(is_data_empty(empty_data))  # True 예상

orders_amt = analysis.build_order_amounts(pd.DataFrame(), pd.DataFrame())
print(orders_amt.empty)  # True 예상, 에러 없이 반환되어야 함
```

## 5. 실제 결과
- 출력값: `is_data_empty(empty_data)` → True. `build_order_amounts`에 빈 DataFrame을 넣어도
  예외 없이 `order_amount` 컬럼이 붙은 빈 DataFrame을 반환함.
- 예상과 다른 점: 없음. 존재하지 않는 카테고리 조합으로 필터링했을 때도 `apply_filters()`가
  빈 결과를 정상 반환했고, app.py는 `st.warning()` + `st.stop()`으로 안전하게 멈췄다.

## 6. 정상 조건 검증
- assert 또는 대조 계산:
```python
assert is_data_empty(empty_data) is True
assert orders_amt.empty and "order_amount" in orders_amt.columns
```

## 7. 예외 조건 검증
- 조건: 정상 데이터(비어있지 않음)인데, 존재하지 않는 카테고리('없는카테고리')로 필터링
- 결과: `apply_filters()` 결과 orders_f, order_items_f 모두 0행. app.py에서 `orders_f.empty` 분기를
  타서 Traceback 없이 `st.warning("선택한 조건에 해당하는 주문 데이터가 없습니다...")` 표시 후 정상 종료됨.

## 8. AI 코드에서 수정한 부분
1. `build_order_amounts()`에 `orders.empty or order_items.empty` 가드 조건을 추가해,
   빈 데이터에서도 merge 없이 바로 `order_amount=0.0` 컬럼을 붙여 반환하도록 했다.
2. app.py에서 원본 데이터 빈 값 체크(`is_data_empty`)와 필터 결과 빈 값 체크(`orders_f.empty`)를
   두 단계로 분리해서, 각각 다른 안내 문구(st.error / st.warning)를 보여주도록 했다.

## 9. 내 말로 설명
빈 데이터는 두 가지 경우가 있다. 하나는 CSV 파일 자체가 비어있거나 없는 경우, 다른 하나는 파일은 정상인데 사용자가 고른 필터 조합에 해당하는 데이터가 하나도 없는 경우다. 앞의 경우는 애초에 지표를 계산할 재료 자체가 없는 거라 is_data_empty()로 데이터 로딩 직후에 바로 걸러서 st.error + st.stop()으로 끝낸다. 뒤의 경우는 원본 데이터는 멀쩡하니까 필터를 적용한 뒤(apply_filters() 호출 후) orders_f.empty로 따로 체크해서 st.warning으로 안내한다.

## 10. 아직 이해되지 않는 부분