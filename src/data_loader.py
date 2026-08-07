from pathlib import Path
import pandas as pd

def load_data(data_dir="../data/raw"):
    """
    4개의 CSV 데이터를 읽어오고 날짜 타입을 변환하는 공통 함수
    """
    path = Path(data_dir)
    
    # 1. 파일 불러오기
    customers = pd.read_csv(path / "customers.csv")
    products = pd.read_csv(path / "products.csv")
    orders = pd.read_csv(path / "orders.csv")
    order_items = pd.read_csv(path / "order_items.csv")
    
    # 2. 날짜 타입 변환
    customers['signup_date'] = pd.to_datetime(customers['signup_date'])
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    return customers, products, orders, order_items
