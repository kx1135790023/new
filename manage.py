from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db,create_app
import sys
import os
sys.path.append("./")
app = create_app("development")
# Flask-script
manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)
print(app.url_map)



if __name__ == '__main__':
    manager.run()