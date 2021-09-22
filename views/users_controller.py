from flask import render_template, request, session, make_response
# session - это словарь, в который пользователь сможет что-то записать
# и эта сессия будет храниться
from werkzeug.security import generate_password_hash
from time import strftime
from config import app
from models.user import User


class UsersController(object):

    #Функция, которая загружает страницу
    @staticmethod
    @app.route('/users/admin')#маршрут к странице
    def admin():#статический тут сайт, по-єтому нет self
        return render_template('users/admin.html')

    @staticmethod
    @app.route('/users/logout')
    def logout():
        session.pop('user', None) # \удалить из сессии пользователя. Функция Flask
        return render_template('users/logout.html')

    @staticmethod
    @app.route('/users/profile')
    def profile():
        return render_template('users/profile.html')

    @staticmethod
    @app.route('/users/register', methods=['GET', 'POST'])
    def register():
        # получение данных из формы ввода пароля и сохранение юзера в базе Данных
        if request.method == 'GET':
            return render_template('users/register.html')
        elif request.method == 'POST':
            message = 'Регистрация провалена'
            mess_color = 'red'

            login = request.form.get('login')
            pass1 = request.form.get('pass1')
            pass2 = request.form.get('pass2')
            email = request.form.get('email')

            password = generate_password_hash(pass1)
            regdate = strftime('%Y-%m-%d %H:%M:%S') # или %H:%i:$s
            status = 'new_user'
            User.register(login, password, email, regdate, status)

            message = 'Вы успешно зарегистрированы! Регистрация успешно завершена.'
            mess_color = 'green'
            return render_template('users/register_info.html', context={
                'message': message,
                'mess_color': mess_color
            }) # Транзитный словарь КОНТЕКСТ

    @staticmethod
    @app.route('/users/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('users/login.html')
        elif request.method == 'POST':
            message = 'Авторизация провалена'
            mess_color = 'red'

            login = request.form.get('login')
            pass1 = request.form.get('pass1')
            rem = request.form.get('rem') #rem - remember запомнить пользователя.  Оставаться в системе Чекбокс

            if User.auth(login, pass1): # функция проверяет, подош'л ли пароль
                session['user'] = login # регистраиция пользователя в сессии (в куки файле)
                if rem == 'yes':
                    response = make_response('setting cookie user')
                    response.set_cookie('user', login, max_age=7*24*3600) #7 дней пользователь будет сохраняться в системе
                message = 'Вы успешно авторизованы!'
                mess_color = 'green'
            else:
                message = 'Пользователь не найден!'
                mess_color = 'red'

            return render_template('users/login_info.html', context={
                'message': message,
                'mess_color': mess_color
            })  # Транзитный словарь КОНТЕКСТ