import socket

def run_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 65432)  # Use the same IP and port as the server
    print(f"Connecting to server at {server_address}...")
    client_socket.connect(server_address)

    try:
        # Send a greeting message to the server
        client_message = "Hello, Server!"
        client_socket.sendall(client_message.encode())
        print(f"Sent to server: {client_message}")

        # Receive the server's response
        server_message = client_socket.recv(1024).decode()
        print(f"Server says: {server_message}")

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    run_client()
