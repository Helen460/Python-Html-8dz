#Консольний застосунок "База даних магазину продуктів"
import os 

products = []

def load_from_file():
    global products
    try:
        if os.path.exists('products.txt'):
            with open('products.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    product_data = line.strip().split(', ')
                    products.append([product_data[0], product_data[1], float(product_data[2]), int(product_data[3])])
    except Exception as e:
        print("Помилка при завантаженні даних з файлу:", e)

def save_to_file():
    try:
        with open('products.txt', 'w', encoding='utf-8') as f:
            for product in products:
                f.write(', '.join(map(str, product)) + '\n')
        print("База даних збережена у файл.")
    except Exception as e:
        print("Помилка при збереженні даних у файл:", e)

def add_product():
    name = input("Введіть назву продукту: ")
    category = input("Введіть категорію продукту: ")
    
    while True:
        try:
            price = float(input("Введіть ціну продукту: "))
            break
        except ValueError:
            print("Помилка! Ціна повинна бути числом.")
    
    while True:
        try:
            quantity = int(input("Введіть кількість на складі: "))
            break
        except ValueError:
            print("Помилка! Кількість повинна бути цілим числом.")
    
    products.append([name, category, price, quantity])
    print("Продукт", name, "додано в базу даних.")

def view_products():
    if len(products) == 0:
        print("База даних порожня.")
    else:
        print("\nСписок продуктів:")
        print("{:<20}{:<20}{:<10}{:}".format("Назва", "Категорія", "Ціна", "Кількість"))
        print('-' * 60)
        for product in products:
            print("{:<20}{:<20}{:<10.2f}{:}".format(product[0], product[1], product[2], product[3]))

def find_product():
    name = input("Введіть назву продукту для пошуку: ")
    found = False
    for product in products:
        if product[0].lower() == name.lower():
            print("\nЗнайдений продукт:")
            print("{:<20}{:<20}{:<10}{:}".format("Назва", "Категорія", "Ціна", "Кількість"))
            print('-' * 60)
            print("{:<20}{:<20}{:<10.2f}{:}".format(product[0], product[1], product[2], product[3]))
            found = True
            break
    if not found:
        print("Продукт", name, "не знайдено.")

def delete_product():
    name = input("Введіть назву продукту для видалення: ")
    global products
    products = [product for product in products if product[0].lower() != name.lower()]
    print("Продукт", name, "видалено з бази даних.")

def update_product():
    name = input("Введіть назву продукту для оновлення: ")
    for product in products:
        if product[0].lower() == name.lower():
            print("\nОберіть, що ви хочете змінити для продукту", name, ":")
            print("1. Ціна")
            print("2. Кількість на складі")
            choice = input("Ваш вибір: ")
            
            if choice == "1":
                while True:
                    try:
                        new_price = float(input("Введіть нову ціну: "))
                        product[2] = new_price
                        print("Ціна продукту", name, "оновлена.")
                        break
                    except ValueError:
                        print("Помилка! Ціна повинна бути числом.")
            elif choice == "2":
                while True:
                    try:
                        new_quantity = int(input("Введіть нову кількість на складі: "))
                        product[3] = new_quantity
                        print("Кількість продукту", name, "оновлена.")
                        break
                    except ValueError:
                        print("Помилка! Кількість повинна бути цілим числом.")
            else:
                print("Невірний вибір.")
            break
    else:
        print("Продукт", name, "не знайдено.")

def menu():
    while True:
        print("\nМеню:")
        print("1. Переглянути всі продукти")
        print("2. Додати новий продукт")
        print("3. Знайти продукт за назвою")
        print("4. Видалити продукт")
        print("5. Оновити продукт")
        print("6. Зберегти базу даних у файл")
        print("7. Вийти з програми")
        
        choice = input("Оберіть дію: ")
        
        if choice == "1":
            view_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            find_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            update_product()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            save_to_file()
            print("Завершення роботи програми...")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def main():
    load_from_file()
    menu()

if __name__ == "__main__":
    main()