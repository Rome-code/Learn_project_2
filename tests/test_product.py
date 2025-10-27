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