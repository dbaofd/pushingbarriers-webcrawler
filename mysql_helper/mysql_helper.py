import pymysql
import datetime

def connect_db():
    print("connecting to Mysql")
    db = pymysql.connect('localhost', 'root', 'root', 'PB')#uqANDpushingbarriers911@
    print("successfully connected")
    return db


def close_db(db):
    db.close()


def insert_db(db, gamesInfo):
    cursor = db.cursor()
    sql="INSERT INTO game(game_team,game_round, game_date, game_time, game_venue, game_address, game_opposition, game_team_id) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)"
    param=[]
    for ele in gamesInfo:
        param.append([ele.get_team(), ele.get_rnd(), ele.get_date(), ele.get_time(), ele.get_venue(), ele.get_address(), ele.get_opposition(), ele.get_team_id()])
    try:
        cursor.executemany(sql, param)
        db.commit()
        print("insert successfully!")
    except Exception as e:
        print("fail to insert data!")
        print(e)
        db.rollback()

def truncate_db(db):
    cursor=db.cursor()
    sql="TRUNCATE TABLE game"
    try:
        cursor.execute(sql)
        db.commit()
        print("truncate successfully!")
    except Exception as e:
        print("fail to truncate data!")
        print(e)
        db.rollback()

def set_update_time(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM gameupdatetime")
    today = datetime.datetime.now();
    if(len(cursor.fetchall())==0):
        sql="INSERT INTO gameupdatetime(gameupdatetime_date) VALUE (%s)"
        try:
            cursor.execute(sql,today)
            db.commit()
            print("Insert updatetime successfully!")
        except Exception as e:
            print("fail to insert updatetime!")
            print(e)
            db.rollback()
    else:
        sql="UPDATE gameupdatetime SET gameupdatetime_date = '%s' WHERE gameupdatetime_id = %d"%(datetime.datetime.strftime(today, "%Y/%m/%d"),1)
        try:
            cursor.execute(sql)
            db.commit()
            print("update updatetime successfully!")
        except Exception as e:
            print("fail to update updatetime!")
            print(e)
            db.rollback()