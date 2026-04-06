from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass
import pytest


def test_product_initialization() -> None:
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

    product_object = Product("Test Product", "Test Description", 123.45, 10)

    """Проверяем вывод суммы произведений цены на количество у объектов"""
    print(product1 + product2)
    captured = capsys.readouterr()
    assert captured.out == "2580000.0\n"

    assert product_object.price == 123.45
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

    assert product_1.price == 30000


def test_price_property_write() -> None:
    product_1 = Product("Some", "desc", 12345, 1)
    product_1.price = 54321  # вызывает setter
    assert product_1.price == 54321.0

def test_addition_smartphone() -> None:
    """Создаем объекты Smartphone"""
    smartphone1 = Smartphone("Samsung Galaxy", "флагманский смартфон", 180000.0, 5, "3.36 ГГц", "S23 Ultra", "256 GB", "Серый")
    smartphone2 = Smartphone("Iphone", "смартфон от компании apple, Gray space", 210000.0, 8, "3.5 ГГц", "15", "512 GB", "Синий")

    """Проверка корректности сложения цен смартфонов"""

    assert smartphone1 + smartphone2 == 390000

    """Тест вывода ошибки при сложении объекта класса со сторонним объектом"""
    with pytest.raises(TypeError):
        result = smartphone1 + "not_a_smartphone"

def test_addition_lawn_grass() -> None:

    lawn_grass1 = LawnGrass("Barenbrug", " ", 5000, 5, " ", " ", " ")
    lawn_grass2 = LawnGrass("Turfline", " ", 11000, 8, " ", " ", " ")

    assert lawn_grass1 + lawn_grass2 == 16000
