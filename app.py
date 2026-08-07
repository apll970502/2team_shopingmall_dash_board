"""
app.py - STEP 4: 필터 한 개
------------------------------------------------------------
STEP 3에 사이드바 필터(상품 카테고리)를 추가한다.
필터를 products에 적용해 '전체 고객 수' 옆에 '필터링된 상품 수' 지표를 추가,
필터 선택에 따라 지표가 바뀌는 것을 확인할 수 있게 한다.
------------------------------------------------------------
"""

import streamlit as st

from src.data_loader import load_data, is_data_empty

st.set_page_config(page_title="이커머스 데이터 대시보드", page_icon="📊", layout="wide")

st.title("📊 이커머스 데이터 대시보드")
st.caption("고객 · 상품 · 주문 · 주문상세 데이터를 기반으로 핵심 현황을 확인합니다.")


@st.cache_data
def get_data():
    return load_data()


raw_data = get_data()

if is_data_empty(raw_data):
    st.error("데이터를 불러오지 못했습니다. data/raw/ 폴더의 CSV 파일을 확인해주세요.")
    st.stop()

customers = raw_data["customers"]
products = raw_data["products"]

# ---- 필터 (사이드바) ----
st.sidebar.header("🔎 필터")
category_options = sorted(products["category"].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect("상품 카테고리", category_options)

products_f = products[products["category"].isin(selected_categories)] if selected_categories else products

# ---- 지표 ----
st.subheader("핵심 지표")
col1, col2 = st.columns(2)
col1.metric("전체 고객 수", f"{customers['customer_id'].nunique():,} 명")
col2.metric("필터링된 상품 수", f"{products_f['product_id'].nunique():,} 개")