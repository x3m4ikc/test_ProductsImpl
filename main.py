class Product:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class ProductsImpl:
    def __init__(self):
        self.products = []

    def __check(self, product: Product) -> bool:
        for item in self.products:
            if item.id == product.id:
                return True

    def add_product(self, product: Product) -> bool:
        if self.__check(product):
            return False
        self.products.append(product)
        return True

    def delete_product(self, product: Product) -> bool:
        if self.__check(product):
            self.products.remove(product)
            return True
        return False

    def find_product_name(self, product) -> str:
        if self.__check(product):
            return product.name
        return ""

    def find_by_name(self, name: str) -> list:
        list_id = []
        for item in self.products:
            if item.name == name:
                list_id.append(item.id)
        return list_id
