"""
data_loader.py
------------------------------------------------------------
customers / products / orders / order_items 4개의 CSV 파일을
읽어와 pandas DataFrame으로 반환하는 모듈.

CSV 컬럼 정의
- customers.csv    : customer_id, name, gender, age, city, signup_date
- products.csv     : product_id, product_name, category, price
- orders.csv       : order_id, customer_id, order_date, payment_method, order_status
- order_items.csv  : orderitemid, order_id, product_id, quantity, unit_price
------------------------------------------------------------
"""

from pathlib import Path
import pandas as pd

# project_root/data/raw
DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

REQUIRED_FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
}


def load_data(data_dir: Path = DATA_DIR) -> dict:
    """
    4개 CSV 파일을 읽어 딕셔너리 형태로 반환한다.
    파일이 없거나 비어 있으면 빈 DataFrame으로 채워 반환하며,
    이후 app.py에서 is_data_empty()로 빈 데이터 여부를 확인한다.
    """
    data = {}
    for key, filename in REQUIRED_FILES.items():
        path = data_dir / filename
        try:
            df = pd.read_csv(path)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            df = pd.DataFrame()
        data[key] = df

    # 날짜 컬럼 파싱 (컬럼이 존재할 때만)
    if "signup_date" in data["customers"].columns:
        data["customers"]["signup_date"] = pd.to_datetime(
            data["customers"]["signup_date"], errors="coerce"
        )
    if "order_date" in data["orders"].columns:
        data["orders"]["order_date"] = pd.to_datetime(
            data["orders"]["order_date"], errors="coerce"
        )

    return data


def is_data_empty(data: dict) -> bool:
    """4개 테이블 중 하나라도 비어 있으면 True를 반환한다."""
    return any(df is None or df.empty for df in data.values())