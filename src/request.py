
import socket
import sys

def send_request_socket(ip, port, path, method, version, headers):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    req = f"{method} {path} {version}\r\n"
    for current in headers:
        req += f"{current}: {headers[current]}\r\n"
    req += "\r\n"

    client_socket.sendall(req.encode())
    reponse = client_socket.recv(4096)

    status = get_response_status(reponse.decode())
    print(f"\nRequest sent: {status}.\nPath: {path}, method: {method}, version: {version}.")
    if (status == 200):
        print(f"\n\n[GOT IT] favorable status {status} with the following request:\n\n{req}")
        sys.exit()

    client_socket.close()


def get_response_status(decoded):
    lignes = decoded.split('\r\n')
    status_code = int(lignes[0].split(' ')[1])
    return status_code
