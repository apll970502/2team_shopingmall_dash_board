"""
app.py - STEP 3: 지표 한 개
------------------------------------------------------------
STEP 2에 st.metric()으로 '전체 고객 수' 지표 1개를 추가한다.
로딩 확인용 st.write는 제거한다.
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

st.subheader("핵심 지표")
st.metric("전체 고객 수", f"{customers['customer_id'].nunique():,} 명")