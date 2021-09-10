from config import mysql
# новость

class User(object):

    @staticmethod
    def register() -> None: # self отсутствует, т.к. статический метод
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаём курсор
        sql_query = """
            insert into users (login, password, email, regdate, status)
            values (%s, #%s, %s, %s)
        """
        cursor.execute(sql_query, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def login() -> None:
        pass