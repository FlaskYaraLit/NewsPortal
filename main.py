from config import app
from views.home_controller import HomeController
from views.news_controller import NewsController
from views.users_controller import UsersController

if __name__ == '__main__':
    hc = HomeController() #так мы запускаем "слушателя". -> hc - неважное название
    nc = NewsController()
    uc = UsersController()
    app.run(debug=True) # debug=True включает отладчик
