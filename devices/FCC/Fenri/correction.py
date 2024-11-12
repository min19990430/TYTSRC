import math

#判斷原始數值落在校正5點的位置後，取2點並計算
def corr(ai,b,c):
    re_data = 0
    variable = b
    signal = c
    if (ai < signal[0] or ai < signal[1]) and signal[0] != signal[1]:
        re_data = Calculation(signal[0], variable[0], signal[1], variable[1], ai)
    elif ai < signal[2] and signal[1] != signal[2]:
        re_data = Calculation(signal[1], variable[1], signal[2], variable[2], ai)
    elif ai < signal[3] and signal[2] != signal[3]:
        re_data = Calculation(signal[2], variable[2], signal[3], variable[3], ai)
    elif (ai < signal[4] or ai >= signal[4]) and signal[3] != signal[4]:
        re_data = Calculation(signal[3], variable[3], signal[4], variable[4], ai)
    elif ai >= signal[3] and signal[2] != signal[3]:
        re_data = Calculation(signal[2], variable[2], signal[3], variable[3], ai)
    elif ai >= signal[2] and signal[1] != signal[2]:
        re_data = Calculation(signal[1], variable[1], signal[2], variable[2], ai)
    elif (ai >= signal[1] or ai > signal[0]) and signal[0] != signal[1]:
        re_data = Calculation(signal[0], variable[0], signal[1], variable[1], ai)
    return re_data

#線性回歸
def Calculation(x0,y0,x1,y1,ai):
    arr_x = [x0,x1]
    arr_y = [y0,y1]
    x_avg = float((x0+x1)/2.0)
    y_avg = float((y0+y1)/2.0)
    
    mdcross_sum = 0
    xdif_square_sum =0
    re_data = 0
    
    for i in range(2):
        xdif = float(arr_x[i] - x_avg) 
        ydif = float(arr_y[i] - y_avg)
        mdcross_sum += xdif * ydif
        xdif_square_sum += math.pow(xdif, 2)

    if xdif_square_sum <= 0:
        return 0
    else:
        b = mdcross_sum / xdif_square_sum

    a = y_avg - b * x_avg

    re_data = a + (b* ai)
    if re_data<0:
        re_data = 0
    
    return re_data
