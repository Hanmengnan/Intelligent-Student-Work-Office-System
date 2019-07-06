import sqlite3
import pymysql
from settings import *

current_id = 0

def NewestVisitor():

    global current_id

    db = pymysql.connect(
        host="192.168.1.100",
        user="root",
        password="admin",
        database="test-zzx")
    cursor = db.cursor()
    sql = 'select MAX(id) from record'
    cursor.execute(sql)
    MaxID = cursor.fetchone()[0]
    # 获取最新的一条数据
    current_id = MaxID
    if current_id != 0:
        sql = 'select * from record order by id desc limit {offset};'.format(
            offset=MaxID - current_id)
        cursor.execute(sql)
        Visitors = cursor.fetchall()
    for index in range(len(Visitors)):
        Visitors[2] = Visitors[2].strftime("%Y-%m-%d %H:%M:%S")
    cursor.close()
    db.close()
    return Visitors


def UpdateLocalRecord(remoteRecord):
    '''
    :param remoteRecord: 服务器查询到的新数据
    :return:
    '''
    database = DATABASE_SQLITE_PATH
    db = sqlite3.connect(database=database)   # 链接本地数据库
    cursor = db.cursor()
    for oneRecord in remoteRecord:
        # 插入数据
        sql = f"insert into record (sno,name,st_time) values ('{oneRecord[0]}','{oneRecord[1]}','{oneRecord[2]}')"
        cursor.execute(sql)
    db.commit()


def ChangePage(index):
    list = []
    database = DATABASE_SQLITE_PATH
    f = open("./temp/grade.txt", "r")
    g = f.read()
    grade = g[-2:]
    print(grade)
    db = sqlite3.connect(database=database)
    cursor = db.cursor()
    if grade == "全部":
        sql = f'select * from record where st_name!="" ORDER BY rowid desc limit {(index - 1) * 12},{index * 12}'
    else:
        grade = grade
        print(grade)
        sql = f'select * from record where st_name!="" and sno like "%s%%" ORDER BY rowid desc limit {(index - 1) * 12},{index * 12}'%grade
        print(sql)
    cursor.execute(sql)
    print("1111")
    list = cursor.fetchall()
    cursor.close()
    db.close()
    print(list)
    return list


def DataCount():
    database = DATABASE_SQLITE_PATH
    db = sqlite3.connect(database=database)
    cursor = db.cursor()
    sql = f'select MAX(rowid) from record'
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return int(result[0])


def Detail(id):
    data = []
    database = DATABASE_SQLITE_PATH
    if id != "":
        db = sqlite3.connect(database=database)
        cursor = db.cursor()
        sql = f'select * from tt where sno={id}'
        cursor.execute(sql)

        it_result = cursor.fetchone()
        if (it_result):
            data = {"xy": it_result[0],
                    "nj": it_result[1],
                    "bj": it_result[2],
                    "xh": it_result[3],
                    "xm": it_result[4],
                    "xb": it_result[5],
                    "jg": it_result[6],
                    "mz": it_result[7],
                    "xz": it_result[8],
                    "dh": it_result[12],
                    "jzdh": it_result[13],
                    "ssl": it_result[14],
                    "ss": it_result[15].replace('\n',
                                                ''),
                    "sf": it_result[16],
                    "dz": it_result[17],
                    "js": DATABSE_TEACHER[it_result[1]]}
    return data


def GetPhoto(id):
    database = DATABASE_SQLITE_PATH
    db = sqlite3.connect(database=database)
    cursor = db.cursor()
    sql = f'select * from ncut_face where StudentId={id}'
    cursor.execute(sql)
    photo = cursor.fetchone()
    cursor.close()
    db.close()
    if photo is not None and photo[4] is not None:
        with open("./temp/photo.jpg", 'wb') as file:
            file.write(bytearray.fromhex(photo[4]))
        return True
    return False
