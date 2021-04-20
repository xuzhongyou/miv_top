import pymysql
import datetime
'''
Insert example:
    Server_id=0
    GPU_id=0
    P_id=1345
    U_name="hxk"
    G_mem=23
    Cpu=56
    Mem=70
    Submit_time = datetime.datetime.now()
    End_time = datetime.datetime.now()
    Running_time = End_time - Submit_time
    Command = 'python test.py'
    sql = f"INSERT INTO resource_tb(Server_id,GPU_id,P_id,U_name,G_mem,Cpu,Mem,Submit_time,End_time,Running_time,Command) VALUES ({Server_id},{GPU_id},{P_id},'{U_name}',{G_mem},{Cpu},{Mem},'{Submit_time.strftime('%Y-%m-%d %H:%M:%S')}','{End_time.strftime('%Y-%m-%d %H:%M:%S')}',{Running_time.total_seconds()},'{Command}' )"
    print(f'running time: {Running_time.total_seconds()}')
    print(sql)
    db = db_connection()
    insert_table(sql,db)
'''


def db_connection(host='49.52.10.156',port=3306,user='xzy',
                    passwd='',db='miv_top',charset='utf8'):
    db = pymysql.connect(
         host=host,
         port=port,
         user=user,
         passwd=passwd,
         db =db,
         charset=charset)
    return db

def insert_table(sql,db):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print('Error: Insert error!')
    finally:
        cursor.close()
        db.close()

