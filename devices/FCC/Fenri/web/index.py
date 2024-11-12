import os
from flask import Flask,render_template,request
import sqlite3
import time
import socket
import json
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#db = "/home/pi/Fenri/data.db"
db = "../data.db"

def get_local_ip():
    local_ip = ""
    try:
        socket_objs = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
        ip_from_ip_port = [(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in socket_objs][0][1]
        ip_from_host_name = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
        local_ip = [l for l in (ip_from_ip_port, ip_from_host_name) if l][0]
    except (Exception) as e:
        print("get_local_ip found exception : %s" % e)
    return local_ip if("" != local_ip and None != local_ip) else socket.gethostbyname(socket.gethostname())

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def index2():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/parameter')
def parameter():
    return render_template('parameter.html')

@app.route('/parameter_api', methods = ['GET'])
def parameter_api():
    station = request.args.get('station')
    device = request.args.get('device')
    if station == None:
        station = "A"
    if device == None:
        device = "pH"
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    c = con.cursor()
    select_sql = "SELECT * FROM parameters where station= ? and device = ?"
    cursor = c.execute(select_sql,(station,device,))
    rows = cursor.fetchall()
    for row in rows:
        var = [float(i) for i in row[3].split(',')]
        sig = [float(i) for i in row[4].split(',')]
    con.close()

    return json.dumps({"station":station,"device":device,"variable":var,"signal":sig})
    #return render_template("parameter.html",rows=[var,sig])

def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False
    return True
  
@app.route('/parameter_update')
def parameter_update():
    station = request.args.get('station')
    device = request.args.get('device')
    var = request.args.get('val')
    sig = request.args.get('sig')
    conn=sqlite3.connect(db)
    c = conn.cursor()
    update_sql = "UPDATE parameters SET variable=?, signal=? WHERE station=?and device = ?"
    c.execute(update_sql,(var,sig,station,device))
    conn.commit()
    conn.close()
    return "修改 "+station+" 成功"

@app.route('/real')
def real():
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    c = con.cursor()
    c.execute("SELECT * FROM real order by id")
    data = {'A':{},'B':{},'C':{},'D':{}}
    for row in c:
        station = row["station"]
        datetime = row["datetime"]
        device = row["device"]
        value = row["value"]
        current = row["current"]
        data[station][device] = {'value':value,'current':current,'datetime':datetime}
    return json.dumps(data)

@app.route('/history', methods = ['GET'])
def history():
    datetime = request.args.get('datetime')
    if datetime == None:
        datetime = time.strftime("%Y-%m-%d", time.localtime()) 
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    c = con.cursor()
    select_sql = "SELECT * FROM history where DateTime between ? and ? order by DateTime desc"
    c.execute(select_sql,(datetime+" 00:00:00",datetime+" 23:59:59"))
    rows = c.fetchall()
    return render_template("history.html",rows=rows)

@app.route('/hisapi', methods = ['GET'])
def hisapi():
    dat1 = request.args.get('dat1')
    dat2 = request.args.get('dat2')
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row
    c = con.cursor()
    select_sql = "SELECT * FROM history where DateTime between ? and ? order by DateTime desc"
    c.execute(select_sql,(dat1,dat2))
    datas = []
    for row in c:
        data = {}
        data["DateTime"] = row["DateTime"]
        data["pH"] = row["pH"]
        data["EC"] = row["EC"]
        data["Temp"] = row["Temp"]
        data["hour"] = row["Flow_hour"]
        data["total"] = row["Flow_total"]
        datas.append(data)

    return json.dumps(datas)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=1234)
