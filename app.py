"""
app.py - STEP 2: 데이터 로딩
------------------------------------------------------------
STEP 1에 CSV 4종 로딩을 추가한다.
아직 지표/필터/표/차트는 없고, 로딩이 잘 되는지 행 수만 확인한다.
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

st.success("데이터 로딩 완료")
st.write({name: df.shape for name, df in raw_data.items()})