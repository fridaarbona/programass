

import serial as conn

arduino = conn.Serial(port="COM11", baudrate= 9600, timeout=1)
print("Conexion exitosa")

while True:

    valor = input("ingresa el estado del led:")

    arduino.write(valor.encode())

