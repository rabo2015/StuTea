# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#只有在app对象之后声明，用于导入model否则无法创建表#
##from blog.model import User,Category

#只有在app对象之后声明，用于导入view模块
from blog.controller import blog_manage
#创建项目对象
app = Flask(__name__)

#import os
#print os.environ.keys()
#print os.environ.get('FLASK_SETTINGS')


#加载配置文件内容
app.config.from_object('blog.setting')  #模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASK_SETTINGS') #环境变量，指向配置文件setting的路径

#创建数据库对象
db=SQLALchemy(app)

