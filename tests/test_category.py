import pytest
from src.category import Category
from src.product import Product


def test_category_initialization() -> None:

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    """Создаем категорию"""
    category = Category("Категория", "Описание категории", [product1, product2, product3])

    "Проверяем атрибуты категории"
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert category.products == [product1, product2, product3]
    assert len(category.products) == 3

def test_counts_increase() -> None:
    """Проверяем увеличение чисел в счетчиках"""
    initial_category_count = Category.category_count

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category("Категория2", "Описание2", [product1, product2, product3])

    "Проверяем, что счетчики увеличились"
    assert Category.category_count == initial_category_count + 1

    assert Category.product_count == initial_product_count + 1

def test_str_category(capsys):
    """Создаем несколько продуктов"""
    product_1 = Product("Prod1", "Desc1", 100.0, 2)
    product_2 = Product("Prod2", "Desc2", 200.0, 3)
    products = [product_1, product_2]

    "Создаем категорию"
    category = Category("Категория", "Описание категории", products)

    """Проверяем строковое отображение для класса Category"""
    print(str(category))
    captured = capsys.readouterr()
    assert captured.out == "Категория, количество продуктов: 5 шт.\n"


def test_add_product() -> None:

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем категорию
    category = Category("Электроника", "Технические устройства",[product1, product2, product3])

    # Создаем продукт
    product = Product("Телевизор", "Большой экран", 30000, 10)

    # Добавляем продукт
    category.add_product(product)

    # Получаем список продуктов
    products_list = list(category.get_products())

    # Проверка, что продукт добавлен
    product_found = False
    for p in products_list:
        if "Телевизор" in p:
            product_found = True
            break
    assert product_found, "Продукт не добавлен в категорию"

    # Проверка, что количество продуктов увеличилось
    assert len(products_list) == 4, "Некорректное число продуктов после добавления"

    # Проверка, что исключение выбрасывается при неправильном типе
    try:
        category.add_product("Не товар")
        assert False, "Ожидалось исключение при добавлении непонятного объекта"
    except TypeError:
        pass  # тест прошел успешно


