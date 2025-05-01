from search_sakila import search_movie_title_by_keyword  #search_by_genre_year
from work_with_table_for_record import insert_or_update_query, show_popular_queries
from main_menu_numbering import search_by_first_request, search_by_second_request, search_by_third_request, search_by_fourth_request


def main():
    print("\nПривет смертный ;-) Ты на тестовой проге 'KINOFINDER'.\n")

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

            if choose == 2:
                search_by_second_request()

            if choose == 3:
                search_by_third_request()

            if choose == 4:
                search_by_fourth_request()
        except ValueError as e:
            print(e, "Ошибка: нужно ввести цифру из меню")
            continue









if __name__ == "__main__":
    main()
