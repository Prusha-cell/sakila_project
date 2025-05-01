from connection import conn_write


#Добавление новых запросов в таблицу "запосов" и увеличение счетчика при повторении запросов
def insert_or_update_query(movie_title='', keyword='', genre='', year='', search_type=''):
    connection = conn_write()
    cursor = connection.cursor()

    query = """
        INSERT INTO popular_queries (movie_title, keyword, genre, year, search_type, search_count)
        VALUES (%s, %s, %s, %s, %s, 1)
        ON DUPLICATE KEY UPDATE
            search_count = search_count + 1;
        """
    cursor.execute(query, (movie_title, keyword, genre, year, search_type))
    connection.commit()
    cursor.close()
    connection.close()


# insert_or_update_query(keyword="Magic", search_type="keyword")

# insert_or_update_query(keyword="Magic", genre="Drama", year=1999)


#Вывод самых популярных запросов по типу запроса

def show_popular_queries():
    connection = conn_write()
    cursor = connection.cursor()

    query = """SELECT search_type, count(search_count) cnt
               FROM popular_queries
               GROUP BY search_type
               ORDER BY cnt DESC"""

    cursor.execute(query)
    result = cursor.fetchall()


    cursor.close()
    connection.close()
    return result
