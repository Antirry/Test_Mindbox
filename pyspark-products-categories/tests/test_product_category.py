import pytest
from pyspark.sql import SparkSession
from src.product_category import product_category_pairs

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("test").getOrCreate()

def test_product_with_and_without_categories(spark):
    products = spark.createDataFrame(
        [(1, "Apple"), (2, "Banana"), (3, "Carrot")],
        ["id", "name"]
    )
    categories = spark.createDataFrame(
        [(10, "Fruit"), (20, "Vegetable")],
        ["id", "name"]
    )
    product_category = spark.createDataFrame(
        [(1, 10), (3, 20)],  # Apple->Fruit, Carrot->Vegetable
        ["product_id", "category_id"]
    )

    result = product_category_pairs(products, categories, product_category)

    data = {(row["product_name"], row["category_name"]) for row in result.collect()}

    assert ("Apple", "Fruit") in data
    assert ("Carrot", "Vegetable") in data
    # Banana без категории
    assert ("Banana", None) in data
