import datetime
import uuid
from flask import Flask,render_template,url_for,request,redirect,jsonify,session
from flask_login import login_user,LoginManager,current_user,logout_user
from flask_sessionstore import Session
from flask_wtf import Form ,CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlalchemy.engine import Engine
from sqlalchemy import event,create_engine,or_,desc
from flask_bootstrap import Bootstrap  #flask-bootstrap dosen't install bootstrap-flask then import flask-bootstrap bcs bootstrap-flask is that flask-bootstrap itself.
from flask_login import UserMixin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_moment import Moment # a library to convert utctime to localtime

app=Flask(__name__, template_folder='static')
app.config['SECRET_KEY']='thisi'
app.config['WTF_CSRF_SECRET_KEY']='wtffdjfk'

login_manager=LoginManager()
login_manager.init_app(app)
#or login_manager=LoginManager(app)
Bootstrap(app)
db = SQLAlchemy(app)
csrf=CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///combs.db'
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'
app.config['SESSION_SQLALCHEMY'] = db
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if type(dbapi_connection) is sqlite3.Connection:  # play well with other DB backends
       cursor = dbapi_connection.cursor()
       cursor.execute("PRAGMA foreign_keys=ON")
       cursor.close()

# app.register_blueprint(user, url_prefix='/user')
admin=Admin(app,name='My App',template_mode='bootstrap3')
engine=create_engine('sqlite:///combs.db')
Session(app)
moment=Moment(app)


# Optimizing twitts functions



#end Optimizing twitts functions



if __name__=='__main__':
    app.run(debug='True')