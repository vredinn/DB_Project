from peewee import *


db = SqliteDatabase("t1.db")


class Category(Model):
    id = AutoField()
    name = CharField(60, unique=True)

    class Meta:
        database = db
        db_table = "categories"


class Product(Model):
    id = PrimaryKeyField()
    name = CharField(60)
    price = FloatField()
    category_id = ForeignKeyField(Category, backref="products")

    class Meta:
        database = db
        db_table = "products"


class Tag(Model):
    id = AutoField()
    name = CharField(60, unique=True)

    class Meta:
        database = db
        db_table = "tags"


class ProductTag(Model):
    product = ForeignKeyField(Product, backref="tag_links")
    tag = ForeignKeyField(Tag, backref="product_links")

    class Meta:
        database = db
        db_table = "product_tags"
        primary_key = CompositeKey("product", "tag")


Product.tags = ManyToManyField(Tag, backref="products", through_model=ProductTag)
