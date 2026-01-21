from src.product import Product


def test_product_initialization() -> None:
    """Создаем объект Product"""
    product_object = Product("Test Product", "Test Description", 123.45, 10)

    "Проверяем атрибуты"
    assert product_object.name == "Test Product"
    assert product_object.description == "Test Description"
    assert product_object.price == "123.45"
    assert product_object.quantity == 10


def test_new_product() -> None:
    params = {
        "name": "name",
        "description": "description",
        "price": "120",
        "quantity": "5",
    }
    product_1 = Product.new_product(params)

    assert product_1.name == "name"
    assert product_1.description == "description"
    assert product_1.price == "120"
    assert product_1.quantity == "5"


def test_return_price() -> None:
    product_1 = Product("Телевизор", "Большой экран", 30000, 10)

    assert product_1.price == "30000"


def test_price_property_write() -> None:
    product_1 = Product("Some", "desc", 12345, 1)
    product_1.price = 54321  # вызывает setter
    assert product_1.price == "54321.0"
