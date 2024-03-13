import socket

HEADER = 64
PORT = 5001  # Cambia este puerto al mismo que el servidor
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.1.8'  # Cambia esta IP a la del servidor
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

while True:
    msg = input("Mensaje: ")
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        break

client.close()
