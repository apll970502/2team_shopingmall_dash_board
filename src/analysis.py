"""
analysis.py
------------------------------------------------------------
KPI 계산, 카테고리/상태/월별 집계, 사용자 필터 적용 로직을 담은 모듈.
모든 함수는 순수 함수(입력 -> 출력)로 작성하여 app.py에서 조합해 사용한다.
------------------------------------------------------------
"""

import pandas as pd

# 상태 문자열에 이 키워드가 포함되면 배송완료 / 취소·환불로 간주한다.
DELIVERED_KEYWORDS = ["배송완료"]
CANCEL_REFUND_KEYWORDS = ["취소", "환불"]


def build_order_amounts(orders: pd.DataFrame, order_items: pd.DataFrame) -> pd.DataFrame:
    """
    order_items(quantity * unit_price)를 order_id 기준으로 합산하여
    orders 테이블에 'order_amount' 컬럼으로 병합한다.
    """
    if orders.empty or order_items.empty:
        result = orders.copy()
        result["order_amount"] = 0.0
        return result

    items = order_items.copy()
    items["item_amount"] = items["quantity"] * items["unit_price"]
    order_amount = (
        items.groupby("order_id", as_index=False)["item_amount"]
        .sum()
        .rename(columns={"item_amount": "order_amount"})
    )
    merged = orders.merge(order_amount, on="order_id", how="left")
    merged["order_amount"] = merged["order_amount"].fillna(0.0)
    return merged


def compute_kpis(
    customers: pd.DataFrame,
    products: pd.DataFrame,
    orders_with_amount: pd.DataFrame,
    order_items: pd.DataFrame,
) -> dict:
    """화면 상단에 표시할 8개 핵심 지표를 계산한다."""
    total_customers = customers["customer_id"].nunique() if not customers.empty else 0
    total_products = products["product_id"].nunique() if not products.empty else 0
    total_orders = orders_with_amount["order_id"].nunique() if not orders_with_amount.empty else 0
    total_quantity = int(order_items["quantity"].sum()) if not order_items.empty else 0
    total_amount = float(orders_with_amount["order_amount"].sum()) if not orders_with_amount.empty else 0.0
    avg_order_amount = (total_amount / total_orders) if total_orders else 0.0

    if not orders_with_amount.empty and "order_status" in orders_with_amount.columns:
        status = orders_with_amount["order_status"].astype(str)
        delivered_orders = int(status.str.contains("|".join(DELIVERED_KEYWORDS)).sum())
        cancelled_refunded_orders = int(status.str.contains("|".join(CANCEL_REFUND_KEYWORDS)).sum())
    else:
        delivered_orders = 0
        cancelled_refunded_orders = 0

    return {
        "total_customers": total_customers,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "total_amount": total_amount,
        "avg_order_amount": avg_order_amount,
        "delivered_orders": delivered_orders,
        "cancelled_refunded_orders": cancelled_refunded_orders,
    }


def category_revenue(order_items: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    """카테고리별 매출(수량 * 단가 합)을 매출 기준 내림차순으로 반환한다."""
    if order_items.empty or products.empty:
        return pd.DataFrame(columns=["category", "revenue"])
    items = order_items.merge(products[["product_id", "category"]], on="product_id", how="left")
    items["item_amount"] = items["quantity"] * items["unit_price"]
    result = (
        items.groupby("category", as_index=False)["item_amount"]
        .sum()
        .rename(columns={"item_amount": "revenue"})
        .sort_values("revenue", ascending=False)
        .reset_index(drop=True)
    )
    return result


def status_counts(orders: pd.DataFrame) -> pd.DataFrame:
    """주문 상태별 주문 건수를 건수 기준 내림차순으로 반환한다."""
    if orders.empty:
        return pd.DataFrame(columns=["order_status", "order_count"])
    result = (
        orders.groupby("order_status", as_index=False)["order_id"]
        .nunique()
        .rename(columns={"order_id": "order_count"})
        .sort_values("order_count", ascending=False)
        .reset_index(drop=True)
    )
    return result


def monthly_revenue(orders_with_amount: pd.DataFrame) -> pd.DataFrame:
    """월(YYYY-MM) 기준 주문 금액 합계를 시간순으로 반환한다."""
    if orders_with_amount.empty:
        return pd.DataFrame(columns=["month", "revenue"])
    df = orders_with_amount.dropna(subset=["order_date"]).copy()
    if df.empty:
        return pd.DataFrame(columns=["month", "revenue"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    result = (
        df.groupby("month", as_index=False)["order_amount"]
        .sum()
        .rename(columns={"order_amount": "revenue"})
        .sort_values("month")
        .reset_index(drop=True)
    )
    return result


def payment_method_share(orders: pd.DataFrame) -> pd.DataFrame:
    """결제 방법별 주문 건수를 건수 기준 내림차순으로 반환한다."""
    if orders.empty:
        return pd.DataFrame(columns=["payment_method", "order_count"])
    result = (
        orders.groupby("payment_method", as_index=False)["order_id"]
        .nunique()
        .rename(columns={"order_id": "order_count"})
        .sort_values("order_count", ascending=False)
        .reset_index(drop=True)
    )
    return result


def top_products(order_items: pd.DataFrame, products: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """매출 기준 상위 n개 상품을 반환한다."""
    if order_items.empty or products.empty:
        return pd.DataFrame(columns=["product_name", "revenue"])
    items = order_items.merge(products[["product_id", "product_name"]], on="product_id", how="left")
    items["item_amount"] = items["quantity"] * items["unit_price"]
    result = (
        items.groupby("product_name", as_index=False)["item_amount"]
        .sum()
        .rename(columns={"item_amount": "revenue"})
        .sort_values("revenue", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )
    return result


def apply_filters(
    orders_with_amount: pd.DataFrame,
    order_items: pd.DataFrame,
    customers: pd.DataFrame,
    products: pd.DataFrame,
    categories: list | None = None,
    statuses: list | None = None,
    payment_methods: list | None = None,
    cities: list | None = None,
    date_range: tuple | None = None,
):
    """
    사이드바에서 선택한 조건에 맞춰 orders / order_items / customers를
    함께 필터링하여 반환한다. (조건이 비어있으면 해당 필터는 적용하지 않음)
    """
    orders_f = orders_with_amount.copy()

    if statuses:
        orders_f = orders_f[orders_f["order_status"].isin(statuses)]
    if payment_methods:
        orders_f = orders_f[orders_f["payment_method"].isin(payment_methods)]
    if date_range and len(date_range) == 2 and date_range[0] and date_range[1]:
        start = pd.to_datetime(date_range[0])
        end = pd.to_datetime(date_range[1])
        orders_f = orders_f[(orders_f["order_date"] >= start) & (orders_f["order_date"] <= end)]
    if cities:
        cust_ids = customers.loc[customers["city"].isin(cities), "customer_id"]
        orders_f = orders_f[orders_f["customer_id"].isin(cust_ids)]

    order_items_f = order_items[order_items["order_id"].isin(orders_f["order_id"])].copy()

    if categories:
        product_ids = products.loc[products["category"].isin(categories), "product_id"]
        order_items_f = order_items_f[order_items_f["product_id"].isin(product_ids)]
        # 카테고리 필터는 주문상세 기준이므로, 해당 상품이 포함되지 않은 주문은 orders에서도 제외
        orders_f = orders_f[orders_f["order_id"].isin(order_items_f["order_id"])]

    customers_f = customers[customers["customer_id"].isin(orders_f["customer_id"])].copy()

    return orders_f, order_items_f, customers_f