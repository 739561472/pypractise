# encoding : utf-8

from flask import Flask, render_template, request, session, redirect, url_for
from exts import db
import config
from models import User, Article, Comment
from decorators import login_required


app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/index/')
def index():
    context = {
        'articles': Article.query.order_by('-create_time').all()
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        account = request.form.get('account')
        password = request.form.get('password')
        user = User.query.filter(User.account == account, User.password == password).first()
        if user:
            session['use_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '用户名或密码错误'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        account = request.form.get('account')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 判断
        if User.query.filter(User.account == account).first():
            return '改手机号已被注册，请勿重复注册'
        else:
            if password1 != password2:
                return '两次密码不相等，请核对后再输'
            else:
                user = User(username=username, account=account, password=password2)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/upload/', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        article = Article(title=title, content=content)
        user_id = session.get('use_id')
        article.author = User.query.filter(user_id == user_id).first()
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<article_id>')
def detail(article_id):
    article_detail = Article.query.filter(Article.id == article_id).first()
    return render_template('detail.html', article_detail=article_detail)


@app.route('/add_comment/', methods=['POST'])
@login_required
def add_comment():
    article_id = request.form.get('article_id')
    content = request.form.get('comment_content')
    comment = Comment(content=content)
    user_id = session.get('use_id')
    comment.author = User.query.filter(User.id == user_id).first()
    comment.article = Article.query.filter(Article.id == article_id).first()
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail', article_id=article_id))


if __name__ == '__main__':
    app.run()
