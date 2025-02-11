from mysql_util import MysqlUtil as mysql
from flask import flash
from datetime import datetime

def xinjianthing(neirong,time,leixing,user):
    db=mysql()
    sql="INSERT INTO thingrecord (neirong, time, leixing, user) VALUES ('{}', '{}', '{}', '{}');".format(neirong,time,leixing, user)
    print(sql)
    db.fetchone(sql)
    db=mysql()
    sql="SELECT * FROM thingrecord ORDER BY id DESC LIMIT 1;"
    jg = db.fetchone(sql)
    return str(jg)

def get_system_mysql(nr:str):
    jieguo="从mysql取系统设置的值，非用户事件"
    print(nr=="leixiing")
    if nr=="leixing":
        db=mysql()
        sql="SELECT leixing FROM thingtype order by id"
        jg = db.fetchall(sql)
        jieguo=[i['leixing'] for i in jg]
    return jieguo

def get_mima(user_name:str):
    db = mysql()
    sql = "SELECT mima FROM users WHERE yonghuming='{}';".format(user_name)
    jg = db.fetchone(sql)
    if jg==None:
        return "用户不存在"
    else:
        return jg['mima']

def zhuce(user_name:str, password:str,xingming:str):
    db = mysql()
    sql="select * from users where yonghuming='{}';".format(user_name)
    jg = db.fetchone(sql)
    if jg==None:
        db=mysql()
        sql = "insert into users(yonghuming,mima,nicheng) values('%s','%s','%s')"%(user_name,password,xingming)
        print(sql)
        db.fetchone(sql)
        flash("用户名：%s\n密码：%s\n使用名称：%s"%(user_name, password,xingming))
        return "1"
    else:
        return "-1"

def GetThingsByUser(user_name:str, thing_type="all",kaishitime="2020-01-01",jieshutime="2025-01-01",thingleixing='科研'):
    print(user_name)
    db = mysql()
    if thing_type=='all':
        sql = "SELECT * FROM thingsrecord WHERE is_deleted=0 and id in (select id from thingrecord where user='{}') order by wancheng, time".format(user_name)
    if thing_type=="undone":
        sql = "SELECT * FROM thingsrecord WHERE wancheng=0 and is_deleted=0 and id in (select id from thingrecord where user='{}') order by time".format(user_name)
    print(thing_type,sql)
    jg = db.fetchall(sql)
    if type(jg) == 'str':
        return "0"
    else:
        for i in jg:
            print(i)
        return jg

def GetNichengByUser(user_name:str):
    db = mysql()
    sql = "SELECT nicheng FROM users WHERE yonghuming='{}';".format(user_name)
    jg = db.fetchone(sql)
    if len(jg)==0:
        return "尚未设置用户名"
    else:
        return jg['nicheng']

def ThingExistByid(id):
    db = mysql()
    sql="SELECT EXISTS(SELECT 1 FROM thingrecord WHERE id={} AND is_deleted=0) ".format(id)
    jg=db.fetchone(sql)
    for k,v in jg.items():
        return v
def DeleteThingByid(id):
    if ThingExistByid(id)==1:
        db = mysql()
        sql="DELETE FROM thingrecord WHERE id='{}';".format(id)
        sql="UPDATE thingrecord SET is_deleted = 1 WHERE id = {};".format(id)
        db.update(sql) #update不能用fecthone
        return ThingExistByid(id)==0
    else:
        return -1 #不存在

def DoneThingByid(id,donetag=1,done_time='2025-01-01'):
    db = mysql()
    sql="UPDATE thingrecord SET wancheng = {}, end_time='{}' WHERE id = {};".format(donetag,done_time,id)
    print(sql)
    db.update(sql) #update不能用fecthone
    return 1

def EditThingByid(neirong,time,leixing,endtime,wancheng,id):
    db = mysql()
    sql = "UPDATE thingrecord SET neirong='%s', time='%s', leixing='%s', end_time='%s', wancheng='%s' WHERE id = %s" % (neirong,time,leixing,endtime,wancheng,id)
    print(sql)
    db.update(sql)  # update不能用fecthone
    return "修改成功"

if __name__ == '__main__':
    print(DeleteThingByid(22))
