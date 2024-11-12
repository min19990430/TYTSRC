
import requests

HEADERS = {'Content-Type': 'application/json',"Accept":'*/*'}
#HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;'}
server = "http://118.163.66.142:27001"
datas = {"device_uuid": "b68eb407-9e33-48fb-aadf-a8e5de411583","di": ""}
all_device = ['A_pH', 'A_Temp', 'A_Level', 'B_pH', 'B_Temp', 'B_Level', 'C_pH', 'C_Temp', 'C_Level', 'D_pH', 'D_Temp', 'D_Level']

def send(tim,data):
    try:
        values = [data[key] for key in all_device]
        datas["ai"] = values
        datas["datetime"] = tim
        r = requests.post(server+"/api/v1/Catch/Signal", headers=HEADERS,json = [datas],timeout=5)
        ok = r.status_code
        if ok == 200:
            return "ok"
        else:
            return "err"
    except Exception as ex:
        print(ex)
        return "err"