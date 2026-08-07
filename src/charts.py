"""
charts.py
------------------------------------------------------------
외부 패키지 없이 streamlit 내장 차트(st.bar_chart, st.line_chart)만 사용한다.
plotly 등 별도 시각화 라이브러리를 설치할 필요가 없다.

각 함수는 analysis.py의 집계 결과(DataFrame)를 받아
화면에 직접 차트를 렌더링한다(반환값 없음).
------------------------------------------------------------
"""

import streamlit as st
import pandas as pd


def category_revenue_bar(df: pd.DataFrame) -> None:
    """카테고리별 매출 막대 차트"""
    chart_df = df.set_index("category")["revenue"]
    st.bar_chart(chart_df, x_label="카테고리", y_label="매출액(원)")


def status_count_bar(df: pd.DataFrame) -> None:
    """주문 상태별 주문 건수 막대 차트"""
    chart_df = df.set_index("order_status")["order_count"]
    st.bar_chart(chart_df, x_label="주문 상태", y_label="주문 건수")


def monthly_revenue_line(df: pd.DataFrame) -> None:
    """월별 주문 금액 추이 라인 차트"""
    chart_df = df.set_index("month")["revenue"]
    st.line_chart(chart_df, x_label="월", y_label="주문 금액(원)")


def payment_method_bar(df: pd.DataFrame) -> None:
    """결제 방법별 주문 건수 막대 차트 (streamlit에는 내장 파이차트가 없어 막대로 대체)"""
    chart_df = df.set_index("payment_method")["order_count"]
    st.bar_chart(chart_df, x_label="결제 방법", y_label="주문 건수")


def top_products_bar(df: pd.DataFrame) -> None:
    """Top 5 상품 매출 가로 막대 차트"""
    chart_df = df.set_index("product_name")["revenue"]
    st.bar_chart(chart_df, horizontal=True, x_label="매출액(원)", y_label="상품명")