# PySpark Products-Categories

## Задача
Вернуть все пары «Имя продукта – Имя категории» и продукты без категорий.

## Установка (ДЛЯ ЛИНУКС СИСТЕМ)
```bash
git clone https://github.com/Antirry/Test_Mindbox.git
cd Test_Mindbox
cd pyspark-products-categories
pip install -r requirements.txt

sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
source ~/.bashrc

pytest -v tests/test_product_category.py
```
---

У нас есть три датафрейма:

- products(id, name)
- categories(id, name)
- product_category(product_id, category_id) — связь многие-ко-многим.

Нужно вернуть один датафрейм, содержащий:

- все пары «Имя продукта – Имя категории»,
- а также продукты без категорий (с null в поле категории).

Для этого используем LEFT JOIN:

- products LEFT JOIN product_category → получаем все продукты, даже без связей.
- затем LEFT JOIN с categories → получаем имена категорий.
- В результате будет датафрейм с колонками: product_name, category_name.

---

## Вопросы/предположения

1. В условии не уточнено, нужно ли возвращать продукты без категорий в отдельном датафрейме или вместе. Я сделал **вместе** (с `null` в колонке категории).  
2. Предположил, что схема таблиц стандартная: `products(id, name)`, `categories(id, name)`, `product_category(product_id, category_id)`.  
3. Для тестов использовал `pytest` и локальный Spark (`local[1]`).  

