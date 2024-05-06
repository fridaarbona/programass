import serial as conn

arduino = conn.Serial(port="COM11", baudrate= 9600, timeout=1)
print("Conexion exitosa")

while True:
    a = arduino.readline()
    a = a.decode()
    a = a.strip()
    print(a)

