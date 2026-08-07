"""
app.py
------------------------------------------------------------
고객 / 상품 / 주문 / 주문상세 데이터를 탐색하는 Streamlit 대시보드.

구성 순서
1. 기본 화면       : 페이지 설정, 제목/설명
2. 데이터 로딩     : src.data_loader.load_data()
3. 지표            : st.metric() 8개
4. 필터            : 사이드바 5종 필터
5. 표 출력         : st.dataframe(filtered_data)
6. 차트            : Plotly 차트 5개 + 해석 텍스트
7. 빈 데이터 처리  : 원본/필터 결과가 비어있는 경우 안내
실행: streamlit run app.py
------------------------------------------------------------
"""

import streamlit as st
import pandas as pd

from src.data_loader import load_data, is_data_empty
from src import analysis
from src import charts


# ------------------------------------------------------------
# 1. 기본 화면
# ------------------------------------------------------------
st.set_page_config(page_title="이커머스 데이터 대시보드", page_icon="📊", layout="wide")

st.title("📊 이커머스 데이터 대시보드")
st.caption("고객 · 상품 · 주문 · 주문상세 데이터를 기반으로 핵심 현황을 확인합니다.")


# ------------------------------------------------------------
# 2. 데이터 로딩
# ------------------------------------------------------------
@st.cache_data
def get_data():
    return load_data()


raw_data = get_data()

# 7. 빈 데이터 처리 (원본 데이터가 없는 경우)
if is_data_empty(raw_data):
    st.error(
        "❗ 데이터를 불러오지 못했습니다. "
        "`data/raw/` 폴더에 customers.csv, products.csv, orders.csv, order_items.csv "
        "파일이 모두 존재하는지 확인해주세요."
    )
    st.stop()

customers = raw_data["customers"]
products = raw_data["products"]
orders = raw_data["orders"]
order_items = raw_data["order_items"]

orders_with_amount = analysis.build_order_amounts(orders, order_items)


# ------------------------------------------------------------
# 4. 필터 (사이드바)
# ------------------------------------------------------------
st.sidebar.header("🔎 필터")

category_options = sorted(products["category"].dropna().unique().tolist())
status_options = sorted(orders["order_status"].dropna().unique().tolist())
payment_options = sorted(orders["payment_method"].dropna().unique().tolist())
city_options = sorted(customers["city"].dropna().unique().tolist())

selected_categories = st.sidebar.multiselect("상품 카테고리", category_options)
selected_statuses = st.sidebar.multiselect("주문 상태", status_options)
selected_payments = st.sidebar.multiselect("결제 방법", payment_options)
selected_cities = st.sidebar.multiselect("고객 도시", city_options)

min_date = orders["order_date"].min()
max_date = orders["order_date"].max()
if pd.isna(min_date) or pd.isna(max_date):
    selected_date_range = None
else:
    selected_date_range = st.sidebar.date_input(
        "주문 기간",
        value=(min_date.date(), max_date.date()),
        min_value=min_date.date(),
        max_value=max_date.date(),
    )
    if isinstance(selected_date_range, (tuple, list)) and len(selected_date_range) != 2:
        selected_date_range = None

if st.sidebar.button("필터 초기화"):
    st.rerun()

orders_f, order_items_f, customers_f = analysis.apply_filters(
    orders_with_amount,
    order_items,
    customers,
    products,
    categories=selected_categories,
    statuses=selected_statuses,
    payment_methods=selected_payments,
    cities=selected_cities,
    date_range=selected_date_range,
)


# 7. 빈 데이터 처리 (필터 결과가 없는 경우)
if orders_f.empty:
    st.warning("선택한 조건에 해당하는 주문 데이터가 없습니다. 필터 조건을 변경해보세요.")
    st.stop()


# ------------------------------------------------------------
# 3. 지표 (필터링된 데이터 기준)
# ------------------------------------------------------------
kpis = analysis.compute_kpis(customers_f, products, orders_f, order_items_f)

st.subheader("핵심 지표")
row1 = st.columns(4)
row1[0].metric("전체 고객 수", f"{kpis['total_customers']:,} 명")
row1[1].metric("전체 상품 수", f"{kpis['total_products']:,} 개")
row1[2].metric("전체 주문 수", f"{kpis['total_orders']:,} 건")
row1[3].metric("총 주문 수량", f"{kpis['total_quantity']:,} 개")

row2 = st.columns(4)
row2[0].metric("총 주문 금액", f"{kpis['total_amount']:,.0f} 원")
row2[1].metric("평균 주문 금액", f"{kpis['avg_order_amount']:,.0f} 원")
row2[2].metric("배송완료 주문 수", f"{kpis['delivered_orders']:,} 건")
row2[3].metric("취소/환불 주문 수", f"{kpis['cancelled_refunded_orders']:,} 건")

st.divider()


# ------------------------------------------------------------
# 5. 표 출력
# ------------------------------------------------------------
st.subheader("주문 상세 데이터")

