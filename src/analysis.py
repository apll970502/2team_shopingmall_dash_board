import pandas as pd

def merge_datasets(customers, products, orders, order_items):
    """
    데이터를 병합하고 총 금액 컬럼을 생성하는 함수
    """
    order_items['total_amount'] = order_items['quantity'] * order_items['unit_price']
    
    df = order_items.merge(products, on='product_id', how='left')
    df = df.merge(orders, on='order_id', how='left')
    df = df.merge(customers, on='customer_id', how='left')
    
    return df

def get_key_metrics(df):
    """
    쇼핑몰 핵심 지표(총 매출액, 총 주문 건수, 평균 주문 금액)를 계산하는 함수
    """
    total_revenue = df['total_amount'].sum()
    total_orders = df['order_id'].nunique()
    aov = total_revenue / total_orders if total_orders > 0 else 0
    
    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "aov": aov
    }