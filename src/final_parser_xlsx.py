import os
import subprocess
import json
import pandas as pd


def generate_demo_data():
    brands = ["Gloria Jeans", "Colin's", "Ostin", "Mango", "Zarina", "Incotex", "befree"]
    items = []
    for i in range(25):
        brand = brands[i % len(brands)]
        price = 3500 + (i * 317) % 7000
        rating = round(4.0 + (i % 6) * 0.1, 1)
        items.append(
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
    return items


def filter_items(items, min_rating=4.5, max_price=10000, country="Россия"):
    return [
        item
        for item in items
        if item["rating"] >= min_rating
        and item["price"] <= max_price
        and item["country"] == country
    ]


def save_to_xlsx(data, filename):
    pd.DataFrame(data).to_excel(filename, index=False, engine="openpyxl")


def main():
    items = generate_demo_data()
    save_to_xlsx(items, "полный_каталог_пальто.xlsx")
    save_to_xlsx(filter_items(items), "отфильтрованный_каталог.xlsx")
    for file in ("полный_каталог_пальто.xlsx", "отфильтрованный_каталог.xlsx"):
        if os.path.exists(file):
            subprocess.Popen(["start", "", file], shell=True)


if __name__ == "__main__":
    main()
