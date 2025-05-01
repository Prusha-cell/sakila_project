from work_with_table_for_record import insert_or_update_query, show_popular_queries
from search_sakila import search_movie_title_by_keyword, search_by_genre_name, search_by_genre_year


#Работа по первому запросу
def search_by_first_request():
    while True:
        keyword = input("\nВведи ключевые слова (латиница и/или цифры, через пробел): ").strip()

        #Oставляем только латиницу без спец символов
        if all(word.isalnum() and word.isascii() for word in keyword.split()):

            # Логируем запрос в таблицу популярных запросов
            insert_or_update_query(keyword=keyword, search_type="keyword")

            #Построчный ввод
            page = 0
            while True:
                results = search_movie_title_by_keyword(keyword, page)

                if not results:
                    if page == 0:
                        print("\nНичего не найдено по этому запросу.")
                        print("-" * 80)
                        break
                    else:
                        exit_or_m_menu = input("\nРезультатов больше нет!"
                                               "\nХотите вернуться в основное меню (y/n)")
                        if exit_or_m_menu == "y":
                            print("-" * 80)
                            return
                        else:
                            print("\nДо свидания!")
                            exit()
                for num, title in enumerate(results, page * 10 + 1):
                    print(f"{num}) {title}")

                if len(results) < 10:
                    exit_or_m_menu = input("\nРезультатов больше нет!"
                                           "\nХотите вернуться в основное меню (y/n): ")
                    if exit_or_m_menu == "y":
                        return
                    else:
                        print("\nДо свидания!")
                        exit()

                next_page = input("\nПоказать следующие 10 результатов? (y/n): ").lower()
                if next_page == "y":
                    page += 1
                else:
                    return
        else:
            print("Ошибка: используй только латинские буквы и/или цифры, без символов.")
            print("-" * 80)

            continue


#Работа по второму запросу
def search_by_second_request():
    while True:
        result_genres = search_by_genre_name()

        genre_dict = {}
        for num, title in enumerate(result_genres, 1):
            genre_dict[num] = title
            print(f"{num}) {title}")

        try:
            genre_num = int(input("Введи номер жанра из списка: ").strip())
            genre_name = genre_dict.get(genre_num)
            if not genre_name:
                print("Ошибка: жанр с таким номером не найден. Попробуй снова.")
                print("-" * 80)
                continue
        except ValueError:
            print("Ошибка: нужно ввести число.")
            continue


        while True:
            year_of_film = input("Введи год от 1900 до 2025: ").strip()
            if not year_of_film.isdigit() or len(year_of_film) != 4 or not (1900 <= int(year_of_film) <= 2025):
                print("Ошибка: можно вводить только года (из четырёх цифр) от 1900 до 2025.")
                continue
            break

        # Логируем запрос
        insert_or_update_query(genre=genre_name, year=year_of_film, search_type="genre_year")

        # Постраничный вывод
        page = 0
        while True:
            result_genres_years = search_by_genre_year(genre_name, year_of_film, page)
            # print(result_genres_years)

            if not result_genres_years:
                if page == 0:
                    print("\nНичего не найдено по этому запросу.")
                    break
                else:
                    exit_or_m_menu = input("\nРезультатов больше нет!\nХотите вернуться в основное меню (y/n): ")
                    if exit_or_m_menu.lower() == "y":
                        return
                    else:
                        print("\nДо свидания!")
                        exit()

            for num, (title, genre, year) in enumerate(result_genres_years, page * 10 + 1):
                print("-" * 80)
                print(f"{num}) Title: {title}\nGenre: {genre}\nYear: {year}")
                print("-" * 80)

            if len(result_genres_years) < 10:
                exit_or_m_menu = input("\nРезультатов больше нет!\nХотите вернуться в основное меню (y/n): ")
                if exit_or_m_menu.lower() == "y":
                    return
                else:
                    print("\nДо свидания!")
                    exit()

            next_page = input("\nПоказать следующие 10 результатов? (y/n): ").lower()
            if next_page == "y":
                page += 1
            else:
                return


#Работаем по третьему запросу
def search_by_third_request():
    top_queries = show_popular_queries()
    if not top_queries:
        print("Пока еще нет ни одного запроса.")
        return

    for num, (search_type, cnt) in enumerate(top_queries, 1):
        print(f"{num}) Search type: {search_type}\n   Amount: {cnt}")

    exit_or_m_menu = input("\nХотите вернуться в основное меню? (y/n): ").lower().strip()
    if exit_or_m_menu == "y":
        return
    else:
        print("\nДо свидания!")
        exit()


def search_by_fourth_request():
    print("До свидания!")
    exit()
