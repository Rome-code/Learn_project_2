import pytest
from main import Product, Category

def test_product_initialization():
    """Создаем объект Product"""
    product_object = Product("Test Product", "Test Description", 123.45, 10)

    "Проверяем атрибуты"
    assert product_object.name == "Test Product"
    assert product_object.description == "Test Description"
    assert product_object.price == 123.45
    assert product_object.quantity == 10

def test_category_initialization():
    """Создаем несколько продуктов"""
    product_1 = Product("Prod1", "Desc1", 100.0, 2)
    product_2 = Product("Prod2", "Desc2", 200.0, 3)
    products = [product_1, product_2]

    "Создаем категорию"
    category = Category("Категория", "Описание категории", products)

    "Проверяем атрибуты категории"
    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products) == 2
    assert category.products[0].name == "Prod1"
    assert category.products[1].name == "Prod2"

def test_counts_increase():
    """Проверяем увеличение чисел в счетчиках"""
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    product = Product("Prod3", "Desc3", 150.0, 5)
    category = Category("Категория2", "Описание2", [product])

    "Проверяем, что счетчики увеличились"
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 1