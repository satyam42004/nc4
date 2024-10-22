import socket

def receive_file(client_socket):
    file_name = 'received_file.txt'  # Name of the file to save
    with open(file_name, 'wb') as file:
        print(f"Receiving file and saving as: {file_name}")
        while True:
            # Receive file data in chunks
            file_data = client_socket.recv(1024)
            if not file_data:
                break
            file.write(file_data)
    print(f"File {file_name} received successfully.")

def run_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 65432)  # Use the same IP and port as the server
    print(f"Connecting to server at {server_address}...")
    client_socket.connect(server_address)

    try:
        # Receive the file from the server
        receive_file(client_socket)
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    run_client()
