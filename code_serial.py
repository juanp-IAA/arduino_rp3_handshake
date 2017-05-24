import serial


# ls /dev/tty*  -> para ver que USB se esta usando
# De hecho, podriamos hacer cat /dev/ttyUSB0 para leer directamente 
# sin usar Python

ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1 :
    msg = ser.readline()
    print msg
