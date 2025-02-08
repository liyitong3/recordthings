from flask import Flask, request, render_template,flash,session,send_file,url_for
from hanshu import *
from json import dumps

app = Flask(__name__)
app.secret_key="lyt"

@app.route("/ajax")
def ajax():
    return render_template("ajax_tools.html")
@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico")

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def hello_world():
    #return render_template("base/xinjianthing.html", leixiing=things_type)
    things_type = get_system_mysql("leixing")
    print(things_type)
    if len(session) == 0 or session['status'] != 1:
        return render_template("zhuye_nologin.html",leixing=things_type)
    else:
        return render_template('zhuye.html',leixing=things_type)

@app.route('/zhuce', methods=['GET', 'POST'])
def zhucezhanghao():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        biaodan = request.get_json()
        print(biaodan)
        user_name = biaodan["username"]
        password = biaodan["password"]
        xingming = biaodan["xm"]
        return zhuce(user_name,password,xingming)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'status' not in session or ('status' not in session and session['status'] == 0):
            return render_template('login.html')
        elif 'status' in session and session['status'] == 1:
            flash(session["user"]+" 已登录")
        return render_template('login.html')
    else:
        biaodan=request.get_json()
        print(biaodan)
        user_name = biaodan["username"]
        password = biaodan["password"]
        pwd_server = get_mima(user_name)
        print(user_name,password,pwd_server,pwd_server=="用户不存在")
        if 'status' in session and session['status'] == 1:
            return "2"
        if pwd_server=="用户不存在":
            flash("用户不存在\n请检查用户名，确认无误后重新登陆。")
            return "0"
        if pwd_server == password:
            session['status']=1
            session['user']=user_name
            return "1"
        else:
            flash("密码错误\n请检查密码，确认无误后重新登陆。")
            return "-1"

@app.route('/zhuxiao',methods=['GET', 'POST'])
def zhuxiao():
    if 'status' not in session or ('status' not in session and session['status']==0):
        flash("请先登陆")
    else:
        session['status']=0
        flash(session["user"]+" 注销成功")
    return render_template("zhuxiao.html")

@app.route("/xinjianjishi", methods=['POST','GET'])
def xinjian_thing():
    if request.method == 'GET':
        things_type=get_system_mysql("leixing")
        print(things_type)
        return render_template("xinjianjishi.html", leixing=things_type)
    else:
        print(session['status'])
        if len(session)==0 or session['status']!=1:
            return "请先登录"
        else:
            neirong=request.form.get("neirong")
            shijian=request.form.get("time")
            leixing=request.form.get("leixing")
            user=session['user']
            return xinjianthing(neirong,shijian,leixing,user)

@app.route("/bianjineirong", methods=['POST','GET'])
def bianjineirong():
    if request.method == 'GET':
        things_type=get_system_mysql("leixing")
        id=request.args.get('id')
        if id==None:
            return "祝你生日快乐"
        db=mysql()
        sql="SELECT * FROM thingsrecord WHERE id='{}';".format(id)
        jg=db.fetchone(sql)
        print(jg)
        return render_template("base/bianjineirong.html", leixing=things_type, yuanxianneirong=jg)
    else:
        nr=request.form.get("neirong")
        time=request.form.get("time")
        leixing=request.form.get("leixing")
        endtime=request.form.get("end_time")
        wancheng=request.form.get("wancheng")
        id=request.form.get("id")
        print(nr,time,leixing,endtime,wancheng,id)
        return EditThingByid(nr,time,leixing,endtime,wancheng,id)

@app.route("/sql/get_things_list", methods=['POST','GET'])
def get_things_list():
    if request.method == 'GET':
        return "祝你生日快乐吧"
    else:
        user_name=request.form.get("yonghuming")
        print(user_name) #结果是'liyitong'，下面需要把单引号去掉
        sjfw=request.form.get("shujufanwei")
        if sjfw=="tiaojian":
            kaishitime=request.form.get("kaishishijian")
            jieshutime=request.form.get("jieshushijian")
            thingleixing=request.form.get("thingleixing")
            jieguo = GetThingsByUser(user_name.replace("'", ""), sjfw,kaishitime,jieshutime,thingleixing)
        else:
            jieguo=GetThingsByUser(user_name.replace("'",""),sjfw)
        shujuchangdu=len(jieguo)
        jg={
              "code": 0,
              "msg": "当前待处理业务列表",
              "count": shujuchangdu,
              "data": jieguo
            }
        return dumps(jg)
@app.route("/sql/delete_id", methods=['POST','GET'])
def delete_id(): #删除事件，根据事件id号
    if request.method == 'GET':
        return "李一桐真漂亮"
    else:
        id=request.form.get("id")
        if DeleteThingByid(id)==1:
            return "删除成功"
        else:
            return "没有这个事件或者无权限处理该id"

@app.route("/sql/done_id", methods=['POST','GET'])
def done_id(): #删除事件，根据事件id号
    if request.method == 'GET':
        return "李一桐真漂亮"
    else:
        id=request.form.get("id");
        donetag=request.form.get("donetag")
        # 获取当前的日期和时间
        now = datetime.now()
        # 格式化日期和时间
        formatted_now = now.strftime('%Y-%m-%d')
        print(donetag)
        if DoneThingByid(id,donetag,formatted_now)==1:
            return ("已标记完成" if donetag==1 or donetag=="1" else "已标记未完成")
        else:
            return "没有这个事件或者无权限处理该id"

@app.route("/ceshi/<web_filename>",methods=['GET'])
def ceshiweb(web_filename):
    return render_template(web_filename+".html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
