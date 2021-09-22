from config import mysql
# новость

class Article(object):

    @staticmethod
    def add_article(title, about, content, image, publish, user_id, status) -> None:
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаём курсор
        sql_query = """
                    insert into news (title, about, content, image, publish, user_id, status)
                    values (%s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(sql_query, (title, about, content, image, publish, user_id, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all_articles() -> list:
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаём курсор
        sql_query = """
            select * from news
        """
        cursor.execute(sql_query)
        # connection.commit() не нужно комитить, т.к. мі ничего не изменили в базе
        result = cursor.fetchall()  # вместо этого мы берём из базы данные
        cursor.close()
        connection.close()
        return result
