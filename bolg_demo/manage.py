# encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from index import app
from models import User, Article, Comment

# 绑定app和db
migrate = Migrate(app, db)
# 初始化对象
manager = Manager(app)
# 添加迁移脚本
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
