import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",  # Replace with your database name
    user="postgres",
    password="yourpassword"
)
conn.autocommit = True

cursor = conn.cursor()

cursor.execute("CREATE DATABASE store")

cursor.close()
conn.close()

conn = psycopg2.connect(
    host="localhost",
    database="store",
    user="postgres",
    password="yourpassword"
)
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price NUMERIC(10, 2)
    )
""")

cursor.execute("""
    CREATE TABLE orders (
        id SERIAL PRIMARY KEY,
        product_id INT,
        quantity INT
    )
""")

products_data = [
    ('Product A', 10.99),
    ('Product B', 20.49),
    ('Product C', 5.99),
    ('Product D', 15.75),
    ('Product E', 8.50)
]

for product in products_data:
    cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", product)

orders_data = [
    (1, 2),
    (3, 1),
    (2, 3),
    (4, 2),
    (5, 4)
]

for order in orders_data:
    cursor.execute("INSERT INTO orders (product_id, quantity) VALUES (%s, %s)", order)

cursor.execute("""
    SELECT p.name, p.price, o.quantity, (p.price * o.quantity) AS total_price
    FROM products p
    JOIN orders o ON p.id = o.product_id
""")

result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()
