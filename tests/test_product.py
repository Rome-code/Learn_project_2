import pytest
from src.product import Product


def test_product_initialization():
    """Создаем объект Product"""
    product_object = Product("Test Product", "Test Description", 123.45, 10)

    "Проверяем атрибуты"
    assert product_object.name == "Test Product"
    assert product_object.description == "Test Description"
    assert product_object.price == 123.45
    assert product_object.quantity == 10

def test_total_sum(capsys):
    """Создаем объект Product"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


    """Проверяем вывод суммы произведений цены на количество у объектов"""
    print(product1 + product2)
    captured = capsys.readouterr()
    assert captured.out == "2580000.0\n"