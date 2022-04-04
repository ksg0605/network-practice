import socket

HOST = 'localhost'
PORT = 4000

def run_client(host, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    msg = input('> : ')
    s.sendall(msg.encode())
    res = s.recv(1024)
    print(f'>> : {res.decode()}')

if __name__ == '__main__':
  run_client(HOST, PORT)