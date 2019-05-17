import pymysql
from settings import *
def visitor():
    global current_id
    db = pymysql.connect(host=DATABASE_IP, user=DATABASE_USER, password=DATABASE_PASSWORD, database=DATABASE_DB)
    cursor = db.cursor()
    sql_max_id = 'select MAX(id) from record'
    cursor.execute(sql_max_id)
    max_id = cursor.fetchone()[0]
    #获取最新的一条数据
    cursor.close()
    cursor=db.cursor()
    result=[]
    if current_id==0:
        current_id=max_id
    else:
        sql='select * from record order by id desc limit {offset};'.format(offset=max_id-current_id)
        cursor.execute(sql)
        tm=cursor.fetchall()
        for item in tm:
            xh=item[1]
            sql=f'select * from tt where xh={xh}'
            cursor.execute(sql)
            it_result=cursor.fetchone()
            if(it_result):
                data={"xy":it_result[0],"nj":it_result[1],"bj":it_result[2],"xh":it_result[3],"xm":it_result[4],"xb":it_result[5],"jg":it_result[6],"mz":it_result[7],"xz":it_result[8],"ss":it_result[9].replace('\n',''),"sf":it_result[10],"dz":it_result[11]}
                result.append(data)
        current_id=max_id
        db.close()
    return result
