import sqlite3
import os

DB_PATH = ('./database.db')

PRODUCTS = [
    {"name": "яблоко", "price": 33.7, "description": "яблоко сочное, Голден", "category": "фрукты", "img": "https://static.vecteezy.com/system/resources/previews/047/309/519/non_2x/green-apple-isolated-on-transparent-free-png.png"},
    {"name": "банан", "price": 89.9, "description": "бананы спелые, Эквадор", "category": "фрукты", "img": "https://static.vecteezy.com/system/resources/thumbnails/019/876/139/small/banana-fruit-isolated-on-white-background-free-photo.jpg"},
    {"name": "апельсин", "price": 120.5, "description": "апельсины сладкие, Марокко", "category": "фрукты", "img": "https://static.vecteezy.com/system/resources/previews/023/875/688/non_2x/orange-fruit-isolated-on-white-background-free-photo.jpg"},
    {"name": "груша", "price": 149.0, "description": "груши сочные, конференц", "category": "фрукты", "img": "https://static.vecteezy.com/system/resources/previews/027/628/020/non_2x/pear-isolated-on-white-background-free-photo.jpg"},
    {"name": "виноград", "price": 299.0, "description": "виноград кишмиш, без косточек", "category": "фрукты", "img": "https://static.vecteezy.com/system/resources/previews/027/628/025/non_2x/grapes-isolated-on-white-background-free-photo.jpg"},
    {"name": "киви", "price": 89.0, "description": "киви спелый, Новая Зеландия", "category": "фрукты", "img": "https://static.vecteezy.com/system/resources/previews/027/628/035/non_2x/kiwi-fruit-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "болгарские перцы", "price": 88.9, "description": "красные болгарские перцы", "category": "овощи", "img": "https://metropolis-online.ru/upload/iblock/0f0/xb5cgpn01l93pd1058aah2x1vkmls4op.png"},
    {"name": "помидоры", "price": 159.0, "description": "помидоры черри, тепличные", "category": "овощи", "img": "https://static.vecteezy.com/system/resources/previews/027/628/002/non_2x/tomatoes-isolated-on-white-background-free-photo.jpg"},
    {"name": "огурцы", "price": 99.9, "description": "огурцы свежие, грунтовые", "category": "овощи", "img": "https://static.vecteezy.com/system/resources/previews/027/628/015/non_2x/cucumbers-isolated-on-white-background-free-photo.jpg"},
    {"name": "картофель", "price": 45.0, "description": "картофель мытый, сорт Гала", "category": "овощи", "img": "https://static.vecteezy.com/system/resources/previews/027/628/040/non_2x/potatoes-isolated-on-white-background-free-photo.jpg"},
    {"name": "морковь", "price": 39.9, "description": "морковь молодая, пучок", "category": "овощи", "img": "https://static.vecteezy.com/system/resources/previews/027/628/050/non_2x/carrots-isolated-on-white-background-free-photo.jpg"},
    {"name": "лук репчатый", "price": 35.0, "description": "лук репчатый, желтый", "category": "овощи", "img": "https://static.vecteezy.com/system/resources/previews/027/628/060/non_2x/onion-isolated-on-white-background-free-photo.jpg"},
    {"name": "капуста", "price": 59.0, "description": "капуста белокочанная, свежая", "category": "овощи", "img": "https://static.vecteezy.com/system/resources/previews/027/628/070/non_2x/cabbage-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "куриное филе", "price": 299.0, "description": "филе куриной грудки, охлаждённое", "category": "мясо", "img": "https://static.vecteezy.com/system/resources/previews/027/628/045/non_2x/chicken-breast-isolated-on-white-background-free-photo.jpg"},
    {"name": "говяжий фарш", "price": 450.0, "description": "фарш из говядины, свежий", "category": "мясо", "img": "https://static.vecteezy.com/system/resources/previews/027/628/030/non_2x/ground-beef-isolated-on-white-background-free-photo.jpg"},
    {"name": "свиная шейка", "price": 399.0, "description": "шейка свиная, охлаждённая", "category": "мясо", "img": "https://static.vecteezy.com/system/resources/previews/027/628/075/non_2x/pork-meat-isolated-on-white-background-free-photo.jpg"},
    {"name": "куриные крылья", "price": 189.0, "description": "крылья куриные, охлаждённые", "category": "мясо", "img": "https://static.vecteezy.com/system/resources/previews/027/628/080/non_2x/chicken-wings-isolated-on-white-background-free-photo.jpg"},
    {"name": "индейка филе", "price": 549.0, "description": "филе индейки, диетическое", "category": "мясо", "img": "https://static.vecteezy.com/system/resources/previews/027/628/085/non_2x/turkey-meat-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "лосось филе", "price": 899.0, "description": "филе лосося, охлаждённое", "category": "рыба", "img": "https://static.vecteezy.com/system/resources/previews/027/628/090/non_2x/salmon-fillet-isolated-on-white-background-free-photo.jpg"},
    {"name": "минтай", "price": 249.0, "description": "минтай замороженный, тушка", "category": "рыба", "img": "https://static.vecteezy.com/system/resources/previews/027/628/095/non_2x/fish-isolated-on-white-background-free-photo.jpg"},
    {"name": "креветки", "price": 699.0, "description": "креветки тигровые, замороженные", "category": "рыба", "img": "https://static.vecteezy.com/system/resources/previews/027/628/100/non_2x/shrimps-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "молоко", "price": 79.9, "description": "молоко 2.5%, 1 литр", "category": "молочные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/055/non_2x/milk-bottle-isolated-on-white-background-free-photo.jpg"},
    {"name": "сыр российский", "price": 599.0, "description": "сыр твёрдый, 45% жирности", "category": "молочные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/065/non_2x/cheese-isolated-on-white-background-free-photo.jpg"},
    {"name": "творог", "price": 89.0, "description": "творог 5%, 200 г", "category": "молочные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/105/non_2x/cottage-cheese-isolated-on-white-background-free-photo.jpg"},
    {"name": "сметана", "price": 69.0, "description": "сметана 15%, 300 г", "category": "молочные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/110/non_2x/sour-cream-isolated-on-white-background-free-photo.jpg"},
    {"name": "кефир", "price": 59.0, "description": "кефир 2.5%, 1 литр", "category": "молочные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/115/non_2x/kefir-isolated-on-white-background-free-photo.jpg"},
    {"name": "йогурт", "price": 45.0, "description": "йогурт натуральный, 125 г", "category": "молочные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/120/non_2x/yogurt-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "яйца С1", "price": 89.0, "description": "яйца куриные, категория С1, 10 шт", "category": "яйца", "img": "https://static.vecteezy.com/system/resources/previews/027/628/125/non_2x/eggs-isolated-on-white-background-free-photo.jpg"},
    {"name": "яйца отборные", "price": 119.0, "description": "яйца куриные, отборные, 10 шт", "category": "яйца", "img": "https://static.vecteezy.com/system/resources/previews/027/628/130/non_2x/eggs-carton-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "хлеб белый", "price": 45.0, "description": "хлеб пшеничный, нарезка", "category": "хлеб", "img": "https://static.vecteezy.com/system/resources/previews/027/628/135/non_2x/white-bread-isolated-on-white-background-free-photo.jpg"},
    {"name": "хлеб чёрный", "price": 55.0, "description": "хлеб ржаной, бородинский", "category": "хлеб", "img": "https://static.vecteezy.com/system/resources/previews/027/628/140/non_2x/rye-bread-isolated-on-white-background-free-photo.jpg"},
    {"name": "батон", "price": 39.0, "description": "батон нарезной, свежий", "category": "хлеб", "img": "https://static.vecteezy.com/system/resources/previews/027/628/145/non_2x/baguette-isolated-on-white-background-free-photo.jpg"},
    {"name": "булочки", "price": 29.0, "description": "булочки сдобные, 4 шт", "category": "хлеб", "img": "https://static.vecteezy.com/system/resources/previews/027/628/150/non_2x/buns-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "рис", "price": 89.0, "description": "рис длиннозёрный, 1 кг", "category": "крупы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/155/non_2x/rice-isolated-on-white-background-free-photo.jpg"},
    {"name": "гречка", "price": 79.0, "description": "гречневая крупа, 1 кг", "category": "крупы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/160/non_2x/buckwheat-isolated-on-white-background-free-photo.jpg"},
    {"name": "овсянка", "price": 59.0, "description": "овсяные хлопья, 500 г", "category": "крупы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/165/non_2x/oatmeal-isolated-on-white-background-free-photo.jpg"},
    {"name": "макароны", "price": 69.0, "description": "макароны из твёрдых сортов, 450 г", "category": "крупы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/170/non_2x/pasta-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "тушёнка", "price": 149.0, "description": "говядина тушёная, 338 г", "category": "консервы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/175/non_2x/canned-meat-isolated-on-white-background-free-photo.jpg"},
    {"name": "горошек", "price": 49.0, "description": "горошек зелёный, 400 г", "category": "консервы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/180/non_2x/canned-peas-isolated-on-white-background-free-photo.jpg"},
    {"name": "кукуруза", "price": 55.0, "description": "кукуруза сладкая, 400 г", "category": "консервы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/185/non_2x/canned-corn-isolated-on-white-background-free-photo.jpg"},
    {"name": "тунец", "price": 129.0, "description": "тунец в собственном соку, 185 г", "category": "консервы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/190/non_2x/canned-tuna-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "кетчуп", "price": 89.0, "description": "кетчуп томатный, 300 г", "category": "соусы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/195/non_2x/ketchup-isolated-on-white-background-free-photo.jpg"},
    {"name": "майонез", "price": 79.0, "description": "майонез провансаль, 250 г", "category": "соусы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/200/non_2x/mayonnaise-isolated-on-white-background-free-photo.jpg"},
    {"name": "соевый соус", "price": 119.0, "description": "соус соевый, 200 мл", "category": "соусы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/205/non_2x/soy-sauce-isolated-on-white-background-free-photo.jpg"},
    {"name": "соль", "price": 25.0, "description": "соль поваренная, 1 кг", "category": "соусы", "img": "https://static.vecteezy.com/system/resources/previews/027/628/210/non_2x/salt-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "вода минеральная", "price": 49.0, "description": "вода газированная, 1 л", "category": "напитки", "img": "https://static.vecteezy.com/system/resources/previews/027/628/215/non_2x/water-bottle-isolated-on-white-background-free-photo.jpg"},
    {"name": "сок апельсиновый", "price": 89.0, "description": "сок прямого отжима, 1 л", "category": "напитки", "img": "https://static.vecteezy.com/system/resources/previews/027/628/220/non_2x/orange-juice-isolated-on-white-background-free-photo.jpg"},
    {"name": "чай чёрный", "price": 149.0, "description": "чай листовой, 100 г", "category": "напитки", "img": "https://static.vecteezy.com/system/resources/previews/027/628/225/non_2x/black-tea-isolated-on-white-background-free-photo.jpg"},
    {"name": "кофе молотый", "price": 299.0, "description": "кофе арабика, 250 г", "category": "напитки", "img": "https://static.vecteezy.com/system/resources/previews/027/628/230/non_2x/coffee-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "шоколад молочный", "price": 69.0, "description": "шоколад молочный, 100 г", "category": "сладости", "img": "https://static.vecteezy.com/system/resources/previews/027/628/235/non_2x/chocolate-isolated-on-white-background-free-photo.jpg"},
    {"name": "печенье", "price": 59.0, "description": "печенье песочное, 300 г", "category": "сладости", "img": "https://static.vecteezy.com/system/resources/previews/027/628/240/non_2x/cookies-isolated-on-white-background-free-photo.jpg"},
    {"name": "мармелад", "price": 79.0, "description": "мармелад фруктовый, 250 г", "category": "сладости", "img": "https://static.vecteezy.com/system/resources/previews/027/628/245/non_2x/marmalade-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "чипсы", "price": 89.0, "description": "чипсы картофельные, 150 г", "category": "снеки", "img": "https://static.vecteezy.com/system/resources/previews/027/628/250/non_2x/chips-isolated-on-white-background-free-photo.jpg"},
    {"name": "сухарики", "price": 39.0, "description": "сухарики ржаные, 80 г", "category": "снеки", "img": "https://static.vecteezy.com/system/resources/previews/027/628/255/non_2x/crackers-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "пельмени", "price": 199.0, "description": "пельмени домашние, 900 г", "category": "замороженные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/260/non_2x/dumplings-isolated-on-white-background-free-photo.jpg"},
    {"name": "овощная смесь", "price": 129.0, "description": "смесь овощей, 400 г", "category": "замороженные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/265/non_2x/frozen-vegetables-isolated-on-white-background-free-photo.jpg"},
    {"name": "мороженое", "price": 89.0, "description": "мороженое пломбир, 400 г", "category": "замороженные", "img": "https://static.vecteezy.com/system/resources/previews/027/628/270/non_2x/ice-cream-isolated-on-white-background-free-photo.jpg"},
    
    {"name": "масло сливочное", "price": 129.0, "description": "масло 82.5%, 180 г", "category": "масло", "img": "https://static.vecteezy.com/system/resources/previews/027/628/275/non_2x/butter-isolated-on-white-background-free-photo.jpg"},
    {"name": "масло подсолнечное", "price": 89.0, "description": "масло рафинированное, 1 л", "category": "масло", "img": "https://static.vecteezy.com/system/resources/previews/027/628/280/non_2x/sunflower-oil-isolated-on-white-background-free-photo.jpg"},
]


def init_db(DB_PATH):

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS product(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            category TEXT NOT NULL,
            img TEXT
        )
    """)

    for product in PRODUCTS:
        cur.execute("""
            INSERT INTO product (name, price, description, category, img)
            VALUES (?, ?, ?, ?, ?)
        """, (
            product ["name"],
            product ["price"],
            product ["description"],
            product ["category"],
            product ["img"],
        ))

    con.commit()

    cur.execute("SELECT COUNT(*) FROM product")
    count = cur.fetchone()[0]
    print(f"+: {DB_PATH}")
    print(f"add product: {count}")

    con.close()
    return count

if __name__ == "__main__":
    init_db(DB_PATH)