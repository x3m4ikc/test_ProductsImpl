class Product:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class ProductsImpl:
    def __init__(self) -> None:
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

    def find_product_name(self, id: int) -> str:
        for item in self.products:
            if item.id == id:
                return item.name
        return ""

    def find_by_name(self, name: str) -> list:
        matches = []
        for item in self.products:
            if item.name == name:
                matches.append(item.id)
        return matches
