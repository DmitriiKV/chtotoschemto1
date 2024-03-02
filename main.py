from flask import Flask, render_template, redirect
from data import db_session
from data.user import User
from data.news import News
import datetime as dt
from forms.user import RegisterForms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekret_key_aaaaaaa'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForms()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("register.html", title="Registration", form=form, message="PAROL NE SOVPADAJET!!!")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template("register.html", title="Registration", form=form, message="TAKOJ EMEJL UZHE ISPOLZUJETCA!!!")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.check_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template("register.html", title="Registration", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/successfull')
    return render_template('login.html', title='Autorization', form=form)



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
