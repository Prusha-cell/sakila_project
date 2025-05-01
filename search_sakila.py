from connection import conn_read


#Поиск названия фильма по ключевому слову
def search_movie_title_by_keyword(keyword, page):
    connection = conn_read()
    cursor = connection.cursor()
    query = """SELECT title
               FROM film
               WHERE title LIKE %s
               LIMIT 10 OFFSET %s"""
    cursor.execute(query, (f"%{keyword}%", page * 10))
    list_titles = list(map(lambda x: x[0], cursor.fetchall()))

    cursor.close()
    connection.close()
    return list_titles


# Поиск по названию всех жанров
def search_by_genre_name():
    connection = conn_read()
    cursor = connection.cursor()
    query_by_genre_name = """SELECT category.name
                             FROM category
                             GROUP BY category.name"""
    cursor.execute(query_by_genre_name)
    list_genre_names = list(map(lambda x: x[0], cursor.fetchall()))

    cursor.close()
    connection.close()
    return list_genre_names


#Поиск по жанру и году
def search_by_genre_year(genre, year, page):
    connection = conn_read()
    cursor = connection.cursor()
    query = """SELECT film.title, category.name, release_year
               FROM film
               INNER JOIN film_category ON film.film_id = film_category.film_id
               INNER JOIN category ON category.category_id = film_category.category_id
               WHERE LOWER(category.name) = LOWER(%s) AND release_year = %s
               LIMIT 10 OFFSET %s;"""

    cursor.execute(query, (genre, year, page * 10))
    list_queries = cursor.fetchall()

    cursor.close()
    connection.close()
    return list_queries


