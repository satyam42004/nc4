import socket

def run_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('localhost', 65432)  # You can change 'localhost' to your IP address if needed
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print(f"Connected to {client_address}")

        # Receive the message from the client
        client_message = connection.recv(1024).decode()
        print(f"Client says: {client_message}")

        # Send a response
        server_message = "Hello, Client!"
        connection.sendall(server_message.encode())
        print(f"Sent to client: {server_message}")

    finally:
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    run_server()
