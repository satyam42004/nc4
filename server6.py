import socket

def send_file(connection):
    file_name = 'file_to_send.txt'  # Specify the file you want to send
    try:
        with open(file_name, 'rb') as file:
            print(f"Sending file: {file_name}")
            while True:
                # Read file data in chunks
                file_data = file.read(1024)
                if not file_data:
                    break
                connection.sendall(file_data)
        print("File sent successfully.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        connection.sendall(b'File not found.')

def run_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('localhost', 65432)  # Change 'localhost' to your server's IP if needed
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print(f"Connected to {client_address}")
        send_file(connection)
    finally:
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    run_server()
