import socket
import time
import concurrent.futures
import json
import os

target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

start_time = time.time()
print(f"Scanning target: {target}")

open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    
    if result == 0:
        try:
            service_name = socket.getservbyport(port)
            print(f"Port {port} is OPEN ({service_name})")
        except OSError:
            print(f"Port {port} is OPEN (Unknown Service)")
        
        open_ports.append({"port": port, "service": "open"})
        
    s.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

end_time = time.time()
total_time = end_time - start_time
print(f"Scan completed in {total_time:.2f} seconds.")

current_path = os.getcwd()
print(f"Current working directory: {current_path}")

file_path = os.path.join(current_path, "scan_results.json")
with open(file_path, "w") as f:
    json.dump(open_ports, f, indent=4)
    
print(f"Results saved to: {file_path}")
