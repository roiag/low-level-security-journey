import socket
import struct

def main():
    try:
        opcode = int(input("Enter opcode (1 = multiply by 3, 2 = add to itself): "))
        value = int(input("Enter value to process: "))
    except ValueError:
        print("❌ Invalid input. Please enter integers only.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 9999))

        message = struct.pack('<BI', opcode, value)

        client_socket.sendall(message)
        print(f"[*] Sent opcode {opcode} with value {value}")

    except Exception as e:
        print(f"❌ Connection error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
