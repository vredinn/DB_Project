import sqlite3


def program():

    match input(
        "Выберите действие:\n1. вывести все товары\n2. вывести список доступных категорий\n3. добавить товар\n4. добавить категорию\n5. удалить товар\n0. выйти\n"
    ):
        case "1":
            with sqlite3.connect("t1.db") as conn:
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT p.id, p.name, p.price, c.name FROM products AS p JOIN categories AS c ON p.category_id = c.id"
                )
                products = cursor.fetchall()
                for product in products:
                    print(
                        f"Название товара: {product[1]}, Стоимость: {product[2]}, Категория: {product[3]}"
                    )
            program()
        case "2":
            with sqlite3.connect("t1.db") as conn:
                cursor = conn.cursor()
            cursor.execute("SELECT * FROM categories")
            categories = cursor.fetchall()
            for category in categories:
                print(f"Категория: {category[1]}")
            program()
        case "3":
            with sqlite3.connect("t1.db") as conn:
                cursor = conn.cursor()
                print("Выберите категорию товара:")
                cursor.execute("SELECT * FROM categories")
                categories = cursor.fetchall()
                for category in categories:
                    print(f"{category[0]}. {category[1]}")

                category_id = int(input())

                name = input("Введите название товара: ")

                price = float(input("Введите цену товара: "))

                cursor.execute(
                    "INSERT INTO products (name, price, category_id) VALUES (:name, :price, :category_id)",
                    {"name": name, "price": price, "category_id": category_id},
                )

                conn.commit()

            print("Товар добавлен.")
            program()
        case "4":
            with sqlite3.connect("t1.db") as conn:
                cursor = conn.cursor()
                name = input("Введите название Категории: ")

                cursor.execute(
                    "INSERT INTO categories (name) VALUES (:name)",
                    {"name": name},
                )

                conn.commit()
            print("Категория добавлена.")
            program()
        case "5":
            with sqlite3.connect("t1.db") as conn:
                cursor = conn.cursor()
                print("Выберите товар для удаления:")
                cursor.execute(
                    "SELECT p.id, p.name, p.price, c.name FROM products AS p JOIN categories AS c ON p.category_id = c.id"
                )
                products = cursor.fetchall()
                for product in products:
                    print(
                        f"ID: {product[0]} Название товара: {product[1]}, Стоимость: {product[2]}, Категория: {product[3]}"
                    )
                id = int(input("Введите id товара: "))
                cursor.execute("DELETE FROM products WHERE id = :id", {"id": id})
                conn.commit()
            print("Товар удален.")
            program()
        case "0":
            exit
        case _:
            print("Неверный выбор.")
            program()


program()
