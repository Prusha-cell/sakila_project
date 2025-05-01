from main_menu_numbering import (
    search_by_first_request,
    search_by_second_request,
    search_by_third_request,
    search_by_fourth_request,
)


def main():
    print("\nПривет, смертный ;-) Ты на тестовой проге 'KINOFINDER'.\n")

    while True:
        print("----------------------MAIN MENU-----------------------\n")
        print("1. Поиск фильма по ключевому слову\n"
              "2. Поиск фильма по жанру и году\n"
              "3. Показать топ популярных запросов по типу\n"
              "4. Выход")
        try:
            choose = int(input("\nВведи цифру из меню: "))
            if choose == 1:
                search_by_first_request()
            elif choose == 2:
                search_by_second_request()
            elif choose == 3:
                search_by_third_request()
            elif choose == 4:
                search_by_fourth_request()
                break
            else:
                print("Ошибка: введена цифра вне диапазона 1–4. Попробуй снова.")
        except ValueError:
            print("Ошибка: нужно ввести цифру из меню, а не текст или символы.")
            continue


if __name__ == "__main__":
    main()
