from flask import render_template
from config import app

class HomeController(object):

    #Функция, которая загружает страницу
    @staticmethod
    @app.route('/')#маршрут к странице
    def index():#статический тут сайт, по-єтому нет self
        """Метод для загрузки шаблона главной страницы"""
        return render_template('home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        """Метод для загрузки шаблона страницы Про сайт"""
        return render_template('home/about.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        """Метод для загрузки шаблона страницы Контактов"""
        return render_template('home/contact.html')