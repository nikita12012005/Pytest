from users_collection import UsersCollection
from users_collection import ProductsCollection


def main():
    # Create instances of collection classes
    users_collection = UsersCollection()
    products_collection: ProductsCollection = ProductsCollection()

    # Insert documents
    user_data = {"username": "john_doe", "email": "john@example.com"}
    users_collection.insert_one(user_data)

    product_data = [{"name": "Product 1", "price": 19.99},
                    {"name": "Product 2", "price": 29.99}]
    products_collection.insert_many(product_data)

    # Find documents
    user_query = {"username": "john_doe"}
    user_result = users_collection.find_one(user_query)
    print("User:", user_result)

    product_query = {"price": {"$gt": 20}}
    product_results = products_collection.find(product_query)
    print("Products:", product_results)


if __name__ == "__main__":
    main()
