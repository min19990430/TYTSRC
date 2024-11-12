import sqlite3
import datetime

dbfile = "data.db"

def select_parameter(station,devs):
    var = [0,0,0,0,0]
    sig = [0,0,0,0,0]
    try:
        conn=sqlite3.connect(dbfile,timeout = 30)
        c = conn.cursor()
        select_sql = "SELECT * FROM parameters where station = ? and device = ?"
        cursor = c.execute(select_sql,(station,devs,))
        rows = cursor.fetchall()
        for row in rows:
            var = [float(i) for i in row[3].split(',')]
            sig = [float(i) for i in row[4].split(',')]
        conn.close()
        return [var,sig]
    except Exception as ex:
        print("select_parameter ex = ", ex)
        conn.close()
        return [var,sig]

def insert_history(data):
    try:
        conn = sqlite3.connect(dbfile,timeout = 30)
        c = conn.cursor()
        colums = ','.join(data.keys())
        values = [data[col] for col in data]
        insert_sql = f"INSERT INTO history({colums}) values(?,?,?,?,?,?,?,?,?,?,?,?,?);"
        c.execute(insert_sql,values)
        conn.commit()
        conn.close()
    except Exception as ex:
        print("insert_history ex = ", ex)
        conn.close()

def insert_backup(data):
    try:
        conn = sqlite3.connect(dbfile,timeout = 30)
        c = conn.cursor()
        colums = ','.join(data.keys())
        values = [data[col] for col in data]
        insert_sql = f"INSERT INTO backup({colums}) values(?,?,?,?,?,?,?,?,?,?,?,?,?);"
        c.execute(insert_sql,values)
        conn.commit()
        conn.close()
    except Exception as ex:
        print("insert_backup ex = ", ex)
        conn.close()

        
def select_backup():
    try:
        result = {}
        conn=sqlite3.connect(dbfile,timeout = 30)
        cursor = conn.cursor()
        select_sql = "SELECT * FROM backup order by DateTime"
        cursor.execute(select_sql)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        for row in rows:
            row_dict = {columns[i]: row[i] for i in range(len(columns))}
            result = row_dict         
        conn.close()
        return result
    except Exception as ex:
        print("select_backup ex = ", ex)
        conn.close()
        
def delete_backup(dat):
    try:
        conn=sqlite3.connect(dbfile,timeout = 30)
        c = conn.cursor()
        sql = "DELETE FROM backup where DateTime = ?;"
        c.execute(sql,(dat,))
        conn.commit()
        conn.close()
    except Exception as ex:
        print("delete_backup ex = ", ex)
        conn.close()


def update_real(value,current,station,device,status):
    dt = datetime.datetime.today()
    dat_format = dt.strftime("%Y-%m-%d %H:%M:%S")
    conn=sqlite3.connect(dbfile,timeout = 30)
    c = conn.cursor()
    update_sql = "UPDATE real SET datetime=?,value=?, current=? WHERE station = ? and device=?"
    if status == "err":
        c.execute(update_sql,("Disconnected",value,current,station,device))      
    elif status == "setup":
        c.execute(update_sql,("setup",value,current,station,device))
    else:
        c.execute(update_sql,(dat_format,value,current,station,device))
    conn.commit()
    conn.close()
