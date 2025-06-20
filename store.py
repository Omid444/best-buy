from products import Product

class Store:


    def __init__(self, pro_list):
        self.product_list: list[Product] = pro_list
        self.total_price: float = 0


    def add_product(self, product):
        """Add product to store"""
        self.product_list.append(product)


    def remove_product(self, product):
        """Removes a product from store"""
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total"""
        return len(self.product_list)


    def get_all_products(self) -> list[Product]:
        """Return list of all active product"""
        active_products = [product_item for product_item in self.product_list if product_item.is_active()]
        return active_products


    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        self.total_price: float = 0
        print(" befor loop total price:", self.total_price)
        for item in shopping_list:
            self.total_price += item[0].buy(item[1])
            print("total price:", self.total_price)
        return round(float(self.total_price),2)


