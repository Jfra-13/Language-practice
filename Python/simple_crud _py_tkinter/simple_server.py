# from socket import *
# import socket

# def createServer():
#     serverSocket = socket(AF_INET, SOCK_STREAM)
#     try:
#         serverSocket.bind(('localhost', 9000))
#         serverSocket.listen(5)
#         while(1):
#             (clientSocket, address) = serverSocket.accept()
#             rd = clientSocket.recv(5000).decode()
#             pieces = rd.split("\n")
#             if ( len(pieces) > 0 ) : print(pieces[0])
            
#             data = 'HTTP/1.1 200 OK\r\n'
#             data += 'Content-Type: text/html; charset=utf-8\r\n'
#             data += '\r\n'
#             data += '<html><body>Hello Word</body></html>\r\n\r\n'
#             clientSocket.sendall(data.encode())
#             clientSocket.shutdown(SHUT_WR)
            
#     except KeyboardInterrupt:
#         print('\nShutting down...\n');
#     except Exception as exc:
#         print('Error:\n');
#         print(exc)
#     serverSocket.close()
    
# print('Access http://localhost:9000')
# createServer()

# ---------------------------------------------------------------------

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('127.0.0.1', 9000))
# cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')
    
# mysock.close()

from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.1.8"
PORT = 9999

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        
        self.wfile.write(bytes("<html><body><h1> Hello World! </h1></body></html>", "utf-8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"Time": "' + date + '" }' ,"utf-8"))
        

    
server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running...")
server.serve_forever()
server.server_close()
print("Server stopped!")