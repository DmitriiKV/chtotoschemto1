from flask import Flask, render_template
from data import db_session
from data.user import User
from data.news import News
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekret_key_aaaaaaa'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


def main():
    db_session.global_init("db/blog_db.sqlite")
    # # user = User()
    # # user.name = 'Gennadij'
    # # user.about = 'about Gennadij'
    # # user.email = 'gennadij@gennadij.com'
    # db_sess = db_session.create_session()
    # # db_sess.add(user)
    # # user = db_sess.query(User)
    # # for user in db_sess.query(User).all():
    # #     print(user.name)
    # # db_sess.commit()
    # #
    # # db_sess = db_session.create_session()
    # # user = db_sess.query(User).filter(User.id == 1).first()
    # # print(user.name)
    # # user.name = 'user name new'
    # # user.created_data = dt.datetime.now()
    # # db_sess.commit()
    # # db_sess.query(User).filter(User.id >= 3).delete()
    # # db_sess.commit()
    #

    # user = db_sess.query(User).filter(User.id == 3).first()
    # news = News(title='Pervaja zapis', content='mnogo mnogo mnogo texta slova bukvi aaaaaaaaaaa', user=user,
    #             is_private=False)
    # user.news.append(news)
    # db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
