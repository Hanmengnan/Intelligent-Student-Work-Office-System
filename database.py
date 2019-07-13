import sqlite3
import pymysql
from settings import *

current_id = 0

def NewestVisitor():
    """
    检查主数据库有无新数据插入
    :return:
    """
    global current_id #上一次记录的最新的rowid
    db = pymysql.connect(
        host="192.168.1.100",
        user="root",
        password="admin",
        database="test-zzx")#主数据库连接配置
    cursor = db.cursor()
    sql = 'select MAX(id) from record'
    cursor.execute(sql)
    MaxID = cursor.fetchone()[0]# 获取最新的一条数据
    if current_id != 0:
        sql = 'select * from record order by id desc limit {offset};'.format(
            offset=MaxID - current_id)
        cursor.execute(sql)
        Visitors = cursor.fetchall()
        Visitors = list(Visitors)
        for index in range(len(Visitors)):
            if Visitors[index][2]!="":
                Visitors[index]=list(Visitors[index])
                Visitors[index][4] = Visitors[index][4].strftime("%Y-%m-%d %H:%M:%S")#将时间格式改为字符串

        cursor.close()
    current_id = MaxID#更新最新的rowid
    db.close()
    return Visitors


def UpdateLocalRecord(remoteRecord):
    '''
    将著数据库的新数据插入到sqlite数据库
    :param remoteRecord: 服务器查询到的新数据
    :return:
    '''
    DataBase = DATABASE_SQLITE_PATH
    db = sqlite3.connect(database=DataBase)   # 链接本地数据库
    cursor = db.cursor()
    for oneRecord in remoteRecord:
        # 插入数据
        sql = f"insert into record (sno,st_name,st_time) values ('{oneRecord[1]}','{oneRecord[2]}','{oneRecord[4]}')"
        cursor.execute(sql)
    db.commit()#insert语句必须


def ChangePage(index):
    """
    翻页时，sqlite数据库配合操作
    :param index:
    :return:
    """
    list = []
    DataBase = DATABASE_SQLITE_PATH
    file = open("./temp/grade.txt", "r")
    g = file.read()
    grade = g[-2:]#年级信息
    db = sqlite3.connect(database=DataBase)
    cursor = db.cursor()
    if grade == "全部":
        sql = f'select * from record where st_name!="" ORDER BY rowid desc limit {(index - 1) * RECORD_ROWNUM},{index * RECORD_ROWNUM}'
    else:
        sql = f'select * from record where st_name!="" and sno like "%s%%" ORDER BY rowid desc limit {(index - 1) * 12},{index * 12}'%grade
    cursor.execute(sql)
    list = cursor.fetchall()
    cursor.close()
    db.close()
    return list


def DataCount():
    """
    查询数据总数，用于计算页数
    :return:
    """
    file = open("./temp/grade.txt" , "r")
    g = file.read()
    grade = g[-2:]  # 年级信息

    DataBase = DATABASE_SQLITE_PATH
    db = sqlite3.connect(database=DataBase)
    cursor = db.cursor()

    if grade == "全部":
        sql = f'select * from record'
    else:
        sql = f'select * from record where st_name!="" and sno like "%s%%"' % grade
    cursor.execute(sql)
    result = len(cursor.fetchall())
    cursor.close()
    db.close()
    return int(result)#result为元组


def Detail(id):
    """
    显示学生详细信息
    :param id:
    :return:
    """
    data = {}
    DataBase = DATABASE_SQLITE_PATH
    if id != "":
        db = sqlite3.connect(database=DataBase)
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
    """
    显示学生照片
    :param id:
    :return:
    """
    DataBase = DATABASE_SQLITE_PATH
    db = sqlite3.connect(database=DataBase)
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
