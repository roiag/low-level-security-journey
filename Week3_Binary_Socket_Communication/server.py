import socket
import struct

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 9999))

    server_socket.listen(1)
    print("[*] Server listening on port 9999...")

    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address}")

    data = client_socket.recv(1024)
    print(f"[*] Received data: {data}")
    result = struct.unpack('<BI', data)
    if result[0] == 1:
        x=result[1]*3
        print(f"[*] {result[1]} * 3 = {x}")
    elif result[0] == 2:
        x=result[1]+result[1]
        print(f"[*] {result[1]} * 2 = {x}")
    else:
        Exception("Error. opcode is invalid")
    client_socket.close()
    server_socket.close()
    print("[*] Server closed.")


if __name__ == "__main__":
    main()
