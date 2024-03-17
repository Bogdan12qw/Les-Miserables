import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    
    print("\033[91m +-----------------+")
    print("\033[91m-- Les Miserables --    ")
    print("\033[91m +-----------------+")
    print("")
    print("\033[91m Тг:https://t.me/+CDFiq3vAlSkxNDdi")
    print("")
    print("\033[91mМеню:")
    print("-----")
    print("\033[91m1. Номер")
    print("\033[91m2. DDOS")
    print("\033[91m3. IP")
    print("\033[91m4. Почта")
    print("\033[91m5. Бомбер")
    print("-----")
    print("\033[91m0. Выход")

def run_file(file_num):
    if file_num == 1:
        os.system("python try001.py")
    elif file_num == 2:
        os.system("python try002.py")
    elif file_num == 3:
        os.system("python try003.py")
    elif file_num == 4:
        os.system("python try004.py")
    elif file_num == 5:
        os.system("python try005.py")
    else:
        print("Некорректный выбор.")

def main():
    while True:
        display_menu()
        choice = input("Выберите опцию: ")
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4', '5']:
            run_file(int(choice))
        else:
            print("Некорректные данные. Попробуйте снова.")

if __name__ == "__main__":
    main()