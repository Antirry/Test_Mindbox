from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def product_category_pairs(products: DataFrame, categories: DataFrame, product_category: DataFrame) -> DataFrame:
    """
    Возвращает датафрейм с парами (Имя продукта, Имя категории),
    включая продукты без категорий (category_name = null).
    """
    # products: id, name
    # categories: id, name
    # product_category: product_id, category_id

    joined = (
        products.alias("p")
        .join(product_category.alias("pc"), F.col("p.id") == F.col("pc.product_id"), how="left")
        .join(categories.alias("c"), F.col("pc.category_id") == F.col("c.id"), how="left")
        .select(F.col("p.name").alias("product_name"), F.col("c.name").alias("category_name"))
    )
    return joined
