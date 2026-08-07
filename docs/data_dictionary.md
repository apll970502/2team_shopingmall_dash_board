# 데이터 컬럼 정의서 (Data Dictionary)

## 1. customers.csv (고객 정보)
- `customer_id`: 고객 고유 ID (기본키)
- `name`: 고객 이름
- `age`: 고객 연령
- `signup_date`: 가입일 (datetime)

## 2. products.csv (상품 정보)
- `product_id`: 상품 고유 ID (기본키)
- `product_name`: 상품명
- `category`: 상품 카테고리
- `price`: 상품 단가

## 3. orders.csv (주문 정보)
- `order_id`: 주문 고유 ID (기본키)
- `customer_id`: 주문한 고객 ID (외래키)
- `order_date`: 주문 일자 (datetime)

## 4. order_items.csv (주문 상세 정보)
- `order_id`: 주문 고유 ID (외래키)
- `product_id`: 상품 고유 ID (외래키)
- `quantity`: 주문 수량
- `unit_price`: 구매 당시 단가