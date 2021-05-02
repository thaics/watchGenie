import pymysql
from pymysql import cursors
from pymysql.cursors import DictCursor

def connect():
    try:
        connect = pymysql.connect(
        user = 'root', password = 'password', host = 'localhost', database = 'movieGenie',
        )
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        return connect, cursor
    except:
        print('Could not connect to database')
        return None

