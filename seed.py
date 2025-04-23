from models import *

TABLES = [Category, Product, Tag, ProductTag]

with db:
    db.drop_tables(TABLES, safe=True)
    db.create_tables(TABLES, safe=True)

    food = Category.create(name="Еда")
    clothes = Category.create(name="Одежда")
    tech = Category.create(name="Техника")

    bread = Product.create(name="Хлеб", price=50, category_id=food)
    cheese = Product.create(name="Сыр", price=100, category_id=food)
    tshirt = Product.create(name="Футболка", price=500, category_id=clothes)
    laptop = Product.create(name="Ноутбук", price=50000, category_id=tech)

    eco = Tag.create(name="Эко")
    fresh = Tag.create(name="Свежий")
    sale = Tag.create(name="Скидка")

    ProductTag.create(product=bread, tag=eco)
    ProductTag.create(product=cheese, tag=fresh)
    ProductTag.create(product=tshirt, tag=sale)
    ProductTag.create(product=laptop, tag=sale)
