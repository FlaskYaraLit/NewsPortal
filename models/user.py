from config import mysql
# новость
from werkzeug.security import check_password_hash

class User(object):

    @staticmethod
    def register(login, password, email, regdate, status) -> None: # self отсутствует, т.к. статический метод
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаём курсор
        sql_query = """
            insert into users (login, password, email, regdate, status)
            values (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_query, (login, password, email, regdate, status))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def auth(login, password) -> bool:
        connection = mysql.get_db()
        cursor = connection.cursor()  # создаём курсор
        sql_query = """
            select login, password from users where login=%s
        """
        cursor.execute(sql_query, (login, ))
        result = cursor.fetchall() # fetchall - то Выбрать всё
        k = len(result) # result список кортежей (тип данных)

        cursor.close()
        connection.close()

        if k == 0:
            return False
        else:
            return check_password_hash(result[0][1], password)




