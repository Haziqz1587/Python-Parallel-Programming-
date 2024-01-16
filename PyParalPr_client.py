import socket

def main():
    # Client settings
    host = "192.168.153.129"
    port = 8484

    # Create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Receive and print the quote from the server
    quote = client_socket.recv(1024).decode()
    print(f"Quote of the Day: {quote}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    main()
