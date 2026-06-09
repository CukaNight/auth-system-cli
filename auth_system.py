import json
import os 
from getpass import getpass

USERS_FILE = "users.json"

def load_user():
    if os.path.exists(USERS_FILE):
        with open('users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            return(data)
    else:
        return[]
    
def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4, ensure_ascii=False)

def  register():
    users = load_user()

    username = input("Логин - ")
    def is_username_taken(username, users):
        for user in users:
            if user["username"] == username:
                return True
        return False
    
    if is_username_taken(username, users):
        print("❌ Логин занят, придумайте другой.")
        return
    else:
        pass
    
    password = getpass("Придумайте пароль - ")
    check_password = getpass("Подтвердите пароль - ")

    if users:
        next_id = max(user["id"] for user in users) +1
    else:
        next_id = 1

    if password != check_password:
        print("❌ Пароли не совпадают!")
        return
    else:
        new_user = {"id": next_id, "username": username, "password": password}

    users.append(new_user)
    save_users(users)
    print("✅ Регистрация завершена теперь вы можете войти в аккаунт!")

def login():
    users = load_user()

    if not users:
        print("❌ Нет зарегистрированных пользователей. Сначала зарегистрируйтесь.")
        return False

    login = input("Логин: ")
    password = getpass("Пароль: ")

    for user in users:
        if user["username"] == login and user["password"] == password:
            print(f"✅ Добро пожаловать, {login}!")
            return True
        
    print("❌ Неверный логин или пароль.")
    return False

def main():
    while True:
        print("\n📋 Меню:")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        try:
            choice = int(input("Твой выбор: "))
        except ValueError:
            print("Ошибка! Введи число.")
            continue

        if choice == 1:
            register()
        elif choice == 2:
            if login():
                print("Доступ в систему разрешён.")
                break
        elif choice == 3:
            print("Выход.")
            break
        else:
            print("Выберите пункт от 1 до 3!")

if __name__ == "__main__":
    main()