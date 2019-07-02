import pymysql
from crawlers import Fixture
import datetime

def connectdb():
    print("connecting to Mysql")
    db = pymysql.connect('localhost', 'root', 'root', 'PB')
    print("successfully connected")
    return db


def closedb(db):
    db.close()


def insertdb(db, gamesInfo):
    cursor = db.cursor()
    sql="INSERT INTO game(team,round, date, time, venue, address, opposition) VALUES (%s, %s, %s,%s, %s, %s,%s)"
    param=[]
    for ele in gamesInfo:
        param.append([ele.get_team(), ele.get_rnd(), ele.get_date(), ele.get_time(), ele.get_venue(), ele.get_address(), ele.get_opposition()])
    try:
        cursor.executemany(sql, param)
        db.commit()
        print("insert successfully!")
    except Exception:
        print("fail to insert data!")
        print(Exception)
        db.rollback()