display_df = (
    order_items_f
    .merge(orders_f[["order_id", "customer_id", "order_date", "payment_method", "order_status"]], on="order_id", how="left")
    .merge(customers[["customer_id", "name", "city"]], on="customer_id", how="left")
    .merge(products[["product_id", "product_name", "category"]], on="product_id", how="left")
)
display_df["item_amount"] = display_df["quantity"] * display_df["unit_price"]
display_df = display_df[[
    "order_id", "order_date", "order_status", "payment_method",
    "name", "city", "product_name", "category",
    "quantity", "unit_price", "item_amount",
]].sort_values("order_date", ascending=False)

st.dataframe(display_df, use_container_width=True, hide_index=True)
st.caption(f"필터 조건에 해당하는 주문상세 {len(display_df):,}행")

st.divider()


# ------------------------------------------------------------
# 6. 차트
# ------------------------------------------------------------
st.subheader("차트로 보는 현황")

col1, col2 = st.columns(2)

# 카테고리별 매출
with col1:
    cat_rev = analysis.category_revenue(order_items_f, products)
    if cat_rev.empty:
        st.info("카테고리별 매출 데이터가 없습니다.")
    else:
        charts.category_revenue_bar(cat_rev)
        top_cat = cat_rev.iloc[0]
        bottom_cat = cat_rev.iloc[-1]
        st.caption(
            f"매출이 가장 높은 카테고리는 **{top_cat['category']}**"
            f"({top_cat['revenue']:,.0f}원), 가장 낮은 카테고리는 **{bottom_cat['category']}**"
            f"({bottom_cat['revenue']:,.0f}원)입니다. "
            "카테고리 간 매출 격차가 크다면 특정 상품군에 대한 의존도가 높다는 뜻일 수 있습니다. "
            "다만 이 수치만으로는 마진율이나 재고 비용까지는 알 수 없어, 수익성 판단에는 추가 데이터가 필요합니다."
        )

# 주문 상태별 건수
with col2:
    status_df = analysis.status_counts(orders_f)
    if status_df.empty:
        st.info("주문 상태 데이터가 없습니다.")
    else:
        charts.status_count_bar(status_df)
        top_status = status_df.iloc[0]
        st.caption(
            f"가장 많은 주문 상태는 **{top_status['order_status']}**"
            f"({top_status['order_count']:,}건)입니다. "
            "취소·환불 비중이 높다면 배송이나 상품 품질에 문제가 있을 가능성을 점검해볼 필요가 있습니다. "
            "다만 이 차트는 건수 기준이라 취소/환불로 인한 금액 손실 규모까지는 보여주지 않습니다."
        )

col3, col4 = st.columns(2)

# 월별 주문 금액 추이
with col3:
    monthly_df = analysis.monthly_revenue(orders_f)
    if monthly_df.empty:
        st.info("월별 주문 금액 데이터가 없습니다.")
    else:
        charts.monthly_revenue_line(monthly_df)
        peak = monthly_df.loc[monthly_df["revenue"].idxmax()]
        low = monthly_df.loc[monthly_df["revenue"].idxmin()]
        st.caption(
            f"주문 금액이 가장 높았던 달은 **{peak['month']}**({peak['revenue']:,.0f}원), "
            f"가장 낮았던 달은 **{low['month']}**({low['revenue']:,.0f}원)입니다. "
            "특정 월에 매출이 몰린다면 프로모션이나 계절적 요인이 있었는지 확인해볼 만합니다. "
            "다만 이 차트만으로는 매출 변동이 마케팅 때문인지 자연적 수요 변화인지 구분하기 어렵습니다."
        )

# 결제 방법별 건수
with col4:
    payment_df = analysis.payment_method_share(orders_f)
    if payment_df.empty:
        st.info("결제 방법 데이터가 없습니다.")
    else:
        charts.payment_method_bar(payment_df)
        top_payment = payment_df.iloc[0]
        share = top_payment["order_count"] / payment_df["order_count"].sum() * 100
        st.caption(
            f"가장 많이 사용된 결제 방법은 **{top_payment['payment_method']}**"
            f"(전체의 {share:.1f}%)입니다. "
            "특정 결제 수단에 쏠려 있다면 해당 채널의 수수료나 장애가 발생할 때 리스크가 커질 수 있습니다. "
            "다만 이 비율은 결제 수단별 고객 만족도나 실패율까지는 설명하지 못합니다."
        )

# Top 5 상품
top_prod_df = analysis.top_products(order_items_f, products, n=5)
if not top_prod_df.empty:
    charts.top_products_bar(top_prod_df)
    best = top_prod_df.sort_values("revenue", ascending=False).iloc[0]
    st.caption(
        f"매출 1위 상품은 **{best['product_name']}**({best['revenue']:,.0f}원)입니다. "
        "특정 상품이 매출을 견인하고 있다면 해당 상품의 재고·공급 안정성이 매우 중요해집니다. "
        "다만 매출 상위 상품이 반드시 수익 기여도가 가장 높은 상품이라고 단정할 수는 없으며, "
        "원가나 반품률 데이터가 없으면 실제 이익 기여도는 별도로 확인해야 합니다."
    )