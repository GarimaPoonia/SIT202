import socket

print("DNS Server Started!!")
print("Author: Garima (2110994804)")

# IP address and port number to bind the socket to
address = ("127.0.0.1", 50)

# Size of buffer for receiving queries
bufferSize = 1024

# DNS records stored as dictionaries
type_A = {"example.com": "10.0.0.1", "google.com": "20.0.0.1", "yahoo.com": "30.0.3.3"}
type_CNAME = {"www.facebook.com": "facebook.com", "www.instagram.com": "instagram.com", "www.twitter.com": "twitter.com"}

# Create a UDP socket
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port number
UDP_sock.bind(address)

# Listen for incoming client queries
while True:
    print("---------------------------------------------------------------------------")
    print(f"Listening for client at {address[0]}:{address[1]}")
    query, client_address = UDP_sock.recvfrom(bufferSize)
    print(f"Client query: {query.decode()}")

    # Check if the query matches a Type A record
    if query.decode() in type_A:
        response = f"A,{type_A[query.decode()]}"
    # Check if the query matches a CNAME record
    elif query.decode() in type_CNAME:
        response = f"CNAME,{type_CNAME[query.decode()]}"
    else:
        response = "None"

    # Send the response back to the client
    UDP_sock.sendto(response.encode(), client_address)
