# A simple port scanner that scans a range of ports on a target host.
# It prompts the user for a target address or IP, and a range of ports to scan
# It checks each port in the range to see if it is open or closed
# It uses the socket library to create a TCP connection to each port
# It prints the status of each port and the time taken for the scan
# It is intended for educational purposes only and should not be used for malicious purposes


import socket
from datetime import datetime

target = input("Enter the target address or ip: ")


## Function to get a valid port input from the user
# This function will keep prompting the user until a valid port number is entered.
# A valid port number is an integer between 1 and 65535.
def get_valid_port_input(prompt):
    while True:
        try:
            port = int(input(prompt))
            if 1 <= port <= 65535:
                return port
            else:
                print("Error: Port number must be between 1 and 65535. Please try again.\n")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.\n")



# Function to perform a port scan on the target host
# It scans a range of ports from start_port to end_port
# It prints the status of each port (open or closed)
# It handles exceptions for hostname resolution and connection errors
# It also prints the time taken for the scan
# If no open ports are found, it informs the user
def port_scan(target, start_port, end_port):
    found_open_port = False
    try:
        ip = socket.gethostbyname(target)
        print(f"Scanning the target {ip}")
        print("Time started at", datetime.now())
        print("")
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("port {}: open".format(port))
                found_open_port = True
            sock.close()
            
        # After the loop finishes, check the flag's state
        if not found_open_port: 
            print(f"No open ports found in the range {start_port}-{end_port}.")
        
        print("\nScanning finished at", datetime.now())
        
    # Handle exceptions for hostname resolution and connection errors
    except socket.gaierror:
        print("Hostname could not be resolved\n")
    
    # Handle exceptions for connection errors 
    except socket.error:
        print("could not connect to server\n")
    
    # Handle any other exceptions that may occur  
    except Exception: 
        print("Something wrong...")



start_port = get_valid_port_input("Enter the starting port number (1-65535): ")

# Loop until a valid ending port is provided
while True:
    end_port = get_valid_port_input("Enter the ending port number (1-65535): ")
    if end_port >= start_port:
        break # Valid range, exit loop
    else:
        print(f"Error: Ending port ({end_port}) cannot be less than starting port ({start_port}). Please try again.\n")


port_scan(target, start_port, end_port)

# takes a long time because it performs each port check one after another,
# and each check on a closed or filtered port forces it to wait for the full 1-second timeout.