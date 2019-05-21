from flask import Flask
import pymysql

app = Flask(__name__)
current_id=0

@app.route('/')
def visitor():
    global current_id
    db = pymysql.connect(host="10.5.102.59", user="root", password="admin", database="test-zzx")
    # if(current_id==None):
    #     current_id=00
    teacher={"2015":"李伟、杨乾振","2016":"靳现凯","2017":"刘霁炜","2018":"杨和佳"}
    cursor = db.cursor()
    sql_max_id = 'select MAX(id) from record'
    cursor.execute(sql_max_id)
    max_id = cursor.fetchone()[0]
    #获取最新的一条数据
    cursor.close()
    cursor=db.cursor()
    result=[]
    # sql = 'CREATE TRIGGER test_tri AFTER INSERT ON record FOR EACH ROWSET select * from record order by orderfield desc/asc limit {current_id},{offset};'.format(
    #     offset=max_id - current_id,current_id=current_id)1
    # 抽取上次记录id到现在id的数量
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
            print(it_result)
            if(it_result):

                data={"xy":it_result[0],"nj":it_result[1],"bj":it_result[2],"xh":it_result[3],"xm":it_result[4],"xb":it_result[5],"jg":it_result[6],"mz":it_result[7],"xz":it_result[8],"ss":it_result[9].replace('\n',''),"sf":it_result[10],"dz":it_result[11],"js":teacher[it_result[1]]}
                result.append(data)
        # print(max_id[0]-current_id)
        current_id=max_id
        db.close()
    return result


if __name__ == '__main__':
    app.run(host='10.5.102.59',debug=True)