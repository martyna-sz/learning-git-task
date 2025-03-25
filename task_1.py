shopping_list = {
"piekarnia" : ["chleb", "pączek", "bułki"],
"warzywniak" : ["marchew", "seler", "rukola"]
}
for shop, products in shopping_list.items():
    print(f"Idę do {shop} i kupuję tam {products}")

capitalized_letters = {shop.capitalize(): [product.capitalize() for product in products]
                        for shop, products in shopping_list.items()}
print(capitalized_letters)
for shop, products in capitalized_letters.items():
    print(f"{shop}: {products}")

all_products = sum(len(products) for products in shopping_list.values())
print(f"W sumie kupuję {all_products} produktów")

print("Hello")

for i in range (1,100):
    if i % 5 == 0:
        print(i, end=" ")