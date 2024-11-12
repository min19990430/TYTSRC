from pyModbusTCP.client import ModbusClient
import time
import threading
import pytz
from datetime import datetime
#-----------------------
import sensor
import correction
import sqlite_use
import postdata


all_device = ['A_pH', 'A_Temp', 'A_Level', 'B_pH', 'B_Temp', 'B_Level', 'C_pH', 'C_Temp', 'C_Level', 'D_pH', 'D_Temp', 'D_Level']

original_value = {device: 0 for device in all_device}
correction_value = {device: 0 for device in all_device}
device_status = {device: 'setup' for device in all_device}

# modbus tcp client
read_temp_client = ModbusClient(host="192.168.100.48", port=502, unit_id=1,timeout=3)    
read_level_client = ModbusClient(host="192.168.100.48", port=502, unit_id=1,timeout=3)   

# 溫度感測器接在資料搜集器ET-7015，此流程為透過 modbus tcp 讀取數值。
def read_ET7015():
    err_count = 6 #連線失敗次數倒數，當為0時判斷為斷線
    while True:
        time.sleep(5)
        try:
            if not read_temp_client.is_open:
                if not read_temp_client.open():
                    if err_count == 0:
                        #print(f"connect {read_temp_client.host} error")
                        original_value['A_Temp'] = 0
                        original_value['B_Temp'] = 0
                        original_value['C_Temp'] = 0
                        original_value['D_Temp'] = 0
                        device_status['A_Temp'] = 'err'
                        device_status['B_Temp'] = 'err'
                        device_status['C_Temp'] = 'err'
                        device_status['D_Temp'] = 'err'
                    else:
                        err_count -=1
                        #print('et7015 err count = ',err_count)
            else:
                c = read_temp_client.read_input_registers(0,10)
                if c is not None:
                    original_value['A_Temp'] = c[0]
                    original_value['B_Temp'] = c[1]
                    original_value['C_Temp'] = c[2]
                    original_value['D_Temp'] = c[3]
                    device_status['A_Temp'] = 'ok'
                    device_status['B_Temp'] = 'ok'
                    device_status['C_Temp'] = 'ok'
                    device_status['D_Temp'] = 'ok'
                    err_count = 6
        except Exception as ex:
            print("read_ET7015 ex = ", ex)

# 液位感測器接在資料搜集器ET-7017，此流程為透過 modbus tcp 讀取數值。
def read_ET7017():
    err_count = 6 #連線失敗次數倒數，當為0時判斷為斷線
    while True:
        time.sleep(5)
        try:
            if not read_level_client.is_open:
                if not read_level_client.open():
                    if err_count == 0:
                        #print(f"connect {read_level_client.host} error")
                        original_value['A_Level'] = 0
                        original_value['B_Level'] = 0
                        original_value['C_Level'] = 0
                        original_value['D_Level'] = 0
                        device_status['A_Level'] = 'err'
                        device_status['B_Level'] = 'err'
                        device_status['C_Level'] = 'err'
                        device_status['D_Level'] = 'err'
                    else:
                        err_count -=1
                        #print('et7015 err count = ',err_count)
            else:
                c = read_level_client.read_input_registers(0,10)
                if c is not None:
                    original_value['A_Level'] = c[0]
                    original_value['B_Level'] = c[1]
                    original_value['C_Level'] = c[2]
                    original_value['D_Level'] = c[3]
                    device_status['A_Level'] = 'ok'
                    device_status['B_Level'] = 'ok'
                    device_status['C_Level'] = 'ok'
                    device_status['D_Level'] = 'ok'
                    err_count = 6
        except Exception as ex:
            print("read_ET7017 ex = ", ex)

