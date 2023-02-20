"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
goods = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def one_product_sales(items_sold):
    sales_sum = 0
    for item in items_sold:
        sales_sum += item
    return sales_sum

avg_item_sold = 0
all_sales = 0
avg_all_item = 0
for one_good in goods:
    items_sold_sum = one_product_sales(one_good['items_sold'])
    print(f"сумма продаж {one_good['product']}: {items_sold_sum}")
    avg_item_sold = round(one_product_sales(one_good['items_sold']) / len(one_good['items_sold']), 2)
    print(f"среднее количество продаж {one_good['product']}: {avg_item_sold}")
    all_sales += items_sold_sum
    avg_all_item += avg_item_sold

avg_all_item_sold = round(avg_all_item / len(goods), 2)
print(f"общая сумма продаж: {all_sales}")
print(f"среднее количество продаж всех товаров: {avg_all_item_sold}")



# не понял как избавиться от первого for, я так понимаю должно считаться через sum() в блоке функции, а потом через for подтягиваться, гуглил, но нашел только обращение через разные импорты, я так понимаю тут все проще. Не выкупил, как обратиться к списку внутри словаря, внутри списка)
# def one_product_sales(items_sold):
#   sales_sum = sum(goods['items_sold])
#   return sales_sum

