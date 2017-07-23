import serial, csv
from time import sleep
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0',9600)
ser.write("*".encode())

#while True
ard = (b"3")
ser.write(ard)
serData = ser.readline().strip().rsplit()
hum = float(serData[0])
temp = float(serData[1])
state = float(serData[2])

csvname = open('www/data/data.csv', 'a')
writer = csv.writer(csvname, lineterminator='\n')
writer.writerow([datetime.now().strftime('%Y/%m/%d %H:%M:%S'),temp,hum])
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
print("温度:",temp,'C')
print("湿度:",hum,'%')
print("state:",state)
print('\n')
