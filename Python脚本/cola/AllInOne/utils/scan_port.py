import socket
from .print_color import print_color_text, RED, BLUE


class ScanPort:
    """TCP/UDP 端口探测"""
    def __init__(self, targetip, port):
        self.targetip = targetip
        self.port = port

    def scan_tcp(self):

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(2)
                result = sock.connect_ex((self.targetip, self.port))

                if result == 0:
                    print_color_text(f"TCP {self.targetip}:{self.port} is open", BLUE)

                else:
                    print_color_text(f"TCP {self.targetip}:{self.port} is closed", BLUE)

        except socket.error as e:
            print_color_text(f"ERROR: {e}", RED)

    
    def scan_udp(self):

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(2)
                # 发送空数据包
                sock.sendto(b'', (self.targetip, self.port))

                try:
                    data, _ = sock.recvfrom(1024)
                    print_color_text(f"UDP {self.targetip}:{self.port} is open", BLUE)

                except socket.timeout:
                # 没有响应，可能是端口未开放或者被防火墙过滤
                    print_color_text(f"UDP {self.targetip}:{self.port} may be open or filter", BLUE)

        except socket.error as e:
            print_color_text(f"ERROR: {e}", RED)


# if __name__ == "__main__":
#     pass