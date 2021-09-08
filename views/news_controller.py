from flask import render_template
from config import app

class NewsController(object):

    #Функция, которая загружает страницу
    @staticmethod
    @app.route('/news/create')#маршрут к странице
    def create():#статический тут сайт, по-єтому нет self
        return render_template('news/create.html')

    @staticmethod
    @app.route('/news/delete')
    def delete():
         return render_template('news/delete.html')

    @staticmethod
    @app.route('/news/details')
    def details():
        return render_template('news/details.html')

    @staticmethod
    @app.route('/news/list')
    def list():
        return render_template('news/list.html')

    @staticmethod
    @app.route('/news/update')
    def update():
         return render_template('news/update.html')