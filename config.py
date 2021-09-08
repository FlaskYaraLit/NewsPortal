from flask import Flask
from flaskext.mysql import MySQL

#созда'м ссілку на приложение
app = Flask(__name__)
#Для безопасности. Если заблокирован аккаунт на хостинге, то провайдер спросит Секретный ключ
#для разблокировки нашего сайтана хостинге.
#http://www.md5.cz/ тут простое слово преобразуется в сложный длинный текст, но по жесткому алгоритму
#из itstep123 будет:d917274a73d200ab842c70309624f5ba
#Конфигурируем наше приложение
app.config['SECRET_KEY'] = 'd917274a73d200ab842c70309624f5ba'
#АВТОЗАГРУЗКА ШАБЛОНОВ САЙТА
app.config['TEMPLATES_AUTO_RELOAD'] = True


app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='root'
app.config['MYSQL_DATABASE_DB'] = 'newsportal_db'

mysql = MySQL()
mysql.init_app(app)