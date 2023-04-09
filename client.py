import socket

# IP address and port number to send the query to
address = ("127.0.0.1", 50)

# Size of buffer for receiving query responses
bufferSize = 1024

# Create a UDP socket
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Author: Garima (2110994804)")

while True:
    print("---------------------------------------------------------------------------")
    query = input("Enter hostname/alias name: ")
    UDP_sock.sendto(query.encode(), address)  # Send the query to the server

    # Receive the response from the server
    query_response, server_address = UDP_sock.recvfrom(bufferSize)
    print("Server Response on your Query: " + str(query_response.decode()))

    # Ask the user if they want to continue
    is_next = input("Continue? Y/N: ")
    if is_next.lower() != "y":
        break
