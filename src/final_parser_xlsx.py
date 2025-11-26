import requests
import pandas as pd
import json
from datetime import datetime


def generate_demo_data():
    demo_items = []
    brands = ["Gloria Jeans", "Colin's", "Ostin", "Mango", "Zarina", "Incotex", "befree"]
    for i in range(25):
        brand = brands[i % len(brands)]
        price = 3500 + (i * 317) % 7000
        rating = round(4.0 + (i % 6) * 0.1, 1)
        demo_items.append(
            {
                "product_url": f"https://www.wildberries.ru/catalog/{10000000 + i}/detail.aspx",
                "article": 10000000 + i,
                "name": f"Пальто шерстяное {brand} классическое {i + 1}",
                "price": price,
                "description": "Шерстяное пальто, тёплое, стильное",
                "image_urls": "https://img1.wbstatic.net/1.jpg,https://img1.wbstatic.net/2.jpg",
                "characteristics": json.dumps({"состав": "80 % шерсть"}),
                "seller_name": brand,
                "seller_url": f"https://www.wildberries.ru/seller/{1000 + i}",
                "sizes": "S,M,L,XL",
                "quantity": 10 + i,
                "rating": rating,
                "feedbacks": 10 + i * 2,
                "country": "Россия",
            }
        )
    return demo_items


def filter_items(items, min_rating=4.5, max_price=10000, country="Россия"):
    return [
        item
        for item in items
        if item["rating"] >= min_rating
        and item["price"] <= max_price
        and item["country"] == country
    ]


def save_to_xlsx(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False, engine="openpyxl")


def main():
    print("=" * 60)
    print("ПАРСЕР WILDBERRIES ДЛЯ ТЕСТОВОГО ЗАДАНИЯ")
    print("=" * 60)

    items = generate_demo_data()
    print(f"Создано {len(items)} демонстрационных товаров")

    save_to_xlsx(items, "полный_каталог_пальто.xlsx")
    print('Файл сохранен: полный_каталог_пальто.xlsx')

    filtered = filter_items(items)
    save_to_xlsx(filtered, "отфильтрованный_каталог.xlsx")
    print(f'Файл сохранен: отфильтрованный_каталог.xlsx, товаров: {len(filtered)}')

    with open("README.txt", "w", encoding="utf-8") as f:
        f.write("Файлы созданы автоматически\n")
    print("Создан файл README.txt")
    print("=" * 60)


if __name__ == "__main__":
    main()