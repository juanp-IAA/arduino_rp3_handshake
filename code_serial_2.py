import serial


# ls /dev/tty*  -> para ver que USB se esta usando
# De hecho, podriamos hacer cat /dev/ttyUSB0 para leer directamente 
# sin usar Python

# Escribe en el puerto serie un numero n hacia el puerto serie
# n debe de ser n<9 and n>0

ser = serial.Serial('/dev/ttyUSB0', 9600)

print "Imprimimos por el puerto serie el valor"
msg = ser.write('9')

print "Done."    

