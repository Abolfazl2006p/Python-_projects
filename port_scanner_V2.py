import socket
import time

target = input("Enter target iP or domain: ")
start_time = time.time()
print(f"Scanning target: {target}")
print(f"Scanning target: {target}")
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            service_name = socket.getservbyport(port)
            print(f"port {port} is OPEN ({service_name})")
        except OSError:
            print(f"port {port} is OPEN (Unknown Service)")    
        print(f"port {port} is OPEN")

    s.close()
print("Scan finished!") 
end_time = time.time()
total_time = end_time - start_time
print(f"Scan completed in {total_time:.2f} seconds.")      