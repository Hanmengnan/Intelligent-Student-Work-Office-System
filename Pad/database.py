from flask import Flask
import pymysql

app = Flask(__name__)
current_id=0

def visitor():
    global current_id
    db = pymysql.connect(host="192.168.1.100", user="root", password="admin", database="test-zzx")
    teacher={"2015":"李伟、杨乾振","2016":"靳现凯","2017":"刘霁炜","2018":"杨和佳"}
    cursor = db.cursor()
    sql_max_id = 'select MAX(id) from record'
    cursor.execute(sql_max_id)
    max_id = cursor.fetchone()[0]
    #获取最新的一条数据
    cursor.close()
    cursor=db.cursor()
    result=[]
    # 抽取上次记录id到现在id的数量
    if current_id==0:
        current_id=max_id
    else:
        sql='select * from record order by id desc limit {offset};'.format(offset=max_id-current_id)
        cursor.execute(sql)
        tm=cursor.fetchall()
        for item in tm:
            xh=item[1]
            time=item[2]
            sql=f'select * from tt where 学号={xh}'
            cursor.execute(sql)
            it_result=cursor.fetchone()
            if(it_result):
                data={"time":time,"xy":it_result[0],"nj":it_result[1],"bj":it_result[2],"xh":it_result[3],"xm":it_result[4],"xb":it_result[5],"jg":it_result[6],"mz":it_result[7],"xz":it_result[8],"dh":it_result[9],"jzdh":it_result[10],"ssl":it_result[11],"ss":it_result[12].replace('\n',''),"sf":it_result[13],"dz":it_result[14],"js":teacher[it_result[1]]}
                result.append(data)
        current_id=max_id
        db.close()
    return result

def tableVisitor():
    db = pymysql.connect(host="192.168.1.100", user="root", password="admin", database="test-zzx")
    teacher = {"2015": "李伟、杨cursor = db.cursor()乾振", "2016": "靳现凯", "2017": "刘霁炜", "2018": "杨和佳"}
    cursor = db.cursor()
    sql_list = 'select * from record'
    cursor.execute(sql_list)
    list = cursor.fetchone()
    cursor.close()
    return list
def change_page(index):
    db = pymysql.connect(host="192.168.1.100", user="root", password="admin", database="test-zzx")
    cursor = db.cursor()
    sql = f'select * from record ORDER BY ID desc limit {(index-1)*12},{index*12}'
    cursor.execute(sql)
    list = cursor.fetchall()
    f=open("./grade.txt","r")
    g=f.read()
    grade=g[-2:]
    for item in list:
        nj=item[1][:2]
        if grade=="全部"or nj ==grade:
            pass
        else:
            list.pop(item)
    cursor.close()
    print()
    return list
def dataCount():
    db = pymysql.connect(host="192.168.1.100", user="root", password="admin", database="test-zzx")
    cursor = db.cursor()
    sql = f'select * from record'
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return len(result)


def detail(id):
    global current_id
    db = pymysql.connect(host="192.168.1.100", user="root", password="admin", database="test-zzx")
    teacher = {"2015": "李伟、杨乾振", "2016": "靳现凯", "2017": "刘霁炜", "2018": "杨和佳"}
    cursor = db.cursor()

    sql = f'select * from tt where 学号={id}'
    cursor.execute(sql)
    it_result = cursor.fetchone()
    if (it_result):
        data = { "xy": it_result[0], "nj": it_result[1], "bj": it_result[2],
                "xh": it_result[3], "xm": it_result[4], "xb": it_result[5], "jg": it_result[6],
                "mz": it_result[7], "xz": it_result[8], "dh": it_result[9], "jzdh": it_result[10],
                "ssl": it_result[11], "ss": it_result[12].replace('\n', ''), "sf": it_result[13],
                "dz": it_result[14], "js": teacher[it_result[1]]}
    db.close()
    return data