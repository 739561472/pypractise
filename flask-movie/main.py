import os
from flask import Flask, render_template
from home.views import home as home_blueprint
from admin.views import admin as admin_blueprint
from exts import db, app
import config


app.config.from_object(config)
app.config["SECRET_KEY"] = '071d32979f144e4ba19aa5cdaf71466b'
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
with app.app_context():
    db.init_app(app)
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404


if __name__ == '__main__':
    app.run()