# pH 感測器 接在FCC上，此流程為透過 modnus rtu 讀取數值。
def read_rs485():
    station = ['A','B','C','D'] 
    ph_id = [2,3,4,5] #pH感測器的RS485 ID
    ph_err_count = [6,6,6,6] #連線失敗次數倒數，當為0時判斷為斷線
    while True:
        try:
            for i in range(4):
                dt = datetime.today()
                dat_format = dt.strftime("%Y-%m-%d %H:%M:%S")
                _id =  ph_id[i]
                s = station[i]
                key = f'{s}_pH'
                ph = sensor.read_ph(_id)
                if ph[0] != 'err':
                    original_value[key] = ph[1]
                    device_status[key] = 'ok'
                    ph_err_count[i] = 6
                else:
                    if ph_err_count[i] == 0:
                        original_value[key] = 0
                        device_status[key] = 'err'
                    else:
                        ph_err_count[i] -=1
                        #print(f'{dat_format} {key} count = {ph_err_count[i]}')
                time.sleep(1)
        except Exception as ex:
            print("read_rs485 ex = ", ex)
                
        
# 將數值進行5點校正
def calculate():
    try:
        station = ['A','B','C','D']
        for s in station:
            # 讀取資料庫內的5點參數
            pH_PM = sqlite_use.select_parameter(s,"pH") 
            Temp_PM = sqlite_use.select_parameter(s,"Temp")
            Level_PM = sqlite_use.select_parameter(s,"Level")
            # 感測器原始數值
            ph_ma = original_value[f'{s}_pH']
            temp_ma = original_value[f'{s}_Temp']
            level_ma = original_value[f'{s}_Level']
            # 感測器狀態
            ph_st = device_status[f'{s}_pH']
            temp_st = device_status[f'{s}_Temp']
            level_st = device_status[f'{s}_Level']
            # 感測器進行校正
            ph = round(correction.corr(ph_ma, pH_PM[0], pH_PM[1]), 2)   
            temp = round(correction.corr(temp_ma, Temp_PM[0], Temp_PM[1]), 1)
            level = round(correction.corr(level_ma, Level_PM[0], Level_PM[1]), 1) 
            correction_value[f'{s}_pH'] = ph
            correction_value[f'{s}_Temp'] = temp
            correction_value[f'{s}_Level'] = level
            # 將校正後的值寫入資料庫
            sqlite_use.update_real(str(ph),str(ph_ma),s,"pH",ph_st)  
            sqlite_use.update_real(str(temp),str(temp_ma),s,"Temp",temp_st)            
            sqlite_use.update_real(str(level),str(level_ma),s,"Level",level_st)     
    except Exception as ex:
        print("calculate ex = ", ex)
        
# 主流程
def thread_master():
    setup = False
    last_minute = 0
    while True:
        time.sleep(1)
        dtime = datetime.today()
        dt_m = int(dtime.strftime("%M"))
        dt_s = int(dtime.strftime("%S"))
        dat_format = dtime.strftime("%Y-%m-%d %H:%M:00")
        
        timezone = pytz.timezone('Asia/Taipei')
        dt = timezone.localize(dtime)
        formatted_time = dt.isoformat()
        
        if dt_s%2 == 0:
            calculate() #進行校正
            bak_data = sqlite_use.select_backup() #搜尋是否有資料需要回補
            print(bak_data)
            if not bak_data:
                pass
                print("bak_data = ",bak_data)
            else:
                bak_time = bak_data["DateTime"]
                post_st = postdata.send(bak_time,bak_data) #上傳回補的資料
                if post_st == "ok":
                    sqlite_use.delete_backup(bak_data["DateTime"])#刪除回補的資料             
            
        if last_minute != dt_m:
            last_minute = dt_m
            if setup:
                db_data = correction_value
                db_data["DateTime"] = formatted_time#dat_format
                sqlite_use.insert_history(db_data)#寫入歷史資料
                post_st = postdata.send(formatted_time,correction_value) #上傳資料
                if post_st != "ok": #上傳失敗，寫入一份資料到備份
                    sqlite_use.insert_backup(db_data)     
            else:
                setup = True


t1 = threading.Thread(target=read_ET7015)
t2 = threading.Thread(target=read_rs485)
t3 = threading.Thread(target=read_ET7017)

t1.start()
t2.start()
t3.start()

t4 = threading.Thread(target=thread_master)
time.sleep(10)
t4.start()