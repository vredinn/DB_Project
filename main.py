from models import *
from peewee import *


def show_categories():
    for c in Category.select():
        print(f"{c.id}: {c.name}")


def show_products():
    for p in Product.select():
        tags = [t.tag.name for t in p.tag_links]
        print(
            f"{p.id}: {p.name} ({p.category_id.name}) - {p.price} руб. | Теги: {', '.join(tags)}"
        )


def add_category():
    name = input("Введите название категории: ")
    Category.create(name=name)
    print("Категория добавлена.")


def add_product():
    name = input("Название товара: ")
    price = float(input("Цена: "))
    show_categories()
    cat_id = int(input("ID категории: "))
    product = Product.create(name=name, price=price, category_id=cat_id)

    tag_names = input("Введите теги через запятую: ").split(",")
    for tag_name in tag_names:
        tag, _ = Tag.get_or_create(name=tag_name.strip())
        ProductTag.create(product=product, tag=tag)
    print("Товар добавлен.")


def delete_product():
    show_products()
    pid = int(input("ID товара для удаления: "))
    ProductTag.delete().where(ProductTag.product == pid).execute()
    Product.delete_by_id(pid)
    print("Удалено.")


def update_product():
    show_products()
    pid = int(input("ID товара для изменения: "))
    product = Product.get_by_id(pid)

    new_name = input(f"Новое имя ({product.name}), оставить пустым — без изменений: ")
    if new_name:
        product.name = new_name

    new_price = input(
        f"Новая цена ({product.price}), оставить пустым — без изменений: "
    )
    if new_price:
        product.price = float(new_price)

    new_tags = input("Новые теги (через запятую, оставить пустым — без изменений): ")
    if new_tags:
        # Удалить старые связи
        ProductTag.delete().where(ProductTag.product == product).execute()

        tag_names = [name.strip() for name in new_tags.split(",") if name.strip()]
        for tag_name in tag_names:
            tag, _ = Tag.get_or_create(name=tag_name)
            ProductTag.create(product=product, tag=tag)

    if input("Хотите изменить категорию? (y/n): ").lower() == "y":
        show_categories()
        new_cat = int(input(f"ID новой категории ({product.category_id.id}): "))
        if new_cat:
            try:
                category = Category.get_by_id(int(new_cat))
                product.category_id = category.id
            except Category.DoesNotExist:
                print("Категория с таким ID не найдена.")

    product.save()
    print("Товар изменён.")


def menu():
    while True:
        print(
            """
1 - Вывести категории
2 - Вывести товары
3 - Добавить категорию
4 - Добавить товар
5 - Удалить товар
6 - Изменить товар
0 - Выйти
"""
        )
        choice = input("Выбор: ")
        if choice == "1":
            show_categories()
        elif choice == "2":
            show_products()
        elif choice == "3":
            add_category()
        elif choice == "4":
            add_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            update_product()
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    db.connect()
    menu()
    db.close()
