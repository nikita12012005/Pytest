class BaseMongo:
    pass


class UsersCollection(BaseMongo):
    def __init__(self):
        super().__init__('mydatabase', 'users')

    def insert_one(self, user_data):
        pass

    def find_one(self, user_query: object) -> object:
        pass


class ProductsCollection(BaseMongo):
    def __init__(self):
        super().__init__('mydatabase', 'products')

    def insert_many(self, product_data):
        pass

    def find(self, product_query):
        pass
